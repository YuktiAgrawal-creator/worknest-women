from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken


def _make_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    # Add compatibility claim 'id'
    refresh['id'] = str(user.id)
    access = refresh.access_token
    access['id'] = str(user.id)
    return str(access)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    token = _make_tokens_for_user(user)
    data = UserSerializer(user).data
    return Response({"success": True, "token": token, "user": data}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"success": False, "message": 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.filter(email__iexact=email).first()
        if user is None or not user.check_password(password):
            return Response({"success": False, "message": 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        token = _make_tokens_for_user(user)
        data = UserSerializer(user).data
        return Response({"success": True, "token": token, "user": data})
    except Exception:
        return Response({"success": False, "message": 'Login failed. Please try again.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    user = request.user
    data = UserSerializer(user).data
    return Response({"success": True, "user": data})
