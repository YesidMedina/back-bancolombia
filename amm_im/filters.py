from amm_im.models import AmmImModel, EmailAmmImModel
import django_filters


class AmmFilters(django_filters.FilterSet):
    class Meta:
        model = AmmImModel 
        fields = ['service_manager']