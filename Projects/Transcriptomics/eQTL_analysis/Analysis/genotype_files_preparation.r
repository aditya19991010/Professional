#Preparing SNP details files for eQTL analysis
##generation of SNP ID with position on chormosome

setwd("/home/sumit2/MMNP_RNAseqdata/MMNP_eQTL/Matrix_eQTL_Analysis/01_Raw_Data/Genotype_Data/")
snp_id <- read.table("SNP_ID_data_Chr_ALL_MMNP_MCduo_info09_b37_171_23042018_trans_mod2.txt", sep = "\t", header = T)


# Create a new column to specify the condition for separation
snp_id_data$condition <- ifelse(grepl("^[A-Za-z]", snp_id_data$snp_id), "alphabet", "numeric")


# Separate the SNP column based on the condition
snp_id_data <- snp_id_data %>%
  separate(CHR.SNP, into = c("chr","snp_id", "position", "ref", "alt"), sep = ":",
           extra = "drop",
           convert = TRUE,
           remove = FALSE) %>%
  mutate(snp_id = ifelse(condition == "alphabet", snp_id, paste(snp_id, position, sep = ":")))
snp_id_data$condition == "numeric"

snp_id_data.final <- snp_id_data[, c("snp_id","chrCHR","POS")]

write.csv(snp_id_data.final, "SNP_ID_ChrPos_ALL_MMNP_MCduo_info09_b37_171_23042018_trans_mod3.txt")

snp_id.only <- snp_id_data[, c("snp_id")]

write.csv(snp_id.only, "SNP_ID_only_MMNP_MCduo_info09_b37_171_23042018_trans.txt")
