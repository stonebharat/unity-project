from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from rest_framework.fields import empty
from rest_framework.pagination import CursorPagination
from rest_framework import filters
from .serializers import LeadSerializer
from .models import Lead


class LeadList(generics.ListCreateAPIView):
    """
    List all leads, or create a new lead.
    """
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['-created']