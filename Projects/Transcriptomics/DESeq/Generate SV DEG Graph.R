#statistical plots 
library("EnhancedVolcano")

getwd() 
setwd("I:/Aditya/MMNP_DEA/Output/")

#hist
# Extract the p-values
design_str <- as.character(design_sv)

# design_str <- gsub("~", "", as.character(design))
design_str <- design_str[2]
design_str

csv_file_name <- paste0("ddsDE_sva_BMI_M3_result_ordered_design_", design_str, ".csv")
pdf_file_name <- paste0(design_str, ".pdf")
lfc_csv_file_name <- paste0("filtered_lfc_g1_ordered_design_", design_str, ".csv")

csv_file_name

write.csv(ddsDE_sva_BMI_M3_result, file = csv_file_name) 

write.csv(filtered_lfc_g1, file = lfc_csv_file_name) 

# write.csv(filtered_lfc_g1, file ="ddsDE_sva_BMI_M3_result_ordered_LFC_g1_design_Batch + BMI + csex + Allocation_adjCount_preservedAllo_adj_sex+BMI.csv")

fig.dim = c(11.7, 8.3)
pdf(file = pdf_file_name, paper = "a4r", compress = T, title = design_str)

par(mfrow=c(1,1))
p_values <- ddsDE_sva_BMI_M3_result$pvalue

# Create a histogram
hist(p_values,  xlim = c(0,0.1), ylab = "Frequency of transcripts", breaks = 1000, col = "grey", xlab = "p-values", main = "p-value Histogram")

# Add significance cutoff lines 
abline(v = 2, col = "red", lty = 2)


par(mfrow=c(2,1))
plotMA(ddsDE_sva_Allocation_M3, ylim=c(-2,2), main = "MA plot DESeq Allocation SV" ) #Use Biogeneric plot function not limma's.

#triangle shows the direction of fold changes and blue colored genes shows significantly different expressed genes
vsd <- vst(ddsDE_sva_Allocation_M3, blind = T)
vsd_assay <- assay(vsd)

vsd_tassay <- t(vsd_assay)
head(vsd_tassay)

vsd$csex <- as.factor(vsd$csex)
vsd$Batch <- as.factor(vsd$Batch)



plotPCA(vsd, intgroup=c("Allocation"))
assay(vsd) <- limma::removeBatchEffect(assay(vsd), c(vsd$Batch))
vsd_assay_rmBatch <- assay(vsd)
meanSdPlot(assay(vsd), ranks = F)

plotPCA(vsd, intgroup=c("csex"))

# ggplot(PCAplot, aes(x = PC1, y = PC2, color = Allocation)) +  
#   geom_point(size = 3)+  
#   coord_fixed() + 
#   xlab(paste0("PC1", percentVar[1], "% variance")) + 
#   ylab(paste0("PC2", percentVar[2], "% variance")) +  
#   ggtitle("PCA with VST data")  

#Dispersion plot

par(mfrow=c(1,1))
plotDispEsts(ddsDE_sva_Allocation_M3, main = "Dispersion estimate DE " )
plotDispEsts(vsd, main = "Dispersion estimate DE VSD " )

glimmaMDS(ddsDE, groups = c(ddsDE$Batch))

#basic volcano plot

ddsDE_result$
  cut_padj = 0.05

with(ddsDE_sva_BMI_M3_result, plot(log2FoldChange, -log10(pvalue), pch=20,
                                   main="Volcano plot", xlim=c(-3,5))) 


with(subset(ddsDE_sva_BMI_M3_result, padj< cut_padj),
     points(log2FoldChange, -log10(pvalue), pch=20, col="blue"))

with(subset(ddsDE_sva_BMI_M3_result, padj< cut_padj & abs(log2FoldChange)> 0.5), 
     points(log2FoldChange, -log10(pvalue), pch=20, col="red"))


design(ddsDE_sva_highBMI_M3)
levels(ddsDE_sva_highBMI_M3$Allocation)
DE_dataset = ddsDE_sva_Allocation_M3_result


EnhancedVolcano(DE_dataset, lab = DE_dataset$hgnc_symbol,
                x ='log2FoldChange', FCcutoff = 0.5, y = 'pvalue', pCutoff = alpha,
                xlim = c(-2,2),
                ylim = c(0,10),
                pointSize = 2.0, labSize = 3, 
                col = c('black', 'blue', 'red', 'green2', colAlpha =1),
                vline = c(2,-2), vlineCol = 'deepskyblue3',
                title = 'DESeq2 results',
                subtitle = 'Intervention (76) vs Non Intervention (95) ',
                caption = 'FC cutoff, 0.5 ; p-value cutoff, 0.05',
)




#for ddsMA
# glimmaMA(dds_MA)

# Create two MA plots side by side
library("limma")
library("edgeR")

par(mfrow=c(1,1))
# plotMA(res_lfcShrink, ylim = c(-5,5), main = "res_lfcShrink")
# plotMA(ddsDE_sva_BMI_M3_result,  ylim = c(-5,5), main = "DE result")
# 
# par(mfrow=c(1,3), mar=c(4,4,2,1))
# xlim <- c(1,1e5); ylim <- c(-3,3)
# plotMA(resapeglm, xlim=xlim, ylim=ylim, main="apeglm")
# plotMA(resNormal, xlim=xlim, ylim=ylim, main="normal")
# plotMA(resAsh, xlim=xlim, ylim=ylim, main="ashr")


dev.off()
#Save files

vsd <- vst(dds)
plot_pca(vsd, "Batch")

par(mfrow=c(2,2),mar=c(2,2,1,1))
ylim <- c(-2.5,2.5)

resGA <- results(ddsDE, lfcThreshold=.5, altHypothesis="greaterAbs")
resLA <- results(ddsDE, lfcThreshold=.5, altHypothesis="lessAbs")
resG <- results(ddsDE, lfcThreshold=.5, altHypothesis="greater")
resL <- results(ddsDE, lfcThreshold=.5, altHypothesis="less")

drawLines <- function() abline(h=c(-.5,.5),col="dodgerblue",lwd=2)
plotMA(resGA, ylim=ylim); drawLines()
plotMA(resLA, ylim=ylim); drawLines()
plotMA(resG, ylim=ylim); drawLines()
plotMA(resL, ylim=ylim); drawLines()
