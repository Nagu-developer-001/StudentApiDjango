from django.shortcuts import render
from .serializer import StudentSerializer
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from .models import StudentDetails
# Create your views here.
@api_view(['GET','POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def getDetails(request):
	if request.method == 'GET':
		st_data = StudentDetails.objects.all()
		serialized_data = StudentSerializer(st_data,many=True)
		return JsonResponse({'details':serialized_data.data},safe=False)
	if request.method == 'POST':
		serialized_data = StudentSerializer(data=request.data)
		if serialized_data.is_valid():
			serialized_data.save();
			return Response(serialized_data.data,status=status.HTTP_201_CREATED)
		else:
			return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE'])
@authentication_classes([])  
@permission_classes([AllowAny])
def getData(request,id):
	try:
		st_data = StudentDetails.objects.get(pk=id)
	except StudentDetails.DoesNotExist:
			return Response(status=status.HTTP_400_BAD_REQUEST)
	if request.method == 'GET':
		serialized_data = StudentSerializer(st_data)
		return Response(serialized_data.data)
	if request.method == 'DELETE':
		st_data.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(["GET"])
@authentication_classes([])
@permission_classes([AllowAny])
def getPublicApi(request,id):
	data = requests.get(f"https://fruityvice.com/api/fruit/{id}")
	data = data.json()
	return JsonResponse(data, safe=False)
@api_view(['PUT','PATCH'])
@authentication_classes([])  
@permission_classes([AllowAny])
def updateStudent(request,id):
	try:
		st_data = StudentDetails.objects.get(pk=id)
	except StudentDetails.DoesNotExist:
		return Response(status=status.HTTP_400_BAD_REQUEST)
	if request.method == 'PUT':
		serialized_data = StudentSerializer(st_data,data=request.data)
	if request.method == 'PATCH':
		serialized_data = StudentSerializer(st_data,data=request.data,partial=True)
	if serialized_data.is_valid():
		serialized_data.save();
		return Response(serialized_data.data,status=status.HTTP_200_OK)
	else:
		return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)