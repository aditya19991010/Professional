#!/bin/bash
#SBATCH --job-name="10samtools_idx from openmpi 4.1.4"
#SBATCH --output="10samtools_idx_414.%j.%N.out"
#SBATCH --error="10samtools_idx_414.%j.%N.err"
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --mail-type=BEGIN,FAIL,END
#SBATCH --mail-user=aditya19991010@gmail.com

module load java-11
module load samtools-1.16.1

# Loop through the files
for i in `cat array_srr`
do
  # Set the output file paths
	echo $i
	output_file="${i}_hisat_MYB_bam"
  
  # Run samtools to get statistics


  samtools idxstats "${output_file}_sorted.bam"
done

