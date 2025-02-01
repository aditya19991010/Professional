#Stratifying gender data

female_Sampledata <- sampleData %>% filter(sampleData$csex == 2)
male_Sampledata <- sampleData %>% filter(sampleData$csex == 1)

colnames(rawcounts)

# Fetch names from male_Sampledata$X
female_sample_names <- female_Sampledata$X

# Fetch corresponding column data from sampledata

selected_columns <- rawcounts[, female_sample_names]

# Create another object to store the selected column data
female_rawcounts <- selected_columns
female_Sampledata
