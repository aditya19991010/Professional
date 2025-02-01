# ====================================
# Differential Expression Analysis Script
# ====================================

# ====================================
# Load Required Libraries
# ====================================
library(limma)
library(edgeR)
library(DESeq2)
library(apeglm)
library(tidyverse)
library(pheatmap)
library(ggplot2)
library(ggrepel)
library(RColorBrewer)
library(dplyr)
library(Glimma)
library(sva)
library(EnhancedVolcano)
library(BiocParallel)

# Register parallel processing
register(SnowParam(8))

# ====================================
# Set Working Directory and Load Data
# ====================================
setwd("F:/Aditya/MMNP_DEA/input/ftcount/")

# Load raw counts
rawcounts <- read.csv(file = "Batch123_trimmed_rawcounts.txt", sep = "\t", row.names = 1)
head(rawcounts)

# Save column names
colnames_rawcount <- colnames(rawcounts)
write.csv(colnames_rawcount, file = "colnames_Batch123.txt")

# Load sample annotation data
sampleData <- read.csv(file = "Annotation_file_171samples_csv.csv", header = TRUE, sep = ",")
head(sampleData)

# Filter sample data by sex
female_Sampledata <- sampleData %>% filter(csex == 2)
male_Sampledata <- sampleData %>% filter(csex == 1)

# ====================================
# Design Matrix Setup
# ====================================
# Define design formula
design <- ~Batch + BMI + csex + Allocation
alpha <- 0.05

# Create DESeq dataset
dds <- DESeqDataSetFromMatrix(countData = rawcounts, colData = sampleData, design = design)

# Normalize counts
dds <- estimateSizeFactors(dds)
norm_count <- counts(dds, normalized = TRUE)

# ====================================
# Preprocessing
# ====================================
# Remove lowly expressed genes
keep <- rowSums(counts(dds)) >= 171
dds <- dds[keep,]

# Set factor levels
dds$Allocation <- factor(dds$Allocation, levels = c("A", "B"))

# ====================================
# Differential Expression Analysis
# ====================================
# Run DESeq
ddsDE <- DESeq(dds)

# Extract results
ddsDE_result <- results(ddsDE)
summary(ddsDE_result)

# Filter results by adjusted p-value
ddsDE_result_0.05 <- results(ddsDE, alpha = alpha)
summary(ddsDE_result_0.05)

# Convert results to a data frame
ddsDE_result <- as.data.frame(ddsDE_result)

# ====================================
# Filtering Significant Genes
# ====================================
# Arrange by adjusted p-value
ddsDE_result <- ddsDE_result[order(ddsDE_result$padj),]

# Filter for significant genes
significant_genes <- ddsDE_result %>% filter(padj < alpha)

# Filter for log2 fold change > 1
filtered_lfc_g1 <- ddsDE_result %>% filter(abs(log2FoldChange) > 1)

# Dimensions of filtered results
dim(ddsDE_result)
dim(filtered_lfc_g1)

# ====================================
# Visualization
# ====================================
# Variance stabilization
vsd <- vst(dds, blind = FALSE)
assay_vsd <- assay(vsd)
head(assay_vsd, 3)

# Enhanced Volcano Plot (example visualization)
EnhancedVolcano(
  ddsDE_result,
  lab = rownames(ddsDE_result),
  x = 'log2FoldChange',
  y = 'padj',
  pCutoff = 0.05,
  FCcutoff = 1
)

# ====================================
# Summary and Additional Statistics
# ====================================
# Total significant genes with adjusted p-value < 0.01
pvalue_less_than_0.01 <- sum(ddsDE_result$padj < 0.01, na.rm = TRUE)

# Display top results
head(ddsDE_result, 50)

# End of Script
