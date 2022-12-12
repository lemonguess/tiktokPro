import logging
import time
from TikTokApi import TikTokApi
# from utils.pipline_mysql import add_to_table
# from utils.log_template import Logger
# from config.config import LOGGING
logger = logging.getLogger('log')
TAG_LIST = ["ibrahimovic"]
COUNT = 200


def get_info_by_tags(tag):
    """
    根据tag查找相关视频
    :return:
    """
    with TikTokApi() as api:
        tag = api.hashtag(name=tag)

        for index, video in enumerate(tag.videos(count=COUNT)):
            author_info = parse_author_info(video)
            video_info = parse_video_info(video)
            add_to_table(table_name="author_info_by_tags", item=author_info)
            add_to_table(table_name="video_info_by_tags", item=video_info)
            logger.info("【入库成功】{}".format(video_info.get('url')))
            print(index+1)
            index += 1



def parse_author_info(video):
    """
    解析作者信息
    :return:
    """
    author_dict = video.author.as_dict
    author_stats = video.as_dict.get('authorStats')
    data = {}
    data['author_id'] = author_dict.get('id')  # 用户id
    data['author_name'] = author_dict.get('uniqueId')  # 用户昵称
    data['des'] = author_dict.get('signature')  # 用户简介明细
    data['secUid'] = author_dict.get('secUid')  # UID
    data['followerCount'] = author_stats.get('followerCount')  # 粉丝数
    data['heartCount'] = author_stats.get('heartCount')  # 点赞量
    # data['secUid'] = author_dict.get('secUid')  # 国家or地区
    data['videoCount'] = author_stats.get('videoCount')  # 总投稿量
    data['followingCount'] = author_stats.get('followingCount')  # 作者关注数
    return data


def parse_video_info(video):
    """
    解析该视频信息
    :param video:
    :return:
    """
    data = {}
    data['url'] = "https://www.tiktok.com/@{0}/video/{1}".format(video.author.username, video.id)  # 稿件链接
    data['title'] = video.as_dict.get('desc')  # 稿件标题
    data['tags'] = '#;#'.join([i.name for i in video.hashtags])  # 稿件tag明细
    data['createTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(video.as_dict.get('createTime')))  # 投稿时间
    data['playCount'] = video.stats.get('playCount')  # 稿件播放量
    data['diggCount'] = video.stats.get('diggCount')  # 稿件点赞量
    data['commentCount'] = video.stats.get('commentCount')  # 稿件评论量
    data['shareCount'] = video.stats.get("shareCount")  # 稿件转发量
    return data


if __name__ == '__main__':
    get_info_by_tags(TAG_LIST[0])
