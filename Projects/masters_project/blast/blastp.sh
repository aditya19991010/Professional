#!/bin/bash

echo "To perform blastp"
echo "Enter database file:"
read -r database_file

echo 'Enter database type ("nucl" for nucleotide and "prot" for protein):'
read -r dbtype

makeblastdb -in "$database_file" -dbtype "$dbtype"

if [[ "$dbtype" == "prot" ]]; then
  search_tool="blastp"
else
  search_tool="blastn"
fi

echo "Search tool: $search_tool"

echo "Enter query file:"
read -r query_file

echo "Enter E-value:"
read -r evalue

echo "If needed, add an extra command with '-', else leave blank:"
read -r command

"$search_tool" -query "$query_file" -db "$database_file" -out "${search_tool}_results.out" -evalue "$evalue" -outfmt 6
"$command"

# Check the exit status of the last command
if [ $? -eq 0 ]; then
  echo "The script completed successfully."
else
  echo "The script failed."
fi
