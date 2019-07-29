from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Advertisement
from django.urls import reverse_lazy


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
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdvertisementUpdateView(UpdateView):
    model = Advertisement
    template_name = 'adv_edit.html'
    fields = ['title', 'body']


class AdvertisementDeleteView(DeleteView):
    model = Advertisement
    template_name = 'adv_delete.html'
    context_object_name = 'advertisement'
    success_url = reverse_lazy('advs')
