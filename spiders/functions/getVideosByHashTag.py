import sys
import os
import time
# from TikTokApi import TikTokApi
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
COUNT = 1000
# from utils.TikTokAPI import TikTokAPI
from TikTokAPI.tiktokapi import TikTokAPI
from spiders.functions.util import *


def getVideo(tag, count):
    api = TikTokAPI(read_json_from_file("cookie.json"))
    # api = TikTokAPI()
    return api.getVideosByHashTag(tag, count=count)


def run(tag="soccer", count=COUNT):
    res_list = []
    i = 0
    while i < count:
        countIn = count - i if i + 30 > count else 30
        itemList = getVideo(tag, count=countIn).get('itemList', [])
        res_list += itemList
        i += 30
    for res in res_list:

        parse_info(res)


def parse_info(res):
    if not res:
        return
    video_info = parse_video_info(res)
    author_info = parse_author_info(res)
    item_to_store_user_info(author_info)
    item_to_store_video_info(video_info)


def parse_video_info(res):
    data = {}
    data['vid'] = res.get("id", "")
    if data['vid']:
        data['vid'] = int(data['vid'])
    else:
        return
    data['url'] = "https://www.tiktok.com/@{0}/video/{1}".format(res.get("author", {}).get("id"),
                                                                 res.get("id", ""))  # 稿件链接
    data['title'] = res.get('desc')  # 稿件标题
    data['tags'] = '#;#'.join([i.get("title") for i in res.get("challenges")])  # 稿件tag明细
    data['upload_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(res.get('createTime')))  # 投稿时间
    data['play_count'] = res.get("stats", {}).get('playCount')  # 稿件播放量
    data['digg_count'] = res.get("stats", {}).get('diggCount')  # 稿件点赞量
    data['comment_count'] = res.get("stats", {}).get('commentCount')  # 稿件评论量
    data['share_count'] = res.get("stats", {}).get("shareCount")  # 稿件转发量
    data['author_id'] = res.get('author', {}).get('id', "")  # 用户id
    data['author_name'] = res.get("author", {}).get("uniqueId")  # 用户名称
    return data


def parse_author_info(res):
    data = {}
    data['uid'] = res.get('author', {}).get('id', "")  # 用户id
    if data['uid']:
        data['uid'] = int(data['uid'])
    else:
        return
    data['author_name'] = res.get('author', {}).get('uniqueId', "")  # 用户名称
    data['des'] = res.get('author', {}).get('signature', "")  # 用户简介
    data['fans_total'] = res.get('authorStats', {}).get('followerCount', "")  # 粉丝总数
    data['heart_total'] = res.get('authorStats', {}).get('heartCount', "")  # 总点赞量
    data['followers'] = res.get('authorStats', {}).get('followingCount', "")  # 用户关注数
    data['video_total'] = res.get('authorStats', {}).get('videoCount', "")  # 总投稿量
    data['email'] = get_email(data['des'])  # 电子邮箱
    data['phone'] = get_phone(data['des'])  # 联系电话
    data['area'] = get_area(data['des'])  # 用户地域
    data['url'] = "https://www.tiktok.com/@" + data['author_name']  # 用户主页
    data['sec_uid'] = res.get('author', {}).get('secUid', "")  # 用户标识符
    return data


if __name__ == '__main__':
    run()
