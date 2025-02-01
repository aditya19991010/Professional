#!/bin/bash

# Loop through the files
for i in `cat array_srr`
do
  # Set the input and output file paths
  input_file="${i}_hisat.sam"
  output_file="${i}_hisat.bam"
  
  # Run samtools convert SAM to BAM
  samtools view -bS --threads 40 "${input_file}" > "${output_file}"
  samtools sort "${output_file}" -o "${output_file}_sorted" --threads 40
  samtools index "${output_file}_sorted"
done

