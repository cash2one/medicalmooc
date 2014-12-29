#coding:utf-8
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models


class CustomImage(models.Model):
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=200)  
    img = models.ImageField(upload_to = settings.CUSTOM_IMAGE_DIR) 
    type = models.IntegerField(choices=settings.CUSTOM_IMAGE_CLASS, db_index=True)  #类型
    order_num = models.IntegerField(default=1) #排序号
    created_time = models.DateTimeField(auto_now_add=True, db_index=True)  #创建时间
    updated_time = models.DateTimeField(auto_now_add=True, db_index=True)  #
    
    def get_image_url(self):
        if not self.img:
            return ''
        return '%s%s%s' % (settings.SITE_NAME,settings.STORE_URL, self.img)
    
    def get_edir_url(self):
        return '/syscustom/indexluobo/%s/edit/' % self.id
    def get_delete_url(self):
        return '/syscustom/indexluobo/%s/delete/' % self.id

class CourseClass(models.Model):
    code = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=30)
    order_num = models.IntegerField(default=1) #排序号
    created_time = models.DateTimeField(auto_now_add=True, db_index=True)  #创建时间
    updated_time = models.DateTimeField(auto_now_add=True, db_index=True)  #
