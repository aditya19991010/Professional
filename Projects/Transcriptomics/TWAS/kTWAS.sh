java -jar kTWAS.jar kTWAS -format csv -input_genotype EXAMPLE/CSV_FORMAT/example.csv 
-input_phenotype EXAMPLE/CSV_FORMAT/example.tsv 
-input_phenotype_column 2 -input_phenotype_type binary 
-en_info_path ElasticNet_DB/ElasticNet_Whole_Blood.txt 
-gene ENSG00000250334.5 -plink ~/anaconda/envs/r_env/bin/plink 
-Rscript /apps/codes/R/3.6.1/bin/Rscript -output_folder .


java -jar kTWAS.jar kTWAS -format plink -input_genotype EXAMPLE/PLINK_FORMAT/example.tped 
-input_phenotype EXAMPLE/PLINK_FORMAT/example.tfam -input_phenotype_column 6 -input_phenotype_type binary 
-en_info_path ElasticNet_DB/ElasticNet_Whole_Blood.txt -gene ENSG00000250334.5 
-plink ~/anaconda/envs/r_env/bin/plink -Rscript /apps/codes/R/3.6.1/bin/Rscript -output_folder .
