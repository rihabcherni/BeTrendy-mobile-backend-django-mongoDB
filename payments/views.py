from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from payments.models import PaymentInfo
from payments.serializers import PaymentInfoSerializer

class PaymentInfoListCreateView(generics.ListCreateAPIView):
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PaymentInfoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]