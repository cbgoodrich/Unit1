#Charlie Goodrich
#09/04/17
#stringAnalysis.py - analyzes a string and gives information about the string

fullSentence = input("Enter a sentence: ")
lowerSentence = fullSentence.lower()

sentenceList = fullSentence.split()
characters = len(fullSentence)
word1 = len(sentenceList[0])
word2 = len(sentenceList[1])
word3 = len(sentenceList[2])
word4 = len(sentenceList[3])
word5 = len(sentenceList[4])
word6 = len(sentenceList[5])
word7 = len(sentenceList[6])
word8 = len(sentenceList[7])
word9 = len(sentenceList[8])
letters = word1+word2+word3+word4+word5+word6+word7+word8+word9
print("Your sentence has", len(sentenceList), "words,", letters, "letters, and",
characters, "characters.")


letterSearch = input("Enter a letter search for: ")
print(lowerSentence.count(letterSearch))

wordSearch = input("Enter a word search for: ")
print(lowerSentence.count(wordSearch))