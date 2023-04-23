from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TodoSerializer
from .models import TodoModel

# Create your views here.
@api_view(["get"])
def greetings(request):
    return Response({"message":"Hello World"})

@api_view(["post"])
def addTodo(request):
    try:
        data = request.data
        serialized_data = TodoSerializer(data=data)
        if(serialized_data.is_valid()):
            serialized_data.save()
            return Response({
                "status":True,
                "data":serialized_data.data
            })
    except Exception as e:
        return Response({
                "status":False,
                "msg":"Some Error Occured"
            })

@api_view(['get'])  
def getTodos(request):
    try:
            todos=TodoModel.objects.all()
            serialized_data=TodoSerializer(todos,many=True)
            return Response(
                {
                    "success":True,
                    "data":serialized_data.data
                }
            )
        
    except Exception as e:
        return Response({
                "status":False,
                "msg":"Some Error Occured"
            })
    

@api_view(["patch"])
def updateTodo(request):
    try:
        data = request.data
        if not data.get("id"):
            return Response({
            "status":False,
            "message":"UID required"
        })
        else:
            obj=TodoModel.objects.get(id = data.get("id"))
            serializer = TodoSerializer(obj,data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status":True,
                    "message":"Updated",
                    "data":serializer.data
                })


    except Exception as e:
        print(e)
        return Response({
            "status":False,
            "message":"Error"
        })



@api_view(["delete"])
def deleteTodo(request):
    data = request.data
    if not data.get("id"):
        return Response({
        "status":False,
        "message":"UID required"
    })
    todo = TodoModel.objects.get(id=data.get("id"))
    todo.delete()
    return Response({
        "status":True,
        "message":"Todo is deleted"
    })