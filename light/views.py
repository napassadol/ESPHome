from rest_framework import viewsets
from django.http import HttpResponse
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response

import json

class HttpUtil(object):
    def getRequestData(self,request):
        is_chunked=request.META.get("HTTP_TRANSFER_ENCODING")
        if(is_chunked=="chunked"):
            input_data_tmp=request.stream.read().decode("utf-8")
            input_data=json.loads(input_data_tmp)
        else:
            input_data=request.data
        return input_data

class test_view(APIView):   
    def post(self, request):
        httpUtil = HttpUtil()
        request_data = httpUtil.getRequestData(request)
        return Response(request_data)
