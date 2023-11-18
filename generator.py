with open('./text2copy.txt') as file:
    paragraph = file.read()

    paraCount = int(input('Paragraph count : '))

    for count in range(paraCount):
        with open('./generator.txt' , 'a') as write_text:
            write_text.write(paragraph + '\n\n')