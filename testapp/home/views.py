# from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
from .serializer import Todo


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

@api_view(['GET'])
def get_todo(request):
    todo_obj = Todo.objects.all()
    serializer = TodoSerializer(todo_obj, many= True)
    return Response({
        'status': True,
        'message': 'Todo list is fatched',
        'data': serializer.data
    })





@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'successfully created Todo',
                'data': serializer.data
                
            })
        
        return Response({
        'status': False,
        'message': 'somethng wrong',
        'data': serializer.errors
    })

        


           

    except Exception as e:
        print (e)

    return Response({
        'status': False,
        'message': 'something wrong',
    })    

