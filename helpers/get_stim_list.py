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

def create_cs_from_w(words, vowels_uc = 'AEIOU', vowels_lc = 'aeiou', consonants_uc = 'BCDFGHJKLMNPQRSTVWXYZ', consonants_lc = 'bcdfghjklmnpqrstvwxyz'):
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
    vowels_lc = ['a', 'e', 'i', 'o', 'u']
    vowels_uc = ['A', 'E', 'I', 'O', 'U']
    new_pw = ''
    for char in word:
        if char in vowels_uc:
            new_pw += random.choice(vowels_uc)
        elif char in vowels_lc:
            new_pw += random.choice(vowels_lc)
        else:
            new_pw += char
    return new_pw

def get_nw(word, type = "PW"):
    if type == "PW":
        vowels_lc = ['a', 'e', 'i', 'o', 'u']
        vowels_uc = ['A', 'E', 'I', 'O', 'U']
        new_nw = ''
        for char in word:
            if char in vowels_uc:
                new_nw += random.choice(vowels_uc)
            elif char in vowels_lc:
                new_nw += random.choice(vowels_lc)
            else:
                new_nw += char

    elif type == "CS":
        vowels_lc = ['a', 'e', 'i', 'o', 'u']
        vowels_uc = ['A', 'E', 'I', 'O', 'U']
        consonants_uc = 'BCDFGHJKLMNPQRSTVWXYZ'
        consonants_lc = 'bcdfghjklmnpqrstvwxyz'
        new_nw = ''
        for char in word:
            if char in vowels_uc:
                new_nw += random.choice(consonants_uc)
            elif char in vowels_lc:
                new_nw += random.choice(consonants_lc)
            else:
                new_nw += char
    return new_nw

def create_pw_from_w(words):#, vowels_uc = 'AEIOUÄÖÜ', vowels_lc = 'aeiouäöü', consonants_uc = 'BCDFGHJKLMNPQRSTVWXYZ', consonants_lc = 'bcdfghjklmnpqrstvwxyz'):
    new_pws = []
    for word in words:
        modified_word = get_pw(word)
        #print(modified_word+" Baseword: "+word)
        i = 0
        while modified_word in new_pws:
            i = i + 1
            if i < 60:
                modified_word = get_pw(word)
            else:
                modified_word = "XXXXX"
                print(modified_word + " Baseword: " + word)
        i = 0
        while modified_word in words:
            i = i + 1
            if i < 60:
                modified_word = get_pw(word)
            else:
                modified_word = "XXXXX"
                print(modified_word + " Baseword: " + word)

        new_pws.append(modified_word)
        #print(modified_word+" Baseword: "+word)

    return new_pws


def create_NW_from_w_doubleCheck(words, type):#, vowels_uc = 'AEIOUÄÖÜ', vowels_lc = 'aeiouäöü', consonants_uc = 'BCDFGHJKLMNPQRSTVWXYZ', consonants_lc = 'bcdfghjklmnpqrstvwxyz'):
    new_pws = []
    n = 0
    for word in words:
        i = 0
        modified_word = get_nw(word, type=type)
        while check_string_in_lists(modified_word, words, new_pws):
            i = i + 1
            if i < 600:
                modified_word = get_nw(word, type=type)
            else:
                modified_word = "XXXXX"+word
                n = n+1
                print(modified_word + " Baseword: " + word + " N=", str(n))

        new_pws.append(modified_word)

    return new_pws

def boil_down_NW(words, nwords, type):
    new_pws = []
    for non_word in nwords:
        if "XXXXX" in non_word:
            base_w = random.choice(list(words))
            modified_word = get_nw(base_w, type)
            i=0
            n=0
            while check_string_in_lists(modified_word, words, new_pws):
                i = i + 1
                if i < 600:
                    modified_word = get_nw(base_w, type)
                else:
                    modified_word = "XXXXX" + base_w
                    n = n + 1
                    print(modified_word + " BoilDown Baseword: " + base_w + " N=", str(n))

            new_pws.append(modified_word)
        else:
            new_pws.append(non_word)

    return new_pws
def check_string_in_lists(my_string, list1, list2):
    return my_string in list1 or my_string in list2

def generate_train_test_list(train="Train", test="Test", train_prob=.2, k=1):
    options = [train, test]
    probabilities = [train_prob, 1 - train_prob]

    result = random.choices(options, probabilities, k=k)

    return result