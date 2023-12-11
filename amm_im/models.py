from django.db import models

class AmmImModel(models.Model):
    id_user = models.IntegerField(max_length=2)
    tool = models.CharField(max_length=50)
    global_collection = models.CharField(max_length=200)
    filial = models.CharField(max_length=200)
    service_manager = models.CharField(max_length=500)
    sub_service = models.CharField(max_length=500)
    service_optional = models.CharField(max_length=500)
    monitor_resource = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    environment = models.CharField(max_length=50)
    platform = models.CharField(max_length=200)
    rol = models.CharField(max_length=200)
    name_device = models.CharField(max_length=200)
    ip_divice = models.CharField(max_length=200)
    baseline = models.CharField(max_length=200)
    item_configuration = models.CharField(max_length=200)
    ic_configuration = models.CharField(max_length=200)
    alert_generation = models.CharField(max_length=200)
    intervalo = models.CharField(max_length=200)
    action = models.CharField(max_length=200)
    alert_hours = models.CharField(max_length=200)
    major = models.CharField(max_length=100)
    critical = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    impact = models.CharField(max_length=1000)
    special_rule = models.CharField(max_length=200)
    details = models.CharField(max_length=1000)
    spectrum_soi = models.CharField(max_length=50)
    status = models.BooleanField()
    maintenance = models.BooleanField()
    order_number_oc = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

       
    class Meta:
        db_table = 'amm_im'
        ordering = ['-created_at']
        
class EmailAmmImModel(models.Model):
    group_email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email_notification = models.CharField(max_length=500)
    order_oc = models.CharField(max_length=500)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

       
    class Meta:
        db_table = 'email_amm_im'
        ordering = ['-created_at']
        
        
# class Excel_file_upload(models.Model):
#     excel_file_upload = models.FileField(upload_to='excel') 


class BaseLineAmmImModel(models.Model):
    name_baseline = models.CharField(max_length=100)
    type_configuration = models.CharField(max_length=100)
    item_configuration = models.CharField(max_length=500)
    major = models.CharField(max_length=50)  
    critical = models.CharField(max_length=50) 
    group_support = models.CharField(max_length=100)  
    impact = models.CharField(max_length=1000)  
    details = models.CharField(max_length=500)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

       
    class Meta:
        db_table = 'baseline_amm_im'
        ordering = ['-created_at']    
    
      
        
        
        
            
        
