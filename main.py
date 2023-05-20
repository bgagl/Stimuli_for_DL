import pandas as pd
from re import compile

from helpers.get_stim_list import get_stims, generate_train_test_list, \
    boil_down_NW, create_NW_from_w_doubleCheck

if __name__ == '__main__':
    stims = get_stims(lexicon="/Users/bg/PycharmProjects/Stimuli_for_DL/lexica/SUBTLEX_BEN_RAW_umlautchange.csv",
                      colname="Word",
                      word_length=[3,4,5],
                      sep=";")
    stims_ = [item for item in stims if not (isinstance(item, float) or any(char.isdigit() for char in item))]
    stims__ = [item for item in stims_ if not any(char.isdigit() for char in item)]
    stims_s = [x for x in stims__ if str(x).isalnum()]
    stims_s_ = [word for word in stims_s if not any(char.isupper() and index > 0 for index, char in enumerate(word))]
    #stim_df = pd.DataFrame(stims_s)
    #stim_df["stims_upper"] = [str(x).upper() for x in stims_s]
    #stims_upper_wo_rep = list(set(stims_upper))
    stims_s_wo_rep_vowel = [x for x in stims_s_ if any(vowel in x for vowel in 'AEIOUaeiou')]

    tmp = [string.lower() for string in stims_s_wo_rep_vowel]
    to_rem_words = ["lest","masst","lust","dur","lost","list","last", "nan"]
    tmp = [item for item in tmp if item not in to_rem_words]
    stims_s_wo_rep_vowel = set(tmp)
    #lest masst lust dur lost list last
    print(len(stims_s_wo_rep_vowel))

    stim_df = pd.DataFrame(stims_s_wo_rep_vowel)
#    stim_df["Word"] = stims_s_wo_rep_vowel
    stim_df.rename(columns={0: 'Word'}, inplace=True)

    stim_df["CS_v1"] = create_NW_from_w_doubleCheck(words=stims_s_wo_rep_vowel, type="CS")
    stim_df["CS_v1"] = boil_down_NW(words=stims_s_wo_rep_vowel, nwords=stim_df["CS_v1"], type="CS")

    stim_df["CS_v2"] = create_NW_from_w_doubleCheck(words=stims_s_wo_rep_vowel, type="CS")
    stim_df["CS_v2"] = boil_down_NW(words=stims_s_wo_rep_vowel, nwords=stim_df["CS_v2"], type="CS")

    stim_df["CS_v3"] = create_NW_from_w_doubleCheck(words=stims_s_wo_rep_vowel, type="CS")
    stim_df["CS_v3"] = boil_down_NW(words=stims_s_wo_rep_vowel, nwords=stim_df["CS_v3"], type="CS")

    stim_df["PW_v1"] = create_NW_from_w_doubleCheck(words=stims_s_wo_rep_vowel, type="PW")
    stim_df["PW_v1"] = boil_down_NW(words=stims_s_wo_rep_vowel, nwords=stim_df["PW_v1"], type="PW")

    stim_df["PW_v2"] = create_NW_from_w_doubleCheck(words=stims_s_wo_rep_vowel, type="PW")
    stim_df["PW_v2"] = boil_down_NW(words=stims_s_wo_rep_vowel, nwords=stim_df["PW_v2"], type="PW")

    stim_df["PW_v3"] = create_NW_from_w_doubleCheck(words=stims_s_wo_rep_vowel, type="PW")
    stim_df["PW_v3"] = boil_down_NW(words=stims_s_wo_rep_vowel, nwords=stim_df["PW_v3"], type="PW")

    stim_df["train_test"] = generate_train_test_list(train_prob=0.8, k=len(stims_s_wo_rep_vowel))

    stim_df.to_csv("/Users/bg/PycharmProjects/Stimuli_for_DL/output/words_pw_cs_tt.csv")


