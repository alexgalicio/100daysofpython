import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for index, row in df.iterrows()}

word = input("Enter a word: ").upper()
output = [alphabet[letter] for letter in word]
print(output)
