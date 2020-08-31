# basic_functions.py

import os


def make_dir(path_name):
    try:
        os.mkdir(path_name)
    except FileExistsError:
        pass


def read_file2list(path_name):  # , encoding='UTF-8'
    # result = chardet.detect(open(path_name, "rb").read())
    #
    # char_enc = result['encoding']

    try:
        with open(path_name, 'rt', encoding='UTF-8') as source_text:   # , encoding=encoding
            lines_ls = source_text.readlines()
            if lines_ls:
                for i in range(len(lines_ls)):
                    lines_ls[i] = lines_ls[i].strip()
        return lines_ls
    except FileNotFoundError:
        raise FileNotFoundError
    except Exception as e:
        try:
            with open(path_name, 'rt', encoding='ANSI') as source_text:   # , encoding=encoding
                print(e)
                lines_ls = source_text.readlines()
                if lines_ls:
                    for i in range(len(lines_ls)):
                        lines_ls[i] = lines_ls[i].strip()
            return lines_ls
        except Exception as e:
            try:
                with open(path_name, 'rt', encoding='gbk') as source_text:  # , encoding=encoding
                    print(e)
                    lines_ls = source_text.readlines()
                    if lines_ls:
                        for i in range(len(lines_ls)):
                            lines_ls[i] = lines_ls[i].strip()
                return lines_ls
            except Exception as e:
                print(e)
                return []

    # pprint.pprint(lines_ls)



