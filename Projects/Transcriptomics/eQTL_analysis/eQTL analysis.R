
install.packages("MatrixEQTL")
library(MatrixEQTL)

#importing Toy dataset
base.dir = find.package("MatrixEQTL")
base.dir

SNP_file_name <- paste(file = "http://www.bios.unc.edu/research/genomic_software/Matrix_eQTL/Sample_Data/SNP.txt", sep = "" )
head(SNP_file_name)

gene_file_name <- paste(base.dir, "/data/GE.txt", sep = "")
head(expression)

covariates_file_name <- paste(base.dir,  "/data/Covariates.txt", sep = "")
head(covariates_file_name)

gene_location_file_name <- paste(f <- <- 