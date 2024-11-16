# 
# Create a module, CSVProcessor. It should contain functions for loading CSV data from an external file (titanic.csv), calculating total number of columns, calculating total number of rows and filling missing values in any column with zero. Use Pandas read_csv and other Pandas and Numpy functions. Import this module into another program and demonstrate invoking these methods.

# Create a module, JSONProcessor. It should contain functions for loading JSON data from an external file and printing JSON data. The JSON file should contain following player details. Create a JSON file with this information. 
# {
# 			{
# 				“player_name”: “Shubham”
# 				“player_email”: “shubham@abc.org”
# 				“player_score: 45
# 				“man_of_the_match”: false
# 			},
# 			{
# 				“player_name”: “Rohit”
# 				“player_email”: “rohit@abc.org”
# 				“player_score: 75
# 				“man_of_the_match”: false
# 			},
# 			{
# 				“player_name”: “Virat”
# 				“player_email”: “virat@abc.org”
# 				“player_score: 100
# 				“man_of_the_match”: false
# 			}
# ]
# }
# Load this file into a dictionary using the JSON module.  Set the man_of_the_match field to True for a player who has scored the maximum score among all players. Write back this information into a new JSON file.  
# 
# Create a base class, CDataProcessor with two properties - samples and features - and a method PrintDatasetInfo(). The two properties are initialized using the number of rows and columns of a Pandas dataframe that is passed to the constructor during object creation. The PrintDatasetInfo() method should print the number of samples and features.
# 
# Derive a new class, CCSVProcessor from the CDataProcessor class. This derived class should have two properties - filename and dfData - The filename is initialized to path of the CSV file specified during object createion. The dfData is initialized to empty dataframe. The CCSVProcessor class should contain two methods - LoadData() and ConvertToJSON() - LoadData should load the CSV data into a dfData property of this class (use Pandas read_csv method). It should also invoke its parent class __init__ method passing the dfData, so that, parent’s samples and features are populated correctly.   ConvertToJSON() should create a new JSON file using the dfData (use Pandas to_json method)
# 
# Derive a new class, CJSONProcessor from the CDataProcessor class. This derived class should have two properties - filename and dfData - The filename is initialized to path of the JSON file specified during object createion. The dfData is initialized to empty dataframe. The CJSONProcessor class should contain a method - LoadData() - LoadData should load the JSON data into a dfData property of this class (use Pandas read_json method). It should also invoke its parent class __init__ method passing the dfData, so that, parent’s samples and features are populated correctly. 
# 
# Create an object of CCSVProcessor using the file titanic.csv. Load the data and invoke PrintDatasetInfo() to print the number of samples and features in this dataset.
# Create an object of CCSVProcessor using the file ODI-Batting_Cricket_Analytics.csv. This file is copied in my Google drive code folder.  Load the data and invoke ConvertToJSON() method to create a new ODI-Batting_Cricket_Analytics.JSON file.
# Create an object of CJSONProcessor(), load the data and invoke PrintDatasetInfo() to print the number of features and columns of this dataset.
# 
# Test if a DNA sequence contains an EcoRI restriction site using regular expressions.
# dna = "ATCGCGAATTCAC"
# pattern = GAATTC
# 
# Check for the presence of an AvaII recognition site, which can have two different sequences: GGACC and GGTCC. Use regular expressions.
# dna = "ATCGCGAATTCAC"
# pattern = GGACC and GGTCC
# 
# Check for the presence of a BisI restriction site using regular expression character groups: A character group is a pair of square brackets with a list of characters inside them.
# dna = "ATCGCGAATTCAC"
# pattern = GCNGC, where N represents any base, i.e. A, T, G, C
# 
# Here's a complex pattern to identify full-length eukaryotic messenger RNA sequences - ^AUG[AUGC]{30,1000}A{5,10}$    Can you describe in a few bullet points what matches will occur?
# 
# Take a DNA sequence and determine whether or not it contains any ambiguous bases – i.e. any bases that are not A, T, G or C. If there is a non ambiguous base, print the non ambiguous base
# dna = "ATCGCGYAATTCAC"
# 
# Write a regular expression to extract the genus name and species name into separate variables. For example, if scientific_name = "Homo sapiens", the output should be genus is Homo, species is sapiens. Test your program with another example of scientific_name = “Drosophila melanogaster”.
# Take a DNA sequence and determine whether or not it contains any ambiguous bases – i.e. any bases that are not A, T, G or C. If there are ambiguous bases, print all ambiguous bases and their positions.
# dna = "CGATNCGGAACGATC"
# 
# Here's a DNA sequence with the bits that we want to extract in bold:
# ACTGCATTATATCGTACGAAATTATACGCGCG
# Extract the bits of the string that match the pattern (highlighted in bold) using findall():
# 
# Write a regular expression to split the DNA string wherever we see a base that isn't A, T, G or C. if the dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG", the output should be ['ACT', 'GCAT', 'GCTACGT', 'ACGAT', 'CGA', 'TCG']
# 
# Here's a list of made up gene accession names:
# accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
# Write a program that will print only the accession names that satisfy the following criteria – treat each criterion separately:
# 
# contain the number 5
# contain the letter d or e
# contain the letters d and e in that order
# contain the letters d and e in that order with a single letter between them
# contain both the letters d and e in any order
# start with x or y
# start with x or y and end with e
# contain three or more digits in a row
# end with d followed by either a, r or p
# 
# Download dna.txt from the usual code folder in my drive. The file contains a made up DNA sequence. Predict the fragment lengths that we will get if we digest the sequence with two made up restriction enzymes – AbcI, whose recognition site is ANT/AAT, and AbcII, whose recognition site is GCRW/TG. The forward slashes (/) in the recognition sites represent the place where the enzyme cuts the DNA.
