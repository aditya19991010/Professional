# Load required libraries
library(sva)
BiocManager::install("SummarizedExperiment", force = TRUE)
library("SummarizedExperiment")
install.packages("rafalib")
library(Glimma)
library(rafalib)

# Preprocess data
ddsDE_sva <- ddsDE
norm.cts <- counts(ddsDE_sva, normalized=TRUE)
norm.cts <- norm.cts[rowSums(norm.cts) > 171,]

sampledata_sv <- sampleData
sampledata_BMI <- sampledata_sv
sampledata_Allocation <- sampledata_sv

# Create data frames for storing test results
KW_data <- data.frame(row.names = c("Allocation", "BMI", "csex", "Batch", "cbmi"))
wilcox_data <- data.frame(row.names = c("Allocation", "BMI", "csex", "Batch", "cbmi"))

# Set up design
design_sv = ~sampledata_sv$cbmi + as.factor(sampledata_sv$csex) +  
  as.factor(sampledata_sv$Batch) + as.factor(sampledata_sv$Allocation) + 
  as.factor(sampledata_sv$BMI)
design_null = ~sampledata_sv$cbmi + as.factor(sampledata_sv$csex) +  
  as.factor(sampledata_sv$Batch) + as.factor(sampledata_sv$Allocation)
mm <- model.matrix(design_sv, colData(ddsDE_sva))
mm0 <- model.matrix(design_null , colData(ddsDE_sva))

# Find surrogate variables
n.sv = num.sv(rawcounts, mm, method="leek")
fit <- svaseq(norm.cts, mod=mm, mod0=mm0)
num_cols_to_paste <- fit$n.sv

# Add surrogate variables to sampledata
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  sampledata_Allocation[[col_name]] <- as.numeric(fit$sv[, i])
  sampledata_BMI[[col_name]] <- as.numeric(fit$sv[, i])
}

# Perform statistical tests and store results in KW_data and wilcox_data
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  kruskal_result <- kruskal.test(get(col_name) ~ cbmi, data = sampledata_BMI)
  KW_data[5, col_name] <- kruskal_result$p.value
  
  WC_data <- wilcox.test(get(col_name) ~ Batch, data = sampledata_BMI, exact = FALSE)
  wilcox_data[4, col_name] <- WC_data$p.value
}


# View results
View(KW_data)
view(wilcox_data)

# Save results to CSV files
csv_file_name_wc <- paste0("MMNO_svs_wilcox_test", design_sv[2], ".csv")
csv_file_name_KW <- paste0("MMNO_svs_KW_test", design_sv[2], ".csv")
write.csv(wilcox_data, file = csv_file_name_wc) 
write.csv(KW_data, file = csv_file_name_KW) 

# Add surrogate variable data to sampledata_matrix
sampledata_matrix <- sampledata_BMI

# Additional data manipulations...

# Visualizations and exploratory analysis...

# Read gene expression and covariate files
expData_file_name <- system.file("folder containing the data", "CAD_Expression.csv", package="ExpressionNormalizationWorkflow")
exprs <- read.table(expData_file_name, header=TRUE, sep=",", row.names=1, as.is=TRUE)

expDesign_file_name <- system.file("folder containing the data", "CAD_ExptDsgn.csv", package="ExpressionNormalizationWorkflow")
covrts <- read.table(expDesign_file_name, header=TRUE, sep=",", row.names=1, as.is=TRUE)
