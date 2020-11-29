import os
import shutil
from loguru import logger
import traceback
import time


def move_wechat_file(file, wechat_id):
    try:
        time.sleep(10)
        if not os.path.isfile(file):
            print("%s not exist!" % (file))
        else:
            fpath, fname = os.path.split(file)  # 分离文件名和路径
            dst_path = "C:/wamp64/www/paul/file/" + wechat_id + '/'
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)  # 创建路径
            shutil.move(file, dst_path + fname)  # 移动文件
            logger.info("move %s -> %s" % (file, dst_path + fname))
    except Exception as e:
        traceback.print_exc()
        logger.error(e)
