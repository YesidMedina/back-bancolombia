from rest_framework.serializers import ModelSerializer
from amm_im.models import AmmImModel, EmailAmmImModel


class AmmImSerializer(ModelSerializer):
    class Meta:
        model = AmmImModel
        fields = '__all__'
    
class EmailAmmImSerializer(ModelSerializer):
    class Meta:
        model = EmailAmmImModel
        fields = '__all__'
        

      