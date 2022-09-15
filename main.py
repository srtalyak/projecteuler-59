# This program is a solution for
# Project Euler Problem 59
# https://projecteuler.net/problem=59

# decrypt the message and find the sum of the ASCII values in the original text


from itertools import permutations


def openFileAndSplit(fileName, separator="\n"):
    # to simplify getting data from text files
    file = open(fileName, "r")
    liste = file.read()
    file.close()
    return liste.split(separator)


commonEnglishWords = openFileAndSplit("commonEnglishWords.txt", "\n")

# this list is temporary because ascii values in list are in string format
temporaryList = openFileAndSplit("p059_cipher.txt", ",")
asciiValues = []
for temp in temporaryList:
    asciiValues.append(int(temp))
del temporaryList  # no longer needed

alphabet = "abcdefghijklmnopqrstuvwxyz"

for possibleKeys in permutations(alphabet, 3):
    plainText = ""
    commonEnglishWordsNumber = 0

    # increasing the number of elements in the key list up to number of elements in the asciiValues list
    key = possibleKeys * (len(asciiValues) // 3 + 2)
    for i in range(len(asciiValues)):
        plainText += chr(asciiValues[i] ^ ord(key[i]))  # XOR method

    for word in commonEnglishWords:
        if word in plainText:
            commonEnglishWordsNumber += 1
        if commonEnglishWordsNumber > 10:  # controls if there are enough number of common words in text
            print(plainText, end="\n\n")
            sumOfAsciiValues = 0
            for char in plainText:
                sumOfAsciiValues += ord(char)
            print("The key is: {}".format("".join(key[:3])))
            print("Sum of the ASCII values is: {}".format(sumOfAsciiValues))
            break
