from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def get_jobs(request):
    category = request.query_params.get('category')
    type_q = request.query_params.get('type')
    search = request.query_params.get('search')
    skill = request.query_params.get('skill')
    qs = Job.objects.filter(status='open')
    if category:
        qs = qs.filter(category=category)
    if type_q:
        qs = qs.filter(type=type_q)
    if skill:
        qs = qs.filter(skills__id=skill)
    if search:
        qs = qs.filter(models=models)
    qs = qs.order_by('-createdAt')
    return Response({"success": True, "jobs": JobSerializer(qs, many=True).data})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_job(request, id):
    try:
        job = Job.objects.get(pk=id)
        return Response({"success": True, "job": JobSerializer(job).data})
    except Job.DoesNotExist:
        return Response({"success": False, "message": 'Job not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_job(request):
    data = request.data.copy()
    data['postedBy'] = request.user.id
    serializer = JobSerializer(data=data)
    if serializer.is_valid():
        job = serializer.save()
        return Response({"success": True, "job": JobSerializer(job).data}, status=status.HTTP_201_CREATED)
    return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_jobs(request):
    qs = Job.objects.filter(postedBy=request.user).order_by('-createdAt')
    return Response({"success": True, "jobs": JobSerializer(qs, many=True).data})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_job(request, id):
    try:
        job = Job.objects.get(pk=id, postedBy=request.user)
    except Job.DoesNotExist:
        return Response({"success": False, "message": 'Job not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = JobSerializer(job, data=request.data, partial=True)
    if serializer.is_valid():
        job = serializer.save()
        return Response({"success": True, "job": JobSerializer(job).data})
    return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_recommended(request):
    user = request.user
    skill_ids = user.skills.values_list('id', flat=True)
    qs = Job.objects.filter(skills__id__in=skill_ids, status='open').order_by('-createdAt')[:6]
    return Response({"success": True, "jobs": JobSerializer(qs, many=True).data})
