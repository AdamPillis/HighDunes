from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('<slug:slug>/', views.ReviewInDetail.as_view(), name='review_page'),
    path('like/<slug:slug>/', views.ReviewLike.as_view(), name='review_like'),
    path(
        'dislike/<slug:slug>/',
        views.ReviewDislike.as_view(),
        name='review_dislike'
        ),
]
