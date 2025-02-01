
analysis <- c("ddsDE_sva_highBMI_M3", "ddsDE_sva_lowBMI_M3", "ddsDE_sva_Allocation_M3", "ddsDE_sva_BMI_M3" )


for (i in 1:num_cols_to_paste) {
  col_name <- paste0("sv", i) 
  high_BMI_sampledata_sv[[col_name]] <- paste0(fit$sv[, i])
  high_BMI_sampledata_sv[[col_name]] <- as.numeric(high_BMI_sampledata_sv[[col_name]])
}

for (i in analysis) {
  # Print levels of Allocation
  print(levels(i$Allocation))
  
  # Print design of i
  print(i@design)
  
  # Create a variable name for the summary
  sum_var <- paste0(i, "_result")
  
  # Print the summary
  print(summary(get(sum_var)))
}

ddsDE_sva_highBMI_M3@design
levels(ddsDE_sva_highBMI_M3$Allocation)
summary(ddsDE_sva_highBMI_M3_result, alpha = 0.05)

ddsDE_sva_lowBMI_M3@design
levels(ddsDE_sva_lowBMI_M3$Allocation)
summary(ddsDE_sva_lowBMI_M3_result, alpha = 0.05)

ddsDE_sva_Allocation_M3@design
levels(ddsDE_sva_Allocation_M3$Allocation)
summary(ddsDE_sva_Allocation_M3_result, alpha = 0.05)

ddsDE_sva_BMI_M3@design
levels(ddsDE_sva_BMI_M3$BMI)
summary(ddsDE_sva_BMI_M3_result, alpha = 0.05)

# List of objects
object_list <- list(
  ddsDE_sva_highBMI_M3 = ddsDE_sva_highBMI_M3,
  ddsDE_sva_lowBMI_M3 = ddsDE_sva_lowBMI_M3,
  ddsDE_sva_Allocation_M3 = ddsDE_sva_Allocation_M3,
  ddsDE_sva_BMI_M3 = ddsDE_sva_BMI_M3
)

# Iterate through the list
for (obj_name in names(object_list)) {
  obj <- object_list[[obj_name]]
  
  # Print design levels
  cat(obj_name, "@design\n")
  cat("levels(", obj_name, "$Allocation)\n")
  print(levels(obj$Allocation))
  
  # Print summary
  cat("summary(", obj_name, "_result)\n")
  print(summary(get(paste0(obj_name, "_result"))))
  
  cat("\n")  # Separate output for each object
}



