#!/bin/bash

module load anaconda3
conda activate LGI_aditya

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
  # Set the output file paths
  output_file_1="${file}_1_trim.fastq"
  
  fastqc --threads 40 --outdir SRA_QC_04 "${output_file_1}_1P"
done
