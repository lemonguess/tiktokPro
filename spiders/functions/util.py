import json
import os
import re
import django
import sys
from django.db import IntegrityError
from datetime import datetime
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TikTokBackEnd.settings')
django.setup()
logger = logging.getLogger('log')
from spiders.models import TiktokUsersInfo, TiktokVideosInfo


def read_json_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    if type(data) is str:
        return json.loads(data)
    return data


def get_email(meta):
    email = re.findall("[\w\.-]+@[\w\.-]+", meta)
    email = email[2:-2] if email else None
    return email


def get_phone(meta):
    ...


def get_area(meta):
    ...


def item_to_store_user_info(data):
    try:
        TiktokUsersInfo.objects.create(**data)
        logger.info("【已创建数据】:::")
    except IntegrityError:
        try:
            TiktokUsersInfo.objects.filter(uid=data['uid']).filter().update(**data, update_time=datetime.now())
            logger.info("【已更新数据】:::")
        except Exception as err:
            logger.error(err)
    except Exception as err:
        logger.error(err)
    finally:
        logger.info(data)


def item_to_store_video_info(data):
    try:
        TiktokVideosInfo.objects.create(**data)
        logger.info("【已创建数据】:::")
    except IntegrityError:
        try:
            TiktokVideosInfo.objects.filter(uid=data['vid']).filter().update(**data, update_time=datetime.now())
            logger.info("【已更新数据】:::")
        except Exception as err:
            logger.error(err)
    except Exception as err:
        logger.error(err)
    finally:
        logger.info(data)
