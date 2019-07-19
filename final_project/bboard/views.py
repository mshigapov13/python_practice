from django.views.generic import ListView, DetailView
from .models import Advertisement


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advs.html'
    context_object_name = 'all_advertisement_list'


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'adv_detail.html'
