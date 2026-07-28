from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_transactions(request):
    qs = Transaction.objects.filter(user=request.user).order_by('-date')
    return Response({"success": True, "transactions": TransactionSerializer(qs, many=True).data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_transaction(request):
    data = request.data.copy()
    data['user'] = request.user.id
    serializer = TransactionSerializer(data=data)
    if serializer.is_valid():
        t = serializer.save()
        return Response({"success": True, "transaction": TransactionSerializer(t).data}, status=status.HTTP_201_CREATED)
    return Response({"success": False, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
