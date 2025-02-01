#!/bin/bash

# Loop through the files
for i in `cat array_srr`
do
  # Set the input and output file paths
  input_file="${i}_hisat.bam_sorted"
  output_file="${i}_sorted_hisat.bam"
  
  # Run samtools convert SAM to BAM
  mv "${input_file}" "${output_file}"
done

