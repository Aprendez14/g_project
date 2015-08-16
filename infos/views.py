from infos.models import Info
from infos.serializers import InfoSerializer
from rest_framework import generics


class InfoList(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class InfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
