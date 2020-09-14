import random
import os.path

input_txt = os.path.join(os.path.dirname(__file__), 'input.txt')
# Read in all the words in one go
with open(input_txt) as f:
    words = f.read()

# TODO: analyze which words can follow other words
nextWord = {}
wordList = words.split()
for (i, word) in enumerate(wordList[:-1]):
    if word in nextWord:
        nextWord[word].append(wordList[i + 1])
    else:
        nextWord[word] = [wordList[i + 1]]


# TODO: construct 5 random sentences
#upper case start to sentence
def startWords(s):
    firstLetter = s[1] if (s[0] == '\"' and len(s) > 1) else s[0]
    return firstLetter.isupper()

#punctuate the ending
def endWords(s):
    finalLetter = s[-2]  if (s[-1] == '\"' and len(s) > 1) else s[-1]
    return finalLetter in ["?", "!", "."]

#show the results (hopefully)

def printRando(numOfSentences):
    print("\n")
    for _ in range(numOfSentences):
        word = random.choice(wordList)
        while not startWords(word):
            word = random.choice(wordList)
        sentence = word

        word = random.choice(nextWord[word])
        sentence += " " + word

        while not endWords(word):
            word = random.choice(nextWord[word])
            sentence += " " + word

        if sentence.count('\"') % 2 != 0:
            if sentence[-1] =='\"':
                sentence = sentence[:-1]
            else:
                sentence += '\"'
        print(f"{sentence}\n")

printRando(5)
#WORKS!! Prints but my quotes don't work
