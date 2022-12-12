from django.db import models


class TiktokUsersInfo(models.Model):
    uid = models.BigIntegerField(verbose_name='用户id', primary_key=True)
    author_name = models.TextField(verbose_name='用户名称', null=True)
    des = models.TextField(verbose_name='用户简介', null=True)
    url = models.TextField(verbose_name='用户主页', null=True)
    fans_total = models.TextField(verbose_name='粉丝总数', null=True)
    heart_total = models.TextField(verbose_name='总点赞量', null=True)
    video_total = models.TextField(verbose_name='总投稿量', null=True)
    followers = models.TextField(verbose_name='用户关注数', null=True)
    sec_uid = models.TextField(verbose_name='用户标识符', null=True)
    area = models.TextField(verbose_name='用户地域', null=True)
    email = models.TextField(verbose_name='电子邮箱', null=True)
    phone = models.TextField(verbose_name='联系电话', null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'tiktok_users_info'

    def __str__(self):
        return '%s' % (self.author_name)


class TiktokVideosInfo(models.Model):
    vid = models.BigIntegerField(verbose_name='视频id', primary_key=True)
    title = models.TextField(verbose_name='稿件标题', null=True)
    url = models.TextField(verbose_name='稿件链接', null=True)
    upload_time = models.DateTimeField(verbose_name='投稿时间', null=True)
    tags = models.TextField(verbose_name='稿件tag明细', null=True)
    play_count = models.TextField(verbose_name='稿件播放量', null=True)
    digg_count = models.TextField(verbose_name='稿件点赞量', null=True)
    comment_count = models.TextField(verbose_name='稿件评论量', null=True)
    share_count = models.TextField(verbose_name='稿件转发量', null=True)
    author_id = models.BigIntegerField(verbose_name='作者id', null=False)
    author_name = models.TextField(verbose_name='用户名称', null=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        db_table = 'tiktok_videos_info'

    def __str__(self):
        return '%s' % (self.title)
