#!/bin/bash

sam_dir="~/aditya/pupil/02_Alignmnet/SAM/"
# Loop through the files
for i in ${sam_dir}
do
  # Set the input and output file paths
  input_file="${i}.sam"
  output_file="${i}.bam"
  
  # Run samtools convert SAM to BAM
  samtools view -bS --threads 40 "${input_file}" > "${output_file}"
  samtools sort "${output_file}" -o "${output_file}_sorted" --threads 40
  samtools index "${output_file}_sorted"
done
