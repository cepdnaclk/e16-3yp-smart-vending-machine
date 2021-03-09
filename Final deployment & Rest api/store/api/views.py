from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Order,OrderItem
from store.api.serializers import orderSerializer,OrderItemSerializer
from account.decorators import unauthenticated_user, allowed_users, admin_only



@api_view(['GET', 'POST'])
@allowed_users(allowed_roles=['admin'])
def order_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = orderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = orderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@allowed_users(allowed_roles=['admin'])
def order_detail(request, pk):
    """
    Retrieve, update order
    """
    try:
        orders = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = orderSerializer(orders)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = orderSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     