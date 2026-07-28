from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Skill
from .serializers import SkillSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def list_skills(request):
    skills = Skill.objects.all()
    return Response({"success": True, "skills": SkillSerializer(skills, many=True).data})

@api_view(['POST'])
@permission_classes([AllowAny])
def create_skill(request):
    serializer = SkillSerializer(data=request.data)
    if serializer.is_valid():
        s = serializer.save()
        return Response({"success": True, "skill": SkillSerializer(s).data}, status=status.HTTP_201_CREATED)
    return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
