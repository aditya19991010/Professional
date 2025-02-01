# =====================================================
# Statistical Plots for Differential Expression Analysis
# =====================================================

# Set working directory
getwd() 
setwd("F:/Aditya/MMNP_DEA/Output/")

# -----------------------------------------------------
# File Naming and Saving Results
# -----------------------------------------------------

# Extract the design formula
design_str <- as.character(design)[2]  # Extract design from the formula
csv_file_name <- paste0("ddsDE_result_ordered_design_", design_str, ".csv")
lfc_csv_file_name <- paste0("filtered_lfc_g1_ordered_design_", design_str, ".csv")
pdf_file_name <- paste0(design_str, ".pdf")

# Save DESeq2 results and filtered LFC data
write.csv(ddsDE_result, file = csv_file_name) 
write.csv(filtered_lfc_g1, file = lfc_csv_file_name) 

# -----------------------------------------------------
# Generate Statistical Plots
# -----------------------------------------------------

# PDF Settings for A4 Paper
fig.dim <- c(11.7, 8.3)
pdf(file = pdf_file_name, paper = "a4r", compress = TRUE, title = design_str)

# -----------------------------------------------------
# Histogram of p-values
# -----------------------------------------------------
par(mfrow = c(1, 1))  # Single plot layout
p_values <- ddsDE_result$pvalue

# Create the histogram
hist(
  p_values, 
  xlim = c(0, 0.1), 
  ylab = "Frequency of Transcripts", 
  breaks = 1000, 
  col = "grey", 
  xlab = "p-values", 
  main = "p-value Histogram"
)

# Add a significance cutoff line
abline(v = alpha, col = "red", lty = 2)

# -----------------------------------------------------
# MA Plot
# -----------------------------------------------------
par(mfrow = c(1, 2))  # Layout for side-by-side plots
plotMA(
  ddsDE, 
  ylim = c(-2, 2), 
  main = "MA Plot DESeq Allocation"
)

# -----------------------------------------------------
# PCA Plot
# -----------------------------------------------------
vsd <- vst(ddsDE_sva_Allocation_M1)  # Variance-stabilizing transformation
vsd$csex <- as.factor(vsd$csex)
vsd$Batch <- as.factor(vsd$Batch)

# Uncorrected PCA plot
plotPCA(vsd, intgroup = c("Allocation"))

# Corrected PCA plot (removing batch effects)
assay(vsd) <- limma::removeBatchEffect(assay(vsd), vsd$Batch)
plotPCA(vsd, intgroup = c("csex"))

# -----------------------------------------------------
# Dispersion Plots
# -----------------------------------------------------
par(mfrow = c(1, 3))  # Three plots side-by-side
plotDispEsts(ddsDE_sva_Allocation_M1, main = "Dispersion Estimate - Model 1")
plotDispEsts(ddsDE_sva_Allocation_M2, main = "Dispersion Estimate - Model 2")
plotDispEsts(ddsDE_sva_Allocation_M3, main = "Dispersion Estimate - Model 3")

# -----------------------------------------------------
# Volcano Plot
# -----------------------------------------------------
pdf(
  "I:/Aditya/MMNP_DEA/Output/graphs/Volcano_DE_sva_BMI_M3_FDR_0.05.pdf", 
  width = 12, height = 8, compress = TRUE
)

cut_padj <- 0.05  # Significance cutoff for padj
with(
  DE_dataset, 
  plot(
    log2FoldChange, -log10(pvalue), 
    pch = 20, 
    main = "Volcano Plot", 
    xlim = c(-3, 5)
  )
)

# Highlight significant genes
with(
  subset(DE_dataset, padj < cut_padj),
  points(log2FoldChange, -log10(pvalue), pch = 20, col = "blue")
)
with(
  subset(DE_dataset, padj < cut_padj & abs(log2FoldChange) > 0.5), 
  points(log2FoldChange, -log10(pvalue), pch = 20, col = "red")
)

# Enhanced volcano plot
EnhancedVolcano(
  ddsDE_alloca_result, 
  lab = rownames(ddsDE_alloca_result),
  x = 'log2FoldChange', y = 'pvalue', pCutoff = 0.1, 
  FCcutoff = 0.5, pointSize = 2.0, labSize = 3, 
  col = c('black', 'blue', 'red', 'green2'),
  title = "DEG Intervention Group Only (75 vs 96), FCcutoff = 0.5, FDR 0.1",
  titleLabSize = 15
)

# -----------------------------------------------------
# Finalize PDF
# -----------------------------------------------------
dev.off()  # Close PDF device

# -----------------------------------------------------
# Summary and Cleanup
# -----------------------------------------------------
summary(DE_dataset)
