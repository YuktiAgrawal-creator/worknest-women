from rest_framework import serializers
from .models import Application
from accounts.serializers import UserSerializer
from jobs.serializers import JobSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    applicant = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)
    appliedAt = serializers.DateTimeField()
    updatedAt = serializers.DateTimeField()

    class Meta:
        model = Application
        fields = ['_id','id','job','applicant','coverLetter','status','interviewDate','notes','appliedAt','updatedAt']

    def get__id(self, obj):
        return str(obj.id)
