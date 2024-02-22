from django.shortcuts import render
from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# from .forms import BookingForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
import json
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def menu(request):
    menu_items  = Menu.objects.all()
    return render(request=request, template_name= 'menu.html',context= {'menu': menu_items})

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return HttpResponse({"message":"This view is protected"})

# Menu -> GET & POST 
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

# Single Menu Item For Retrieving, Update or Delete   
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    # The queryset attribute is not filtered, but the
    # DRF automatically filters it based on the pk 
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    # By using ModelViewSet, you inherit default implementations for actions
    # like listing, creating, retrieving, updating, and deleting objects for your Booking model
    # without having to write repetitive code for each action
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer            
