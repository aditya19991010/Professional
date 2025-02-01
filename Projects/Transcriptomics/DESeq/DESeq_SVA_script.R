# Differential analysis using Surrogate variable

library("limma") 
library("edgeR")

BiocManager::install("DESeq2")
library("DESeq2")
BiocManager::install("apeglm")
library("apeglm")
library("tidyverse")
library(pheatmap) 
library(ggplot2) 
library(ggrepel)
library(RColorBrewer) 
library(dplyr) 
BiocManager::install("Glimma")
library(Glimma)
library(sva)
BiocManager::install("EnhancedVolcano")
library(EnhancedVolcano)
library("BiocParallel")

register(SnowParam(8))

getwd() 
setwd("/Users/sumitpaliwal/Library/CloudStorage/OneDrive-Personal/CCMB/CCMB2022/MMNP/For_RNA-seq/DESeq_data")
Data_rawcounts <- read.csv(file = "Batch123_trimmed_rawcounts_mod.txt", sep = "\t", row.names = 1) 
head(Data_rawcounts)
# colnames_rawcount <- colnames(rawcounts)

# write.csv(colnames_rawcount, file = "colnames_Batch123.txt")

Data_PhenoData <- read.csv(file = "Pheno_file_Data_.csv", header = TRUE, sep = ",")
Data_PhenoData$Batch <- factor(Data_PhenoData$Batch)
Data_PhenoData$cov2 <- factor(Data_PhenoData$cov2)
Data_PhenoData$cov1 <- factor(Data_PhenoData$cov1, levels = c("low","high"))
Data_PhenoData$Allocation <- factor(Data_PhenoData$Allocation, levels = c("A","B"))

str(Data_PhenoData)

female_Data_PhenoData <- Data_PhenoData %>% filter(Data_PhenoData$cov2 == 2)
male_Data_PhenoData <- Data_PhenoData %>% filter(Data_PhenoData$cov2 == 1)


colnames(Data_PhenoData)


#design for effect of allocation on sex
design1 = ~cov1 + Batch + cov2 + cov3 + Allocation
alpha = 0.05

Data_dds1 <- DESeqDataSetFromMatrix(countData = Data_rawcounts, colData = Data_PhenoData, design = design1)

# norm_count <- estimateSizeFactors(ddsDE)
# sizeFactors(norm_count)

# norm_count <- counts(norm_count, normalized = T)

#checking NA values
# row_has_na <- any(is.na(rawcounts[3, ]))
# col_has_na <- any(is.na(sampleData[, 1]))

# # set reference for the factor
# dds$cov2 <- factor(dds$cov2, levels = c("1", "2"))
# dds$Allocation <- factor(dds$Allocation, levels = c("A","B"))
# dds$cov1 <- factor(dds$cov1, levels = c("high", "low"))
# dds$Batch <- factor(dds$Batch, levels = c("1","2","3"))


#remove lowely expressed genes 
# keep <- rowSums(counts(dds)) >= 
# dds<- dds[keep,]

#keep <- rowSums(counts(dds)) >= 10
keep <- rowSums(counts(Data_dds1) >= 2) >= 71
keep2 <- rowSums(counts(Data_dds1) >= 1) >= 71
Data_dds1_keep <- Data_dds1[keep,]
Data_dds1_keep2 <- Data_dds1[keep2,]
# set factor level
# dds$Allocation <- relevel(dds$Allocation, ref = "A")

#NOTE: collapse technical replicates, never collapse biological replicates

# main DESeq
Data_dds1 <- DESeq(Data_dds1)
Data_dds1_result <- results(Data_dds1)
Data_dds1_result_ordered <- Data_dds1_result[order(Data_dds1_result$padj),]
head(Data_dds1_result_ordered)
summary(Data_dds1_result)

Data_dds1_keep <- DESeq(Data_dds1_keep)
Data_dds1_keep_result <- results(Data_dds1_keep)
Data_dds1_keep_result_ordered <- Data_dds1_keep_result[order(Data_dds1_keep_result$padj),]
head(Data_dds1_keep_result_ordered)
summary(Data_dds1_keep_result)

