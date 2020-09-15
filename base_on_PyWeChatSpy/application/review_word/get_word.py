import time
from util.week import determine_date
from util.basic_functions import read_file2list

path_fr = 'application/review_word/word_data_fr.csv'
path_en = 'application/review_word/word_data_en.csv'
path_test = 'word_data_fr.csv'


# class WordInfo:
#     def __init__(self, language, word: str, review_date: str, review_times: int):
#         self.language = language
#         self.word = word
#         self.review_date = review_date
#         self.review_times = review_times
#         self.interval = 0  # int
#         self.possibility = 1.00
#
#     def determine(self, date_today):
#         t_today_strp = time.strptime(date_today, '%Y-%m-%d')
#         t_today = time.mktime(t_today_strp)
#         t_review_date_strp = time.strptime(self.review_date, '%Y-%m-%d')
#         t_review_date = time.mktime(t_review_date_strp)
#         self.interval = (t_today - t_review_date) // 86400
#         self.possibility = 0.8 ** self.review_times + 0.04 * self.interval
#         if self.possibility > 1:
#             self.possibility = 1


class WordInfo:
    def __init__(self, language: str, word: str, create_time: str, review_time: str, review_times: int or str,
                 add_times: int or str, collect_level: int):
        self.language = language
        self.word = word
        self.create_time = create_time
        self.review_time = review_time if review_time else create_time
        self.review_times = review_times
        self.add_times = add_times
        self.collect_level = collect_level

        self.interval = 0  # int
        self.possibility = 1.00

    def determine(self, date_today):
        t_today_strp = time.strptime(date_today, '%Y-%m-%d')
        t_today = time.mktime(t_today_strp)
        t_review_date_strp = time.strptime(self.review_time, '%Y-%m-%d')
        t_review_date = time.mktime(t_review_date_strp)
        self.interval = (t_today - t_review_date) // 86400
        self.possibility = 0.8 ** self.review_times + 0.04 * self.interval
        if self.possibility > 1:
            self.possibility = 1


# def get_word(if_english: bool):
#     word_info_ls = []
#     try:
#         if if_english:
#             word_list = read_file2list(path_en)
#             language = 'English'
#         else:
#             word_list = read_file2list(path_fr)
#             language = 'French'
#     except Exception as e:
#         language = ''
#         print(e)
#         word_list = read_file2list(path_test)
#
#     for word in word_list:
#         word_info = WordInfo(language, word.split(',')[0], word.split(',')[1], int(word.split(',')[2]))
#         word_info.determine(determine_date())
#         word_info_ls.append(word_info)
#     return word_info_ls


if __name__ == '__main__':
    # word_info_list = get_word(if_english=False)
    raise Exception('test')
