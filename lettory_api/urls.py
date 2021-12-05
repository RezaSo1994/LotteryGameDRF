from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserDataList.as_view()),
    path('data', views.TotalDataList.as_view()),
    # path('prouduct/<int:pk>/', views.ProductDetail.as_view()),

]
