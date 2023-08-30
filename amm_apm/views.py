from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from amm_apm.models import AmmApmModel, EmailAmmApmModel
from amm_apm.serializers import AmmApmSerializer, EmailAmmApmSerializer

class AmmApmApiView(APIView):
    def get(self, request):
        serializer = AmmApmSerializer(AmmApmModel.objects.all(), many=True)    
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        
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
        service = self.get_object(id)
        if(service==None):
            return Response(status=status.HTTP_200_OK, data={'error': 'Not found data'})
        serializer = AmmApmSerializer(service, data=request.data)
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
          
class EmailAmmApmApiView(APIView):
    def get(self, request):
        serializer = EmailAmmApmSerializer(EmailAmmApmModel.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
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
        if(service==None):
            return Response(status=status.HTTP_200_OK, data={'error': 'Not found data'})
        serializer = EmailAmmApmSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    def delete(self, request, id):
        service = self.get_object(id)
        service.delete()
        response = {'deleted': False}
        return Response(status=status.HTTP_200_OK, data=response)
    
 