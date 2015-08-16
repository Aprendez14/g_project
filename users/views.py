from users.models import User
from users.serializers import UserSerializer
from rest_framework import generics
# Para el endpoint inicial
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'ranking': reverse('ranking-list', request=request, format=format)
    })


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RankingList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("-points")
    serializer_class = UserSerializer
