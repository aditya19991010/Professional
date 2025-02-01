#!/bin/bash

#read -p 'Enter path to Fastq files directory: ' fastq_dir
fastq_dir=/home/aditya/ChIP_Seq_Analysis_groth/00_RawData/FastQ
# Check if the directory exists
if [ ! -d "$fastq_dir" ]; then
	echo "Error: Directory $fastq_dir does not exist."
	exit 1
fi

# Create output directory if it doesn't exist
output_dir=/home/aditya/ChIP_Seq_Analysis_groth/02_Alignment/SAM
mkdir -p "$output_dir"

for item in "$fastq_dir/"*; do
	if [[ "$item" == *.fastq ]]; then
		fastq_name=$(basename "${item}" ".fastq")
		echo "Reading file ${fastq_name}"
        
		bowtie2 -p 60 -q --local \
		-x ~/ChIP_Seq_Analysis_groth/02_Alignment/BAM_index/GCA_000001635.9_GRCm39_full_analysis_set.fna.bowtie_index \
		-U "$item" \
		-S "$output_dir/${fastq_name}.sam"
        
		echo "SAM file saved in $output_dir/${fastq_name}.sam"
	else
		echo "Skipping non-fastq file: $item"
	fi
done
