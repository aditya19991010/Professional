# Load required libraries for enrichment analysis
library("org.Hs.eg.db")
library(AnnotationDbi)
library("reactome.db")
BiocManager::install("DOSE")
library(ensembldb)
library(DOSE)
library(pathview)
library(enrichplot)
library(GOSemSim)

# Select columns from org.Hs.eg.db
columns(org.Hs.eg.db)

# Perform enrichment analysis on significant genes
Entrez_res_ddsDE <- ddsDE_result[ddsDE_result$entrezid %in% keys(reactome.db, "ENTREZID") & !is.na(ddsDE_result$padj), ]
head(Entrez_res_ddsDE)

# Retrieve Reactome annotations
reactomeTable <- AnnotationDbi::select(reactome.db, 
                                       keys = as.character(Entrez_res_ddsDE$entrezid),
                                       keytype = "ENTREZID",
                                       columns = c("ENTREZID", "REACTOMEID"))
head(reactomeTable)

# Convert IDs and add to ddsDE_result
ddsDE_result$hgnc_symbol <- convertIDs(rownames(ddsDE_result), "ENSEMBL", "SYMBOL", org.Hs.eg.db)
ddsDE_result$entrezid <- convertIDs(row.names(ddsDE_result), "ENSEMBL", "ENTREZID", org.Hs.eg.db)
ddsDE_result$ontoall <- convertIDs(row.names(ddsDE_result), "ENSEMBL", "ONTOLOGY", org.Hs.eg.db)

head(ddsDE_result, 20)

# Create background dataset for hypergeometric testing
all_genes <- as.character(row.names(ddsDE_result))

# Extract significant results
signif_res <- ddsDE_result[ddsDE_result$padj < 0.1 & !is.na(ddsDE_result$padj), ]
signif_genes <- as.character(rownames(signif_res))

# Run GO enrichment analysis
ego <- enrichGO(gene = signif_genes, universe = all_genes,
                keyType = "ENSEMBL",
                OrgDb = org.Hs.eg.db,
                ont = "BP",
                pAdjustMethod = "BH",
                qvalueCutoff = 0.1,
                readable = TRUE)

# Output results from GO analysis to a table
cluster_summary <- data.frame(ego)
cluster_summary

# Visualize results
dotplot(ego, showCategory = 50)
data(geneList)

# Calculate pairwise term similarity and plot
d <- godata('org.Hs.eg.db', ont = "BP")
ego2 <- pairwise_termsim(ego, method = "Wang", semData = d)
emapplot(ego2)
emapplot_cluster(ego2)

# Color genes by log2 fold changes
signif_res_lFC <- signif_res$log2FoldChange
cnetplot(ego,
         categorySize = "pvalue",
         showCategory = 5,
         foldChange = signif_res_lFC, vertex.label.font = 6)

# Additional visualizations
library(enrichplot)
library(UpSetR)

upsetplot(ego)

# Perform GSEA using clusterProfiler and Pathview
library(biomaRt)

datasets <- listDatasets(ensembl)
head(datasets)
searchDatasets(mart = ensembl, pattern = "hsapiens")

ensembl <- useEnsembl(biomart = "genes", dataset = "hsapiens_gene_ensembl")

# Fetch gene information
mart <- useDataset("hsapiens_gene_ensembl", useMart("ensembl"))
genes <- getBM(filters = "ensembl_gene_id",
               attributes = c("ensembl_gene_id", "entrezgene_id"), values = all_genes,
               mart = mart)

# Preprocess gene data
indNA <- which(is.na(genes$entrezgene_id))
genes_noNA <- genes[-indNA,]
indnodup <- which(duplicated(genes_noNA$entrezgene_id) == FALSE)
genes_noNA_nodup <- genes_noNA[indnodup,]
lFC <- ddsDE_result$log2FoldChange[-indNA]
lFC <- lFC[indnodup]
names(lFC) <- genes_noNA_nodup$entrezgene_id

# Sort fold changes in decreasing order
lFC <- sort(lFC, decreasing = TRUE)

# Run GSEA on KEGG pathways
gseaKEGG <- gseKEGG(geneList = lFC,
                    organism = "hsa",
                    minGSSize = 5,
                    pvalueCutoff = 0.1,
                    verbose = FALSE)

# Extract GSEA results
gseaKEGG_results <- gseaKEGG@result
