#open txt file
wordsfiles = open("words_alpha.txt", "r")

#read in all the lines
lines = wordsfiles.read().split("\n")

sortedDict = {}

#adds all the words to a dict. key is the sorted word in alphabetical order, value is a list of every word the key can make. Ex {"dgo": [dog, god]}
def  sortList(wordList):
    for word in wordList:
        sortedLetters = "".join(sorted(word))

        #if sorted word doesn't exist in Dict, add the key along with the word
        if(sortedDict.get(sortedLetters) == None):
            sortedDict[sortedLetters] = [word]

        #if sorted word already exist in Dict, append new word to the list
        else:
            temp = sortedDict[sortedLetters]
            temp.append(word)
            sortedDict[sortedLetters] = temp


#return the list of words for a given input of letters
def findWords(letters):
    letters = letters.lower()
    sortedLetters = "".join(sorted(letters))
    answerList = sortedDict.get(sortedLetters)
    return answerList


#makes Dict with given list of Words
sortList(lines)

# function call with letters
answer = findWords("dgo")
print(answer)













