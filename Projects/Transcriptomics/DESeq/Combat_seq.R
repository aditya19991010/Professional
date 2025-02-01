# Using Combat package for Batch correction

#Installing packages
if (!("clusterProfiler" %in% installed.packages())) {
  # Install this package if it isn't installed yet
  BiocManager::install("clusterProfiler", update = FALSE)
}

if (!("msigdbr" %in% installed.packages())) {
  # Install this package if it isn't installed yet
  BiocManager::install("msigdbr", update = FALSE)
}

if (!("org.Hs.eg.db" %in% installed.packages())) {
  # Install this package if it isn't installed yet
  BiocManager::install("org.Hs.eg.db", update = FALSE)
}

# Attach the library
library(clusterProfiler)

# Package that contains MSigDB gene sets in tidy format
library(msigdbr)

# Human annotation package we'll use for gene identifier conversion
library(org.Mm.eg.db)

# We will need this so we can use the pipe: %>%
library(magrittr)

library('sva')
library('limma')

rm_batcheffect <- removeBatchEffect(rawcounts, sampleData$Batch) 
rm_batcheffect
adjusted_counts <- ComBat_seq(rawcounts, batch=sampleData$Batch, group=sampleData$Allocation)

cov1 <- as.data.frame(sampleData$cov1)
cov2 <- as.matrix(sampleData$cov2)
covar_mat <- cbind(cov1, cov2)
vsd_assay <- assay(vsd)

adjusted_counts <- ComBat_seq(vsd_assay, batch= sampleData$Batch, batch2 = sampleData$cov2, group = sampleData$Allocation, covar_mod = covar_mat)
adjusted_counts <- round(adjusted_counts)

View(adjusted_counts)
getwd()

write.csv(adjusted_counts, file = "adjustedCount.csv") 

non_integer_values <- adjusted_counts[!is.integer(adjusted_counts)]
view(non_integer_values)

plotPCA(adjusted_counts, intgroup="cov2")
