# Google-Unigram-Viewer
allows a user to enter a word and search for historical information on the usage of that word across the years

Google Books provides a valuable service that allows users to search a digital database of books and magazines. This database, scanned and converted to text using optical character recognition, spans from the 1500s to the most recent data available in 2008. As part of this project, we will be working with a subset of the database and leveraging the Google Ngram Viewer tool to perform statistical analysis.

Project Tasks

Task 1: Compute Relative Letter Frequency
Compute the relative frequencies of the 26 English letters across all data in our database.

Task 2: Compute the Number of Printed Words
Compute the total number of printed words as a function of the year. This information will be plotted to observe trends in the increase or decrease of printed words over the years.

Task 3: Compute Trends
Choose a starting year and an ending year, then identify which words saw the greatest increase or decrease in usage during this timespan.

Task 4: Find Most Similar Words
Calculate the most similar words using historical counts of words. The smaller the word count differences between words over the years, the more similar they will be considered.

Getting Started

Data
Google provides approximately 4 Gigabytes of zip files representing unigram data. To make the data more manageable for this project, it has been filtered in several ways, including retaining only data from 1900-2008 and keeping words that are entirely lowercase letters and have appeared at least 10,000 times in print for some year.

Data Files

All words
Words beginning with 'a'
Words beginning with 'z'
Words beginning with a vowel
A very short data file containing partial data for only three words
Provided Code
Source files for the project, each corresponding to a specific task:

testLetterFreq.py: for testing your program for Task 1.
testPrintedWords.py: for testing your program for Task 2.
testTrending.py: for testing your program for Task 3.
testWordSimilarity.py: for testing your program for Task 4.
