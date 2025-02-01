#!bin/bash

#To construct profiles from multiple sequence alignments

echo "Enter the file name"
read msafile

echo "If you want an extra command then add it with '-', else left blank"
read extra_command1 

hmmbuild "$msafile".hmm "$msafile" "$extra_command1"

echo "Enter query file name for search"
read query_file

#To search homologous sequences in the hmmprofile

echo "If you want an extra command then add it with '-', else left blank"
read extra_command2 
hmmsearch "$msafile".hmm "$query_file" "$extra_command2"

if [ $? -eq 0 ]; then
  echo "Search has been completed successfully."
else
  echo "The script failed."
fi
