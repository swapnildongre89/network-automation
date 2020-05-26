from rest_framework import serializers
from Inventory.models import Routers, Switches, Firewalls, Loadbalancers

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Routers

        fields= ('hostname', 'ipadd', 'datacenter')