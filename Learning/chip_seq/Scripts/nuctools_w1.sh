#!/bin/bash

#Path variables
path_bed=~/epi_young_old_human/encode_data/F42_ENCBS168AIQ/bamfiles/bedfile/
scrip_path=~/tools/NucTools/

# Ensure Output Directory Exists
mkdir -p "${path_bed}"
mkdir -p "${nuchtool_path}/OCC"

#change dir
cd "${path_bed}/../bamfile"

#Convert BAM to bed
for i in *bam; do
	basename=$(basename ${i} ".bam")
	bedtools bamtobed -i "${i}" | pigz > "${path_bed}"/"${basename}".bed.gz
	echo "Bed files of ${basename} generated succesfully at ${path_bed}\n"
done

echo "Bedtool work finished\n"


# Path Variables
nuchtool_path=~/epi_young_old_human/encode_data/F42_ENCBS168AIQ/nuchtools_data


# Navigate to BED File Directory
cd "${path_bed}" || exit

# Process Each GZ File
for j in *.gz; do
	basename=$(basename "${j}" ".bed.gz")	
	echo "\nSelected ${basename} file"
    
    # Step 1: Extend Reads
    perl "${scrip_path}/extend_SE_reads.pl" \
        --gzip \
        -in "${j}" \
        -out "${nuchtool_path}/${basename}.ext.bed.gz" \
	-fL 147
	echo "extend_SE_reads done"
    
    # Step 2: Extract Chromosome Data
    perl "${scrip_path}/extract_chr_bed.pl" \
	--gzip \
	-in "${nuchtool_path}/${basename}.ext.bed.gz" \
	-out "${basename}" \
	--pattern="chr1" \
	--chromosomes=1
	echo "extracting chr bed file"

	#Step 3: Calculating bed occupancy
        perl "${scrip_path}/bed2occupancy_average.pl" \
        --gzip \
        -in "chr1.${basename}.bed.gz" \
        -out "chr1.${basename}.occ.bed.gz" \
        -odir "${nuchtool_path}/OCC" \
        -use \
        -w 1

        echo "Calculating BED occupancy ${i}..\n"
done

echo "Job Finished...\n"
