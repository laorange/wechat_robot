import pymysql
import re

from application.review_word.get_word import WordInfo

from util.time_util import *

import traceback

path_fr = 'word_data_fr.csv'
path_en = 'word_data_en.csv'

db = pymysql.connect("localhost", "root", "paulniubi", "wechat_robot")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")


def sql_str_execute(sql_str: str):
    try:
        db.ping(reconnect=True)
        # 执行sql语句
        cursor.execute(sql_str)
        # 执行sql语句
        db.commit()
        return True

    except Exception as e:
        print(e)
        traceback.print_exc()
        # 发生错误时回滚
        db.rollback()
        return False


def add_user(wechat_id: str, grade: int, class_a_or_b: str, class_p_ab_cd: str, class_f_ab_cd_e: str):
    sql = f"\
        INSERT INTO `wechat_robot`.`user_list` \
        (`wechat_id`, `grade`, `class_a_or_b`, `class_p_ab_cd`, `class_f_ab_cd_e`) \
        VALUES ('{wechat_id}', {grade}, '{class_a_or_b}', '{class_p_ab_cd}', '{class_f_ab_cd_e}');"
    return sql_str_execute(sql)


def delete_user(wechat_id: str):
    sql = f"DELETE FROM `wechat_robot`.`user_list` WHERE (`wechat_id` = '{wechat_id}');"
    return sql_str_execute(sql)


def check_user(wechat_id: str):
    sql = f"select * from user_list WHERE (`wechat_id` = '{wechat_id}')"
    try:
        db.ping(reconnect=True)
        # 执行sql语句
        cursor.execute(sql)

        row = cursor.fetchone()
        # print(type(row), end='')
        # print(f"{wechat_id}: {row}")
        return row

    except Exception as e:
        print(e)
        # 发生错误时回滚
        db.rollback()
        return 'error'


def get_user_list_all_data():
    user_list = []
    sql = "select * from user_list"

    db.ping(reconnect=True)
    cursor.execute(sql)

    num = 0
    while True:
        row = cursor.fetchone()
        # print(type(row), end='')
        if not row:
            break
        num += 1
        # print(row)
        user_list.append(row)
    print('用户数:', num)
    return user_list


def get_user_list_wechat_id():
    user_list = []
    sql = "select `wechat_id` from user_list"

    db.ping(reconnect=True)
    cursor.execute(sql)

    num = 0
    while True:
        row = cursor.fetchone()
        # print(type(row), end='')
        if not row:
            break
        num += 1
        # print(row)
        user_list.append(row[0])
    print('用户数:', num)
    return user_list


def count_user_each_grade():
    grade_ls = []

    sql1 = 'SELECT DISTINCT `grade` FROM `wechat_robot`.`user_list`;'

    db.ping(reconnect=True)
    cursor.execute(sql1)
    while True:
        row = cursor.fetchone()
        if not row:
            break
        grade_ls.append(str(row[0]))

    grade_dict = {}
    for grade in grade_ls:
        grade_dict[str(grade)] = 0

    sql = "select * from user_list"

    db.ping(reconnect=True)
    cursor.execute(sql)

    num = 0
    while True:
        row = cursor.fetchone()
        # print(type(row), end='')
        if not row:
            break
        num += 1
        # print(row)
        if str(row[2]) in grade_ls:
            grade_dict[str(row[2])] += 1

    sum_str = '总用户数:' + str(num)
    count_user_in_grade_str = ''
    for grade in grade_ls:
        count_user_in_grade_str = count_user_in_grade_str + str(grade) + '级用户数:' + str(grade_dict[str(grade)]) + '\n\n'

    send_str = sum_str + '\n\n' + count_user_in_grade_str.strip()
    return send_str


def count_ask(wechat_id, situation_code: int):
    situation = ''
    if situation_code == 0:
        situation = 'today'
    elif situation_code == 1:
        situation = 'tom'
    elif situation_code == 2:
        situation = 'dat'
    elif situation_code == 3:
        situation = 'far'
    if situation:
        sql1 = f"select `ask_{situation}` from `wechat_robot`.`user_list` WHERE (`wechat_id` = '{wechat_id}')"

        db.ping(reconnect=True)
        cursor.execute(sql1)
        ask_times = int(cursor.fetchone()[0])

        sql2 = f"UPDATE `wechat_robot`.`user_list` SET `ask_{situation}` = '{ask_times + 1}' WHERE (`wechat_id` = '{wechat_id}');"
        sql_str_execute(sql2)


def set_remark(wechat_id, remark):
    sql = f"UPDATE `wechat_robot`.`user_list` SET `remark` = '{remark}' WHERE (`wechat_id` = '{wechat_id}');"
    print(wechat_id, ':', remark)
    sql_str_execute(sql)


