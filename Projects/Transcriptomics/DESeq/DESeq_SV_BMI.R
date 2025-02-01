#Differential for BMI SVs

#Model 1 -  Including all SVs 
#Model 2 -  Includes SV of Indpendent variable + SVs correlated with covariates
#Model 3 -  Model2 - SV of Independent variable 


#design for DESeq Model 1
ddsDE_sva_BMI_M1 <- ddsDE_sva

for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  ddsDE_sva_BMI_M1[[col_name]] <- paste0(sampledata_BMI[[col_name]])
  ddsDE_sva_BMI_M1[[col_name]] <- as.numeric(sampledata_BMI[[col_name]])
}

view(ddsDE_sva_BMI_M1$sv1)

design(ddsDE_sva_BMI_M1) <- ~ sv1 + sv2 + sv3 + sv4 + sv5 + sv6 + sv7 + sv8 + sv9 + sv10 + sv11 + sv12 + sv13 + sv14 + sv15 + sv16 + sv17 + sv18 + sv19 + sv20 + sv21 + BMI

# # set reference for the factor
# ddsDE_sva$Allocation <- factor(dds$Allocation, levels = c("A","B"))
ddsDE_sva_BMI_M1$BMI <- factor(ddsDE_sva_BMI_M1$BMI, levels = c("high", "low"))

#remove lowely expressed genes 
keep <- rowSums(counts(ddsDE_sva_BMI_M1)) >= 171
ddsDE_sva_BMI_M1 <- ddsDE_sva_BMI_M1[keep,]

# main DESeq
ddsDE_sva_BMI_M1 <- DESeq(ddsDE_sva_BMI_M1)
ddsDE_sva_BMI_M1_result <- results(ddsDE_sva_BMI_M1)

summary(ddsDE_sva_BMI_M1_result)

ddsDE_sva_BMI_M1_result <- as.data.frame(ddsDE_sva_BMI_M1_result)
ddsDE_sva_BMI_M1_result <- ddsDE_sva_BMI_M1_result[order(ddsDE_sva_result$padj),]

# #Model2
# design for DESeq  

ddsDE_sva_BMI_M2 <- ddsDE_sva

for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  ddsDE_sva_BMI_M2[[col_name]] <- paste0(sampledata_BMI[[col_name]])
  ddsDE_sva_BMI_M2[[col_name]] <- as.numeric(sampledata_BMI[[col_name]])
}

view(ddsDE_sva_BMI_M2$sv1)
design(ddsDE_sva_BMI_M2) <- ~ sv1 + sv2 + sv3 + sv4 + sv11  + sv12 + sv14 +  sv13 + sv16 + sv17 + BMI

# # set reference for the factor
# ddsDE_sva$Allocation <- factor(dds$Allocation, levels = c("A","B"))
ddsDE_sva_BMI_M2$BMI <- factor(ddsDE_sva_BMI_M2$BMI, levels = c("high", "low"))

#remove lowely expressed genes 
keep <- rowSums(counts(ddsDE_sva_BMI_M2)) >= 171
ddsDE_sva_BMI_M2 <- ddsDE_sva_BMI_M2[keep,]

# main DESeq
ddsDE_sva_BMI_M2 <- DESeq(ddsDE_sva_BMI_M2)
ddsDE_sva_BMI_M2_result <- results(ddsDE_sva_BMI_M2)
summary(ddsDE_sva_BMI_M2_result)

ddsDE_sva_BMI_M2_result <- as.data.frame(ddsDE_sva_BMI_M2_result)
ddsDE_sva_result

# #Model3
# design for DESeq  

ddsDE_sva_BMI_M3 <- ddsDE_sva

for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  ddsDE_sva_BMI_M3[[col_name]] <- paste0(sampledata_BMI[[col_name]])
  ddsDE_sva_BMI_M3[[col_name]] <- as.numeric(sampledata_BMI[[col_name]])
}

design(ddsDE_sva_BMI_M3) <- ~ sv1 + sv2 + sv3 + sv4 + sv11  + sv13 + sv16 + sv17 + BMI

# # set reference for the factor
# ddsDE_sva$Allocation <- factor(dds$Allocation, levels = c("A","B"))
ddsDE_sva_BMI_M3$BMI <- factor(ddsDE_sva_BMI_M3$BMI, levels = c("high", "low"))

#remove lowely expressed genes 
keep <- rowSums(counts(ddsDE_sva_BMI_M3)) >= 171
ddsDE_sva_BMI_M3 <- ddsDE_sva_BMI_M3[keep,]

# main DESeq
ddsDE_sva_BMI_M3 <- DESeq(ddsDE_sva_BMI_M3)
ddsDE_sva_BMI_M3_result <- results(ddsDE_sva_BMI_M3)
summary(ddsDE_sva_BMI_M3_result)

design(ddsDE_sva_BMI_M3)
ddsDE_sva_BMI_M3_result <- as.data.frame(ddsDE_sva_BMI_M3_result)
ddsDE_sva_BMI_M3_result

csv_m1 <- paste0("MMNP_DEA+SVA","21_SVs_BMI",".csv")
csv_m2 <- paste0("MMNP_DEA+SVA",design(ddsDE_sva_BMI_M2)[2],".csv")
csv_m3 <- paste0("MMNP_DEA+SVA",design(ddsDE_sva_BMI_M3)[2],".csv")

getwd()
setwd("F:/Aditya/MMNP_DEA/Output/csv/ddsDE+\ SV")

write.csv(ddsDE_sva_BMI_M1_result,csv_m1)
write.csv(ddsDE_sva_BMI_M2_result, csv_m2)
write.csv(ddsDE_sva_BMI_M3_result, csv_m3)