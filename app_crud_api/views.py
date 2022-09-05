from platform import python_build
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializers(stu  , many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')


    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializers(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Created Successfully....!!!!!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type='application/json')
