from celery import shared_task
from django.utils.timezone import localdate, now
from datetime import timedelta
from .models import Lead
@shared_task(name="print_new_emails_this_month")
def print_new_mails_this_month():
    today_date = localdate()
    first_date = today_date.replace(day=1)
    
    total_leads = Lead.objects.filter(created__date__gte=first_date).count()
    print(f'{total_leads} new emails this month')
    return "succesfully printed this month's new emails "