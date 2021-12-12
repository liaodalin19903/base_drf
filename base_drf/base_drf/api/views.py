#-*- coding:utf-8 -*-
# Author: jamison



from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,  # 已经证明的
    IsAdminUser, # 是管理员
    IsAuthenticatedOrReadOnly, # 已经证明的或者只读
)
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from ..models import Message
from .serializers import (
    MessageSerializer,
    MessageCreateSerializer,
)



class MessageCreatAPIView(APIView):
    serializer_class = MessageCreateSerializer
    def post(self, request):
        receive_group = request.data.get("receive_group_id", None)
        receive_user = request.data.get("receive_user_id", None)
        title = request.data.get("title", None)
        content = request.data.get("content", None)

        if receive_group is not None and receive_group != '':

            pass
            return Response(data="发送成功", status=HTTP_200_OK)

        if receive_user is not None and receive_user != '':
            pass
            return Response(data="发送成功", status=HTTP_200_OK)

class MessageAdminListAPIView(ListAPIView):
    """
    管理员罗列消息
    """
    serializer_class = MessageSerializer
    permission_classes = []
    queryset = Message.objects.all()#.distinct('message_num')
    # queryset = Message.objects.values('message_num').distinct()


class MessageRetrieveAPIView(RetrieveAPIView):
    serializer_class = MessageSerializer
    permission_classes = []
    queryset = Message.objects.all()







