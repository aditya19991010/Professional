#!/bin/bash

# Loop through the files
for i in `cat array_srr`
do
  # Set the input and output file paths
  input_file_1="${i}_1_trim.fastq_1P"
  input_file_2="${i}_2_trim.fastq_2P"
 
  # Renaming
  mv "${input_file_1}" "${i}_1_trim.fq"
  mv "${input_file_2}" "${i}_2_trim.fq"
done

