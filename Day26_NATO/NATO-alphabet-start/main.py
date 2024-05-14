import pandas

datas = pandas.read_csv('nato_phonetic_alphabet.csv')
new_data = {row.letter: row.code for (index, row) in datas.iterrows()}

word = input('Enter your word:').upper()
output = [new_data[letter] for letter in word]
print(output)
