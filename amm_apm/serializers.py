from rest_framework.serializers import ModelSerializer
from amm_apm.models import AmmApmModel, EmailAmmApmModel


class AmmApmSerializer(ModelSerializer):
    class Meta:
        model = AmmApmModel
        fields = '__all__'
    
class EmailAmmApmSerializer(ModelSerializer):
    class Meta:
        model = EmailAmmApmModel
        fields = '__all__'
   