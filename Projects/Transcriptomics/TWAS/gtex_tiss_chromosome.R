source("code/gtex_v7_nested_cv_elnet.R")
"%&%" <- function(a,b) paste(a,b, sep='')

argv <- commandArgs(trailingOnly = TRUE)
chrom <- argv[1]
chrom <- 1

#tiss <- argv[1]
#chrom <- argv[2]

PATH = "/home/sumit2/tools/MetaXcan/PredictDB-Tutorial/data_MMNP/output"
snp_annot_file <- PATH %&% "/snp_annot.chr" %&% chrom %&% ".txt"
gene_annot_file <- PATH %&% "/gene_annot_v2.parsed.txt"
genotype_file <- PATH %&% "/genotype.chr" %&% chrom %&% ".txt"
expression_file <- PATH %&%  "/transformed_expression_clean_TPM_logTrans_quantNorm_limma_adj_SV_v3.txt"
covariates_file <- PATH %&%  "/PhenoData_171sample_mod1.csv"
prefix <- "Model_training"

main(snp_annot_file, gene_annot_file, genotype_file, expression_file, covariates_file, as.numeric(chrom), prefix, null_testing=FALSE)