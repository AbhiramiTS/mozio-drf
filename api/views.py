from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from .serializers import ProviderSerializer, ServiceAreaSerializer, QuerySerializer
from .models import Provider, ServiceArea


# API OVERVIEW
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Provider List':'/provider-list',
        'Provider Detail View':'/provider-detail/<str:pk>/',
        'Provider Create':'/provider-create',
        'Provider Update':'/provider-update/<str:pk>/',
        'Provider Delete':'/provider-delete/<str:pk>/',
        '*********************':'*********************',
        'Polygon List':'/polygon-list',
        'Polygon Create':'/polygon-create',
        'Polygon Update':'/polygon-update/<str:pk>/',
        'Polygon Delete':'/polygon-delete/<str:pk>/',
        '*********************':'*********************',
        'Query':'query/<float:latitude>/<float:longitude>',
    }
    return Response(api_urls)



"""
Create, Retrieve, Update and Delete Provider

"""

@api_view(['GET'])
def providerList(request):
    provider_objects = Provider.objects.all()
    serializer = ProviderSerializer(provider_objects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def providerDetail(request, pk):
    provider_object = Provider.objects.get(id=pk)
    serializer = ProviderSerializer(provider_object, many=False)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def providerCreate(request):
    serializer = ProviderSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def providerUpdate(request, pk):
    provider_object = Provider.objects.get(id=pk)
    serializer = ProviderSerializer(instance=provider_object, data=request.data)   
    if serializer.is_valid():
        serializer.save()        
    return Response(serializer.data)

@api_view(['DELETE'])
def providerDelete(request, pk):
    provider_object = Provider.objects.get(id=pk)
    provider_object.delete()       
    return Response("Item succesfully deleted !!!")



"""
Create, Retrieve, Update and Delete GeoPolygon

"""

@api_view(['GET'])
def polygonList(request):
    poly_objects = ServiceArea.objects.all()
    serializer = ServiceAreaSerializer(poly_objects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def polygonCreate(request):
    serializer = ServiceAreaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def polygonUpdate(request, pk):
    poly_object = ServiceArea.objects.get(id=pk)
    serializer = ServiceAreaSerializer(instance=poly_object, data=request.data)
    if serializer.is_valid():
        serializer.save()  
    return Response(serializer.data)

@api_view(['DELETE'])
def polygonDelete(request, pk):
    poly_object = ServiceArea.objects.get(id=pk)
    poly_object.delete()
    return Response("Item succesfully deleted !!!")



"""
Function to query the data. takes a lat/lng pair as arguments from the URL query parameters 
and returns a list of polygons that include the given lat/lng.

"""

@api_view(['GET'])
def query(request,latitude,longitude):
    polygon_list = list()
    point = Point(float(latitude), float(longitude))
    poly_objects = ServiceArea.objects.all()
    for polygons in poly_objects:
        result = eval(polygons.coordinates)
        polygon = Polygon(result)
        if polygon.contains(point):
            polygon_list.append(polygons)

    serializer = QuerySerializer(polygon_list, many=True)
    if serializer is not None:
        return Response(serializer.data)
    else:
        return Response('Error! Provider List is Empty.')
    

