# Differential Allocation of Surrogate Variables (SVs) using DESeq2

# ============================
# Initialization and Settings
# ============================

# Set the working directory for output
output_dir <- "F:/Aditya/MMNP_DEA/Output/csv/ddsDE+_SV"
setwd(output_dir)

# Minimum counts threshold to retain genes
min_counts_threshold <- 171

# Alpha for DESeq results
alpha <- 0.05

# ============================
# Helper Function Definitions
# ============================

# Add surrogate variables (SVs) to the design matrix
add_surrogate_variables <- function(dds, sampledata, num_svs) {
  for (i in 1:num_svs) {
    col_name <- paste0("sv", i)
    dds[[col_name]] <- as.numeric(sampledata[[col_name]])
  }
  return(dds)
}

# Run DESeq pipeline
run_deseq <- function(dds, design_formula, allocation_levels, output_file) {
  # Set the design formula
  design(dds) <- design_formula
  
  # Set reference levels for the Allocation factor
  dds$Allocation <- factor(dds$Allocation, levels = allocation_levels)
  
  # Filter lowly expressed genes
  keep <- rowSums(counts(dds)) >= min_counts_threshold
  dds <- dds[keep, ]
  
  # Perform DESeq analysis
  dds <- DESeq(dds)
  
  # Save results
  results_data <- results(dds, alpha = alpha)
  write.csv(results_data, file = output_file)
  
  # Display summary
  print(summary(results_data))
  return(results_data)
}

# ============================
# Model Implementations
# ============================

# Common settings
num_svs <- 21  # Total surrogate variables
allocation_levels <- c("A", "B")  # Reference levels for the Allocation factor

# Sample data with surrogate variables
ddsDE_sva <- ddsDE_sva  # Original DESeq object
sampledata_Allocation <- sampledata_Allocation  # Dataframe with surrogate variables

# ---------
# Model 1: Include All SVs
# ---------

cat("Running Model 1: All SVs\n")
ddsDE_sva_M1 <- add_surrogate_variables(ddsDE_sva, sampledata_Allocation, num_svs)
design_formula_M1 <- as.formula(paste("~", paste0("sv", 1:num_svs, collapse = " + "), "+ Allocation"))
output_file_M1 <- "MMNP_DEA+SVA_21_SVs_Allo.csv"
ddsDE_sva_Allocation_M1_result <- run_deseq(ddsDE_sva_M1, design_formula_M1, allocation_levels, output_file_M1)

# ---------
# Model 2: Subset of SVs (including Allocation and covariate-related SVs)
# ---------

cat("Running Model 2: Subset of SVs\n")
subset_svs_M2 <- c(1, 2, 3, 4, 11, 12, 13, 14, 15, 17)
ddsDE_sva_M2 <- add_surrogate_variables(ddsDE_sva, sampledata_Allocation, num_svs)
design_formula_M2 <- as.formula(paste("~", paste0("sv", subset_svs_M2, collapse = " + "), "+ Allocation"))
output_file_M2 <- "MMNP_DEA+SVA_Subset_SVs.csv"
ddsDE_sva_Allocation_M2_result <- run_deseq(ddsDE_sva_M2, design_formula_M2, allocation_levels, output_file_M2)

# ---------
# Model 3: Subset of SVs (excluding independent variable-related SVs)
# ---------

cat("Running Model 3: Reduced Subset of SVs\n")
subset_svs_M3 <- c(2, 3, 4, 11, 12, 13, 14, 15, 17)
ddsDE_sva_M3 <- add_surrogate_variables(ddsDE_sva, sampledata_Allocation, num_svs)
design_formula_M3 <- as.formula(paste("~", paste0("sv", subset_svs_M3, collapse = " + "), "+ Allocation"))
output_file_M3 <- "MMNP_DEA+SVA_Reduced_SVs.csv"
ddsDE_sva_Allocation_M3_result <- run_deseq(ddsDE_sva_M3, design_formula_M3, allocation_levels, output_file_M3)

# ============================
# Summary of Results
# ============================

cat("Model 1 Results:\n")
print(head(ddsDE_sva_Allocation_M1_result))

cat("Model 2 Results:\n")
print(head(ddsDE_sva_Allocation_M2_result))

cat("Model 3 Results:\n")
print(head(ddsDE_sva_Allocation_M3_result))
