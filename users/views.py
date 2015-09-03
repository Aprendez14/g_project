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
from django.http import Http404


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'ranking': reverse('ranking-list', request=request, format=format),
        'actions': reverse('action-list', request=request, format=format)
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
        except Action.DoesNotExist:
            raise Http404


    def get(self, request, pk, pk2, format=None):
        user = self.get_object_user(pk)
        action = self.get_object_action(pk2)

        if action.id==1:
            # Log up
            return HttpResponse("You have been successfully logged up. Welcome!")

        elif action.id==2:
            # Sign in
            return HttpResponse("Hello again. Come in!")

        elif action.id==3:
            # Log out
            return HttpResponse("We hope see you soon!")

        elif action.id==4:
            user.points += 10
            user.save()
            return HttpResponse("Well done, +10 points!! ")

        elif action.id==5:
            user.points += 20
            user.save()
            return HttpResponse("Well done, +20 points!! ")

        elif action.id==6:
            user.points += 50
            user.save()
            return HttpResponse("Well done, +50 points!! ")

        elif action.id==7:
            user.bronze_badges += 1
            user.save()
            return HttpResponse("Great! You have earned a bronze badge! ")

        elif action.id==8:
            user.silver_badges += 1
            user.save()
            return HttpResponse("Great! You have earned a silver badge! ")

        elif action.id==9:
            user.golden_badges += 1
            user.save()
            return HttpResponse("Congratulation, you have earned a golden badge! ")

        elif action.id==10:
            # The percentage completed at this level is increased by 5 units
            if user.percent_in_level <= 95:
                user.percent_in_level += 5
                user.save()
                return HttpResponse("Good job! Your progress advances +5% in this level!")
            else:
                user.level += 1
                user.percent_in_level = 0
                user.save()
                return HttpResponse("Congratulation! You have reached a new level!")

        elif action.id==11:
            # The percentage completed at this level is increased by 10 units
            if user.percent_in_level <= 90:
                user.percent_in_level += 10
                user.save()
                return HttpResponse("Good job! Your progress advances +10% in this level!")
            else:
                user.level += 1
                user.percent_in_level = 0
                user.save()
                return HttpResponse("Congratulation! You have reached a new level!")

        elif action.id==12:
            # The user complete the level with an only action.
            user.level += 1
            user.percent_in_level = 0
            user.save()
            return HttpResponse("Congratulation! You have reached a new level!")

        # ACTIONS THAT TAKE AWAY POINTS
        elif action.id==13:
            if user.points > 10:
                user.points -= 10
                user.save()
                return HttpResponse("Ouch! You have lost 10 points. Cheer up! ")
            else:
                user.points = 0
                user.save()
                return HttpResponse("Your scores is 0, cheer up! Fall seven times and stand up eight!")

        elif action.id==14:
            if user.points > 20:
                user.points -= 20
                user.save()
                return HttpResponse("Ouch! You have lost 20 points. Cheer up!")
            else:
                user.points = 0
                user.save()
                return HttpResponse("Your scores is 0. Cheer up! Fall seven times and stand up eight!")

        elif action.id==15:
            if user.points > 50:
                user.points -= 50
                user.save()
                return HttpResponse("Ouch! You have lost 50 points. Cheer up! Cheer up!")
            else:
                user.points = 0
                user.save()
                return HttpResponse("Your scores is 0. Cheer up! Fall seven times and stand up eight!")

        # ACTIONS THAT TAKE AWAY PROGRESS IN LEVEL
        elif action.id==16:
            # The percentage completed at this level is decreased by 5 units.
            if user.percent_in_level > 5:
                user.percent_in_level -= 5
                user.save()
                return HttpResponse("-5% in your progress. Come on! You can do better!")
            else:
                user.percent_in_level = 0
                user.save()
                return HttpResponse("Your progress is 0% in this level, cheer up! You can do better!")

        elif action.id==17:
            # The percentage completed at this level is decreased by 10 units.
            if user.percent_in_level > 10:
                user.percent_in_level -= 10
                user.save()
                return HttpResponse("-10% in your progress. Come on! You can do better!")
            else:
                user.percent_in_level = 0
                user.save()
                return HttpResponse("Your progress is 0% in this level, cheer up! You can do better!")

        elif action.id==18:
            # Feedback and 10 points for visit
            user.points += 10
            user.save()
            return HttpResponse("Thank you for your visit. +10 points!")

        elif action.id==19:
            # Feedback and 10 points for click
            user.points += 10
            user.save()
            return HttpResponse("Thank you for click here. +10 points!")

        elif action.id==20:
            # Feedback and 10 points for vote
            user.points += 10
            user.save()
            return HttpResponse("Thank you for your vote. +10 points!")

        elif action.id==21:
            # Feedback and 10 points for comment
            user.points += 10
            user.save()
            return HttpResponse("Thank you for your comment. +10 points!")

        elif action.id==22:
            # Feedback and 10 points for upload a file
            user.points += 10
            user.save()
            return HttpResponse("Your file has been successfully uploaded. +10 points!")

        elif action.id==23:
            # Feedback and 10 points for watch a video
            user.points += 10
            user.save()
            return HttpResponse("Great video, right? +10 points!")

        #PROBAR SI ESTO ES NECESARIO:
#        serializer = ActionSerializer(action, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#        serializer = UserSerializer(user_, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Listar y detallar las acciones (funciona OK)

class ActionList(generics.ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
