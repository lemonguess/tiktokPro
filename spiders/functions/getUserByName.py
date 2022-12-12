import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from utils.TikTokAPI import TikTokAPI

from spiders.functions.util import *


def getUser(user_name):
    api = TikTokAPI(read_json_from_file("cookie.json"))
    return api.getUserByName(user_name)
def parse_info(res):
    data = {}
    data['uid'] = res.get('userInfo', {}).get('user', {}).get('id', "")  # 用户id
    if data['uid']:
        data['uid'] = int(data['uid'])
    else:
        return
    data['author_name'] = res.get('userInfo', {}).get('user', {}).get('uniqueId', "")  # 用户名称
    data['des'] = res.get('userInfo', {}).get('user', {}).get('signature', "")  # 用户简介
    data['fans_total'] = res.get('userInfo', {}).get('stats', {}).get('followerCount', "")  # 粉丝总数
    data['heart_total'] = res.get('userInfo', {}).get('stats', {}).get('heart', "")  # 总点赞量
    data['followers'] = res.get('userInfo', {}).get('stats', {}).get('followingCount', "")  # 用户关注数
    data['video_total'] = res.get('userInfo', {}).get('stats', {}).get('videoCount', "")  # 总投稿量
    data['email'] = get_email(data['des'])  # 电子邮箱
    data['phone'] = get_phone(data['des'])  # 联系电话
    data['area'] = get_area(data['des'])  # 用户地域
    data['url'] = "https://www.tiktok.com/@" + data['author_name']  # 用户主页
    data['sec_uid'] = res.get('userInfo', {}).get('user', {}).get('secUid', "")  # 用户标识符
    return data

def run(user_name="themermaidscale"):
    res = getUser(user_name)
    data = parse_info(res)
    item_to_store_user_info(data)


if __name__ == '__main__':
    run()
