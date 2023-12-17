'''
    File_name= letterFreq.py
    Author: Saumya Dhayal
'''
from wordData import *
def trending(words, startYr, endYr):
    '''
    Inputs:
    words: A dictionary mapping words to dictionaries with years and counts.
    startYr: An integer, the starting year for the computation of the trending words.
    endYr: An integer, the ending year for the computation of the trending words.
    Output:
    A list containing a tuple (word, trend) entry for each word for which qualifying data exists. The data is of
    most occurring words, that is, most trending words in that range of years.
    The list is sorted in decreasing trend value.
    '''
    trending_list = []

    for word, counts in words.items():
        if str(startYr) in counts and str(endYr) in counts:
            start_count, end_count = counts[str(startYr)], counts[str(endYr)]

            if int(start_count) >= 1000 and int(end_count) >= 1000:
                trend = int(end_count) / int(start_count)
                trending_list.append((word, trend))

    trending_list.sort(key=lambda x: x[1], reverse=True)
    return trending_list

def main():
    file = input("Enter word file: ")
    startYr=input("Enter starting year: ")
    endYr = input("Enter ending year: ")
    print("The top 10 trending words from ",startYr," to ", endYr, ": ")
    ex=trending(readWordFile(file), startYr, endYr)
    for i in range(0,10):
        print(ex[i][0])
    print("The bottom 10 trending words from ", startYr, " to ", endYr, ": ")
    for i in range(-1,-11, -1 ):
        print(ex[i][0])


if __name__ == "__main__":
    main()