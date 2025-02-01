#!/bin/bash

conda activate QC

base_dir="/home/aditya/ChIP_Seq_Analysis_groth"

fastqc -o "${base_dir}"/01_QualityControl/SAM --threads 60 "${base_dir}"/02_Alignment/SAM
fastqc -o "${base_dir}"/01_QualityControl/FastQC_reports --threads 60 "${base_dir}"/00_RawData/FastQ
