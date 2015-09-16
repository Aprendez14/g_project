from students.models import Student, Action
from students.serializers import StudentSerializer, ActionSerializer
from rest_framework import generics
# for initial endpoint
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# others
from rest_framework.views import APIView
from django.http import HttpResponse
from django.http import Http404

from django.contrib import admin
admin.autodiscover()
from rest_framework import permissions, serializers
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'students': reverse('student-list', request=request, format=format),
        'point ranking': reverse('ranking-point-list', request=request, format=format),
        'level ranking': reverse('ranking-level-list', request=request, format=format),
        'golden badges ranking': reverse('ranking-golden-list', request=request, format=format),
        'silver badges ranking': reverse('ranking-silver-list', request=request, format=format),
        'bronze badges ranking': reverse('ranking-bronze-list', request=request, format=format),

        'actions': reverse('action-list', request=request, format=format)
    })

# list and detail of students
class StudentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticated,)

# list and detail of actions
class ActionList(generics.ListCreateAPIView):
    queryset = Action.objects.all().order_by("id")
    serializer_class = ActionSerializer

class ActionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

# list of rankings
class RankingPointList(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by("-points")
    serializer_class = StudentSerializer

class RankingLevelList(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by("-level")
    serializer_class = StudentSerializer

class RankingGoldenList(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by("-golden_badges")
    serializer_class = StudentSerializer

class RankingSilverList(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by("-silver_badges")
    serializer_class = StudentSerializer

class RankingBronzeList(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by("-bronze_badges")
    serializer_class = StudentSerializer


class StudentAction(APIView):

    def get_object_student(self, pk_u):
        try:
            return Student.objects.get(pk=pk_u)
        except Student.DoesNotExist:
            raise Http404


    def get_object_action(self, pk_a):
        try:
            return Action.objects.get(pk=pk_a)
        except Action.DoesNotExist:
            raise Http404


    def get(self, request, pk, pk2, format=None):
        student = self.get_object_student(pk)
        action = self.get_object_action(pk2)

        #serializer = StudentSerializer(student)

        if action.id==1:
            # Log up
            return HttpResponse("You have been successfully logged up. Welcome!")



        # Sign in
        elif action.id==2:

            if student.learning_style=="Undefined":
                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("Hello again. Are you ready for this?")

                elif student.player_type=="Socializer":
                    return HttpResponse("Hello again. Come in, your friends hope you.")

                elif student.player_type=="Killer":
                    return HttpResponse("Are not you still the #1? Do they know you!")

                elif student.player_type=="Explorer":
                    return HttpResponse("Hello again, come in and discover it!")

                else:
                    return HttpResponse("Hello again. Come in!")

            elif student.player_type=="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Activist":
                    return HttpResponse("Hello again! Your imagination is free here.")

                elif student.learning_style=="Reflector":
                    return HttpResponse("Hello again, experience a bit.")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("Hello! What do you want to do today?")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("Hello again! There are still many issues to resolve here.")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("Hello again, come in to see this!")

                elif student.learning_style=="Auditory":
                    return HttpResponse("Hello again! That sounds so good, right?")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("Hello again! Nice day, can you feel it?")

                else:
                    return HttpResponse("Hello again. Come in!")

# /////////////////////////////////////////

        elif action.id==3:
            # Log out
            #student.last_login = datetime.datetime.now()
            if student.learning_style=="Undefined":
                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("You still have to get many badges. See you soon!")

                elif student.player_type=="Socializer":
                    return HttpResponse("We and your friends will miss you, come back soon!")

                elif student.player_type=="Killer":
                    return HttpResponse("That is all? See you soon!")

                elif student.player_type=="Explorer":
                    return HttpResponse("See you soon! You still have much to discover.")

                else:
                    return HttpResponse("We hope see you soon!")

            elif student.player_type=="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Activist":
                    return HttpResponse("Trust yourself and keep your engagement. See you soon!")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic" and student.player_type=="Undefined":
                    return HttpResponse("")

                else:
                    return HttpResponse("We hope see you soon!")

# /////////////////////////////////////////

        elif action.id==4:
            student.points += 10
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("Good job! +10 points, go on!")

                elif student.player_type=="Socializer":
                    return HttpResponse("Yes! +10 points, tell your friends it!")

                elif student.player_type=="Killer":
                    return HttpResponse("+10 points, no bad. But do you conform with that?")

                elif student.player_type=="Explorer":
                    return HttpResponse("Good! +10 points, step by step knowledge comes...")

                else:
                    return HttpResponse("Well done, +10 points!! ")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Activist":
                    return HttpResponse("+10 points, this is getting exciting!")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("Your points is growing up! +10 points, ")

                elif student.learning_style=="Auditory":
                    return HttpResponse("+10 points never sounds bad")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("+10 points. Keep practicing!")
                else:
                    return HttpResponse("Well done, +10 points!! ")

# /////////////////////////////////////////

        elif action.id==5:
            student.points += 20
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("Great job! +20 points, that is the way!")

                elif student.player_type=="Socializer":
                    return HttpResponse("Good! +20 points, You will make many friends if you keep this up!")

                elif student.player_type=="Killer":
                    return HttpResponse("+20 points, really no bad!")

                elif student.player_type=="Explorer":
                    return HttpResponse("Great! +20 points, go on, you still have much to discover.")
                else:
                    return HttpResponse("We hope see you soon!")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Activist":
                    return HttpResponse("+20 points, this is getting exciting!")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("Your points is growing up! +10 points, ")

                elif student.learning_style=="Auditory":
                    return HttpResponse("+10 points never sounds bad")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("+10 points. Keep practicing!")

            else:
                return HttpResponse("Well done, +20 points!! ")

# /////////////////////////////////////////

        elif action.id==6:
            student.points += 50
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("Awesome! +50 points!")

                elif student.player_type=="Socializer":
                    return HttpResponse("Great! +50 points, your friends will be proud of you!")

                elif student.player_type=="Killer":
                    return HttpResponse("+50 points, you shows who's boss!")

                elif student.player_type=="Explorer":
                    return HttpResponse("Great! +50 points, go on and be curious.")
                else:
                    return HttpResponse("We hope see you soon!")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Activist":
                    return HttpResponse("Great! +50 points, keep it up!")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("+50 points! This looks really good.")

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body>+50 points! Repeat it yourself: I'm working really well! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)
#                    serializer = ActionSerializer(action, data=request.data)
#                    if serializer.is_valid():
#                        serializer.save()
#                        return Response(serializer.data)
#                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("+50 points... this deserves a dance!")

            else:
                return HttpResponse("Well done, +50 points!! ")

# /////////////////////////////////////////

        elif action.id==7:
            student.bronze_badges += 1
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("Great! +1 bronze badge, the gold will soon arrive.")

                elif student.player_type=="Socializer":
                    return HttpResponse("Great! +1 bronze badge, good topic to start a conversation!")

                elif student.player_type=="Killer":
                    return HttpResponse("+1 bronze badge, better than nothing, right?")

                elif student.player_type=="Explorer":
                    return HttpResponse("Great! +1 bronze badge, the search yields results!")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if student.learning_style=="Activist":
                    return HttpResponse("+1 bronze badge! New experiences await you.")

                elif student.learning_style=="Reflector":
                    return HttpResponse("+1 bronze badge! This is just the beginning, keep practicing.")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("Great! +1 bronze badge, your intuition works!")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("Great! +1 bronze badge, this is better than any hypothesis!")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("Great! +1 bronze badge, it looks so great, right?")

                elif student.learning_style=="Auditory":
                    return HttpResponse("Great! +1 bronze badge! Listen for improvement.")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("Great! +1 bronze badge, you could almost touch it!")

            else:
                return HttpResponse("Great! You have earned a bronze badge! ")

# /////////////////////////////////////////

        elif action.id==8:
            student.silver_badges += 1
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if student.learning_style=="Activist":
                    return HttpResponse("Great! +1 silver badge. Go on, even greater challenges await you!")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Great! You have earned a silver badge! ")

# /////////////////////////////////////////

        elif action.id==9:
            student.golden_badges += 1
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if student.learning_style=="Activist":
                    return HttpResponse("Wow! +1 golden bagde, are you excited? You should!")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("+1 golden bagde! Take a photo!")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Congratulation, you have earned a golden badge! ")

# /////////////////////////////////////////

        elif action.id==10:
            # The percentage completed at this level is increased by 5 units
            if student.percent_in_level <= 95:
                student.percent_in_level += 5
                student.save()
                if student.learning_style=="Undefined":
                    if student.player_type=="Achiever":
                        return HttpResponse("")

                    elif student.player_type=="Socializer":
                        return HttpResponse("")

                    elif student.player_type=="Killer":
                        return HttpResponse("")

                    elif student.player_type=="Explorer":
                        return HttpResponse("")

                elif student.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if student.learning_style=="Activist":
                        return HttpResponse("")

                    elif student.learning_style=="Reflector":
                        return HttpResponse("")

                    elif student.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif student.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("Good job! Your progress advances +5% in this level!")
            else:
                student.level += 1
                student.percent_in_level = 0
                student.save()
                if student.learning_style=="Undefined":
                    if student.player_type=="Achiever":
                        return HttpResponse("")

                    elif student.player_type=="Socializer":
                        return HttpResponse("")

                    elif student.player_type=="Killer":
                        return HttpResponse("")

                    elif student.player_type=="Explorer":
                        return HttpResponse("")

                elif student.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if student.learning_style=="Activist":
                        return HttpResponse("")

                    elif student.learning_style=="Reflector":
                        return HttpResponse("")

                    elif student.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif student.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("Congratulation! You have reached a new level!")

# /////////////////////////////////////////

        elif action.id==11:
            # The percentage completed at this level is increased by 10 units
            if student.percent_in_level <= 90:
                student.percent_in_level += 10
                student.save()
                if student.learning_style=="Undefined":
                    if student.player_type=="Achiever":
                        return HttpResponse("")

                    elif student.player_type=="Socializer":
                        return HttpResponse("")

                    elif student.player_type=="Killer":
                        return HttpResponse("")

                    elif student.player_type=="Explorer":
                        return HttpResponse("")

                elif student.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if student.learning_style=="Activist":
                        return HttpResponse("")

                    elif student.learning_style=="Reflector":
                        return HttpResponse("")

                    elif student.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif student.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("Good job! Your progress advances +10% in this level!")

            else:
                student.level += 1
                student.percent_in_level = 0
                student.save()
                return HttpResponse("Congratulation! You have reached a new level!")

# /////////////////////////////////////////

        elif action.id==12:
            # The student complete the level with an only action.
            student.level += 1
            student.percent_in_level = 0
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if student.learning_style=="Activist":
                    return HttpResponse("")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Congratulation! You have reached a new level!")

# ///// ACTIONS THAT TAKE AWAY POINTS /////

        elif action.id==13:
            if student.points > 10:
                student.points -= 10
                student.save()
                if student.learning_style=="Undefined":
                    if student.player_type=="Achiever":
                        return HttpResponse("-10 points. Concentrate. You can do it.")

                    elif student.player_type=="Socializer":
                        return HttpResponse("-10 points, don't worry, nobody is looking.")

                    elif student.player_type=="Killer":
                        return HttpResponse("-10 points, this should not happen. Cheer up!")

                    elif student.player_type=="Explorer":
                        return HttpResponse("-10 points, small mistake, don't miss your curiosity.")

                elif student.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if student.learning_style=="Activist":
                        return HttpResponse("-10 points. Don't worry, use your imagination.")

                    elif student.learning_style=="Reflector":
                        return HttpResponse("-10 points, no rush. Observe!")

                    elif student.learning_style=="Pragmatist":
                        return HttpResponse("-10 points, don't worry and keep experimenting!")

                    elif student.learning_style=="Theoretician":
                        return HttpResponse("-10 points, your plan has gone wrong this time. Don't worry.")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("-10 points, Cheer up! Don't lose sight of the objective.")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("-10 points, don't worry, it sounds worse than it really is.")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("-10 points, don't worry, experiencing obstacles is part of the way.")

                else:
                    return HttpResponse("Ouch! You have lost 10 points. Cheer up! ")
            else:
                student.points = 0
                student.save()
                return HttpResponse("Your scores is 0, cheer up! Fall seven times and stand up eight!")

# /////////////////////////////////////////

        elif action.id==14:
            if student.points > 20:
                student.points -= 20
                student.save()
                if student.learning_style=="Undefined":
                    if student.player_type=="Achiever":
                        return HttpResponse("")

                    elif student.player_type=="Socializer":
                        return HttpResponse("")

                    elif student.player_type=="Killer":
                        return HttpResponse("")

                    elif student.player_type=="Explorer":
                        return HttpResponse("")

                elif student.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if student.learning_style=="Activist":
                        return HttpResponse("")

                    elif student.learning_style=="Reflector":
                        return HttpResponse("")

                    elif student.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif student.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("Ouch! You have lost 20 points. Cheer up!")
            else:
                student.points = 0
                student.save()
                return HttpResponse("Your scores is 0. Cheer up! Fall seven times and stand up eight!")

# /////////////////////////////////////////

        elif action.id==15:
            if student.points > 50:
                student.points -= 50
                student.save()
                if student.learning_style=="Undefined":
                    if student.player_type=="Achiever":
                        return HttpResponse("")

                    elif student.player_type=="Socializer":
                        return HttpResponse("")

                    elif student.player_type=="Killer":
                        return HttpResponse("")

                    elif student.player_type=="Explorer":
                        return HttpResponse("")

                elif student.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if student.learning_style=="Activist":
                        return HttpResponse("")

                    elif student.learning_style=="Reflector":
                        return HttpResponse("")

                    elif student.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif student.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("Ouch! You have lost 50 points. Cheer up! Cheer up!")
            else:
                student.points = 0
                student.save()
                return HttpResponse("Your scores is 0. Cheer up! Fall seven times and stand up eight!")

# /// ACTIONS THAT TAKE AWAY PROGRESS IN LEVEL ///

        elif action.id==16:
            # The percentage completed at this level is decreased by 5 units.
            if student.percent_in_level > 5:
                student.percent_in_level -= 5
                student.save()
                if student.learning_style=="Undefined":
                    if student.player_type=="Achiever":
                        return HttpResponse("")

                    elif student.player_type=="Socializer":
                        return HttpResponse("")

                    elif student.player_type=="Killer":
                        return HttpResponse("")

                    elif student.player_type=="Explorer":
                        return HttpResponse("")

                elif student.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if student.learning_style=="Activist":
                        return HttpResponse("")

                    elif student.learning_style=="Reflector":
                        return HttpResponse("")

                    elif student.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif student.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("-5% in your progress. Come on! You can do better!")

            else:
                student.percent_in_level = 0
                student.save()
                return HttpResponse("Your progress is 0% in this level, cheer up! You can do better!")

# /////////////////////////////////////////

        elif action.id==17:
            # The percentage completed at this level is decreased by 10 units.
            if student.percent_in_level > 10:
                student.percent_in_level -= 10
                student.save()
                if student.learning_style=="Undefined":
                    if student.player_type=="Achiever":
                        return HttpResponse("")

                    elif student.player_type=="Socializer":
                        return HttpResponse("")

                    elif student.player_type=="Killer":
                        return HttpResponse("")

                    elif student.player_type=="Explorer":
                        return HttpResponse("")

                elif student.player_type=="Undefined":
                    # LEARNING STYLES MECHANICS
                    if student.learning_style=="Activist":
                        return HttpResponse("")

                    elif student.learning_style=="Reflector":
                        return HttpResponse("")

                    elif student.learning_style=="Pragmatist":
                        return HttpResponse("")

                    elif student.learning_style=="Theoretician":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("")

                else:
                    return HttpResponse("-10% in your progress. Come on! You can do better!")

            else:
                student.percent_in_level = 0
                student.save()
                return HttpResponse("Your progress is 0% in this level, cheer up! You can do better!")

# ////////// ANOTHER ACTIONS /////////////

        elif action.id==18:
            # Feedback and 10 points for visit
            student.points += 10
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if student.learning_style=="Activist":
                    return HttpResponse("")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Thank you for your visit. +10 points!")

# /////////////////////////////////////////

        elif action.id==19:
            # Feedback and 10 points for click
            student.points += 10
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if student.learning_style=="Activist":
                    return HttpResponse("")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Thank you for click here. +10 points!")

# /////////////////////////////////////////

        elif action.id==20:
            # Feedback and 10 points for vote
            student.points += 10
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if student.learning_style=="Activist":
                    return HttpResponse("")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Thank you for your vote. +10 points!")

# /////////////////////////////////////////

        elif action.id==21:
            # Feedback and 10 points for comment
            student.points += 10
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if student.learning_style=="Activist":
                    return HttpResponse("")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Thank you for your comment. +10 points!")

# /////////////////////////////////////////

        elif action.id==22:
            # Feedback and 10 points for upload a file
            student.points += 10
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if student.learning_style=="Activist":
                    return HttpResponse("")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Your file has been successfully uploaded. +10 points!")

# /////////////////////////////////////////

        elif action.id==23:
            # Feedback and 10 points for watch a video
            student.points += 10
            student.save()
            if student.learning_style=="Undefined":
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined":
                # LEARNING STYLES MECHANICS
                if student.learning_style=="Activist":
                    return HttpResponse("")

                elif student.learning_style=="Reflector":
                    return HttpResponse("")

                elif student.learning_style=="Pragmatist":
                    return HttpResponse("")

                elif student.learning_style=="Theoretician":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Great video, right? +10 points!")
