import re
from util.week import determine_date


def receive_word(words: str):
    word_ls = re.split('[ ,，\n]', words)
    with open('application/review_word/word_data.csv', 'at', encoding='UTF-8') as word_data_csv:
        for word in word_ls:
            if word:
                word_data_csv.write(word+','+determine_date()+',0'+'\n')

