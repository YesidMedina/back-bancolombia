from rest_framework.serializers import ModelSerializer
from amm_im.models import AmmImModel, EmailAmmImModel, BaseLineAmmImModel


class AmmImSerializer(ModelSerializer):
    class Meta:
        model = AmmImModel
        fields = '__all__'
    
class EmailAmmImSerializer(ModelSerializer):
    class Meta:
        model = EmailAmmImModel
        fields = '__all__'

class BaseLineAmmImSerializer(ModelSerializer):
    class Meta:
        model = BaseLineAmmImModel
        fields = '__all__'
        

      