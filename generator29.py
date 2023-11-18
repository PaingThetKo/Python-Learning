words = ['apple', 'orange', 'lime', 'limon', 'lemon']

from random import randint
def randomSentenceGenerator(word):
    randomIndex=randint(0,len(words)-1)
    return f'{words[randomIndex]} {word}'

with open('./text2copy29.txt') as file:
    paragraph = file.read()
    wordLists = paragraph.split()
    sentenceList = list(map(randomSentenceGenerator,wordLists))
    paraCount = int(input('Paragraph count : '))

    for count in range(paraCount):
        with open('./generator29.txt' , 'a') as write_text:
            write_text.write(' '.join(sentenceList) + '\n\n')