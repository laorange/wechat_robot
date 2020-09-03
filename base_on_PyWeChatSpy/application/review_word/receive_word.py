import re
from util.week import determine_date


def receive_word(if_english: bool, words: str):
    word_ls = re.split('[ ,，\n]', words)
    if if_english:
        path = 'application/review_word/word_data_en.csv'
    else:
        path = 'application/review_word/word_data_fr.csv'
    with open(path, 'at', encoding='UTF-8') as word_data_csv:
        for word in word_ls:
            if word:
                word_data_csv.write(word+','+determine_date()+',0'+'\n')
