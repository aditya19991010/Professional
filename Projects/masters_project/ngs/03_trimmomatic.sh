#!/bin/bash


#trimming 13 nucleotide from start of reads

# Define an array of file names
files=(
  "SRR6660738"
  "SRR6660748"
  "SRR6660754"
  "SRR6660764"
  "SRR6660767"
  "SRR6660768"
  "SRR6660772"
  "SRR6660777"
)

# Loop through the files
for file in "${files[@]}"; do
  # Set the input and output file paths
  input_file_1="${file}_1.fastq"
  output_file_1="${file}_2_trim.fastq"
  input_file_2="${file}_2.fastq"
  output_file_2="${file}_2_trim.fastq"
  
  # Run trimmomatic to remove the first 13 bases
  java -jar /home/aditya/software/Trimmomatic/trimmomatic-0.39.jar PE -threads 40 -phred33 "${input_file_1}" "${input_file_2}" "${output_file_1}_1P" "${output_file_1}_1U" "${output_file_2}_2P" "${output_file_1}_2U" HEADCROP:13
done

