from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from amm_apm.models import AmmApmModel, EmailAmmApmModel, JobAmmApmModel
from amm_apm.serializers import AmmApmSerializer, EmailAmmApmSerializer, JobAmmApmSerializer
from rest_framework import generics
from rest_framework import filters
from collections import Counter


class AmmApmRetiredApiView(generics.ListAPIView):
    queryset = AmmApmModel.objects.filter(status= False).order_by('id').reverse()
    serializer_class = AmmApmSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'gestor_broker', '=service_manager', '=filial', 'ip_divice', 'description', 'order_number_oc']

class AmmApmApiView(generics.ListAPIView):
    queryset = AmmApmModel.objects.filter(status= True).order_by('id').reverse()
    serializer_class = AmmApmSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'gestor_broker', '=service_manager', '=filial', 'ip_divice', 'description', 'order_number_oc']


    def post(self, request):
            serializer = AmmApmSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)    

class AmmApmApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return AmmApmModel.objects.get(pk=pk)
        except AmmApmModel.DoesNotExist:
            return None

    def get(self, request, id):
        service = self.get_object(id)
        serializer = AmmApmSerializer(service)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        print(request)
        service = self.get_object(id)
        if service == None:
            return Response(status=status.HTTP_200_OK, data={"error": "Not found data"})
        serializer = AmmApmSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Models Email
class EmailAmmApmGetApiView(generics.ListAPIView):
    queryset = EmailAmmApmModel.objects.all().order_by('id').reverse()
    serializer_class = EmailAmmApmSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['group_email', 'name', 'order_oc', 'email_notification']

class EmailAmmApmApiView(APIView):

    def post(self, request):
        serializer = EmailAmmApmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class EmailAmmApmApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return EmailAmmApmModel.objects.get(pk=pk)
        except EmailAmmApmModel.DoesNotExist:
            return None

    def get(self, request, id):
        service = self.get_object(id)
        serializer = EmailAmmApmSerializer(service)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        service = self.get_object(id)
        if service == None:
            return Response(status=status.HTTP_200_OK, data={"error": "Not found data"})
        serializer = EmailAmmApmSerializer(service, data=request.data)
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

class GraphicsAmmApm(APIView):
    def get(self, request):
        serializer = AmmApmSerializer(
            AmmApmModel.objects.filter(status=request.GET.get("status") != "true"),
            many=True,
        )
        data = serializer.data

        type = []
        for x in data:
            type.append(x["type_configuration"])
            counter_type = Counter(type)

        maintenance = []
        for x in data:
            maintenance.append(x["maintenance"])
            counter_maintenance = Counter(maintenance)

        return Response(
            status=status.HTTP_200_OK, data=[counter_type + counter_maintenance])

class GraphicsAmmApmFull(APIView):
    def get(self, request):
        serializer = AmmApmSerializer(AmmApmModel.objects.all(), many=True)
        data = serializer.data
        total = []
        for x in data:
            total.append(x["status"])
            total_status = Counter(total)
        return Response(status=status.HTTP_200_OK, data=[total_status])
    
class GraphicsFilialAmmApm(APIView):
    def get(self, request):
        serializer = AmmApmSerializer(
            AmmApmModel.objects.filter(status=request.GET.get("status") != "true"),
            many=True,
        )
        data = serializer.data
        total = []
        for x in data:
            total.append(x["filial"])
            total_filial = Counter(total)  
        return Response(status=status.HTTP_200_OK, data=[total_filial])    
    
class GraphicsJobAmmApm(APIView):
    def get(self, request):
        serializer = JobAmmApmSerializer(
            JobAmmApmModel.objects.all(),
            many=True,
        )
        data = serializer.data
        total = []
        for x in data:
            total.append(x["status"])
            total_job = Counter(total) 
            print(total_job)  
        return Response(status=status.HTTP_200_OK, data=[total_job])    
        
    
    
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
                

###JObs###


class JobAmmApmRetiredApiView(generics.ListAPIView):
    queryset = JobAmmApmModel.objects.filter(status= False).order_by('id').reverse()
    serializer_class = JobAmmApmSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'job','id_divice', 'name_menu','order_oc']

class JobAmmApmApiView(generics.ListAPIView):
    queryset = JobAmmApmModel.objects.filter(status= True).order_by('id').reverse()
    serializer_class = JobAmmApmSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'job', 'name_menu','id_divice','order_oc']


    def post(self, request):
            serializer = JobAmmApmSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)   

class JobApmApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return JobAmmApmModel.objects.get(pk=pk)
        except JobAmmApmModel.DoesNotExist:
            return None

    def get(self, request, id):
        service = self.get_object(id)
        serializer = JobAmmApmSerializer(service)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        print(request)
        service = self.get_object(id)
        if service == None:
            return Response(status=status.HTTP_200_OK, data={"error": "Not found data"})
        serializer = JobAmmApmSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)