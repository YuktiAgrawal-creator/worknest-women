from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    date = serializers.DateTimeField()
    class Meta:
        model = Transaction
        fields = ['_id','id','user','type','amount','category','description','date','job','status']
    def get__id(self,obj):
        return str(obj.id)
