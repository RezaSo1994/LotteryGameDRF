from django.urls import path
from . import views


urlpatterns = [
    path('', views.BuyTicketsList.as_view()),
    # path('prouduct/<int:pk>/', views.ProductDetail.as_view()),

]
