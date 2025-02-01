R code for rapid data analysis

set.seed(123)

setwd("….//Rapid_final_results")
?setwd()

#Load the libraries needed for the study
library("DEP") # for Proteomics analysis
library("dplyr") # for data manipulation
library("proteus") # for normalisation function here and is suitable for MaxQuant output as well
library("proteusLabelFree")
library("purrr")
library("ggplot2")
library("SummarizedExperiment")# for assay function
library("proBatch")
library("miceadds") # for imputation

data <- read.csv("Input_100423_SCA.csv")
str(data)
dim(data)
glimpse(data)
colnames(data)
view(data)
grep("Abundance.", names(data), value = TRUE)
data %>% group_by(Accession) %>% summarize(frequency = n()) %>%arrange(desc(frequency)) %>% filter(frequency > 1)
data_unique <- make.unique(data, "Accession","Accession", delim = ";")


data$Accession %>% duplicated() %>% any()
LFQ_columns <- grep("Abundance.", colnames(data)) # get LFQ column numbers
LFQ_columns

#experimental_design<- SCA_design
data_se <- make_se_parse(data_unique, LFQ_columns)
data_se
pairs(assay(data_se[,1:3]))

#Normalization
plot_frequency(data_se) # first check the number of proteins not quantified in any of the samples

#Data filtering and visualization
data_filt<- filter_proteins(data_se, "fraction", min = 0.50)
plot_frequency(data_filt)
plot_numbers(data_se)
plot_numbers(data_filt)
hist(2^assay(data_se)[,"Healthy_A"],n=1000) # on orginal scale using one sample
hist(assay(data_se)[,"Healthy_A"],n=1000) # log2 scale
plot(density(assay(data_se)[,"Healthy_A"],na.rm=TRUE))

# mediancentering normalization is performed on original scale
data_norm_median<- data_filt
assay(data_norm_median) <- proBatch::normalize_data_dm(assay(data_filt, normalize_func='medianCentering'))

#Visualization of normalization
jpeg("normalization.jpg", width = 1000, height = 1000)
normp <- plot_normalization(data_filt, data_norm_median)
normp
dev.off()
meanSdPlot(data_norm_median)
plot_normalization(data_filt, data_norm_median)

#Visualization of missingness of the data
plot_detect(data_filt) # make df such that average of a gene in all conditions in one column and missing information in other
plot_missval(data_filt)
plot_missval(data_se)
plot_missval(data_norm_median)
plot_detect(data_norm_median)

# Extract protein names with missing values in all replicates of at least one condition – characterizing the type of missing proteins
proteins_MNAR<- get_df_long(data_norm_median) %>%
  group_by(name, condition) %>%
  summarize(NAs = all(is.na(intensity))) %>% 
  filter(NAs) %>% 
  pull(name) %>% 
  unique()

MNAR <- names(data_norm_median) %in% proteins_MNAR

#Imputation using cart
data_cart<- data_norm_median
colnames(data_cart) <- paste0("X", 1:ncol(data_cart))

##############################CART_IMPUTATION####################################
# Imputation using mice package
imputed_data<- mice::mice(as.matrix(assay(data_cart)), m = 1, method = 'cart', maxit = 5)
imputed_values<- mice::complete(imputed_data, 1)  # Get imputed values for the first imputation

# Assign imputed values to data_cart
assay(data_cart) <- as.matrix(imputed_values)

colnames(data_cart) <- paste0(colnames(data_norm_median))
colnames(assay(data_cart)) <- colnames(assay(data_norm_median))

##################################################################################

#########_Imputation using QRILC_#################
data_QRILC<- impute(data_norm_median, fun = "QRILC")

#Visualization of the imputation done
plot_imputation(data_norm_median, data_cart)
plot_imputation(data_norm_median, data_QRILC)


#Testing difference
data_diff<- test_diff(data_QRILC, type = "control", control = "Healthy")
dep<- add_rejections(data_diff, alpha = 0.05, lfc = log2(1))

# Create a vector of sex values with the same number of rows as the metadata for checking the batch effect

#process_date<- c("Batch1", "Batch1", "Batch1", "Batch1", "Batch1", "Batch1", "Batch1", "Batch1", "Batch2", "Batch2", "Batch2", "Batch2", "Batch2", "Batch2", "Batch2", "Batch2", "Batch3", "Batch3", "Batch3", "Batch3", "Batch3", "Batch3", "Batch3", "Batch3", "Batch4", "Batch4", "Batch4", "Batch4", "Batch4", "Batch4", "Batch4", "Batch4", "Batch5", "Batch5", "Batch5", "Batch5", "Batch5", "Batch5", "Batch5", "Batch5", "Batch6", "Batch6", "Batch6", "Batch6", "Batch6", "Batch6", "Batch6", "Batch6", "Batch7", "Batch7", "Batch7", "Batch7", "Batch7", "Batch7", "Batch7", "Batch7", "Batch8", "Batch8", "Batch8", "Batch8", "Batch8", "Batch8", "Batch8", "Batch8", "Batch9", "Batch9", "Batch9", "Batch9", "Batch9")

# Add the sex vector as a new column to the colData slot of dep
#dep@colData$processdate<- process_date

#Plotting the primary volcano plot
jpeg("QRILC_final.jpg", width = 1000, height = 1000)
mixed<- plot_volcano(dep, contrast = "SCA_vs_Healthy", label_size = 6, add_names = TRUE)
mixed
dev.off()

#Analyzing the results
dep_results<- analyze_dep(data_QRILC, type = "control", control = "Healthy",alpha = 0.05, lfc = 1)
write.csv(as.data.frame(dep_results@elementMetadata), file="DEP_norm_SCAvN_QRILC.csv")

#Plotting PCA and heatmap
plot_pca(dep, x = 1, y = 2, n = 232, point_size = 4, indicate = "processdate", label = TRUE)
plot_heatmap(dep, type = "centered", kmeans = FALSE,k = 6, col_limit = 10, show_row_names = TRUE)

pdf("QRILC.pdf",   # The directory you want to save the file in
    width = 7, # The width of the plot in inches
    height = 7) # The height of the plot in inches
mixed<- plot_volcano(dep, contrast = "SCA_vs_Healthy", label_size = 6, add_names = TRUE)
mixed
dev.off()
