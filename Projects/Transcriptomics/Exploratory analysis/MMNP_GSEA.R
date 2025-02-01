library( "org.Hs.eg.db" )
columns(org.Hs.eg.db)
#Enrichment analysis perform when 
library(AnnotationDbi)
library("reactome.db")
library(ensembldb)
library(DOSE)
library(pathview)
library(enrichplot)
library(GOSemSim)
library(plotly)
install.packages("gridExtra")
library(grid)
library(gridExtra)


DE_dataset <-  ddsDE_sva_Allocation_M3_result
pAdj <-  0.1 #to extract significant gene


Entrez_res_ddsDE <- DE_dataset[ DE_dataset$entrezid %in% keys( reactome.db, "ENTREZID" ) & !is.na( DE_dataset$padj ), ]

reactomeTable <- AnnotationDbi::select(reactome.db, 
                                       keys=as.character(Entrez_res_ddsDE$entrezid), keytype="ENTREZID", 
                                       columns=c("ENTREZID","REACTOMEID") )

convertIDs <- function( ids, from, to, db, ifMultiple=c("putNA", "useFirst")) {
  stopifnot( inherits( db, "AnnotationDb" ) )
  ifMultiple <- match.arg( ifMultiple )
  suppressWarnings( selRes <- AnnotationDbi::select(
    db, keys=ids, keytype=from, columns=c(from,to) ) )
  if ( ifMultiple == "putNA" ) {
    duplicatedIds <- selRes[ duplicated( selRes[,1] ), 1 ]
    selRes <- selRes[ ! selRes[,1] %in% duplicatedIds, ]
  }
  return( selRes[ match( ids, selRes[,1] ), 2 ] )
}



head(reactomeTable)
DE_dataset$hgnc_symbol <- convertIDs( rownames(DE_dataset), "ENSEMBL", "SYMBOL", org.Hs.eg.db )
DE_dataset$entrezid <- convertIDs( row.names(DE_dataset), "ENSEMBL", "ENTREZID", org.Hs.eg.db )
DE_dataset$ontoall <- convertIDs( DE_dataset$hgnc_symbol, "SYMBOL", "ONTOLOGY", org.Hs.eg.db )

head(DE_dataset, 20)

# Create background dataset for hypergeometric testing using all genes tested for significance in the results
all_genes <- as.character(row.names(DE_dataset))

# Extract significant results
signif_res <- DE_dataset[DE_dataset$padj < 0.12 & !is.na(DE_dataset$padj), ]
signif_genes <- as.character(rownames(signif_res))
head(signif_genes)

library(clusterProfiler)

# Run GO enrichment analysis

Allo_ego <-  ego
ego <- enrichGO(gene = signif_genes, universe = all_genes,
                keyType = "ENSEMBL",
                OrgDb = org.Hs.eg.db,
                ont = "BP",
                pAdjustMethod = "BH",
                qvalueCutoff = 0.1,
                readable = TRUE)

high_ego <-  ego1

ego1 <- enrichGO(gene = signif_genes, universe = all_genes,
                keyType = "ENSEMBL",
                OrgDb = org.Hs.eg.db,
                ont = "CC",
                pAdjustMethod = "BH",
                qvalueCutoff = 0.1,
                readable = TRUE)



pdf("I:/Aditya/MMNP_DEA/Output/graphs/GSEA of ddsDE_sva_Allo_M3_, FDR 0.1.pdf", width = 8, height = 10, compress = T)

# Output results from GO analysis to a table
cluster_summary <- data.frame(ego)
write.csv(cluster_summary, "I:/Aditya/MMNP_DEA/Output/csv/Clustersummary_ddsDE_sva_Allo_M3_BP.csv")

dotplot(ego, showCategory=50, title = "GSEA of DEG SVa Intervention BMI Cellular component, FDR 0.1", font.size = 10, label_format = 50)

data(geneList)

d <- godata('org.Hs.eg.db', ont="BP")
ego2 <- pairwise_termsim(ego, semData = d)

set.seed(123)

emapplot(ego2, cex.params = list(category_node = 0.7, category_label = 0.7))

# To color genes by log2 fold changes

signif_res_lFC <- signif_res$log2FoldChange

cnetplot(ego,
         categorySize="pvalue", 
         showCategory = 10,
         color.params = list(foldChange = 1.25), vertex.label.font=5)



dev.off()

emapplot(ego2, cluster.params = list(cluster = T, method = stats::kmeans, n = NULL, legend = F, label_style = "ggforce", label_words_n = 4, label_format = 100), edge.params = list(show = TRUE, min = 0.2), cex.params = list(category_node = 0.7, category_label = 0.7))



library(enrichplot)
library(UpSetR)

upsetplot(ego)


# GSEA using clusterProfiler and Pathview
library(biomaRt)

datasets <- listDatasets(ensembl)
head(datasets)
searchDatasets(mart = ensembl, pattern = "hsapiens")

ensembl <- useEnsembl(biomart = "genes", dataset = "hsapiens_gene_ensembl")


mart <- useDataset("hsapiens_gene_ensembl", useMart("ensembl"))
genes <- getBM(filters="ensembl_gene_id",
               attributes=c("ensembl_gene_id", "entrezgene_id"), values= all_genes,
               mart=mart)


indNA = which(is.na(genes$entrezgene_id))
genes_noNA <- genes[-indNA,]
indnodup = which(duplicated(genes_noNA$ entrezgene_id) == F)
genes_noNA_nodup <- genes_noNA[indnodup,]

lFC <- DE_dataset$log2FoldChange[-indNA]
lFC <- lFC[indnodup]
names(lFC) <- genes_noNA_nodup$entrezgene_id

# Sort fold changes in decreasing order
lFC <- sort(lFC, decreasing = TRUE)

gseaKEGG <- gseKEGG(geneList = lFC,
                    organism = "hsa",
                    minGSSize = 2, # minimum gene set size
                    pvalueCutoff = 0.1, # padj cutoff value
                    verbose = T)


# Extract the GSEA results
gseaKEGG_results <- gseaKEGG@result
