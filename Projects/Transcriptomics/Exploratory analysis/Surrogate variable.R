#Finding surrogate variable
library(sva)
BiocManager::install("SummarizedExperiment", force = TRUE)
library("SummarizedExperiment")
install.packages("rafalib")
library(rafalib)

ddsDE_sva <- ddsDE
norm.cts <- counts(ddsDE_sva, normalized=TRUE)
norm.cts <- norm.cts[rowSums(norm.cts) > 171,]

sampledata_sv <- sampleData
sampledata_BMI <- sampledata_sv
sampledata_Allocation <- sampledata_sv


# Create KW_data to paste pvalues from tests
KW_data <- data.frame(row.names = c("Allocation", "BMI", "csex", "Batch", "cbmi"))
wilcox_data <- data.frame(row.names = c("Allocation", "BMI", "csex", "Batch" , "cbmi"))

#set up design
design_sv = ~sampledata_sv$cbmi + as.factor(sampledata_sv$csex) +  as.factor(sampledata_sv$Batch) + as.factor(sampledata_sv$Allocation) + as.factor(sampledata_sv$BMI)
design_null = ~sampledata_sv$cbmi + as.factor(sampledata_sv$csex) + as.factor(sampledata_sv$Batch) + as.factor(sampledata_sv$Allocation)
mm <- model.matrix(design_sv, colData(ddsDE_sva))
mm0 <- model.matrix(design_null , colData(ddsDE_sva))

# n.sv = num.sv(rawcounts,mm,method="leek")
# n.sv

fit <- svaseq(norm.cts, mod=mm, mod0=mm0)
fit$n.sv

num_cols_to_paste <- fit$n.sv

# Create a loop to paste the columns in Allocation data
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  sampledata_Allocation[[col_name]] <- paste0(fit$sv[, i])
  sampledata_Allocation[[col_name]] <- as.numeric(sampledata_Allocation[[col_name]])
}

# Create a loop to paste the columns
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  sampledata_BMI[[col_name]] <- paste0(fit$sv[, i])
  sampledata_BMI[[col_name]] <- as.numeric(sampledata_BMI[[col_name]])
}


 # sampledata_matrix[sv1] <- paste0(fit$sv[, i])


# Create a loop to paste the pvalues in KW test
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  kruskal_result <- kruskal.test(get(col_name)  ~ cbmi, data = sampledata_BMI)
  KW_data[5, col_name] <- kruskal_result$p.value
}

# Create a loop to paste the pvalues for wilcox test
for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  WC_data <- wilcox.test(get(col_name) ~ Batch,
                         data = sampledata_BMI,
                         exact = FALSE)
  wilcox_data[4, col_name] <- WC_data$p.value
}


View(KW_data)
view(wilcox_data)
# kruskal.test(sv2 ~ Batch, data = sampledata_sv)


# kruskal_result <- kruskal.test(sv1~ Batch, data = sampledata_sv)
# kruskal_result

getwd()


par(mfrow=c(4,1),mar=c(3,5,3,1))

for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  main <- paste0(col_name, "Batch")
  stripchart( get(col_name)  ~ Batch, data = sampledata_sv  , vertical=TRUE, main= col_name )
  abline(h=0)
}

design_sv

csv_file_name_wc <- paste0("MMNO_svs_wilcox_test",design_sv[2],".csv")
csv_file_name_KW <- paste0("MMNO_svs","KW_test",design_sv[2],".csv")

design_sv
csv_file_name_KW
write.csv(wilcox_data, file = csv_file_name_wc) 
write.csv(KW_data, file = csv_file_name_KW) 


#add svs data in the pheno file

sampledata_matrix <- sampledata_BMI

# Create a loop to paste the columns

for (i in 1:21) {
  col_name <- paste0("sv", i) 
  sampledata_BMI[[col_name]] <- paste0(fit$sv[, i])
  sampledata_BMI[[col_name]] <- as.numeric(sampledata_BMI[[col_name]])
}



as.numeric(sampledata_Allo$sv1)
sampledata_matrix$sv1 <-  paste(sampledata_Allo$sv1)
sampledata_matrix$sv12 <- paste(sampledata_BMI$sv12)
sampledata_matrix$sv14 <- paste(sampledata_BMI$sv14)








kruskal_result <- kruskal.test(get(col_name) ~ BMI, data = sampledata_sv)
kruskal_result

KW_data[[col_name]] <- paste0(kruskal_result$p.value)

abc = sampledata_sv
abc$Allocation = as.factor(abc$Allocation)
abc$sv1 = as.numeric(abc$sv1)



WC_data <- wilcox.test(sv1 ~ Allocation,
                       data = sampledata_sv,
                       exact = FALSE)

kruskal.test(sv1 ~ Allocation, data = sampledata_sv)



rm(KW_data)

for (i in 1:num_cols_to_paste) {
  sv <- paste0("sv",i)
  kruskal_result <- kruskal.test(sv ~ Allocation , data = sampledata_sv)
  KW_data[[col_name]] <- paste0(kruskal_result$p.value)
}

fit$sv[,1]
view(sampledata_sv)


# Assuming you have a data frame named 'data' with 'Allocation' and 'sv1' columns
stripchart(sv1 ~ Allocation, data = sampledata_sv, method = "jitter", main = "Strip Plot of sv1 by Allocation")
stripchart(fit$sv[,1] ~ dds_sva$Batch,vertical=TRUE,main="sv1")

kruskal_result$data.name

boxplot(Allocation ~ sv1, data = sampledata_sv, main = "Box Plot of sv1 by Allocation")

# ggboxplot(sampledata_sv, x = "sv1", y = "Allocation",
#           +           color = "Allocation", palette = c("#FFA500", "#FF0000"),
#           +           ylab = "Allocation", xlab = "sv1")

view(sampledata_sv)
sampledata_sv


bigpar()
dds_sva$BMI <- as.integer(dds_sva$BMI) + 15
plot(fit$sv[,1:2], col=dds_sva$Batch, pch=dds_sva$Allocation, cex=2,
     xlab="sv1", ylab="sv2")
legend("top", levels(dds_sva$Batch), pch=16,
       col=1:3, cex=.8, ncol=3, legend = c(1,2,3) , title="batch")

par(mfrow=c(4,1),mar=c(3,5,3,1))
stripchart(fit$sv[,1] ~ dds_sva$Batch,vertical=TRUE,main="sv1")
abline(h=0)
stripchart(fit$sv[,2] ~ dds_sva$Batch,vertical=TRUE,main="sv2")
abline(h=0)


## read in the file containing the gene expression values
expData_file_name <- system.file("folder containing the data", "CAD_Expression.csv", package="ExpressionNormalizationWorkflow")
exprs <- read.table(expData_file_name, header=TRUE, sep=",", row.names=1, as.is=TRUE)

## read in the file containing the covariates
expDesign_file_name <- system.file("folder containing the data", "CAD_ExptDsgn.csv", package="ExpressionNormalizationWorkflow")
covrts <- read.table(expDesign_file_name, header=TRUE, sep=",", row.names=1, as.is=TRUE)

## read in the file containing the gene expression values
exprs <- sampleData
## read in the file containing the covariates
covrts <- read.csv(file = sampleData, header=TRUE, sep=",", row.names = 1, as.is=TRUE)
