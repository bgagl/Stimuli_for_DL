import pandas as pd
import random

def get_stims(lexicon = "./", word_length=[3,4,5], sep=",", colname = "type"):
    lex = pd.read_csv(lexicon, sep=sep)
    w_list = lex[colname][lex["Spellcheck"]==1]
    n_lett = [len(str(word)) for word in w_list]
    w_df = list(zip(w_list, n_lett))
    df = pd.DataFrame(w_df, columns=["word", "n_lett"])
    w_list_part = []
    for n_letters in word_length:
        w_list_part = w_list_part + list(df["word"][df["n_lett"] == n_letters])

    return w_list_part

def create_cs_from_w(words, vowels_uc = 'AEIOUÄÖÜ', vowels_lc = 'aeiouäöü', consonants_uc = 'BCDFGHJKLMNPQRSTVWXYZ', consonants_lc = 'bcdfghjklmnpqrstvwxyz'):
    #'bcdfghjklmnpqrstvwxyz'
    new_word_list = []
    for word in words:
        new_word = ''
        for char in word:
            if char in vowels_uc:
                new_word += random.choice(consonants_uc)
            elif char in vowels_lc:
                new_word += random.choice(consonants_lc)
            else:
                new_word += char
        new_word_list.append(new_word)

    return new_word_list

def get_pw(word):
    vowels_lc = ['a', 'e', 'i', 'o', 'u','a', 'e', 'i', 'o', 'u','a', 'e', 'i', 'o', 'u','a', 'e', 'i', 'o', 'u', 'ü', 'ä', 'ö']
    vowels_uc = ['A', 'E', 'I', 'O', 'U','A', 'E', 'I', 'O', 'U','A', 'E', 'I', 'O', 'U','A', 'E', 'I', 'O', 'U', 'Ü', 'Ä', 'Ö']
    new_pw = ''
    for char in word:
        if char in vowels_uc:
            new_pw += random.choice(vowels_uc)
        elif char in vowels_lc:
            new_pw += random.choice(vowels_lc)
        else:
            new_pw += char
    return new_pw

def create_pw_from_w(words):#, vowels_uc = 'AEIOUÄÖÜ', vowels_lc = 'aeiouäöü', consonants_uc = 'BCDFGHJKLMNPQRSTVWXYZ', consonants_lc = 'bcdfghjklmnpqrstvwxyz'):
    new_pws = []
    for word in words:
        modified_word = get_pw(word)
        #print(modified_word+" Baseword: "+word)
        while modified_word in words:
            modified_word = get_pw(word)
        new_pws.append(modified_word)
        #print(modified_word+" Baseword: "+word)

    return new_pws


def generate_train_test_list(train="Train", test="Test", train_prob=.2, k=1):
    options = [train, test]
    probabilities = [train_prob, 1 - train_prob]

    result = random.choices(options, probabilities, k=k)

    return result