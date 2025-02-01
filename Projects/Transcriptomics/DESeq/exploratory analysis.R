
# exploratory data analysis
#LFCshrink
# res_lfcShrink <- lfcShrink(ddsDE, coef="Allocation_B_vs_A", type = "apeglm")
resultsNames(ddsDE)
# resNormal <- lfcShrink(ddsDE, coef=2, type="normal")
# resAsh <- lfcShrink(ddsDE, coef=2, type="ashr")
resapeglm <- lfcShrink(ddsDE, coef=2, type="apeglm")

# this gives log2(n + 1)
ntd <- normTransform(dds)
meanSdPlot(assay(ntd))


library("pheatmap")

select <- order(rowMeans(counts(dds,normalized=TRUE)),
                decreasing=TRUE)[1:171]
df <- as.data.frame(colData(dds)[,c("Allocation","BMI")])
pheatmap(assay(ntd)[select,], cluster_rows=FALSE, show_rownames=FALSE,
         cluster_cols=FALSE, annotation_col=df)

colnames(df)[1:2] <- c("GE_values_after_log2(x+1)", "GE_values_after_vst")

lvlds <- c("log2(x+1)", "vst")
df$transformation <- factor(df$transformation, levels = lvlds)
library("hexbin")

ggplot_GE <- ggplot(df, aes(x= "GE_values_after_log2(x+1)", y= "GE_values_after_vst")) + geom_hex(bins = 80) + coord_fixed() + facet_grid(. ~transformation)
ggplot_GE
 

sampleDist <- dist(t(assay(vsd_norm)))
head(sampleDist)

library(pheatmap)
library(RColorBrewer)

ddsDe_norm_sort_BMI <- order(ddsDE_norm$BMI)
vsd_norm <-  vst(ddsDE_norm, blind = F)

head(assay(vsd_norm), 3)

sampleDistmtx <- as.matrix(sampleDist)
rownames(sampleDistmtx) <- paste(vsd_norm$Allocation, sep = "-")
colnames(sampleDistmtx) <- NULL

ddsDE_result[order(ddsDE_result$pvalue),] 

colors <- colorRampPalette(rev(brewer.pal(9, "Blues")))(255)
pheatmap(sampleDistmtx, cluster_rows = sampleDist, cluster_cols = sampleDist,
         color = colors)

vst <- assay(vst(ddsDE))
