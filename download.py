from urllib.request import urlretrieve

link = input ('Image download link : ')

filename = input('Image name : ')

urlretrieve(link, 'images/' + filename + '.png')