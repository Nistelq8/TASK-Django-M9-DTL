from django.shortcuts import render
from .models import IceCream

# Create your views here.
def get_ice_cream(request,ice_cream_id):
    ice_cream = IceCream.objects.get(id=ice_cream_id)
    context = { 
        "ice_cream":{
            'ice cream name': ice_cream.name,
            'ice cream shop': ice_cream.shop,
            'ice cream stock': ice_cream.stock,}
    }
    return render(request, 'ice_cream_details.html', context)   