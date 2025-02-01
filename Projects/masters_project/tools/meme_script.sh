#!/bin/bash

# Define an array of input directories
input_dirs=(
	"/home/locuz/Desktop/professional/dataware/Proso/52848/Result/classification/sequences/"
	"/home/locuz/Desktop/professional/dataware/Proso/52848/Result/classification/sequences/"
	"/home/locuz/Desktop/professional/dataware/Proso/52848/Result/classification/sequences/"
	"/home/locuz/Desktop/professional/dataware/Proso/52848/Result/classification/sequences/"
	"/home/locuz/Desktop/professional/dataware/Proso/52848/Result/classification/sequences/"
	"/home/locuz/Desktop/professional/dataware/Proso/52848/Result/classification/sequences/"
	"/home/locuz/Desktop/professional/dataware/Proso/52848/Result/classification/sequences/"
	"/home/locuz/Desktop/professional/dataware/Proso/52848/Result/classification/sequences/"
)

# Define an array of file names
files=(
  "RLK.fasta"
  "Pto.fasta"
  "Others.fasta"
  "NL.fasta"
  "N.fasta"
  "Kinase.fasta"
  "CNL.fasta"
  "CN.fasta"
)

# Loop through the arrays
for i in "${!input_dirs[@]}"; do
  # Set the input and output directory paths
  input_dir="${input_dirs[$i]}"
  file="${files[$i]}"
  output_dir="${file%.fasta}_output"
  # Run the MEME program with the input file and output directory names
  meme "${input_dir}/${file}" -mod anr -nmotifs 20 -minw 6 -maxw 50 -p 7 -o "${output_dir}"
done