Data_dds1_keep2 <- DESeq(Data_dds1_keep2)
Data_dds1_keep2_result <- results(Data_dds1_keep2)
Data_dds1_keep2_result_ordered <- Data_dds1_keep2_result[order(Data_dds1_keep2_result$padj),]
head(Data_dds1_keep2_result_ordered)
summary(Data_dds1_keep2_result)

#### SVA analysis
Data_dds1_dat <- counts(Data_dds1, normalized=TRUE)
Data_dds1_idx <- rowMeans(Data_dds1_dat) > 1
Data_dds1_dat <- Data_dds1_dat[Data_dds1_idx,]

# Data_dds1_mod <- model.matrix(~ Allocation, colData(Data_dds1))
# Data_dds1_mod0 <- model.matrix(~ 1, colData(Data_dds1))

Data_dds1_cov_mod <- model.matrix(~ as.factor(cov1) + as.factor(Batch) + as.factor(cov2) + ccov1 + Allocation, colData(Data_dds1))
Data_dds1_cov_mod0 <- model.matrix(~ as.factor(cov1) + as.factor(Batch) + as.factor(cov2) + ccov1, colData(Data_dds1))

Data_dds1_cov_svseq <- svaseq(Data_dds1_dat, Data_dds1_cov_mod, Data_dds1_cov_mod0)
Data_dds1_cov_svseq$sv

# par(mfrow=c(5,3), mar=c(3,5,3,1))
# stripchart(Data_dds1_svseq$sv)

Data_dds1_sva <- Data_dds1
Data_dds1_sva$SV1 <- Data_dds1_svseq$sv[,1]
Data_dds1_sva$SV2 <- Data_dds1_svseq$sv[,2]
Data_dds1_sva$SV3 <- Data_dds1_svseq$sv[,3]
Data_dds1_sva$SV4 <- Data_dds1_svseq$sv[,4]
Data_dds1_sva$SV5 <- Data_dds1_svseq$sv[,5]
Data_dds1_sva$SV6 <- Data_dds1_svseq$sv[,6]
Data_dds1_sva$SV7 <- Data_dds1_svseq$sv[,7]
Data_dds1_sva$SV8 <- Data_dds1_svseq$sv[,8]
Data_dds1_sva$SV9 <- Data_dds1_svseq$sv[,9]
Data_dds1_sva$SV10 <- Data_dds1_svseq$sv[,10]
Data_dds1_sva$SV11 <- Data_dds1_svseq$sv[,11]
Data_dds1_sva$SV12 <- Data_dds1_svseq$sv[,12]
Data_dds1_sva$SV13 <- Data_dds1_svseq$sv[,13]
Data_dds1_sva$SV14 <- Data_dds1_svseq$sv[,14]
Data_dds1_sva$SV15 <- Data_dds1_svseq$sv[,15]

design(Data_dds1_sva) <- ~ SV1 + SV2 + SV3 + SV4 + SV5 + SV6 + SV7 + SV8 + SV9 + SV10 + SV11 + SV12 + SV13 + SV14 + SV15 + Allocation

Data_dds1_sva <- DESeq(Data_dds1_sva)

Data_dds1_sva_result <- results(Data_dds1_sva)
summary(Data_dds1_sva_result)
Data_dds1_sva_result_ordered <- Data_dds1_sva_result[order(Data_dds1_sva_result$padj),]

ddsDE_result_0.05 <- results(ddsDE, alpha = alpha)
summary(ddsDE_result_0.05)

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
summary(vsd)

ddsDE_result_0.05 <- results(ddsDE, alpha = alpha)
summary(ddsDE_result_0.05)

pvalue_less_than_0.01 <- sum(ddsDE_result$padj < 0.01, na.rm=TRUE)
pvalue_less_than_0.01 <- sort(ddsDE_result$padj)
pvalue_less_than_0.01

head(ddsDE_result,50) 


library("vsn")
vsd <- vst(ddsDE, blind = F)

head(assay(vsd), 3)


