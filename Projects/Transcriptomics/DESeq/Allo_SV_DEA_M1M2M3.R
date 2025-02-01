# Differential gene expression
## Using Surrogate variables (SVs)

# Differential Expression Analysis for Allocate groups SVs

# Model 1 - Including all SVs
# Model 2 - Includes SV of Independent variable + SVs correlated with covariates
# Model 3 - Model2 - SV of Independent variable

# Load required libraries and data
library(DESeq2)

# Model 1
ddsDE_sva_Allocation_M1 <- ddsDE_sva

# Add SVs to the design
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  ddsDE_sva_Allocation_M1[[col_name]] <- as.numeric(sampledata_Allocation[[col_name]])
}

# Set up design
design(ddsDE_sva_Allocation_M1) <- ~sv1 + sv2 + sv3 + sv4 + sv5 + sv6 + sv7 + sv8 + sv9 + sv10 + 
  sv11 + sv12 + sv13 + sv14 + sv15 + sv16 + sv17 + sv18 + sv19 + 
  sv20 + sv21 + Allocation

# Set reference for the factor
ddsDE_sva_Allocation_M1$Allocation <- factor(ddsDE_sva_Allocation_M1$Allocation, levels = c("A", "B"))

# Remove lowly expressed genes
keep <- rowSums(counts(ddsDE_sva_Allocation_M1)) >= 171
ddsDE_sva_Allocation_M1 <- ddsDE_sva_Allocation_M1[keep,]

# Run DESeq
ddsDE_sva_Allocation_M1 <- DESeq(ddsDE_sva_Allocation_M1)
ddsDE_sva_Allocation_M1_result <- results(ddsDE_sva_Allocation_M1)
summary(ddsDE_sva_Allocation_M1_result)

# Model 2
ddsDE_sva_Allocation_M2 <- ddsDE_sva

# Add SVs to the design
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  ddsDE_sva_Allocation_M2[[col_name]] <- as.numeric(sampledata_Allocation[[col_name]])
}

# Set up design
design(ddsDE_sva_Allocation_M2) <- ~sv1 + sv2 + sv3 + sv4 + sv11 + sv12 + sv13 + sv14 + sv15 +
  sv17 + Allocation

# Set reference for the factor
ddsDE_sva_Allocation_M2$Allocation <- factor(ddsDE_sva_Allocation_M2$Allocation, levels = c("A", "B"))

# Remove lowly expressed genes
keep <- rowSums(counts(ddsDE_sva_Allocation_M2)) >= 171
ddsDE_sva_Allocation_M2 <- ddsDE_sva_Allocation_M2[keep,]

# Run DESeq
ddsDE_sva_Allocation_M2 <- DESeq(ddsDE_sva_Allocation_M2)
ddsDE_sva_Allocation_M2_result <- results(ddsDE_sva_Allocation_M2)
summary(ddsDE_sva_Allocation_M2_result)

# Model 3
ddsDE_sva_Allocation_M3 <- ddsDE_sva

# Add SVs to the design
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  ddsDE_sva_Allocation_M3[[col_name]] <- as.numeric(sampledata_Allocation[[col_name]])
}

# Set up design
design(ddsDE_sva_Allocation_M3) <- ~cbmi + sv2 + sv3 + sv4 + sv11 + sv12 + sv13 + sv14 + sv15 +
  sv17 + Allocation

# Set reference for the factor
ddsDE_sva_Allocation_M3$Allocation <- factor(ddsDE_sva_Allocation_M3$Allocation, levels = c("A", "B"))

# Remove lowly expressed genes
keep <- rowSums(counts(ddsDE_sva_Allocation_M3)) >= 171
ddsDE_sva_Allocation_M3 <- ddsDE_sva_Allocation_M3[keep,]

# Run DESeq
ddsDE_sva_Allocation_M3 <- DESeq(ddsDE_sva_Allocation_M3)
ddsDE_sva_Allocation_M3_result <- results(ddsDE_sva_Allocation_M3, alpha = alpha)
summary(ddsDE_sva_Allocation_M3_result)

# Save results to CSV files
csv_m1 <- paste0("DEA_SVA_21_SVs_Allo.csv")
csv_m2 <- paste0("DEA_SVA_", design(ddsDE_sva_Allocation_M2)[2], ".csv")
csv_m3 <- paste0("DEA_SVA_", design(ddsDE_sva_Allocation_M3)[2], ".csv")

# Set working directory
getwd()
setwd("path/to/directory/ddsDE+SV")

# Write CSV files
write.csv(ddsDE_sva_Allocation_M1_result, csv_m1)
write.csv(ddsDE_sva_Allocation_M2_result, csv_m2)
write.csv(ddsDE_sva_Allocation_M3_result, csv_m3)
