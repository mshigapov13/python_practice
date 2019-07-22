from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Advertisement


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'advs.html'
    context_object_name = 'all_advertisement_list'


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'adv_detail.html'
    context_object_name = 'advertisement'


class AdvertisementCreateView(CreateView):
    model = Advertisement
    template_name = 'adv_new.html'
    fields = ['title', 'author', 'body']


class AdvertisementUpdateView(UpdateView):
    model = Advertisement
    template_name = 'adv_edit.html'
    fields = ['title', 'body']
