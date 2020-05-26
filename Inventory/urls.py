from django.conf.urls import url
from django.urls import path
from .views import index, display_routers, display_switches, display_firewalls, display_loadbalancers, Router_list, Switch_list, Firewall_list, Loadbalancer_list, device_interfaces

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^display_routers$", display_routers, name="display_routers"),
    url(r"^display_switches$", display_switches, name="display_switches"),
    url(r"^display_firewalls$", display_firewalls, name="display_firewalls"),
    url(r"^display_loadbalancers$", display_loadbalancers, name="display_loadbalancers"),
    path("router_list/", Router_list, name="Router_list"),
    path("switch_list/", Switch_list, name="Switch_list"),
    path("firewall_list/", Firewall_list, name="Firewall_list"),
    path("loadbalancer_list/", Loadbalancer_list, name="Loadbalancer_list"),
    path("device_interfaces/", device_interfaces, name="device_interfaces"),
]