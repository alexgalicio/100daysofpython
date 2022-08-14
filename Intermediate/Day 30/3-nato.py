import pandas

df = pandas.read_csv("3-nato_alphabet.csv")
alphabet = {row.letter: row.code for index, row in df.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
