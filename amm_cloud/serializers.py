from rest_framework.serializers import ModelSerializer
from amm_cloud.models import AmmCloudModel, EmailAmmCloudModel, SyntheticAmmCloudModel


class AmmCloudSerializer(ModelSerializer):
    class Meta:
        model = AmmCloudModel
        fields = '__all__'
    
class EmailAmmCloudSerializer(ModelSerializer):
    class Meta:
        model = EmailAmmCloudModel
        fields = '__all__'

class SyntheticAmmCloudSerializer(ModelSerializer):
    class Meta:
        model = SyntheticAmmCloudModel
        fields = '__all__'        
   