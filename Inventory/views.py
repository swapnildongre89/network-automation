from django.shortcuts import render
from .models import Routers, Switches, Firewalls, Loadbalancers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InventorySerializer
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def display_routers(request):
    item= Routers.objects.all()

    context= { "items": item, "header": 'Routers list' }

    return render(request, "index.html", context)

def display_switches(request):
    item= Switches.objects.all()

    context= { "items": item, "header": 'Switches list' }

    return render(request, "index.html", context)

def display_firewalls(request):
    item= Firewalls.objects.all()

    context= { "items": item, "header": 'Firewalls list' }

    return render(request, "index.html", context)

def display_loadbalancers(request):
    item= Loadbalancers.objects.all()

    context= { "items": item, "header": 'Loadbalancers list' }

    return render(request, "index.html", context)


######################################################

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InventorySerializer
from django.http import HttpResponse, JsonResponse

@api_view(['GET'])
def Router_list(request):
    if request.method == 'GET':
        router= Routers.objects.all()
        serializer = InventorySerializer(router, many=True)
        return Response(serializer.data) 

@api_view(['GET'])
def Switch_list(request):
    if request.method == 'GET':
        switch= Switches.objects.all()
        serializer = InventorySerializer(switch, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def Firewall_list(request):
    if request.method == 'GET':
        firewall= Firewalls.objects.all()
        serializer = InventorySerializer(firewall, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def Loadbalancer_list(request):
    if request.method == 'GET':
        loadbalancer= Loadbalancers.objects.all()
        serializer = InventorySerializer(loadbalancer, many=True)
        return Response(serializer.data)


######################################################

# import napalm

# driver = napalm.get_network_driver("ios")

# device = driver(
#         hostname="192.168.0.70",
#         username="sid",
#         password="cisco",
#     )

# device.open()
# print(device.get_interfaces())

# node= device.get_interfaces()['Ethernet0/0']
# device.close()


##################################################################

def device_interfaces(request):
    return HttpResponse("interface page")