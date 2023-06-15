import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.shortcuts import render

from .models import coin_day


def get_all_month(date_part, coin_name="BTC"):
    coin_day_list_1 = coin_day.objects.filter(date_part__startswith=date_part).values("date_part", "name", "value")
    if len(coin_day_list_1) > 0:
        data = []
        for linea in coin_day_list_1:
            if linea["name"] == coin_name:
                data.append({
                    "date_part": linea["date_part"],
                    "value": linea["value"]
                })
    else:
        data = []
    return json.dumps(data)


def get_coin_list_month(date_part):
    coin_day_list_1 = coin_day.objects.filter(date_part__startswith=date_part).values("name").distinct()
    data = []
    if len(coin_day_list_1) > 0:
        for linea in coin_day_list_1:
            data.append(linea["name"])
    return data


def get_value_list_month(date_part, coin_list=["ZEN", "XRB", "ZEC"]):
    coin_day_list_1 = coin_day.objects.filter(date_part__startswith=date_part).values("date_part", "name", "value")
    data = {}
    if len(coin_day_list_1) > 0:
        data = {}
        for linea in coin_day_list_1:
            if linea["name"] in coin_list:
                if not data.get(linea["name"]):
                    data[linea["name"]] = []
                data[linea["name"]].append({
                    "date_part": linea["date_part"],
                    "value": linea["value"]
                })

    data2 = []
    for linea2 in data:
        data2.append({
            "label": linea2,
            "data": data[linea2]
        })

    return json.dumps(data2)


def get_json_list_coins(request, date_part):
    return JsonResponse(json.dumps(get_coin_list_month(date_part)), safe=False)


def get_json_list_values(request, date_part):
    return JsonResponse(get_value_list_month(date_part), safe=False)


def get_json_values(request, date_part):
    return JsonResponse(get_all_month(date_part), safe=False)


def get_json_month_old(request, date_part):
    # coin_day_list = coin_day.objects.get(date_part=dp)
    # template = loader.get_template("coins/index.html")
    # context = {
    #     "coin_day_list": coin_day_list,
    # }
    # return HttpResponse(template.render(context, request))
    coin_day_list_1 = coin_day.objects.filter(date_part__startswith=date_part).values("date_part", "name", "value")
    if len(coin_day_list_1) > 0:
        # json_tmp = json.dumps([])
        data = {
            "min_rate": 0,
            "max_tare": 0,
            "rates": []
        }
        data2 = []
        for linea in coin_day_list_1:
            if linea["value"] > data["max_tare"]:
                data["max_tare"] = linea["value"]
            if linea["value"] < data["min_rate"]:
                data["min_rate"] = linea["value"]
            # data["rates"][linea["date_part"]][linea["name"]] = linea["value"]
            data["rates"].append({ "date_part": linea["date_part"], "name": linea["name"], "value": linea["value"] })


        """
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
        """
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


def getSavedDates(request):
    # tmp_list = json.load(request)
    lista_fechas = []
    for fecha in request:
        lista_fechas.append(fecha["date_part"][0:7])
    return lista_fechas


def index(request):
    coin_day_list_2 = coin_day.objects.filter(date_part="2022-01-01").values("name")
    coin_day_list_1 = coin_day.objects.filter(date_part__iendswith="-01").values("date_part").distinct()
    coin_day_list_1 = getSavedDates(coin_day_list_1)
    context = {
        "dates_saved": coin_day_list_1,
        "coin_names": coin_day_list_2,
    }
    return render(request, "coins/index.html", context)


def month(request, date_part):
    coin_day_list_2 = coin_day.objects.filter(date_part="2022-01-01").values("name")
    coin_day_list_1 = coin_day.objects.filter(date_part__iendswith="-01").values("date_part").distinct()
    coin_day_list_1 = getSavedDates(coin_day_list_1)
    month_data = get_all_month(date_part)
    context = {
        "dates_saved": coin_day_list_1,
        "coin_names": coin_day_list_2,
        "month_data": month_data,
    }
    return render(request, "coins/month.html", context)


def month_list(request, date_part):
    coin_day_list_2 = coin_day.objects.filter(date_part="2022-01-01").values("name")
    coin_day_list_1 = coin_day.objects.filter(date_part__iendswith="-01").values("date_part").distinct()
    coin_day_list_1 = getSavedDates(coin_day_list_1)
    month_data = get_value_list_month(date_part)
    coin_list = get_coin_list_month(date_part)
    context = {
        "dates_saved": coin_day_list_1,
        "coin_names": coin_day_list_2,
        "month_data": month_data,
        "coin_list": coin_list,
    }
    return render(request, "coins/month_list.html", context)
