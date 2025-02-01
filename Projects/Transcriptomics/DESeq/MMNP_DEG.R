if (!require("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("vsn")


library("limma") 
library("edgeR")
library("DESeq2")
library("apeglm")
library("tidyverse")
library(pheatmap) 
library(ggplot2) 
library(ggrepel)
library(RColorBrewer) 
library(dplyr) 
library(Glimma)
library(sva)
library(EnhancedVolcano)
library("BiocParallel")
register(SnowParam(8))

getwd() 
setwd("I:/Aditya/MMNP_DEA/input/ftcount/") 
rawcounts <- read.csv(file = "I:/Aditya/MMNP_DEA/input/Batch123_trimmed_rawcounts_mod.txt", sep = "\t", row.names = 1) 
sampleData <- read.csv(file ="../Pheno_file_MMNPC_171.csv", header = TRUE, sep = ",")


head(rawcounts)
colnames_rawcount <- colnames(rawcounts)
sampleData <- factor(sampleData)
write.csv(colnames_rawcount, file = "colnames_Batch123.txt")

#design for effect of allocation on sex
design = ~ cbmi + csex + Batch + BMI + Allocation
alpha = 0.05

dds <- DESeqDataSetFromMatrix(countData = rawcounts, colData = sampleData, design = design)

norm_count <- estimateSizeFactors(dds)
norm_count <- as.data.frame(norm_count)
write.csv(norm_count, file = "MMNP_DEA_ddsDE_BMI_normcounts.csv")

sizeFactors(norm_count)


# # set reference for the factor
# dds$csex <- factor(dds$csex, levels = c("1", "2"))
dds$Allocation <- factor(dds$Allocation, levels = c("A","B"))
# dds$BMI <- factor(dds$BMI, levels = c("high", "low"))
# dds$Batch <- factor(dds$Batch, levels = c("1","2","3"))


#checking NA values
# row_has_na <- any(is.na(rawcounts[3, ]))
# col_has_na <- any(is.na(sampleData[, 1]))

#remove lowely expressed genes 
keep <- rowSums(counts(dds)) >= 171
dds<- dds[keep,]

# set factor level
dds$Allocation <- relevel(dds$Allocation, ref = "A")
# dds$BMI <- relevel(dds$BMI, ref = "high")

#NOTE: collapse technical replicates, never collapse biological replicates

# main DESeq
ddsDE <- DESeq(dds)
ddsDE_result <- results(ddsDE)
summary(ddsDE_result)

norm_count <- counts(ddsDE, normalized = T)

pvalue_less_than_0.01 <- sum(ddsDE_result$padj < 0.01, na.rm=TRUE)
pvalue_less_than_0.1 <- sort(ddsDE_result$padj)
pvalue_less_than_0.1

head(ddsDE, 10)

#contrasts functions with c(), used if multiple design factors aregiven. 
resultsNames(ddsDE)
par(mfrow=c(1,1))

#Change DESeq objects to R objects(dataframe), needed to perform filtering and arrangement
ddsDE_result <- as.data.frame(ddsDE_result)
class(ddsDE_result)

p_value <- ddsDE_result$pvalue
p_value
head(ddsDE_result)

#arrange in Ascending order of pvalue ddsDE_result_ordered <-
ddsDE_result <- ddsDE_result[order(ddsDE_result$padj),]
head(ddsDE_result, 4)

#To check whether the specific gene differentially expressed or not?
ddsDE_result["ENSG00000211663",]

#extract the most differentially expressed gene, log2fold change <1 or >1 with pvalue 0.01 
# filter based on p value < 0.01 filtered 
ddsDE_result %>% filter(ddsDE_result$padj < alpha)

# filter based on log2fold <1
filtered_lfc_g1 <- ddsDE_result %>% filter(abs(ddsDE_result$log2FoldChange)>1 )

# Retreiving set the filtered dimension of an object.
dim(ddsDE_result) 
dim(filtered_lfc_g1)

# dds_MA <- DESeq(ddsDE, quiet=TRUE) 
ddsDE_result

ddsDE_result_0.05 <- results(ddsDE, alpha = alpha)
summary(ddsDE_result_0.05)

pvalue_less_than_0.01 <- sum(ddsDE_result$padj < 0.01, na.rm=TRUE)
pvalue_less_than_0.01 <- sort(ddsDE_result$padj)
pvalue_less_than_0.01

head(assay(vsd), 3)
head(ddsDE_result,50)

library("vsn")
vsd <- vst(ddsDE, blind = F)
vsd_assay <- assay(vsd)

vsd_tassay <- t(vsd_assay)
head(vsd_tassay)

getwd()
write.csv(vsd_tassay, "vsd_assay_DDSDE_171sample_transpose.csv", sep = ",")
