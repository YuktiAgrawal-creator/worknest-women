from rest_framework import serializers
from .models import Job
from skills.serializers import SkillSerializer
from accounts.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    skills = SkillSerializer(many=True, read_only=True)
    postedBy = UserSerializer(source='postedBy', read_only=True)
    createdAt = serializers.DateTimeField()

    class Meta:
        model = Job
        fields = ['_id','id','title','company','description','requirements','skills','type','category','salary','location','postedBy','applicants','status','isWomenOnly','tags','createdAt']

    def get__id(self, obj):
        return str(obj.id)
