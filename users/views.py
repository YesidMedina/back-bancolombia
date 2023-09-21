from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics, authentication, permissions
import openai
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer, AuthTokenSerializer


class UserApiView(APIView):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)           
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class AuthenticateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    pagination_class = None
    authentication_classes = [authentication.TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    
class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
        


class UserApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, id):
        user = self.get_object(id)
        if user == None:
            return Response(status=status.HTTP_200_OK, data={"error": "Not found data"})
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = self.get_object(id)
        user.delete()
        response = {"deleted": False}
        return Response(status=status.HTTP_200_OK, data=response)


# openai.api_key = "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"

# class OpenAiMonitoring(APIView):
#     def post(self, request):
#         prompt = request.data
#         prompt.is_valid(raise_exception=True)
#         prompt.save()
#         return Response(status=status.HTTP_200_OK, data=prompt.data)

#     def get(self, request):
#         cuestions = 'Plataformas de monitoreo'
#         chat_history = []
#         while True:
#             prompt = prompt
#             if prompt == 'exit':
#                 break
#             else:
#                 chat_history.append({'role': 'user', 'content': prompt})
#                 response = openai.ChatCompletion.create(
#                     model = "gpt-3.5-turbo",
#                     messages = chat_history,
#                     stream=True,

#                 )
#                 collected_messages = []

#                 for chunk in response:
#                     chunk_message = chunk['choices'][0]['delta']
#                     collected_messages.append(chunk_message)
#                     full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
#                     print(full_reply_content, "\033[H\033[J", end="")
#                    # print("\033[H\033[J", end="")


#                 chat_history.append({'role': 'assistant', 'content': (full_reply_content, "\033[H\033[J")})
#                 return Response(status=status.HTTP_200_OK, data=(prompt, full_reply_content))
