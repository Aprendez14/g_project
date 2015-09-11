from users.models import User, Action
from users.serializers import UserSerializer, ActionSerializer
from rest_framework import generics
# for initial endpoint
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# others
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import Http404
import datetime

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'point ranking': reverse('ranking-point-list', request=request, format=format),
        'level ranking': reverse('ranking-level-list', request=request, format=format),
        'golden badges ranking': reverse('ranking-golden-list', request=request, format=format),
        'silver badges ranking': reverse('ranking-silver-list', request=request, format=format),
        'bronze badges ranking': reverse('ranking-bronze-list', request=request, format=format),

        'actions': reverse('action-list', request=request, format=format)
    })

# list and detail of users
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# list and detail of actions
class ActionList(generics.ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

# list of rankings
class RankingPointList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("-points")
    serializer_class = UserSerializer

class RankingLevelList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("-level")
    serializer_class = UserSerializer

class RankingGoldenList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("-golden_badges")
    serializer_class = UserSerializer

class RankingSilverList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("-silver_badges")
    serializer_class = UserSerializer

class RankingBronzeList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by("-bronze_badges")
    serializer_class = UserSerializer


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

        #serializer = UserSerializer(user)

        if action.id==1:
            # Log up
            return HttpResponse("You have been successfully logged up. Welcome!")



        # Sign in
        elif action.id==2:

            if user.learning_style=="Undefined":
                #  PLAYER TYPES MECHANICS - BARTLE
                if user.player_type=="Achiever":
                    return HttpResponse("Hello again. Are you ready for this?")

                elif user.player_type=="Socializer":
                    return HttpResponse("Hello again. Come in, your friends hope you.")

                elif user.player_type=="Killer":
                    return HttpResponse("Are not you still the #1? Do they know you!")

                elif user.player_type=="Explorer":
                    return HttpResponse("Hello again, come in and discover it!")

                else:
                    return HttpResponse("Hello again. Come in!")

            elif user.player_type=="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if user.learning_style=="Activist":
                    return HttpResponse("Hello again! Your imagination is free here.")

                elif user.learning_style=="Reflector":
                    return HttpResponse("Hello again, experience a bit.")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("Hello! What do you want to do today?")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("Hello again! There are still many issues to resolve here.")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("Hello again, come in to see this!")

                elif user.learning_style=="Auditory":
                    return HttpResponse("Hello again! That sounds so good, right?")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("Hello again! Nice day, can you feel it?")

                else:
                    return HttpResponse("Hello again. Come in!")

# /////////////////////////////////////////

        elif action.id==3:
            # Log out
            #user.last_login = datetime.datetime.now()
            if user.learning_style=="Undefined":
                #  PLAYER TYPES MECHANICS - BARTLE
                if user.player_type=="Achiever":
                    return HttpResponse("You still have to get many badges. See you soon!")

                elif user.player_type=="Socializer":
                    return HttpResponse("We and your friends will miss you, come back soon!")

                elif user.player_type=="Killer":
                    return HttpResponse("That is all? See you soon!")

                elif user.player_type=="Explorer":
                    return HttpResponse("See you soon! You still have much to discover.")

                else:
                    return HttpResponse("We hope see you soon!")

            elif user.player_type=="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if user.learning_style=="Activist":
                    return HttpResponse("Trust yourself and keep your engagement. See you soon!")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("")

                elif user.learning_style=="Auditory":
                    return HttpResponse("")

                elif user.learning_style=="Kinesthetic" and user.player_type=="Undefined":
                    return HttpResponse("")

                else:
                    return HttpResponse("We hope see you soon!")

# /////////////////////////////////////////

        elif action.id==4:
            user.points += 10
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("Good job! +10 points, go on!")

                elif user.player_type=="Socializer":
                    return HttpResponse("Yes! +10 points, tell your friends it!")

                elif user.player_type=="Killer":
                    return HttpResponse("+10 points, no bad. But do you conform with that?")

                elif user.player_type=="Explorer":
                    return HttpResponse("Good! +10 points, step by step knowledge comes...")
                else:
                    return HttpResponse("We hope see you soon!")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS - KOLB
                if user.learning_style=="Activist":
                    return HttpResponse("+10 points, this is getting exciting!")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("Your points is growing up! +10 points, ")

                elif user.learning_style=="Auditory":
                    return HttpResponse("+10 points never sounds bad")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("+10 points. Keep practicing!")
                else:
                    return HttpResponse("Well done, +10 points!! ")

# /////////////////////////////////////////

        elif action.id==5:
            user.points += 20
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("Great job! +20 points, that is the way!")

                elif user.player_type=="Socializer":
                    return HttpResponse("Good! +20 points, You will make many friends if you keep this up!")

                elif user.player_type=="Killer":
                    return HttpResponse("+20 points, really no bad!")

                elif user.player_type=="Explorer":
                    return HttpResponse("Great! +20 points, go on, you still have much to discover.")
                else:
                    return HttpResponse("We hope see you soon!")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS - KOLB
                if user.learning_style=="Activist":
                    return HttpResponse("+20 points, this is getting exciting!")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("Your points is growing up! +10 points, ")

                elif user.learning_style=="Auditory":
                    return HttpResponse("+10 points never sounds bad")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("+10 points. Keep practicing!")

            else:
                return HttpResponse("Well done, +20 points!! ")

# /////////////////////////////////////////

        elif action.id==6:
            user.points += 50
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("Awesome! +50 points!")

                elif user.player_type=="Socializer":
                    return HttpResponse("Great! +50 points, your friends will be proud of you!")

                elif user.player_type=="Killer":
                    return HttpResponse("+50 points, you shows who's boss!")

                elif user.player_type=="Explorer":
                    return HttpResponse("Great! +50 points, go on and be curious.")
                else:
                    return HttpResponse("We hope see you soon!")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS - KOLB
                if user.learning_style=="Activist":
                    return HttpResponse("Great! +50 points, keep it up!")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("+50 points! This looks really good.")

                elif user.learning_style=="Auditory":
                    respuesta = "<html><body>+50 points! Repeat it yourself: I'm working really well! </br> Your score is: %s.</body></html>" % user.points
                    return HttpResponse(respuesta)
#                    serializer = ActionSerializer(action, data=request.data)
#                    if serializer.is_valid():
#                        serializer.save()
#                        return Response(serializer.data)
#                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("+50 points... this deserves a dance!")

            else:
                return HttpResponse("Well done, +50 points!! ")

# /////////////////////////////////////////

        elif action.id==7:
            user.bronze_badges += 1
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("Great! +1 bronze badge, the gold will soon arrive.")

                elif user.player_type=="Socializer":
                    return HttpResponse("Great! +1 bronze badge, good topic to start a conversation!")

                elif user.player_type=="Killer":
                    return HttpResponse("+1 bronze badge, better than nothing, right?")

                elif user.player_type=="Explorer":
                    return HttpResponse("Great! +1 bronze badge, the search yields results!")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if user.learning_style=="Activist":
                    return HttpResponse("+1 bronze badge! New experiences await you.")

                elif user.learning_style=="Reflector":
                    return HttpResponse("+1 bronze badge! This is just the beginning, keep practicing.")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("Great! +1 bronze badge, your intuition works!")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("Great! +1 bronze badge, this is better than any hypothesis!")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("Great! +1 bronze badge, it looks so great, right?")

                elif user.learning_style=="Auditory":
                    return HttpResponse("Great! +1 bronze badge! Listen for improvement.")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("Great! +1 bronze badge, you could almost touch it!")

            else:
                return HttpResponse("Great! You have earned a bronze badge! ")

# /////////////////////////////////////////

        elif action.id==8:
            user.silver_badges += 1
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("")

                elif user.player_type=="Socializer":
                    return HttpResponse("")

                elif user.player_type=="Killer":
                    return HttpResponse("")

                elif user.player_type=="Explorer":
                    return HttpResponse("")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if user.learning_style=="Activist":
                    return HttpResponse("Great! +1 silver badge. Go on, even greater challenges await you!")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("")

                elif user.learning_style=="Auditory":
                    return HttpResponse("")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Great! You have earned a silver badge! ")

# /////////////////////////////////////////

        elif action.id==9:
            user.golden_badges += 1
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("")

                elif user.player_type=="Socializer":
                    return HttpResponse("")

                elif user.player_type=="Killer":
                    return HttpResponse("")

                elif user.player_type=="Explorer":
                    return HttpResponse("")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if user.learning_style=="Activist":
                    return HttpResponse("Wow! +1 golden bagde, are you excited? You should!")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("+1 golden bagde! Take a photo!")

                elif user.learning_style=="Auditory":
                    return HttpResponse("")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Congratulation, you have earned a golden badge! ")

# /////////////////////////////////////////

        elif action.id==10:
            # The percentage completed at this level is increased by 5 units
            if user.percent_in_level <= 95:
                user.percent_in_level += 5
                user.save()
                if user.learning_style=="Undefined":
                    if user.player_type=="Achiever":
                        return HttpResponse("")

                    elif user.player_type=="Socializer":
                        return HttpResponse("")

                    elif user.player_type=="Killer":
                        return HttpResponse("")

                    elif user.player_type=="Explorer":
                        return HttpResponse("")

                elif user.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if user.learning_style=="Activist":
                        return HttpResponse("")

                    elif user.learning_style=="Reflector":
                        return HttpResponse("")

                    elif user.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif user.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif user.learning_style=="Visual":
                        return HttpResponse("")

                    elif user.learning_style=="Auditory":
                        return HttpResponse("")

                    elif user.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("Good job! Your progress advances +5% in this level!")
            else:
                user.level += 1
                user.percent_in_level = 0
                user.save()
                if user.learning_style=="Undefined":
                    if user.player_type=="Achiever":
                        return HttpResponse("")

                    elif user.player_type=="Socializer":
                        return HttpResponse("")

                    elif user.player_type=="Killer":
                        return HttpResponse("")

                    elif user.player_type=="Explorer":
                        return HttpResponse("")

                elif user.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if user.learning_style=="Activist":
                        return HttpResponse("")

                    elif user.learning_style=="Reflector":
                        return HttpResponse("")

                    elif user.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif user.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif user.learning_style=="Visual":
                        return HttpResponse("")

                    elif user.learning_style=="Auditory":
                        return HttpResponse("")

                    elif user.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("Congratulation! You have reached a new level!")

# /////////////////////////////////////////

        elif action.id==11:
            # The percentage completed at this level is increased by 10 units
            if user.percent_in_level <= 90:
                user.percent_in_level += 10
                user.save()
                if user.learning_style=="Undefined":
                    if user.player_type=="Achiever":
                        return HttpResponse("")

                    elif user.player_type=="Socializer":
                        return HttpResponse("")

                    elif user.player_type=="Killer":
                        return HttpResponse("")

                    elif user.player_type=="Explorer":
                        return HttpResponse("")

                elif user.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if user.learning_style=="Activist":
                        return HttpResponse("")

                    elif user.learning_style=="Reflector":
                        return HttpResponse("")

                    elif user.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif user.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif user.learning_style=="Visual":
                        return HttpResponse("")

                    elif user.learning_style=="Auditory":
                        return HttpResponse("")

                    elif user.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("Good job! Your progress advances +10% in this level!")

            else:
                user.level += 1
                user.percent_in_level = 0
                user.save()
                return HttpResponse("Congratulation! You have reached a new level!")

# /////////////////////////////////////////

        elif action.id==12:
            # The user complete the level with an only action.
            user.level += 1
            user.percent_in_level = 0
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("")

                elif user.player_type=="Socializer":
                    return HttpResponse("")

                elif user.player_type=="Killer":
                    return HttpResponse("")

                elif user.player_type=="Explorer":
                    return HttpResponse("")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if user.learning_style=="Activist":
                    return HttpResponse("")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("")

                elif user.learning_style=="Auditory":
                    return HttpResponse("")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Congratulation! You have reached a new level!")

# ///// ACTIONS THAT TAKE AWAY POINTS /////

        elif action.id==13:
            if user.points > 10:
                user.points -= 10
                user.save()
                if user.learning_style=="Undefined":
                    if user.player_type=="Achiever":
                        return HttpResponse("-10 points. Concentrate. You can do it.")

                    elif user.player_type=="Socializer":
                        return HttpResponse("-10 points, don't worry, nobody is looking.")

                    elif user.player_type=="Killer":
                        return HttpResponse("-10 points, this should not happen. Cheer up!")

                    elif user.player_type=="Explorer":
                        return HttpResponse("-10 points, small mistake, don't miss your curiosity.")

                elif user.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if user.learning_style=="Activist":
                        return HttpResponse("-10 points. Don't worry, use your imagination.")

                    elif user.learning_style=="Reflector":
                        return HttpResponse("-10 points, no rush. Observe!")

                    elif user.learning_style=="Pragmatist":
                        return HttpResponse("-10 points, don't worry and keep experimenting!")

                    elif user.learning_style=="Theoretician":
                        return HttpResponse("-10 points, your plan has gone wrong this time. Don't worry.")

                    # LEARNING STYLES MECHANICS - PNL
                    elif user.learning_style=="Visual":
                        return HttpResponse("-10 points, Cheer up! Don't lose sight of the objective.")

                    elif user.learning_style=="Auditory":
                        return HttpResponse("-10 points, don't worry, it sounds worse than it really is.")

                    elif user.learning_style=="Kinesthetic":
                        return HttpResponse("-10 points, don't worry, experiencing obstacles is part of the way.")

                else:
                    return HttpResponse("Ouch! You have lost 10 points. Cheer up! ")
            else:
                user.points = 0
                user.save()
                return HttpResponse("Your scores is 0, cheer up! Fall seven times and stand up eight!")

# /////////////////////////////////////////

        elif action.id==14:
            if user.points > 20:
                user.points -= 20
                user.save()
                if user.learning_style=="Undefined":
                    if user.player_type=="Achiever":
                        return HttpResponse("")

                    elif user.player_type=="Socializer":
                        return HttpResponse("")

                    elif user.player_type=="Killer":
                        return HttpResponse("")

                    elif user.player_type=="Explorer":
                        return HttpResponse("")

                elif user.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if user.learning_style=="Activist":
                        return HttpResponse("")

                    elif user.learning_style=="Reflector":
                        return HttpResponse("")

                    elif user.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif user.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif user.learning_style=="Visual":
                        return HttpResponse("")

                    elif user.learning_style=="Auditory":
                        return HttpResponse("")

                    elif user.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("Ouch! You have lost 20 points. Cheer up!")
            else:
                user.points = 0
                user.save()
                return HttpResponse("Your scores is 0. Cheer up! Fall seven times and stand up eight!")

# /////////////////////////////////////////

        elif action.id==15:
            if user.points > 50:
                user.points -= 50
                user.save()
                if user.learning_style=="Undefined":
                    if user.player_type=="Achiever":
                        return HttpResponse("")

                    elif user.player_type=="Socializer":
                        return HttpResponse("")

                    elif user.player_type=="Killer":
                        return HttpResponse("")

                    elif user.player_type=="Explorer":
                        return HttpResponse("")

                elif user.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if user.learning_style=="Activist":
                        return HttpResponse("")

                    elif user.learning_style=="Reflector":
                        return HttpResponse("")

                    elif user.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif user.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif user.learning_style=="Visual":
                        return HttpResponse("")

                    elif user.learning_style=="Auditory":
                        return HttpResponse("")

                    elif user.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("Ouch! You have lost 50 points. Cheer up! Cheer up!")
            else:
                user.points = 0
                user.save()
                return HttpResponse("Your scores is 0. Cheer up! Fall seven times and stand up eight!")

# /// ACTIONS THAT TAKE AWAY PROGRESS IN LEVEL ///

        elif action.id==16:
            # The percentage completed at this level is decreased by 5 units.
            if user.percent_in_level > 5:
                user.percent_in_level -= 5
                user.save()
                if user.learning_style=="Undefined":
                    if user.player_type=="Achiever":
                        return HttpResponse("")

                    elif user.player_type=="Socializer":
                        return HttpResponse("")

                    elif user.player_type=="Killer":
                        return HttpResponse("")

                    elif user.player_type=="Explorer":
                        return HttpResponse("")

                elif user.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if user.learning_style=="Activist":
                        return HttpResponse("")

                    elif user.learning_style=="Reflector":
                        return HttpResponse("")

                    elif user.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif user.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif user.learning_style=="Visual":
                        return HttpResponse("")

                    elif user.learning_style=="Auditory":
                        return HttpResponse("")

                    elif user.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("-5% in your progress. Come on! You can do better!")

            else:
                user.percent_in_level = 0
                user.save()
                return HttpResponse("Your progress is 0% in this level, cheer up! You can do better!")

# /////////////////////////////////////////

        elif action.id==17:
            # The percentage completed at this level is decreased by 10 units.
            if user.percent_in_level > 10:
                user.percent_in_level -= 10
                user.save()
                if user.learning_style=="Undefined":
                    if user.player_type=="Achiever":
                        return HttpResponse("")

                    elif user.player_type=="Socializer":
                        return HttpResponse("")

                    elif user.player_type=="Killer":
                        return HttpResponse("")

                    elif user.player_type=="Explorer":
                        return HttpResponse("")

                elif user.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if user.learning_style=="Activist":
                        return HttpResponse("")

                    elif user.learning_style=="Reflector":
                        return HttpResponse("")

                    elif user.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif user.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif user.learning_style=="Visual":
                        return HttpResponse("")

                    elif user.learning_style=="Auditory":
                        return HttpResponse("")

                    elif user.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("-10% in your progress. Come on! You can do better!")

            else:
                user.percent_in_level = 0
                user.save()
                return HttpResponse("Your progress is 0% in this level, cheer up! You can do better!")

# ////////// ANOTHER ACTIONS /////////////

        elif action.id==18:
            # Feedback and 10 points for visit
            user.points += 10
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("")

                elif user.player_type=="Socializer":
                    return HttpResponse("")

                elif user.player_type=="Killer":
                    return HttpResponse("")

                elif user.player_type=="Explorer":
                    return HttpResponse("")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if user.learning_style=="Activist":
                    return HttpResponse("")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("")

                elif user.learning_style=="Auditory":
                    return HttpResponse("")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Thank you for your visit. +10 points!")

# /////////////////////////////////////////

        elif action.id==19:
            # Feedback and 10 points for click
            user.points += 10
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("")

                elif user.player_type=="Socializer":
                    return HttpResponse("")

                elif user.player_type=="Killer":
                    return HttpResponse("")

                elif user.player_type=="Explorer":
                    return HttpResponse("")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if user.learning_style=="Activist":
                    return HttpResponse("")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("")

                elif user.learning_style=="Auditory":
                    return HttpResponse("")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Thank you for click here. +10 points!")

# /////////////////////////////////////////

        elif action.id==20:
            # Feedback and 10 points for vote
            user.points += 10
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("")

                elif user.player_type=="Socializer":
                    return HttpResponse("")

                elif user.player_type=="Killer":
                    return HttpResponse("")

                elif user.player_type=="Explorer":
                    return HttpResponse("")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if user.learning_style=="Activist":
                    return HttpResponse("")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("")

                elif user.learning_style=="Auditory":
                    return HttpResponse("")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Thank you for your vote. +10 points!")

# /////////////////////////////////////////

        elif action.id==21:
            # Feedback and 10 points for comment
            user.points += 10
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("")

                elif user.player_type=="Socializer":
                    return HttpResponse("")

                elif user.player_type=="Killer":
                    return HttpResponse("")

                elif user.player_type=="Explorer":
                    return HttpResponse("")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if user.learning_style=="Activist":
                    return HttpResponse("")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("")

                elif user.learning_style=="Auditory":
                    return HttpResponse("")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Thank you for your comment. +10 points!")

# /////////////////////////////////////////

        elif action.id==22:
            # Feedback and 10 points for upload a file
            user.points += 10
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("")

                elif user.player_type=="Socializer":
                    return HttpResponse("")

                elif user.player_type=="Killer":
                    return HttpResponse("")

                elif user.player_type=="Explorer":
                    return HttpResponse("")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if user.learning_style=="Activist":
                    return HttpResponse("")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("")

                elif user.learning_style=="Auditory":
                    return HttpResponse("")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Your file has been successfully uploaded. +10 points!")

# /////////////////////////////////////////

        elif action.id==23:
            # Feedback and 10 points for watch a video
            user.points += 10
            user.save()
            if user.learning_style=="Undefined":
                if user.player_type=="Achiever":
                    return HttpResponse("")

                elif user.player_type=="Socializer":
                    return HttpResponse("")

                elif user.player_type=="Killer":
                    return HttpResponse("")

                elif user.player_type=="Explorer":
                    return HttpResponse("")

            elif user.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if user.learning_style=="Activist":
                    return HttpResponse("")

                elif user.learning_style=="Reflector":
                    return HttpResponse("")

                elif user.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif user.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif user.learning_style=="Visual":
                    return HttpResponse("")

                elif user.learning_style=="Auditory":
                    return HttpResponse("")

                elif user.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Great video, right? +10 points!")
