from django.db import models

class AmmApmModel(models.Model):
    id_user = models.IntegerField(max_length=2, blank=True)
    global_collection = models.CharField(max_length=50, blank=True)
    filial = models.CharField(max_length=50, blank=True)
    service_manager = models.CharField(max_length=200, blank=True)
    sub_service = models.CharField(max_length=200, blank=True)
    gestor_broker = models.CharField(max_length=200, blank=True)
    monitor_resource = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    environment = models.CharField(max_length=50, blank=True)
    rol = models.CharField(max_length=50, blank=True)
    name_device = models.CharField(max_length=50, blank=True)
    ip_divice = models.CharField(max_length=50, blank=True)
    type_confiduration = models.CharField(max_length=50, blank=True)
    alert_generation = models.CharField(max_length=200, blank=True)
    status_alert = models.CharField(max_length=200, blank=True)
    metric_configuration = models.CharField(max_length=200, blank=True)
    intervalo = models.CharField(max_length=200, blank=True)
    alert_hours = models.CharField(max_length=100, blank=True)
    major = models.CharField(max_length=100, blank=True)
    pot_major = models.CharField(max_length=100, blank=True)
    op_major = models.CharField(max_length=100, blank=True)
    critical = models.CharField(max_length=100, blank=True)
    pot_critical = models.CharField(max_length=100, blank=True)
    op_critical = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    impact = models.CharField(max_length=500, blank=True)
    special_rule = models.CharField(max_length=200, blank=True)
    details = models.CharField(max_length=500, blank=True)
    spectrum = models.CharField(max_length=50, blank=True)
    status = models.BooleanField()
    order_number_oc = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

       
    class Meta:
        db_table = 'amm_apm'
        ordering = ['-created_at']
        
class EmailAmmApmModel(models.Model):
    group_email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email_notification = models.CharField(max_length=500)
    order_oc = models.CharField(max_length=500)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

       
    class Meta:
        db_table = 'email_amm_apm'
        ordering = ['-created_at']
