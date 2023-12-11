from django.db import models

class AmmCloudModel(models.Model):
    id_user = models.IntegerField(max_length=2)
    tool = models.CharField(max_length=100)
    global_collection = models.CharField(max_length=100)
    filial = models.CharField(max_length=100)
    modulo = models.CharField(max_length=100)
    service_manager = models.CharField(max_length=500)
    sub_service = models.CharField(max_length=500)
    name_alert_back = models.CharField(max_length=500)
    name_alert = models.CharField(max_length=200)
    type_configuration = models.CharField(max_length=200)
    item_configuration = models.CharField(max_length=200)
    value_configuration = models.CharField(max_length=200)
    condition_alert = models.CharField(max_length=100)
    frequencie = models.CharField(max_length=100)
    alert_hours = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    critical = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    impact = models.CharField(max_length=1000)
    details_query = models.CharField(max_length=1000)
    reference_document = models.CharField(max_length=200)
    type_location = models.CharField(max_length=50)
    test_location = models.CharField(max_length=50)
    spectrum = models.CharField(max_length=50)
    status = models.BooleanField()
    maintenance = models.BooleanField()
    order_number_oc = models.CharField(max_length=500)
    state_newrelic = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
  
    class Meta:
        db_table = 'amm_cloud'
        ordering = ['-created_at']
        
class EmailAmmCloudModel(models.Model):
    group_email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email_notification = models.CharField(max_length=500)
    order_oc = models.CharField(max_length=500)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

       
    class Meta:
        db_table = 'email_amm_cloud'
        ordering = ['-created_at']

class SyntheticAmmCloudModel(models.Model):
    name_alert = models.CharField(max_length=500)
    name_proposed = models.CharField(max_length=500)
    item_configuration = models.CharField(max_length=100)
    passed = models.CharField(max_length=200)
    item_configuration_nqrl = models.CharField(max_length=100)
    value_item = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    critical = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    parameter_token = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    status = models.BooleanField()
    order_oc = models.CharField(max_length=500)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

       
    class Meta:
        db_table = 'synthetic_cloud'
        ordering = ['-created_at']        
        
    