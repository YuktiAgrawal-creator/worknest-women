from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Application
from .serializers import ApplicationSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def apply_job(request):
    data = request.data.copy()
    job_id = data.get('job')
    if not job_id:
        return Response({"success": False, "message": 'job is required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        app = Application.objects.create(job_id=job_id, applicant=request.user, coverLetter=data.get('coverLetter',''))
        return Response({"success": True, "application": ApplicationSerializer(app).data}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"success": False, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_applications(request):
    qs = Application.objects.filter(applicant=request.user).order_by('-appliedAt')
    return Response({"success": True, "applications": ApplicationSerializer(qs, many=True).data})
