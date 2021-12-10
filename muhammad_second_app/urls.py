from django.contrib import admin
from django.urls import path
from . import views

app_name = 'muhammad_second_app'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('users/', views.GetUserView.as_view(), name='users'),
    path('countries/', views.GetCountriesList.as_view(), name='countries'),
    path('sales/', views.SalesView.as_view(), name='sales'),
    path('sale_statistics/', views.SaleStatistics.as_view(), name='sale_statistics'),
    path('upload_country_data/', views.UploadCountryData.as_view(), name='upload_country_data'),  # for adding country/city
    path('upload_sales/', views.UploadProductSaleData.as_view(), name='upload_sales'),
]
