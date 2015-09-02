from users.models import User, Action
from users.serializers import UserSerializer, ActionSerializer
from rest_framework import generics
# Para el endpoint inicial
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
#probando
from rest_framework.views import APIView
from django.http import HttpResponse
from django.template import defaultfilters

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
#
#
#
#PROBANDO

class UserAction(APIView):

    def get_object_user(self, pk_u):
        try:
            return User.objects.get(pk=pk_u)
        except User.DoesNotExist:
            raise Http404

    def get_object_action(self, pk_a):
        try:
            return Action.objects.get(pk=pk_a)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, pk2, format=None):
        action = self.get_object_action(pk)

        if action.id==1:
            return HttpResponse("You have been successfully logged up. Welcome!")

        elif action.id==2:
            return HttpResponse("Hello again. Come in!")

        elif action.id==3:
            return HttpResponse("We hope see you soon!")

        elif action.id==4:
            return HttpResponse("Well done, +10 points!! ")

        elif action.id==5:
            return HttpResponse("Well done! You earned a badge!")

        else:
           return HttpResponse("That action is not defined.")


        serializer = ActionSerializer(action, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar y detallar las acciones (funciona OK)

class ActionList(generics.ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
