# contribution of globin genes in the count matrix

hemoglobin_genes <- c("ENSG00000206172", "ENSG00000188536" ,"ENSG00000244734","ENSG00000229988", "ENSG00000223609","ENSG00000213931", "ENSG00000213934", "ENSG00000196565", "ENSG00000206177","ENSG00000086506","ENSG00000130656", "ENSG00000206178")


for (i in hemoglobin_genes) {
  x <- grep(i, rownames(norm_count))
  print(x)
}

hb_genes_counts <- norm_count[rownames(norm_count) %in% hemoglobin_genes, ]
view(hb_genes_counts)

tot_hb_gene_count <- rowSums(hb_genes_counts)


tnormcount <- as.matrix(t(norm_count))
view(tnormcount)[4,4]
norm_countum <- t(rowSums(tnormcount))
view(norm_countum)

num_genes <- nrow(hb_genes_counts)
num_samples <- ncol(hb_genes_counts)1

# Create an empty matrix to store the percentage of genes
percentage_matrix <- matrix(NA, nrow = num_genes, ncol = num_samples)
rownames(percentage_matrix) <- rownames(hb_genes_counts)
colnames(percentage_matrix) <- colnames(hb_genes_counts)

# Loop through samples
for (sample in 1:num_samples) {
  # Calculate the percentage of genes for each sample
  percentage_matrix[, sample] <- (hb_genes_counts[, sample] / norm_countum[1, sample]) * 100
}

write.csv(norm_countum, "norm_genes_count_171sample.csv")

# create compile matrix

dist_mat <- matrix(data = NA, nrow = 15, ncol = 171)



thb_genes_counts <- as.matrix(t(hb_genes_counts))
thb_genes_counts

countsum <- rowSums(thb_genes_counts)
