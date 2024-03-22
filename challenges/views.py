from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenge = {
    "january": "Start a daily journal to reflect on your thoughts and experiences.",
    "february": "Learn a new skill or hobby, such as playing a musical instrument or painting.",
    "march": "Commit to regular exercise and start a workout routine.",
    "april": "Set aside time for spring cleaning and decluttering your living space.",
    "may": "Focus on personal growth by reading self-help books or taking online courses.",
    "june": "Spend more time outdoors and connect with nature through hiking or gardening.",
    "july": "Volunteer your time to help others in your community.",
    "august": "Plan a budget and save money for future goals or adventures.",
    "september": "Practice mindfulness and meditation to reduce stress and improve mental well-being.",
    "october": "Set goals for yourself and take steps to achieve them.",
    "november": "Express gratitude daily by keeping a gratitude journal or telling loved ones you appreciate them.",
    "december": "Spread kindness and cheer by performing random acts of kindness for others."
}

def index(request):
    list_items = ""
    months = list(monthly_challenge.keys())
    return render(request, "challenges/index.html",{
        "months": months
    })


def monthly_challenge_by_number(request, m):
    months = list(monthly_challenge.keys())
    if m > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[m - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, m):
    try:
        challenge_text = monthly_challenge[m]
        return render(request,"challenges/challenge.html", {
            "text": challenge_text,
            "month_name":m
        })
    except:
        raise Http404("base.html")
    
# Create your views here.
