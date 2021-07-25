from django.urls import path
from .import views


urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('provider-list/', views.providerList, name="provider-list"),
    path('provider-detail/<str:pk>/', views.providerDetail, name="provider-detail"),
    path('provider-create/', views.providerCreate, name="provider-create"),
    path('provider-update/<str:pk>/', views.providerUpdate, name="provider-update"),
    path('provider-delete/<str:pk>/', views.providerDelete, name="provider-delete"),

    path('polygon-list/', views.polygonList, name="polygon-list"),
    path('polygon-create/', views.polygonCreate, name="polygon-create"),
    path('polygon-update/<str:pk>/', views.polygonUpdate, name="polygon-update"),
    path('polygon-delete/<str:pk>/', views.polygonDelete, name="polygon-delete"),
    path('query/<str:latitude>/<str:longitude>', views.query, name="query"),
]