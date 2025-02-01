#!/bin/bash

read -p "Enter path to sam files directory: " sam_path
if  [[ ! -d "${sam_path}" ]]; then
	echo "Directory doesn't exist"
	exit 1
fi

read -p "Enter path to sam files directory: " bam_path
if  [[ ! -d "${bam_path}" ]]; then
	echo "Directory doesn't exist"
	exit 1
fi

read -p "Enter path to samfile target-control table: " table

if [[ ! -f "${table}" ]]; then
	echo "Error: File '${table}' does not exist."
	exit 1
fi


mkdir -p "${bam_path}/sicer"
mkdir -p "${sam_path}/epic"

# Process each line in the table
while read -r target control; do
	# Check if target and control are not empty
	if [[ -z "${target}" || -z "${control}" ]]; then
		echo "Skipping invalid line in table: '${target} ${control}'"
		continue
	fi

	echo "Processing: target = ${target}, control = ${control}"

	# Run epic2 command
	epic2 --treatment "${sam_path}/${target}.sam" \
		  --control "${sam_path}/${control}.sam" \
		  --genome mm10 \
		  --output "${sam_path}/epic/${target}_sam_epic.bed"
	#Run Sicer
	
	sicer --treatment_file "${bam_path}/${target}.bam" \
	--control_file "${bam_path}/${control}.bam"  \
	--species mm10 --cpu 60 -v --output "${bam_path}/sicer/${target}_bam_sicer"

done < "${table}"
