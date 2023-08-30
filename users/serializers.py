from rest_framework.serializers import ModelSerializer
from users.models import UsersModel

class UserSerializer(ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ['id', 'username', 'password']
    