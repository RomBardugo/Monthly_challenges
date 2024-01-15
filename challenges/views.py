from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": 'January - Mission',
    "feburary": 'feburary - Mission',
    "march": 'march - Mission',
    "april": 'april - Mission',
    "may": 'may - Mission',
    "june": 'june - Mission',
    "july": 'july - Mission',
    "august": 'august - Mission',
    "september": 'september - Mission',
    "october": 'october - Mission',
    "november": 'november - Mission',
    "december": 'december - Mission'
}

# Create your views here.


def challenges_menu(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    print(months)
    for month in months:
        redirect_path = reverse("month-challenge", args=[month])
        print(redirect_path)
        list_items += f'<li><a href="{redirect_path}">{month}</a></li>'
    total_html = f"<ul>{list_items}</ul>"
    return HttpResponse(total_html)

def monthly_challenge(request, month):
    if month in monthly_challenges.keys():
        response_data = f"<h1>{monthly_challenges[month]}</h1>"
        return HttpResponse(response_data)
    else:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
