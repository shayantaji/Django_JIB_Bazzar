from rest_framework import viewsets
from . models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserApiView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer