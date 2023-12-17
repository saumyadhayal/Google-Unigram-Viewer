'''
    File_name= letterFreq.py
    Author: Saumya Dhayal
'''
from wordData import *
import matplotlib.pyplot as plt

def printedWords(words):
    '''
    Input:
    words: A dictionary mapping words to dictionaries with years and counts.
    Output:
    A list containing tuples (year, count total words) for each year for which data exists.
    The list must be sorted in ascending order of year.
    '''
    list1 = []
    unique_years = set()
    for word in words:
        for year in words[word]:
            unique_years.add(year)

    # Sort the unique years, converts set to list
    sorted_years = sorted(unique_years)

    for year in sorted_years:
        total_count = 0
        for word in words:
            # Add the count for the current year if available, otherwise add 0
            total_count += int(words[word].get(year, 0))
        tuple_entry = (year, total_count)
        list1.append(tuple_entry)

    return list1


def wordsForYear(year, yearList):
    '''
    Inputs:
    year: an integer representing the year being queried.
    yearList: a list of tuples (year, count total words), as defined in ABOVE function.
    The list must be sorted in ascending order of year.
    Output:
    An integer count representing the total number of printed words for that year.
    If there is no entry in yearList for the requested year, the function returns 0.
    The function also generates a complete plot of the number of printed words as a function of the year.
    '''
    year_num=0
    for i in range(len(yearList)):
        if yearList[i][0] == str(year):
            year_num = yearList[i][1]

    years=[]
    years_count=[]
    for i in range(len(yearList)):
        years.append(yearList[i][0])
        years_count.append(yearList[i][1])

    plt.plot(years, years_count)
    custom_x_ticks = ['1900', '1920', '1940', '1960', '1980', '2000']
    plt.xticks(custom_x_ticks)
    plt.show()

    return year_num

def main():
    file = input("Enter word file: ")
    year = input("Enter year to count: ")
    words= readWordFile(file)
    x = printedWords(words)
    for i in x:
        if i[0] == year:
            print("Total printed words in 1928 :", i[1])


if __name__ == "__main__":
    main()