# from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS'])

def home(request):
    if request.method == 'GET':
        return Response({
        'status': 200,
        'message': 'yes the framework is in working now... congress :)!!!!!!!!',
        'method': 'You call GET method'
    })

    elif request.method == 'POST':
        return Response({
        'status': 200,
        'message': 'The rest framework is working',
        'method': 'You are on POST method'
    })

    elif request.method == 'PUT':
        return Response({
        'status': 200,
        'message': 'The rest framework is working',
        'method': 'You called PUT method'
    })
    else:
        return Response({
        'status': 400,
        'message': 'The rest framework is working but it gives error',
        'method': 'You called invalid method'
    })
