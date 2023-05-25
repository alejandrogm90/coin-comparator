from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path("<str:date_part>/", views.month, name="month"),
    path("month/<str:date_part>/", views.month, name="month"),
    path("example/", views.example, name="example"),
]
