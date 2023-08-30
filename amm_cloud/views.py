from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from amm_cloud.models import AmmCloudModel, EmailAmmCloudModel
from amm_cloud.serializers import AmmCloudSerializer, EmailAmmCloudSerializer

class AmmCloudApiView(APIView):
    def get(self, request):
        serializer = AmmCloudSerializer(AmmCloudModel.objects.all(), many=True)    
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        
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
        service = self.get_object(id)
        if(service==None):
            return Response(status=status.HTTP_200_OK, data={'error': 'Not found data'})
        serializer = AmmCloudSerializer(service, data=request.data)
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
          
class EmailAmmCloudApiView(APIView):
    def get(self, request):
        serializer = EmailAmmCloudSerializer(EmailAmmCloudModel.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
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
        if(service==None):
            return Response(status=status.HTTP_200_OK, data={'error': 'Not found data'})
        serializer = EmailAmmCloudSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    def delete(self, request, id):
        service = self.get_object(id)
        service.delete()
        response = {'deleted': False}
        return Response(status=status.HTTP_200_OK, data=response)
    
 
    
           