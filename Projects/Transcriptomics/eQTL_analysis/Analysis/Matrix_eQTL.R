# Matrix eQTL 

library(MatrixEQTL)
library("BiocParallel")
register(SnowParam(30))

## Location of the package with the data files.

## Settings
# Linear model to use, modelANOVA, modelLINEAR, or modelLINEAR_CROSS
useModel = modelLINEAR # modelANOVA, modelLINEAR, or modelLINEAR_CROS

getwd()
setwd(dir = "/home/sumit2/MMNP_RNAseqdata/MMNP_eQTL/Matrix_eQTL_Analysis/")

# Input 5 files
## Genotype and SNPs location file name
SNP_file_name = paste0(file = "01_Raw_Data/Genotype_Data/Chr_ALL_MMNP_MCduo_info09_b37_171_QC_EDITED_FINAL_23042018_trans_mod3.traw")
snpspos = read.table(file = "01_Raw_Data/Genotype_Data/SNP_ID_ChrPos_ALL_MMNP_MCduo_info09_b37_171_23042018_trans_mod3.txt", header = T, stringsAsFactors = T, sep = ",", rownames = 1);


## Gene expression and location file name
expression_file_name = paste0("01_Raw_Data/Gene_Expression_Data/GExp_deg.csv")

## Add Gene_hBMI_lft_data.csv for 38k genes
genepos = read.table(file = "01_Raw_Data/Gene_Expression_Data/Gene_DEGs_lft_GRCh37.csv", header = FALSE, stringsAsFactors = FALSE, sep = ",")


# Covariates file name
# Set to character() for no covariates
  #Allocation, A == 1, BMI, high == 1

covariates_file_name = paste0("01_Raw_Data/PhenoData_171sample.csv");

# Output file name
output_file_name_cis = tempfile();
output_file_name_tra = tempfile();

# Only associations significant at this level will be saved
pvOutputThreshold_cis = 2e-2;
pvOutputThreshold_tra = 1e-2;

# Error covariance matrix
# Set to numeric() for identity.
errorCovariance = numeric();
# errorCovariance = read.table("Sample_Data/errorCovariance.txt");
# Distance for local gene-SNP pairs

cisDist = 1e6;

## Load genotype data
snps = SlicedData$new();
snps$fileDelimiter = " "; # the TAB character
snps$fileOmitCharacters = "NA"; # denote missing values;
snps$fileSkipRows = 1; # one row of column labels
snps$fileSkipColumns = 1; # one column of row labels
snps$fileSliceSize = 5000; # read file in slices of 2,000 rows
snps$LoadFile(SNP_file_name)

## Load gene expression data
gene = SlicedData$new();
gene$fileDelimiter = ","; # the TAB character
gene$fileOmitCharacters = "NA"; # denote missing values;
gene$fileSkipRows = 1; # one row of column labels
gene$fileSkipColumns = 1; # one column of row labels
gene$fileSliceSize = 2000; # read file in slices of 2,000 rows
gene$LoadFile(expression_file_name);

## Load covariates
cvrt = SlicedData$new();
cvrt$fileDelimiter = ","; # the TAB character
cvrt$fileOmitCharacters = "NA"; # denote missing values;
cvrt$fileSkipRows = 1; # one row of column labels
cvrt$fileSkipColumns = 1; # one column of row labels
if(length(covariates_file_name)>0) {
cvrt$LoadFile(covariates_file_name);
}

## Run the analysis

me.hist = Matrix_eQTL_main(
  snps = snps,
  gene = gene,
  #cvrt = cvrt,
  output_file_name = output_file_name_tra,
  pvOutputThreshold = pvOutputThreshold_tra,
  useModel = useModel,
  errorCovariance = errorCovariance,
  verbose = TRUE,
  output_file_name.cis = output_file_name_cis,
  pvOutputThreshold.cis = pvOutputThreshold_cis,
  snpspos = snpspos,
  genepos = genepos,
  cisDist = cisDist,
  pvalue.hist = TRUE,
  min.pv.by.genesnp = FALSE,
  noFDRsaveMemory = FALSE);

unlink(output_file_name_tra);
unlink(output_file_name_cis);
## Results:
log_file_path <- "05_Results/Summary_Reports/log_summary_eQTL_MMNP_8DEG_info09_QC_genotype_GExp.txt"
# Open the log file for writing
sink(log_file_path, append = FALSE)


cat('Analysis done in: ', me$time.in.sec, ' seconds', '\n');
cat('Detected local eQTLs:', '\n');
show(me$cis$eqtls)
cat('Detected distant eQTLs:', '\n');
show(me$trans$eqtls)

# Close the log file
sink()

me.qq = Matrix_eQTL_main(
  snps = snps,
  gene = gene,
  #cvrt = cvrt,
  output_file_name = output_file_name_tra,
  pvOutputThreshold = pvOutputThreshold_tra,
  useModel = useModel,
  errorCovariance = errorCovariance,
  verbose = TRUE,
  output_file_name.cis = output_file_name_cis,
  pvOutputThreshold.cis = pvOutputThreshold_cis,
  snpspos = snpspos,
  genepos = genepos,
  cisDist = cisDist,
  pvalue.hist = "qqplot",
  min.pv.by.genesnp = FALSE,
  noFDRsaveMemory = FALSE);

unlink(output_file_name_tra);
unlink(output_file_name_cis);
## Results:
log_file_path <- "05_Results/Summary_Reports/log_summary_eQTL_MMNP_8DEG_info09_QC_genotype_GExp.txt"
# Open the log file for writing
sink(log_file_path, append = FALSE)


cat('Analysis done in: ', me.hist$time.in.sec, ' seconds', '\n');
cat('Detected local eQTLs:', '\n');
show(me.hist$cis$eqtls)
cat('Detected distant eQTLs:', '\n');
show(me.hist$trans$eqtls)

# Close the log file
sink()

pdf(file = "05_Results/eQTL_Results/qq plot_MMNP_8DEG_info09_QC_GExp vs Density_QC_SNPs_eQTL_MMNP.pdf",title = "eQTL_MMNP", compress = TRUE, paper = 'a4r')
## Make the histogram of local and distant p-values
plot(me.qq)

dev.off()

