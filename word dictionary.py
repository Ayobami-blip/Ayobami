from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input('Search for a word: ')
    if word == "" :
        break

    print(dictionary.meaning(word))