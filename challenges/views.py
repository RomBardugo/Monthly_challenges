from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
    "december": None #'december - Mission'
}

# Create your views here.


def challenges_menu(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months": months
    })

def monthly_challenge(request, month):
    if month in monthly_challenges.keys():
        return render(request, "challenges/challenge.html", {
            "text": monthly_challenges[month],
            "month": month,
            "monthTitle": month
        })
    else:
        raise Http404()

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
