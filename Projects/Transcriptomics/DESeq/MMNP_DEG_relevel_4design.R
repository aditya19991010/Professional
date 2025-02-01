#design for effect of allocation
design = ~Batch + cbmi + csex + Allocation
alpha = 0.05

dds <- DESeqDataSetFromMatrix(countData = lowBMI_rawcounts, colData = low_BMI_Sampledata, design = design)


#checking NA values
# row_has_na <- any(is.na(rawcounts[3, ]))
# col_has_na <- any(is.na(sampleData[, 1]))

# # set reference for the factor
dds$Allocation <- factor(dds$Allocation, levels = c("A","B"))
# dds$BMI <- factor(dds$BMI, levels = c("high", "low"))


#remove lowely expressed genes 
keep <- rowSums(counts(dds)) >= 100
dds<- dds[keep,]


# set factor level
# dds$BMI <- relevel(dds$BMI, ref = "low")
dds$Allocation <- relevel(dds$Allocation, ref = "B")


#NOTE: collapse technical replicates, never collapse biological replicates

# main DESeq
ddsDE_lowBMI <- DESeq(dds)
ddsDE_lowBMI_result <- results(ddsDE_lowBMI)


dim(counts(dds))
design(ddsDE_lowBMI)
levels(ddsDE_lowBMI$Allocation)
summary(ddsDE_lowBMI_result)

getwd()
setwd("../../Output/")
write.csv(ddsDE_sva_Allocation_M3_result, "deg_Allo_sva_m3.csv")


write.csv(ddsDE_sva_BMI_M3_result, "deg_bmi_sva_m3.csv")
write.csv(ddsDE_sva_highBMI_M3_result, "deg_AvsB_hbmi_sva_m3.csv")
write.csv(ddsDE_sva_lowBMI_M3_result, "deg_AvsB_lbmi_sva_m3.csv")
