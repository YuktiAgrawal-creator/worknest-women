from rest_framework import serializers
from .models import User
from skills.serializers import SkillSerializer

class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    createdAt = serializers.DateTimeField(source='created_at', read_only=True)
    totalEarnings = serializers.FloatField(source='totalEarnings')
    isVerified = serializers.BooleanField(source='isVerified')
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['_id','id','name','email','role','phone','location','bio','avatar','skills','totalEarnings','isVerified','createdAt']

    def get__id(self, obj):
        return str(obj.id)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    class Meta:
        model = User
        fields = ('name','email','password','role','phone','location')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
