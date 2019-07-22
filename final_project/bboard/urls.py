from django.urls import path
from .views import (
    AdvertisementListView,
    AdvertisementDetailView,
    AdvertisementCreateView,
    AdvertisementUpdateView,
    AdvertisementDeleteView,
)

urlpatterns = [
    path('adv/<int:pk>/delete/', AdvertisementDeleteView.as_view(), name='adv_delete'),
    path('adv/<int:pk>/edit/', AdvertisementUpdateView.as_view(), name='adv_edit'),
    path('adv/<int:pk>/', AdvertisementDetailView.as_view(), name='adv_detail'),
    path('adv/new/', AdvertisementCreateView.as_view(), name='adv_new'),
    path('', AdvertisementListView.as_view(), name='advs'),
    
]
