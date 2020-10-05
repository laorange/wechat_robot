import pymysql

from util.basic_functions import read_file2list

# 打开数据库连接
# mysql_data_ls = read_file2list('..//..//data/private_space/mysql.txt')

path_fr = 'word_data_fr.csv'
path_en = 'word_data_en.csv'

db = pymysql.connect("localhost", "root", "paulniubi", "wechat_robot")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")


def sql_str_execute(sql_str: str):
    try:
        # 执行sql语句
        cursor.execute(sql_str)
        # 执行sql语句
        db.commit()
        return True

    except Exception as e:
        print(e)
        # 发生错误时回滚
        db.rollback()
        return False


def mysql_word_data(if_english: bool):
    if if_english:
        path = path_en
        table_name = 'word_list_en'
    else:
        path = path_fr
        table_name = 'word_list_fr'

    word_list = read_file2list(path)
    for word in word_list:
        word_info_ls = word.split(',')

        sql = f"\
        INSERT INTO `wechat_robot`.`{table_name}` \
        (`word`, `create_time`, `review_time`, `review_times`, `add_times`, `collect_level`)\
        VALUES ('{word_info_ls[0]}', '2020-09-15', '', 0, 1, 0);"

        try:
            # 执行sql语句
            cursor.execute(sql)
        # 执行sql语句
            db.commit()

        except pymysql.err.IntegrityError:
            sql1 = f"select add_times from `wechat_robot`.`{table_name}` WHERE (`word` = '{word_info_ls[0]}')"
            cursor.execute(sql1)
            add_times = int(cursor.fetchone()[0])
            sql2 = f"UPDATE `wechat_robot`.`{table_name}` SET `add_times` = '{add_times+1}' WHERE (`word` = '{word_info_ls[0]}');"
            sql_str_execute(sql2)

        except Exception as e:
            print(e)
            # 发生错误时回滚
            db.rollback()

    # # # 2.创建游标对象
    # # cursor2 = db.cursor()
    # # 3.组装sql语句 需要查询的MySQL语句
    # sql = "select * from word_list_fr"
    # # 4.执行sql语句
    # cursor.execute(sql)
    #
    # num = 0
    # while True:
    #     row = cursor.fetchone()
    #     print(type(row), end='')
    #     num += 1
    #     if not row:
    #         break
    #     print(row)
    # print('单词数:', num)


# 关闭数据库连接
def connect_off():
    db.close()


if __name__ == "__main__":
    mysql_word_data(if_english=True)
    mysql_word_data(if_english=False)

    # sql = "\
    #         INSERT INTO `wechat_robot`.`word_list_fr` \
    #         (`word`, `create_time`, `review_time`, `review_times`, `add_times`, `collect_level`)\
    #         VALUES ('hello', '2020-09-13', '2020-09-13', 0, 1, 0);"
    #
    # try:
    #     # 执行sql语句
    #     cursor.execute(sql)
    #     # 执行sql语句
    #     db.commit()
    # # except Exception():
    # #     print('hi')
    #
    # except Exception as e:
    #     print(e)
    #     # 发生错误时回滚
    #     db.rollback()

    connect_off()
