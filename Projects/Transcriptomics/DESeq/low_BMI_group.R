#design for low BMI group
design = ~ cbmi + csex + Batch + Allocation
alpha = 0.05

dds <- DESeqDataSetFromMatrix(countData = lowBMI_rawcounts, colData = low_BMI_Sampledata, design = design)

norm_count <- estimateSizeFactors(dds)
sizeFactors(norm_count)


# # set reference for the factor
# dds$csex <- factor(dds$csex, levels = c("1", "2"))
dds$Allocation <- factor(dds$Allocation, levels = c("A","B"))
# dds$Batch <- factor(dds$Batch, levels = c("1","2","3"))


#checking NA values
# row_has_na <- any(is.na(rawcounts[3, ]))
# col_has_na <- any(is.na(sampleData[, 1]))

#remove lowely expressed genes 
keep <- rowSums(counts(dds)) >= 100
dds<- dds[keep,]

# set factor level
# dds$Allocation <- relevel(dds$Allocation, ref = "B")

#NOTE: collapse technical replicates, never collapse biological replicates

# main DESeq
ddsDE_lowBMI <- DESeq(dds)
ddsDE_lowBMI_result <- results(ddsDE_lowBMI)
summary(ddsDE_lowBMI_result)


setwd("F:/Aditya/MMNP_DEA/Output/csv/")
write.csv(ddsDE_lowBMI_result,"MMNP_DEA_ddsDE_lowBMI_result.csv" )


ddsDE_lowBMI_sva <- ddsDE_lowBMI
norm.cts <- counts(ddsDE_lowBMI_sva, normalized=TRUE)
norm.cts <- norm.cts[rowSums(norm.cts) > 100,]

low_BMI_sampledata_sv <- low_BMI_Sampledata


# Create KW_data to paste pvalues from tests
KW_data <- data.frame(row.names = c("Allocation", "csex", "Batch", "cbmi"))

#set up design
design_sv = ~ low_BMI_Sampledata$cbmi + as.factor(low_BMI_Sampledata$csex) +  as.factor(low_BMI_Sampledata$Batch) + as.factor(low_BMI_Sampledata$Allocation)
design_null = ~ low_BMI_Sampledata$cbmi + as.factor(low_BMI_Sampledata$csex) + as.factor(low_BMI_Sampledata$Batch)
mm <- model.matrix(design_sv, colData(ddsDE_lowBMI_sva))
mm0 <- model.matrix(design_null , colData(ddsDE_lowBMI_sva))

# n.sv = num.sv(rawcounts,mm,method="leek")
# n.sv

fit <- svaseq(norm.cts, mod=mm, mod0=mm0)
fit$n.sv

num_cols_to_paste <- fit$n.sv

# Create a loop to paste the columns
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  low_BMI_sampledata_sv[[col_name]] <- paste0(fit$sv[, i])
  low_BMI_sampledata_sv[[col_name]] <- as.numeric(low_BMI_sampledata_sv[[col_name]])
}

# Create a loop to paste the pvalues in KW test
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
    kruskal_result <- kruskal.test(get(col_name)  ~ cbmi, data = low_BMI_sampledata_sv)
  KW_data[4, col_name] <- kruskal_result$p.value
}

# #Model3
# design for DESeq  

ddsDE_sva_lowBMI_M3 <- ddsDE_lowBMI_sva

for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  ddsDE_sva_lowBMI_M3[[col_name]] <- paste0(low_BMI_sampledata_sv[[col_name]])
  ddsDE_sva_lowBMI_M3[[col_name]] <- as.numeric(low_BMI_sampledata_sv[[col_name]])
}

design(ddsDE_sva_lowBMI_M3) <- ~ sv1 + sv2 + sv3 + sv4 + sv11  + sv13 + sv17 + Allocation

# # set reference for the factor
ddsDE_sva_lowBMI_M3$Allocation <- factor(ddsDE_sva_lowBMI_M3$Allocation, levels = c("A","B"))
# ddsDE_sva_lowBMI_M3$BMI <- factor(ddsDE_sva_lowBMI_M3$BMI, levels = c("low", "low"))

#remove lowely expressed genes 
keep <- rowSums(counts(ddsDE_sva_lowBMI_M3)) >= 100
ddsDE_sva_lowBMI_M3 <- ddsDE_sva_lowBMI_M3[keep,]

# main DESeq
ddsDE_sva_lowBMI_M3 <- DESeq(ddsDE_sva_lowBMI_M3)
ddsDE_sva_lowBMI_M3_result <- results(ddsDE_sva_lowBMI_M3)
summary(ddsDE_sva_lowBMI_M3_result)

write.csv(ddsDE_lowBMI_result,"MMNP_DEA_ddsDE_lowBMI_with_SV_result.csv" )

order(ddsDE_sva_BMI_M3_result$padj)
