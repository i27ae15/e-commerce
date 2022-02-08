from django.shortcuts import render
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, Cart
from .serializers import CartSerializer, OrderSerializer, MyOrderSerializer, ItemCartSerializer

def home(request):

    if request.user.is_authenticated:

        if not len(Cart.objects.filter(user=request.user)):
            Cart.objects.create(user=request.user)


    return render(request, 'home.html', {'section': 'home'})


def shoes(request):
    query = None
    section = 'shoes'

    if request.method == 'POST':
        query = request.POST.get('query')
        section = 'search'

    return render(request, 'shoes.html', {'section': section, 'query':query})


def product_detail(request, product_name):
    return render(request, 'product-detail.html', {'section': 'product_detail', 'product_name': product_name})


def cart(request):
    return render(request, 'cart.html', {})


def sign_up(request):
    return render(request, 'sign-up.html', {})


def log_in(request):
    return render(request, 'login.html', {})


@api_view(['POST'])

def add_to_cart(request):
    data = request.data.copy()

    del data['csrfmiddlewaretoken']
    serializer = ItemCartSerializer(data=data)

    if serializer.is_valid():
        cart = Cart.objects.filter(user=request.user)[0]

        try:
            serializer.save(cart=cart)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GetCartItems(APIView):
    def get(sefl, request, format=None):
        cart = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart, many=True)

        return Response(serializer.data[0]['cart_items'])


@api_view(['POST'])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        paid_amount = sum(item.get('quantity') * item.get('product').price for item in serializer.validated_data['items'])

        try:
            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)