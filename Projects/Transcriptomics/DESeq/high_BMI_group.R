getwd() 
setwd("F:/Aditya/MMNP_DEA/input/ftcount/") 
rawcounts <- read.csv(file = "F:/Aditya/MMNP_DEA/input/Batch123_trimmed_rawcounts_mod2.txt", sep = "\t", row.names = 1) 
sampleData <- read.csv(file ="../Pheno_file_MMNPC_171_v2.csv", header = TRUE, sep = ",")


#Stratifying gender data

high_BMI_Sampledata <- sampleData %>% filter(sampleData$BMI == "high")
low_BMI_Sampledata <- sampleData %>% filter(sampleData$BMI == "low")

colnames(rawcounts)

# Fetch names from male_Sampledata$X
high_BMI_sample_names <- high_BMI_Sampledata$X
low_BMI_sample_names <- low_BMI_Sampledata$X

high_BMI_sample_names

selected_columns <- rawcounts[, low_BMI_sample_names]

selected_columns

# Create another object to store the selected column data
highBMI_rawcounts <- selected_columns

#design for High BMI group
design = ~ cbmi + csex + Batch + Allocation
alpha = 0.05

dds <- DESeqDataSetFromMatrix(countData = highBMI_rawcounts, colData = high_BMI_Sampledata, design = design)

# set reference for the factor
# dds$csex <- factor(dds$csex, levels = c("1", "2"))
dds$Allocation <- factor(dds$Allocation, levels = c("A","B"))
# dds$Batch <- factor(dds$Batch, levels = c("1","2","3"))


#checking NA values
# row_has_na <- any(is.na(rawcounts[3, ]))
# col_has_na <- any(is.na(sampleData[, 1]))

#remove lowely expressed genes 
keep <- rowSums(counts(dds)) >= 71
dds<- dds[keep,]

# set factor level
# dds$Allocation <- relevel(dds$Allocation, ref = "B")

#NOTE: collapse technical replicates, never collapse biological replicates

# main DESeq
ddsDE_high_BMI <- DESeq(dds)
norm_count <- estimateSizeFactors(dds)
ddsDE_highBMI_result <- results(ddsDE_high_BMI)
summary(ddsDE_highBMI_result)

setwd("F:/Aditya/MMNP_DEA/Output/csv/")
write.csv(ddsDE_highBMI_result,"MMNP_DEA_ddsDE_highBMI_result.csv" )

ddsDE_highBMI_sva <- ddsDE_high_BMI
norm.cts <- counts(ddsDE_highBMI_sva, normalized=TRUE)
norm.cts <- norm.cts[rowSums(norm.cts) > 71,]
write.csv(x = norm.cts, file = "MMNP_DEA_ddsDE_highBMI_normcounts.csv", sep = ",",)

#Duplicate highBMI phenotype data
high_BMI_sampledata_sv <- high_BMI_Sampledata


# Create KW_data to paste pvalues from tests
KW_data <- data.frame(row.names = c("Allocation", "csex", "Batch", "cbmi"))

#set up design
design_sv = ~ high_BMI_Sampledata$cbmi + as.factor(high_BMI_Sampledata$csex) +  as.factor(high_BMI_Sampledata$Batch) + as.factor(high_BMI_Sampledata$Allocation)
design_null = ~ high_BMI_Sampledata$cbmi + as.factor(high_BMI_Sampledata$csex) + as.factor(high_BMI_Sampledata$Batch)
mm <- model.matrix(design_sv, colData(ddsDE_sva))
mm0 <- model.matrix(design_null , colData(ddsDE_sva))

# n.sv = num.sv(rawcounts,mm,method="leek")
# n.sv

fit <- svaseq(norm.cts, mod=mm, mod0=mm0)
fit$n.sv

num_cols_to_paste <- fit$n.sv

# Create a loop to paste the columns
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  high_BMI_sampledata_sv[[col_name]] <- paste0(fit$sv[, i])
  high_BMI_sampledata_sv[[col_name]] <- as.numeric(high_BMI_sampledata_sv[[col_name]])
}

# Create a loop to paste the pvalues in KW test
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  kruskal_result <- kruskal.test(get(col_name)  ~ cbmi, data = high_BMI_sampledata_sv)
  KW_data[4, col_name] <- kruskal_result$p.value
}


# #Model3
# design for DESeq  

ddsDE_sva_highBMI_M3 <- ddsDE_highBMI_sva


for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  ddsDE_sva_highBMI_M3[[col_name]] <- paste0(high_BMI_sampledata_sv[[col_name]])
  ddsDE_sva_highBMI_M3[[col_name]] <- as.numeric(high_BMI_sampledata_sv[[col_name]])
}

design(ddsDE_sva_highBMI_M3) <- ~ sv2 + sv3 + sv4 + sv11 + Allocation

# # set reference for the factor
ddsDE_sva$Allocation <- factor(dds$Allocation, levels = c("A","B"))
# ddsDE_sva_highBMI_M3$BMI <- factor(ddsDE_sva_highBMI_M3$BMI, levels = c("high", "low"))

#remove lowely expressed genes 
keep <- rowSums(counts(ddsDE_sva_highBMI_M3)) >= 71
ddsDE_sva_highBMI_M3 <- ddsDE_sva_highBMI_M3[keep,]

# main DESeq
ddsDE_sva_highBMI_M3 <- DESeq(ddsDE_sva_highBMI_M3)
ddsDE_sva_highBMI_M3_result <- results(ddsDE_sva_highBMI_M3)
summary(ddsDE_sva_highBMI_M3_result)

write.csv(ddsDE_sva_highBMI_M3_result,"MMNP_DEA_ddsDE_highBMI_with_SV_result.csv" )
