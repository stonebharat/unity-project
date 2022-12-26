from django.shortcuts import render
from .models import Lead
# Create your views here.
from django.http import HttpResponse
from django.utils.timezone import localdate, now
from datetime import timedelta


def index(request):
    context = {
    }

    leads = Lead.objects.all().order_by('-created')
    today_date = localdate()
    first_date = today_date.replace(day=1)
    context["leads"] = leads
    context["total_emails"] = leads.count()
    context["new_emails"] = leads.filter(created__date__gte = first_date).count()
    context["unsubscribed"] = leads.filter(subscribed=False).count()
    return render(request, 'index.html',context=context)