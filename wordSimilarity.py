from wordData import *
import math
import numpy as np
'''
    File_name= letterFreq.py
    Author: Saumya Dhayal
'''
def topSimilar(words, word):
    """
    Input:
    words: A dictionary mapping words to dictionaries with years and counts.
    word: a word, for which we are looking for similar words.
    Output:
    A list of the top five words including the input word in the descending order of similarity
    Working:
    The code first initializes a matrix with years that store all the values, then to the matrix we add all
    of occurring per year in the word given by user and another of occurring of other words in the file.
    Then, using the given formula it takes cos of angle between the word given
    by user and comparing with each other word. Now, we normalize the matrix and get dot-product between
    the two normalized vectors. The matrices/boxes are made using numpy. Then based on dot-product, we sort
    the matrix and get the 5 most similar words.
    """
    sum_box = 0
    box = np.zeros(2008 - 1900)
    for year in words[word]:
        box[int(year)-1900 - 1] = words[word][year]
    for occurrance in box:
        sum_box += occurrance ** 2
    sqrt1 = math.sqrt(sum_box)
    for i in range(len(box)):
        box[i] = box[i] / sqrt1

    counts = np.zeros((len(words), 2008-1900))
    val = 0
    for word in words:
        sum_box = 0
        for year in words[word]:
            total = int(words[word][year])
            sum_box += total**2
            counts[val][int(year)-1900-1] = total
        sqrt2 = math.sqrt(sum_box)
        for x in range(len(box)):
            counts[val][x] = counts[val][x] / sqrt2
        val += 1

    n = counts.dot(box)
    top_five = np.argsort(n)[-5:]
    top_five = top_five[::-1]

    final = []
    for j in top_five:
        final.append(list(words)[j])
    return final


def main():
    file = input("Enter word file: ")
    word = input("Enter word: ")
    similar_words = topSimilar(readWordFile(file), word)
    list1=[]
    for x in similar_words:
        list1.append(x)
    print(list1)


if __name__ == "__main__":
    main()