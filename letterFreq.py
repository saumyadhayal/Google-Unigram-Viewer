'''
    File_name= letterFreq.py
    Author: Saumya Dhayal
'''
import matplotlib.pyplot as plt
from wordData import *


def letterFreq(words):
    '''
    Input:
    words: A dictionary mapping words to dictionaries with years and counts.
    Output:
    A string containing the 26 lowercase characters in the English alphabet, sorted in decreasing
    order of frequency of occurrence of each character. The function also displays a graph with plotting the
    counts distribution.
    '''
    dict1= {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for i in words:
        letters=list(i)
        for j in letters:
            dict1[j] += 1
            dict1[j] += int(totalOccurrences(i, words))

    sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
    # print("Letters sorted by decreasing frequency: ", end="")
    ordered_str=""
    for i in sorted_dict:
        ordered_str += i
    plt.bar(list(dict1.keys()), list(dict1.values()), color="skyblue")
    plt.show()

    return ordered_str

def main():
    word_file=input("Enter word file: ")
    word_dict=readWordFile(word_file)
    print("Frequency ordering of letters:",letterFreq(word_dict))

if __name__ == "__main__":
    # run main() only when directly invoking this module
    main()