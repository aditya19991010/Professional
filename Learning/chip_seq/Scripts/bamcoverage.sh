#!/bin/bash

input="/home/aditya/ChIP_Seq_Analysis_groth/02_Alignment/BAM/sorted_bam"
out_dir="/home/aditya/ChIP_Seq_Analysis_groth/04_analysis"

#mkdir -p "${out_dir}/deeptools/"
#mkdir -p "${out_dir}/deeptools/bigwig"

#for i in "${input}"/*bam; do
#	filename=$(basename ${i} ".bam")
#	bamCoverage -b ${i} --numberOfProcessors 63  -o "${out_dir}/deeptools/bigwig/${filename}.bw" --normalizeUsing BPM
#done

cd "${out_dir}"/deeptools/bigwig

for i in *bw ; do
	filename=$(basename ${i} ".bw")
	computeMatrix scale-regions -S "${i}" -R /home/aditya/ChIP_Seq_Analysis_groth/04_analysis/gene_mm10/GHR_mm10.bed --regionBodyLength 265597 \
	--outFileName "${filename}"_GHR_sregion.gz  --outFileNameMatrix "${filename}"_GHR_sregion_matrix.csv --missingDataAsZero --binSize 1
done
