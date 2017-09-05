#Charlie Goodrich
#09/04/17
#stringAnalysis.py - analyzes a string and gives information about the string

fullSentence = input("Enter a sentence: ")
lowerSentence = fullSentence.lower()

characters = len(fullSentence)

print("Your sentence has", fullSentence.count(" ") + 1, "words,", 
 len(fullSentence) - fullSentence.count(" "), "letters, and", len(fullSentence),
 "characters.")

letterSearch = input("Enter a letter search for: ")
print(lowerSentence.count(letterSearch))

wordSearch = input("Enter a word search for: ")
print(lowerSentence.count(wordSearch))