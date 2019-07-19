from django.urls import path
from .views import AdvertisementListView, AdvertisementDetailView

urlpatterns = [
    path('adv/<int:pk>/', AdvertisementDetailView.as_view(), name='adv_detail'),
    path('', AdvertisementListView.as_view(), name='advs'),
]
