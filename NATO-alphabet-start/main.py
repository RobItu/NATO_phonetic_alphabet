import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dic = {row.letter: row.code for (index, row) in data.iterrows()}

true_word = True
while true_word:
    try:
        word = input("Type your message: \n").upper()
        nato_word = [nato_dic[letter] for letter in word]
    except KeyError:
        print("Only letters please")
    else:
        print(nato_word)
        true_word = False
