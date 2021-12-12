#-*- coding:utf-8 -*-
# Author:liaomalin

from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    Serializer,
)
from ..models import Message

class MessageCreateSerializer(Serializer):
    receive_group_id = serializers.IntegerField(allow_null=True)
    receive_user_id = serializers.IntegerField(allow_null=True)
    title = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=1024)

    def validate(self, data):
        if data['receive_group_id'] is None and data['receive_user_id'] is None:
            raise serializers.ValidationError(
                "收信息组或者收信息者不能全部为空，其中一个必须有值")
        return data


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

