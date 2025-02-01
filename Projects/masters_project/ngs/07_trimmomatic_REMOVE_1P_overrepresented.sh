#!/bin/bash

# Loop through the files
for i in `cat array_for_orpseq`
do
  # Set the input and output file paths
  input_file_1="${i}_1_trim.fastq_1P"
  output_file_1="${i}_1_trim_rm_ovrpseq.fastq"
  ovrpseq="${i}_1_trim.fastq_1P_fastqc.fasta"
  
  # Run trimmomatic to remove the first 13 bases
  java -jar /home/aditya/software/Trimmomatic/trimmomatic-0.39.jar SE -threads 40 -phred33 "${input_file_1}" "${output_file_1}" ILLUMINACLIP:"${ovrpseq}:2:30:10"
done

