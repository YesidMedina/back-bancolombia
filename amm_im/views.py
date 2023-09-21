from rest_framework import status
from collections import Counter
from rest_framework.views import APIView
from rest_framework.response import Response
from .filters import AmmFilters
from rest_framework.pagination import PageNumberPagination
from django_filters.utils import translate_validation
from amm_im.models import AmmImModel, EmailAmmImModel
from amm_im.serializers import AmmImSerializer, EmailAmmImSerializer
from rest_framework import generics
from rest_framework import filters


class AmmImRetiredApiView(generics.ListAPIView):
    queryset = AmmImModel.objects.filter(status= False).order_by('id').reverse()
    serializer_class = AmmImSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'tool', '=service_manager', '=filial', 'ip_divice', 'description', 'order_number_oc']


class AmmImApiView(generics.ListAPIView):
    queryset = AmmImModel.objects.filter(status= True).order_by('id').reverse()
    serializer_class = AmmImSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'tool', '=service_manager', '=filial', 'ip_divice', 'description', 'order_number_oc']
    
    # def get(self, request):
    #     paginator = PageNumberPagination()
    #     paginator.page_size = 30
    #     filterset = AmmFilters(request.GET,queryset=AmmImModel.objects.filter(status=request.GET.get("status") == "true"
    #         ).order_by("id"),
    #     )
    #     if request.search_fields('id'):
    #         queryset = queryset.filter(status=request.query_params.get())
    #     if not filterset.is_valid():
    #         raise translate_validation(filterset.errors)

    #     queryset = paginator.paginate_queryset(filterset.qs, request)
    #     serializer = AmmImSerializer
    #     serializer = AmmImSerializer(queryset, many=True)
    #     return paginator.get_paginated_response(serializer.data)

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
        print(request.data)
        if service == None:
            return Response(status=status.HTTP_200_OK, data={"error": "Not found data"})
        serializer = AmmImSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request):
    #     print(request.data)
    #     service = object(id)
    #     print(service)
    #     if(service==None):
    #         return Response(status=status.HTTP_200_OK, data={'error': 'Not found data'})
    #     serializer = AmmImSerializer(service, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         print(serializer.data)
    #         return Response(status=status.HTTP_200_OK, data=serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request):
    #     service = self.get_object(id)
    #     serializer = AmmImSerializer(service, data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         print(serializer.data)
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        print(request.data)
        service = list(AmmImModel.objects.filter(id=id).values())
        print(service)
        
        

    def delete(self, request, id):
        service = self.get_object(id)
        service.delete()
        response = {"deleted": False}
        return Response(status=status.HTTP_200_OK, data=response)
        
### search filter #####
   
    
class FilterEmailAmmIm(generics.ListAPIView):
    queryset = EmailAmmImModel.objects.all()
    serializer_class = EmailAmmImSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['group_email', 'name', 'order_oc', 'email_notification']
        
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
        if service == None:
            return Response(status=status.HTTP_200_OK, data={"error": "Not found data"})
        serializer = EmailAmmImSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        service = self.get_object(id)
        service.delete()
        response = {"deleted": False}
        return Response(status=status.HTTP_200_OK, data=response)
    
##### dasboard #####

class GraphicsAmmIm(APIView):
    def get(self, request):
        serializer = AmmImSerializer(
            AmmImModel.objects.filter(status=request.GET.get("status") != "true"),
            many=True,
        )
        data = serializer.data

        tool = []
        for x in data:
            tool.append(x["tool"])
            counter_tool = Counter(tool)

        maintenance = []
        for x in data:
            maintenance.append(x["maintenance"])
            counter_maintenance = Counter(maintenance)

        return Response(
            status=status.HTTP_200_OK, data=[counter_tool + counter_maintenance])

class GraphicsAmmImFull(APIView):
    def get(self, request):
        serializer = AmmImSerializer(AmmImModel.objects.all(), many=True)
        data = serializer.data
        total = []
        for x in data:
            total.append(x["status"])
            total_status = Counter(total)
        return Response(status=status.HTTP_200_OK, data=[total_status])
    
    
####import Export excel####
    
# import pandas as pd   
# from django.conf import settings
# import uuid
# import os
    
# class ExportIMportExcel(APIView):
    
#     def get(self, request):
#         outname = 'excel.xlsx'
#         outdir = './Escritorio'
#         if not os.path.exists(outdir):  
#          os.mkdir(outdir)
#         amm_im_objs = AmmImModel.objects.all()
#         serializer = AmmImSerializer(amm_im_objs, many=True)
#         df = pd.DataFrame(serializer.data)
#         full_name = os.path.join(outdir, outname)
#         # df.to_csv(f'/.dir/{uuid.uuid4()}.csv', encoding='UTF-8')
#         df.to_excel(full_name)
#         return Response(status=status.HTTP_200_OK)
                
