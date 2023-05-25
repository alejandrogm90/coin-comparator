import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render

from .models import coin_day


def month(request, date_part):
    # coin_day_list = coin_day.objects.get(date_part=dp)
    # template = loader.get_template("coins/index.html")
    # context = {
    #     "coin_day_list": coin_day_list,
    # }
    # return HttpResponse(template.render(context, request))
    if date_part == "2022-01-01":
        data = {
            "date_part": ["2022-01-01", "2022-01-02", "2022-01-03"],
            "min_rate": 0,
            "max_tare": 2,
            "rates": {
                "ACP": [0.014931, 0.0065, 0.017178],
                "ADA": [1.380249, 0.00013, 0.01515],
                "ADX": [0.57981, 0.0023, 0.1327]
            }
        }
    else:
        data = {
            "date_part": ["0-0-0"],
            "min_rate": 0,
            "max_tare": 0,
            "rates": {
            }
        }
    data2 = json.dumps(data)
    return JsonResponse(data2, safe=False)


def example(request):
    data = {
        "date_part": "2022-01-02",
        "min_rate": 0,
        "max_tare": 1.5,
        "rates": {
            "ABC": 59.99,
            "ACP": 0.014931,
            "ACT": 0.0065,
            "ACT*": 0.017178,
            "ADA": 1.380249,
            "ADCN": 0.00013,
            "ADL": 0.01515,
            "ADX": 0.57981,
            "ADZ": 0.0023,
            "AE": 0.1327
        }
    }
    data2 = json.dumps(data)
    return JsonResponse(data2, safe=False)


def coins(request):
    data = {
        "date_part": "2022-01-02",
        "min_rate": 0,
        "max_tare": 1.5,
        "rates": {
            "ABC": 59.99,
            "ACP": 0.014931,
            "ACT": 0.0065,
            "ACT*": 0.017178,
            "ADA": 1.380249,
            "ADCN": 0.00013,
            "ADL": 0.01515,
            "ADX": 0.57981,
            "ADZ": 0.0023,
            "AE": 0.1327
        }
    }
    data2 = json.dumps(data)
    return JsonResponse(data2, safe=False)


# def index(request):
#     coin_day_list = coin_day.objects.order_by("date_part")[:5]
#     print(coin_day_list)
#     # template = loader.get_template("coins/index.html")
#     context = {
#         "coin_day_list": coin_day_list,
#     }
#     # return HttpResponse(template.render(context, request))
#     return render(request, "coins/index.html", context)


def index(request):
    coin_day_list_2 = coin_day.objects.filter(date_part="2022-01-01").values("name")
    coin_day_list_1 = coin_day.objects.filter(date_part__iendswith="-01").values("date_part").distinct()
    context = {
        "dates_saved": coin_day_list_1,
        "coin_names": coin_day_list_2,
    }
    return render(request, "coins/index.html", context)


