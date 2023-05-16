import pandas as pd
from re import compile

from helpers.get_stim_list import get_stims, create_cs_from_w, create_pw_from_w, generate_train_test_list

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
    stims_s_wo_rep_vowel = [x for x in stims_s_ if any(vowel in x for vowel in 'AEIOUAEIOUAEIOUAEIOUÄÖÜaeiouaeiouaeiouaeiouöäü')]

    stims_s_wo_rep_vowel = set(stims_s_wo_rep_vowel)
    print(len(stims_s_wo_rep_vowel))

    stim_df = pd.DataFrame(stims_s_wo_rep_vowel)
#    stim_df["Word"] = stims_s_wo_rep_vowel
    stim_df.rename(columns={0: 'Word'}, inplace=True)

    stim_df["CS_v1"] = create_cs_from_w(words=stims_s_wo_rep_vowel)
    stim_df["CS_v2"] = create_cs_from_w(words=stims_s_wo_rep_vowel)
    stim_df["CS_v3"] = create_cs_from_w(words=stims_s_wo_rep_vowel)

    stim_df["PW_v1"] = create_pw_from_w(words=stims_s_wo_rep_vowel)
    stim_df["PW_v2"] = create_pw_from_w(words=stims_s_wo_rep_vowel)
    stim_df["PW_v3"] = create_pw_from_w(words=stims_s_wo_rep_vowel)

    stim_df["train_test"] = generate_train_test_list(train_prob=0.8, k=len(stims_s_wo_rep_vowel))

    stim_df.to_csv("/Users/bg/PycharmProjects/Stimuli_for_DL/output/words_pw_cs_tt.csv")
    #stim_df_ = pd.DataFrame(cs)
    #stim_df_["cond"] = "CS"
    #stim_df_.rename(columns={'0': 'string'})

    #pd.concat([stim_df_, stim_df]).to_csv("/Users/bg/PycharmProjects/Stimuli_for_DL/output/words_cs.csv")
    #print(create_pw_from_w(words=stims_s_wo_rep_vowel[:20]))

    #stim_df_ = pd.DataFrame(pw)
    #stim_df_["cond"] = "PW"
    #stim_df_.rename(columns={'0': 'string'})

    #pd.concat([stim_df_, stim_df]).to_csv("/Users/bg/PycharmProjects/Stimuli_for_DL/output/words_pw__.csv")

