from rest_framework import serializers
from payments.models import PaymentInfo

class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = '__all__'