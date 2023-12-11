from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from amm_cloud.models import AmmCloudModel, EmailAmmCloudModel, SyntheticAmmCloudModel
from amm_cloud.serializers import AmmCloudSerializer, EmailAmmCloudSerializer, SyntheticAmmCloudSerializer
from rest_framework import generics
from rest_framework import filters
from collections import Counter


class AmmCloudRetiredApiView(generics.ListAPIView):
    queryset = AmmCloudModel.objects.filter(status= False).order_by('id').reverse()
    serializer_class = AmmCloudSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'tool', '=service_manager', '=filial', 'order_number_oc']

class AmmCloudApiView(generics.ListAPIView):
    queryset = AmmCloudModel.objects.filter(status= True).order_by('id').reverse()
    serializer_class = AmmCloudSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'tool', '=service_manager', '=filial', 'order_number_oc']


    def post(self, request):
            serializer = AmmCloudSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)    

class AmmCloudApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return AmmCloudModel.objects.get(pk=pk)
        except AmmCloudModel.DoesNotExist:
            return None

    def get(self, request, id):
        service = self.get_object(id)
        serializer = AmmCloudSerializer(service)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        print(request)
        service = self.get_object(id)
        if service == None:
            return Response(status=status.HTTP_200_OK, data={"error": "Not found data"})
        serializer = AmmCloudSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Models Email
class EmailAmmCloudGetApiView(generics.ListAPIView):
    queryset = EmailAmmCloudModel.objects.all().order_by('id').reverse()
    serializer_class = EmailAmmCloudSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['group_email', 'name', 'order_oc', 'email_notification']

class EmailAmmCloudApiView(APIView):

    def post(self, request):
        serializer = EmailAmmCloudSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

class EmailAmmCloudApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return EmailAmmCloudModel.objects.get(pk=pk)
        except EmailAmmCloudModel.DoesNotExist:
            return None

    def get(self, request, id):
        service = self.get_object(id)
        serializer = EmailAmmCloudSerializer(service)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        service = self.get_object(id)
        if service == None:
            return Response(status=status.HTTP_200_OK, data={"error": "Not found data"})
        serializer = EmailAmmCloudSerializer(service, data=request.data)
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

class GraphicsAmmCloud(APIView):
    def get(self, request):
        serializer = AmmCloudSerializer(
            AmmCloudModel.objects.filter(status=request.GET.get("status") != "true"),
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

class GraphicsAmmCloudFull(APIView):
    def get(self, request):
        serializer = AmmCloudSerializer(AmmCloudModel.objects.all(), many=True)
        data = serializer.data
        total = []
        for x in data:
            total.append(x["status"])
            total_status = Counter(total)
        return Response(status=status.HTTP_200_OK, data=[total_status])
    
class GraphicsFilialAmmCloud(APIView):
    def get(self, request):
        serializer = AmmCloudSerializer(
            AmmCloudModel.objects.filter(status=request.GET.get("status") != "true"),
            many=True,
        )
        data = serializer.data
        total = []
        for x in data:
            total.append(x["filial"])
            total_filial = Counter(total)  
        return Response(status=status.HTTP_200_OK, data=[total_filial])    
    
class GraphicsSyntheticAmmCloud(APIView):
    def get(self, request):
        serializer = SyntheticAmmCloudSerializer(
            SyntheticAmmCloudModel.objects.all(),
            many=True,
        )
        data = serializer.data
        total = []
        for x in data:
            total.append(x["status"])
            total_job = Counter(total) 
            print(total_job)  
        return Response(status=status.HTTP_200_OK, data=[total_job])    
                

###JObs###


class SyntheticRetiredApiView(generics.ListAPIView):
    queryset = SyntheticAmmCloudModel.objects.filter(status= False).order_by('id').reverse()
    serializer_class = SyntheticAmmCloudSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'job','id_divice', 'name_menu','order_oc']

class SyntheticApiView(generics.ListAPIView):
    queryset = SyntheticAmmCloudModel.objects.filter(status= True).order_by('id').reverse()
    serializer_class = SyntheticAmmCloudSerializer
    pagination_class = PageNumberPagination
    pagination_class.page_size = 20
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'job', 'name_menu','id_divice','order_oc']


    def post(self, request):
            serializer = SyntheticAmmCloudSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)   

class SyntheticApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return SyntheticAmmCloudModel.objects.get(pk=pk)
        except SyntheticAmmCloudModel.DoesNotExist:
            return None

    def get(self, request, id):
        service = self.get_object(id)
        serializer = SyntheticAmmCloudSerializer(service)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        print(request)
        service = self.get_object(id)
        if service == None:
            return Response(status=status.HTTP_200_OK, data={"error": "Not found data"})
        serializer = SyntheticAmmCloudSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)