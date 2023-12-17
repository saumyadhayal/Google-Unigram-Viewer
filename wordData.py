'''
    File_name= letterFreq.py
    Author: Saumya Dhayal
'''
def readWordFile(fileName):
    '''
    Input:
    filename: name of the file that is to be used for conversion
    Output:
    A dictionary mapping words to dictionaries. The "inner" dictionary associated
    with each word will use years as keys and counts as values.
    '''
    with open("data/" + fileName) as file:
        result_dict = {}
        current_word = None
        word_dict = {}

        for line in file:
            line = line.strip()
            if line.isalpha():
                current_word = line
                word_dict = {}
            else:
                line_num = line.split(",")
                year, count= line_num[0], line_num[1]
                word_dict[year] = count

            result_dict[current_word] = word_dict
    return result_dict


def totalOccurrences(word, words):
    """
    Inputs:
    word: The word for which to calculate the count. Not guaranteed to exist in words.
    words: A dictionary mapping words to dictionaries with years and counts.
    Output:
    The total number of times that a word has appeared in print.
    """
    total=0
    for i in words.keys():
        if i == word:
            for k in words[i]:
                total+=(int(words[i][k]))
    return total

def main():
    word_file=input("Enter word file: ")
    word= input("Enter word: ")
    word_dict=readWordFile(word_file)
    print("Total occurrences of",word,":",totalOccurrences(word, word_dict))

if __name__ == "__main__":
    # run main() only when directly invoking this module
    main()

# end of program file