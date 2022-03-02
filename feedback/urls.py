from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('<slug:slug>/', views.ReviewInDetail.as_view(), name='review_page'),
]
