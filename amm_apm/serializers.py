from rest_framework.serializers import ModelSerializer
from amm_apm.models import AmmApmModel, EmailAmmApmModel, JobAmmApmModel


class AmmApmSerializer(ModelSerializer):
    class Meta:
        model = AmmApmModel
        fields = '__all__'
    
class EmailAmmApmSerializer(ModelSerializer):
    class Meta:
        model = EmailAmmApmModel
        fields = '__all__'
   

class JobAmmApmSerializer(ModelSerializer):
    class Meta:
        model = JobAmmApmModel
        fields = '__all__'
      