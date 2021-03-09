
import django_filters
from django_filters import DateFilter, CharFilter

from store.models import *

class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_ordered", lookup_expr='gte')
	end_date = DateFilter(field_name="date_ordered", lookup_expr='lte')
	# note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer', 'date_ordered' ,'transaction_id']


class ProductFilter(django_filters.FilterSet):
	# start_price = DateFilter(field_name="price", lookup_expr='gte')
	# end_available = DateFilter(field_name="available", lookup_expr='lte')
	note = CharFilter(field_name='name', lookup_expr='icontains')


	class Meta:
		model = Product
		fields = '__all__'
		exclude = ['image', 'digital' , 'name']