from rest_framework import status
import random
from collections import Counter
from rest_framework.views import APIView
from rest_framework.response import Response
from .filters import AmmFilters
from rest_framework.pagination import PageNumberPagination
from django_filters.utils import translate_validation
from amm_im.models import AmmImModel, EmailAmmImModel
from amm_im.serializers import AmmImSerializer, EmailAmmImSerializer



class AmmImApiView(APIView):

    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 1000
        filterset = AmmFilters(request.GET, queryset=AmmImModel.objects.filter(status=request.GET.get('status') == 'true').order_by('id'))
        if not filterset.is_valid():
            raise translate_validation(filterset.errors)

        queryset = paginator.paginate_queryset(filterset.qs, request)
        serializer = AmmImSerializer(queryset, many=True)
        return paginator.get_paginated_response(serializer.data)



    def post(self, request):
        serializer = AmmImSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class AmmImApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return AmmImModel.objects.get(pk=pk)
        except AmmImModel.DoesNotExist:
            return None
    def get(self, request, id):
        service = self.get_object(id)
        serializer = AmmImSerializer(service)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def patch(self, request, id):
        service = self.get_object(id)
        if(service==None):
            return Response(status=status.HTTP_200_OK, data={'error': 'Not found data'})
        serializer = AmmImSerializer(service, data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        print(request.data)      
        service = self.get_object(id)
        if(service==None):
            return Response(status=status.HTTP_200_OK, data={'error': 'Not found data'})
        serializer = AmmImSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        service = self.get_object(id)
        service.delete()
        response = {'deleted': False}
        return Response(status=status.HTTP_200_OK, data=response)



# Models Email

class EmailAmmImApiView(APIView):
    def get(self, request):
        serializer = EmailAmmImSerializer(EmailAmmImModel.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def post(self, request):
        serializer = EmailAmmImSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class EmailAmmImApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return EmailAmmImModel.objects.get(pk=pk)
        except EmailAmmImModel.DoesNotExist:
            return None
    def get(self, request, id):
        service = self.get_object(id)
        serializer = EmailAmmImSerializer(service)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def put(self, request, id):
        service = self.get_object(id)
        if(service==None):
            return Response(status=status.HTTP_200_OK, data={'error': 'Not found data'})
        serializer = EmailAmmImSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        service = self.get_object(id)
        service.delete()
        response = {'deleted': False}
        return Response(status=status.HTTP_200_OK, data=response)

class GraphicsAmmIm(APIView):
    def get(self, request):      
        serializer = AmmImSerializer(AmmImModel.objects.filter(status=request.GET.get('status') != 'true'), many=True)
        data = serializer.data
       
        lista = []
        for x in data:
            lista.append(x['tool'] )
            contador = Counter(lista)
            
        return Response(status=status.HTTP_200_OK, data=[contador])
    
    









