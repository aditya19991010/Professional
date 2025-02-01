#!/bin/bash

conda activate sratools

read -p "Enter file name containing SRA IDs: " SRA
SRA_PATH="/home/aditya/ChIP_Seq_Analysis_groth/00_RawData/SRR_download"

#mkdir -P SRR_download

# Fetch SRA files from server
prefetch -O "$SRA_PATH" --option-file  "$SRA"

# Create path for Fastq-dump
Fastq_path="${SRA_PATH}/../FastQ"

# Make sure the Fastq directory exists
mkdir -p "$Fastq_path"

#Convert all SRA files into fastq
for i in  `cat $SRA` ; do 
	fastq-dump --outdir "${Fastq_path}" $i
done