def get_remark_from_sql(wechat_id: str):
    sql = f"select `remark` from user_list WHERE (`wechat_id` = '{wechat_id}')"
    try:
        db.ping(reconnect=True)
        # 执行sql语句
        cursor.execute(sql)

        row = cursor.fetchone()
        if row:
            row = row[0]
        else:
            row = ''
        # print(type(row), end='')
        # print(f"{wechat_id}: {row}")
        return row

    except Exception as e:
        print(e)
        # 发生错误时回滚
        db.rollback()
        return ''


# TODO: 单词
def add_word_to_mysql(if_english: bool, word_text: str):
    if if_english:
        table_name = 'word_list_en'
    else:
        table_name = 'word_list_fr'

    word_list = word_text.split('\n')
    for word in word_list:
        if word:
            word_info_ls = word.split(',')

            sql = f"\
            INSERT INTO `wechat_robot`.`{table_name}` \
            (`word`, `create_time`, `review_time`, `review_times`, `add_times`, `collect_level`)\
            VALUES ('{word_info_ls[0]}', '2020-09-13', '', 0, 1, 0);"

            try:
                db.ping(reconnect=True)
                # 执行sql语句
                cursor.execute(sql)
                # 执行sql语句
                db.commit()

            except pymysql.err.IntegrityError as e:
                print(e)
                sql1 = f"select add_times from `wechat_robot`.`{table_name}` WHERE (`word` = '{word_info_ls[0]}')"

                db.ping(reconnect=True)
                cursor.execute(sql1)

                add_times = int(cursor.fetchone()[0])
                sql2 = f"UPDATE `wechat_robot`.`{table_name}` SET `add_times` = '{add_times + 1}' WHERE (`word` = '{word_info_ls[0]}');"
                sql_str_execute(sql2)

            except Exception as e:
                print(e)
                # 发生错误时回滚
                db.rollback()


def get_word_from_mysql(if_english: bool):
    word_list = []
    word_info_ls = []
    if if_english:
        table_name = 'word_list_en'
        language = 'English'
    else:
        table_name = 'word_list_fr'
        language = 'French'
    try:
        sql = f"select * from `wechat_robot`.`{table_name}`"

        db.ping(reconnect=True)
        cursor.execute(sql)

        num = 0
        while True:
            row = cursor.fetchone()
            # print(type(row), end='')
            if not row:
                break
            num += 1
            word_list.append(row)
        print(language + ' 数据库中单词数:', num)

        if word_list:
            for word in word_list:
                word_info = WordInfo(language, word[0], word[1], word[2], word[3], word[4], word[5])
                word_info.determine(determine_date())
                word_info_ls.append(word_info)
    except Exception as e:
        print(e)
    return word_info_ls


def review_times_plus1(if_english: bool, word: str):
    if if_english:
        table_name = 'word_list_en'
    else:
        table_name = 'word_list_fr'
    sql1 = f"select review_times from `wechat_robot`.`{table_name}` WHERE (`word` = '{word}')"

    db.ping(reconnect=True)
    cursor.execute(sql1)

    review_times = int(cursor.fetchone()[0])
    sql2 = f"UPDATE `wechat_robot`.`{table_name}` SET `review_times` = '{review_times + 1}' WHERE (`word` = '{word}');"
    sql_str_execute(sql2)
    sql3 = f"UPDATE `wechat_robot`.`{table_name}` SET `review_time` = '{determine_date()}' WHERE (`word` = '{word}');"
    sql_str_execute(sql3)


def clear_review_record(if_english: bool, word: str):
    if if_english:
        table_name = 'word_list_en'
    else:
        table_name = 'word_list_fr'
    sql = f"UPDATE `wechat_robot`.`{table_name}` SET `review_times` = '0' WHERE (`word` = '{word}');"

    db.ping(reconnect=True)
    sql_str_execute(sql)


# 关闭数据库连接
def connect_off():
    db.close()


def change_grade_20dd_dd():
    name_ls = []
    sql1 = 'SELECT `wechat_id` FROM `wechat_robot`.`user_list`;'
    db.ping(reconnect=True)
    cursor.execute(sql1)
    while True:
        row = cursor.fetchone()
        if not row:
            break
        name = row[0]
        name_ls.append(name)
    for name in name_ls:
        sql2 = f"SELECT `grade` FROM `wechat_robot`.`user_list` WHERE (`wechat_id` = '{name}');"
        cursor.execute(sql2)
        row = cursor.fetchone()
        grade = row[0]
        if isinstance(grade, int):
            if grade > 2000:
                new_grade = int(str(row[0])[2:])
        else:
            continue
        sql3 = f"UPDATE `wechat_robot`.`user_list` SET `grade` = {new_grade} WHERE (`wechat_id` = '{name}');"
        sql_str_execute(sql3)


if __name__ == "__main__":
    # mysql_word_data(if_english=True)
    # add_word_to_mysql(if_english=False)
    # get_word_from_mysql(if_english=True)
    # get_word_from_mysql(if_english=False)
    # change_grade_20dd_dd()
    print(count_user_each_grade())
    # delete_user('wxid_l7g2lb2rsop622')
    connect_off()
