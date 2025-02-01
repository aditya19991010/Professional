
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
write.csv(cluster_summary, "clustersummary_anno_highBMI_sva.csv")

pdf(file = "high_BMI_DEG_FDR005_71sample.pdf",paper = 'a4', compress = TRUE)

dotplot(ego, showCategory=50)
data(geneList)

d <- godata('org.Hs.eg.db', ont= c("BP", "CC", "MF"))

ego2 <- pairwise_termsim(ego, method="Wang", semData = d)

emapplot(ego2)
emapplot_cluster(ego2)

# To color genes by log2 fold changes
signif_res_lFC <- signif_res$log2FoldChange
cnetplot(ego,
         categorySize="pvalue",
         showCategory = 5,
         foldChange= signif_res_lFC, vertex.label.font=6)

upsetplot(ego)

# GSEA using clusterProfiler and Pathview
ensembl <- useEnsembl(biomart = "genes", dataset = "hsapiens_gene_ensembl")

datasets <- listDatasets(ensembl)
head(datasets)
searchDatasets(mart = ensembl, pattern = "hsapiens")

mart <- useDataset("hsapiens_gene_ensembl", useMart("ensembl"))
genes <- getBM(filters="ensembl_gene_id",
               attributes=c("ensembl_gene_id", "entrezgene_id"), values= all_genes,
               mart=mart)


indNA = which(is.na(genes$entrezgene_id))
genes_noNA <- genes[-indNA,]
indnodup = which(duplicated(genes_noNA$ entrezgene_id) == F)
genes_noNA_nodup <- genes_noNA[indnodup,]
lFC <- dsDE_highBMI_with_SV$log2FoldChange[-indNA]
lFC <- lFC[indnodup]
names(lFC) <- genes_noNA_nodup$entrezgene_id

# Sort fold changes in decreasing order
lFC <- sort(lFC, decreasing = TRUE)

gseaKEGG <- gseKEGG(geneList = lFC,
                    organism = "hsa",
                    minGSSize = 5, # minimum gene set size
                    pvalueCutoff = 0.5, # padj cutoff value
                    verbose = FALSE)
dev.off()
