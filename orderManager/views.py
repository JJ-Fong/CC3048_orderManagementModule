# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from serializers import *
from rest_framework import status
from rest_framework import serializers
from django.utils.six import BytesIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from service import *
from django.core import serializers
import json


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@api_view(['GET', 'POST'])
def create_order(request):
    if request.method == 'POST':
        try:
            data = JSONRenderer().render(request.data)
            stream = BytesIO(data)
            order_model = JSONParser().parse(stream)
            order = HandleOrderRequest(order_model)
            #serialized_obj = serializers.serialize('json', [ transaction, ])
            #return Response(serialized_obj, status=status.HTTP_202_ACCEPTED)
        except Exception, e:
            return Response({"error":str(e)}, status=status.HTTP_200_ACCEPTED)
        return HttpResponse(order)

@csrf_exempt
@api_view(['GET', 'POST'])
def validate_order(request):
    if request.method == 'POST':
        try:
            data = JSONRenderer().render(request.data)
            stream = BytesIO(data)
            order_model = JSONParser().parse(stream)
            order = ValidateOrderRequest(order_model)
            # serialized_obj = serializers.serialize('json', [ order, ])
            # return Response(serialized_obj, status=status.HTTP_202_ACCEPTED)
        except Exception, e:
            return Response({"error":str(e)}, status=status.HTTP_200_ACCEPTED)
        # jsonobj = json.loads(order)
        # return HttpResponse(jsonobjn)
        return HttpResponse(order)

