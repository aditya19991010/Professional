#eQTL requires clean genotype and gene expression file
## Using imputed subsetted genotyped VCF file

#_______________________

#Plink

conda activate /home/sumit2/miniforge3/

plink
  --double-id
  --extract /home/sumit2/MMNP_RNAseqdata/MMNP_eQTL/Matrix_eQTL_Analysis/01_Raw_Data/rs_ID_info09_MMNP.txt
  --geno 0.05
  --hwe 1e-6
  --maf 0.05
  --make-bed
  --out Chr_ALL_MMNP_MCduo_info09_b37_171_QC_EDITED_FINAL_23042018_trans.raw
  --pca
  --recode A-transpose
  --test-mishap
  --threads 30
  --vcf Chr_ALL_MMNP_MCduo_info05_b37_171_QC_EDITED_filtered_data.vcf

# removing undwanted columns 
awk '{ for (i = 1; i <= NF; i++) if (i != 1 && i != 3 && i != 4 && i != 5 && i != 6) printf "%s%s", $i, (i==NF ? "\n" : FS) }' Chr_ALL_MMNP_MCduo_info09_b37_171_QC_EDITED_FINAL_23042018_trans.raw.traw > Chr_ALL_MMNP_MCduo_info09_b37_171_QC_EDITED_FINAL_23042018_trans_mod.traw


## create SNP position files
# Col1 = SNP, Col2 = chr, Col3=POS

awk '{print $1":"$2, "\t","chr"$1, "\t" $4}' Chr_ALL_MMNP_MCduo_info09_b37_171_QC_EDITED_FINAL_23042018_trans.raw.traw > SNP_ID_data_Chr_ALL_MMNP_MCduo_info09_b37_171_23042018_trans_mod2.txt

#>> continute in R

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
snp_id_data[99972,]

snp_id_data.final <- snp_id_data[, c("snp_id","chrCHR","POS")]

write.csv(snp_id_data.final, "SNP_ID_ChrPos_ALL_MMNP_MCduo_info09_b37_171_23042018_trans_mod3.txt")

snp_id.only <- snp_id_data[, c("snp_id")]

write.csv(snp_id.only, "SNP_ID_only_MMNP_MCduo_info09_b37_171_23042018_trans.txt")
