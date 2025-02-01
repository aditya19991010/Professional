#!/bin/bash

# Loop through the files
for i in `cat array_srr`
do
  # Set the input and output file paths
  input_file="${i}_sorted_hisat.bam"
  output_file="${i}_hisat.tdf"
  
  # Run samtools convert SAM to BAM
  igvtools count "${input_file}" "${output_file}" /home/aditya/NGS/hisat/GCA_003046395.2_Pm_0390_v2_genomic.fna
done

