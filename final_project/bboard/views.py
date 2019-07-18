from django.views.generic import ListView
from .models import Advertisement

class HomePageView(ListView):
    model = Advertisement
    template_name = 'advs.html'
    context_object_name = 'all_advertisement_list'
    
