from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime



class UserApiView(APIView):
    def get(self, request):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)          
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        
        user = User.objects.filter(username=username).first()
        
        if user is None or not user.check_password(password):
            raise AuthenticationFailed('Unauthenticated')
    
        
        payload = {
            'id':user.id,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')       
        response = Response(status=status.HTTP_202_ACCEPTED)       
        response.set_cookie(key= 'jwt', value=token, httponly=True)
        
        response.data = {
            'jwt':token
        }        
        return response
    
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
             raise AuthenticationFailed('Unauthenticated')
                
        try:
          payload = jwt.decode(token, 'secret', algorithms=['HS256'])
          
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated') 
        print(payload['exp'])
        print(datetime.datetime.utcnow().toordinal(), 'date time')
      
        if payload['exp'] <= datetime.datetime.utcnow():
            raise AuthenticationFailed('Token expired') 
      
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
               
        return Response(serializer.data)     


class LogoutView(APIView):
    def post(self, request):
        response = Response(status=status.HTTP_205_RESET_CONTENT)
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


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
