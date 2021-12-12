#-*- coding:utf-8 -*-
# Author: jamison

from django.conf.urls import url
from .views import (
    MessageCreatAPIView,
    MessageAdminListAPIView,
)

urlpatterns = [
    # APIs

    # * 消息 *
    # 创建消息
    url(r'^message/create/$', MessageCreatAPIView.as_view(), name='message-create'),
    #
    url(r'^message/adminlist/$', MessageAdminListAPIView.as_view(), name='message-list'),


]