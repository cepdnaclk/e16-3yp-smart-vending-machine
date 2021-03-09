from rest_framework import serializers
from store.models import Order,OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    
    # order = serializers.StringRelatedField(many=True)
    name=serializers.SerializerMethodField('getName')
    class Meta:
        model = OrderItem
        fields = ['name', 'quantity']
    def getName(self,OrderItem):
        name=OrderItem.product.name
        return name

class orderSerializer(serializers.ModelSerializer):
    customer=serializers.SerializerMethodField('get_c')
    email=serializers.SerializerMethodField('get_c1')
    amountTopay=email=serializers.SerializerMethodField('get_cart_total')
    OrderItems = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['customer','date_ordered','id','transaction_id','complete' ,'email','OrderItems','paidAmount','amountTopay','status' ]
         
    def get_c(self,Order):
        customer = Order.customer.name
        email=Order.customer.email
        return customer 
    
    def get_c1(self,Order):
         
        email=Order.customer.email
        return  email

    def get_cart_total(self,Order):
        return Order.get_cart_total

 