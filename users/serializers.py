from rest_framework import serializers  
from django.contrib.auth import authenticate
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password', 'email', 'first_name', 'last_name', 'is_active']
        extra_kwargs = {'password': {'write_only': True}}
        
class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if user:
           raise serializers.ValidationError('No se pudo autenticar', code='authorization')
        data['user'] = user
        return data
        
           
        
        
    