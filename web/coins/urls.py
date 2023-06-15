from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("get_json_list_coins/<str:date_part>/", views.get_json_list_coins, name="month"),
    path("get_json_list_values/<str:date_part>/", views.get_json_list_values, name="month"),
    path("get_json_values/<str:date_part>/", views.get_json_values, name="month"),
    path("month_list/<str:date_part>/", views.month_list, name="month"),
    path("month/<str:date_part>/", views.month, name="month"),
]
