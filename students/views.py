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


        if action.id==1:
            # Log up
            return HttpResponse("You have been successfully logged up. Welcome!")

# /////////////////////////////////////////

        # Sign in
        elif action.id==2:

            if student.learning_style=="Undefined" and student.player_type!="Undefined":
                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("Hello again. Are you ready for this?")

                elif student.player_type=="Socializer":
                    return HttpResponse("Hello again. Come in, your friends hope you.")

                elif student.player_type=="Killer":
                    return HttpResponse("Are not you still the #1? Do they know you!")

                elif student.player_type=="Explorer":
                    return HttpResponse("Hello again, come in and discover it!")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("Hello again! Your imagination is free here.")

                elif student.learning_style=="Converging":
                    return HttpResponse("Hello again, experience a bit.")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("Hello! What do you want to do today?")

                elif student.learning_style=="Assimilating":
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

        # Log out
        elif action.id==3:

            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("You still have to get many badges. See you soon!")

                elif student.player_type=="Socializer":
                    return HttpResponse("We and your friends will miss you, come back soon!")

                elif student.player_type=="Killer":
                    return HttpResponse("That is all? See you soon!")

                elif student.player_type=="Explorer":
                    return HttpResponse("See you soon! You still have much to discover.")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("Trust yourself and keep your engagement. See you soon!")

                elif student.learning_style=="Converging":
                    return HttpResponse("There is a time for everything. See you soon!")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("See you soon. Stay committed!")

                elif student.learning_style=="Assimilating":
                    return HttpResponse("Will we see you tomorrow? Think it!")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("See you soon!")

                elif student.learning_style=="Auditory":
                    return HttpResponse("No say bye, better see you tomorrow, right?")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("You feel well here, come back soon!")

            else:
                return HttpResponse("We hope see you soon!")

# /////////////////////////////////////////

        elif action.id==4:
            student.points += 10
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body>Good job! +10 points, go on! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body>Yes! +10 points, tell your friends it! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body>+10 points, no bad. But do you conform with that? </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body>Good! +10 points, step by step knowledge comes... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body>+10 points, this is getting exciting! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body>+10 points, that is a good job! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body>+10 points, great job! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body>+10 points, well done. Step by step. </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body>Your points is growing up! +10 points! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body>+10 points never sounds bad. </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body>+10 points. Keep practicing! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Well done, +10 points! </br> Your score is: %s.</body></html>" % student.points
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==5:
            student.points += 20
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body>Great job! +20 points, that is the way! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body>Good! +20 points, You will make many friends if you keep this up! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body>+20 points, really no bad! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body>Great! +20 points, go on, you still have much to discover. </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body>+20 points, exciting experience, right?! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body>+20 points, great analysis! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body>+20 points, well done! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body>+20 points, keep investigating! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body>Your points is growing up! +20 points! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body>+20 points never sounds bad! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body>+20 points. Keep practicing! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Well done, +20 points!! </br> Your score is: %s.</body></html>" % student.points
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==6:
            student.points += 50
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body>Awesome! +50 points! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body>Great! +50 points, your friends will be proud of you! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body>+50 points. Show who is the boss! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body>Great! +50 points, go on and be curious. </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body>Great! +50 points, keep it up! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body>+50 points, thinking before acting is a great idea! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body>Great! +50 points, that's a good attitude. </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body>+50 points! Your logic is great! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body>+50 points! This looks really good. </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body>+50 points! Repeat it yourself: I'm working really well! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body>+50 points... this deserves a dance! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Well done, +50 points!! </br> Your score is: %s.</body></html>" % student.points
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==7:
            student.bronze_badges += 1
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body>Great! +1 bronze badge, the gold will soon arrive. </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body>Great! +1 bronze badge, good topic to start a conversation! </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body>+1 bronze badge, better than nothing, right? </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body>Great! +1 bronze badge, the search yields results! </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body>+1 bronze badge! New experiences await you. </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body>+1 bronze badge! This is just the beginning, keep practicing. </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body>Great! +1 bronze badge, your intuition works! </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body>Great! +1 bronze badge, this is better than any hypothesis! </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body>Great! +1 bronze badge, it looks so great, right? </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body>Great! +1 bronze badge! Listen for improvement. </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body>Great! +1 bronze badge, you could almost touch it! </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Great! You have earned a bronze badge! </br> You have %s bronze badges.</body></html>" % student.bronze_badges
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==8:
            student.silver_badges += 1
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body>+1 silver badge, it's fantastic! But there are better badges yet. </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body>+1 silver badge, with it is easier make new friends! </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body>+1 silver badge, but you prefer the golden badges, right? </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body>+1 silver badge, it demonstrates your experience. </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body>Great +1 silver badge! Go on, even greater challenges await you! </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body>Great +1 silver badge! Organize and win. </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body>Great +1 silver badge! More difficult challenges are waiting for you. </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body>Great +1 silver badge! Planning, then advance! </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body>Wow! +1 silver badge. Imagine when your friends see it. </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body>Wow! +1 silver badge! That sounds so good!. </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body>Wow! +1 silver badge! Do you want touch it, right? </br> You have %s silver badges.</body></html>" % student.silver_badges
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Great! You have earned a silver badge! </br> You have %s silver badges.</body></html>" % student.silver_badges
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==9:
            student.golden_badges += 1
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body>+1 golden bagde, this is the reward for an amazing job! </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body>Great! +1 golden bagde. This is the most prestigious badge. </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body>Yes! +1 golden bagde! Show them who is the boss. </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body>Great! +1 golden bagde, a recognition of your experience and knowledge. </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body>Wow! +1 golden bagde, are you excited? You should! </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body>Great! +1 golden badge. A good analysis pays off! </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body>+1 golden bagde! Amazing! This is called a well used opportunity! </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body>+1 golden bagde! Good job! Be perfectionist. </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body>+1 golden bagde! Amazing! Take a photo! </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body>+1 golden bagde! Amazing! Tell your friends! </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body>+1 golden bagde! Amazing! Can you feeling that? </br> You have %s golden badges.</body></html>" % student.golden_badges
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Congratulations, you have earned a golden badge! </br> You have %s golden badges.</body></html>" % student.golden_badges
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==10:
            # The percentage completed at this level is increased by 5 units
            if student.percent_in_level <= 95:
                student.percent_in_level += 5
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        respuesta = "<html><body>+5% in this level. A little closer! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Socializer":
                        respuesta = "<html><body>+5% in this level. When you progress people are interested in you. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Killer":
                        respuesta = "<html><body>+5% in this level. Hurry up! More rhythm! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Explorer":
                        respuesta = "<html><body>+5% in this level. Strange new things are coming. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        respuesta = "<html><body>+5% in this level. Go for it! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Converging":
                        respuesta = "<html><body>+5% in this level. Observe, analyze, forward. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Accommodating":
                        respuesta = "<html><body>+5% in this level. Let's go! Always advancing! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Assimilating":
                        respuesta = "<html><body>+5% in this level. Reflection pays off! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        respuesta = "<html><body>+5% in this level. If progress grows up is all good. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Auditory":
                        respuesta = "<html><body>+5% in this level. Listen how this goes on! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Kinesthetic":
                        respuesta = "<html><body>+5% in this level. Good sensations, right? </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                else:
                    respuesta = "<html><body>Good job! Your progress advances +5% in this level! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                    return HttpResponse(respuesta)

            else:
                student.level += 1
                student.percent_in_level = 0
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        respuesta = "<html><body>New level! Congratulations! Let's go! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Socializer":
                        respuesta = "<html><body>Congratulations! New level! And more friends! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Killer":
                        respuesta = "<html><body>New level! Let's go! Let's go! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Explorer":
                        respuesta = "<html><body>Congratulations! New level, new world! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        respuesta = "<html><body>Congratulations! New level, new challenges! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Converging":
                        respuesta = "<html><body>Congratulations! New level, new info that needs order! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Accommodating":
                        respuesta = "<html><body>Congratulations! New level, new ground for practice! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Assimilating":
                        respuesta = "<html><body>Congratulations! New level, new things to investigate and analyze. </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        respuesta = "<html><body>Congratulations! A new level is before your eyes! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Auditory":
                        respuesta = "<html><body>Congratulations! You have reached a new level! It sounds good, right? </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Kinesthetic":
                        respuesta = "<html><body>Congratulations! You have reached a new level! Enjoy! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                else:
                    respuesta = "<html><body>Congratulations! You have reached a new level! </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==11:
            # The percentage completed at this level is increased by 10 units
            if student.percent_in_level <= 90:
                student.percent_in_level += 10
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        respuesta = "<html><body>+10% in this level. That's a big step! Go on! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Socializer":
                        respuesta = "<html><body>+10% in this level. A little effort and then socialize. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Killer":
                        respuesta = "<html><body>+10% in this level. You know that this is the way. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Explorer":
                        respuesta = "<html><body>+10% in this level. Discover the next level is nearer. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        respuesta = "<html><body>+10% in this level. What a breakthrough! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Converging":
                        respuesta = "<html><body>+10% in this level. Good analyze, good job. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Accommodating":
                        respuesta = "<html><body>+10% in this level. New challenges are closer. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Assimilating":
                        respuesta = "<html><body>+10% in this level. That is a fantastic planning.! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        respuesta = "<html><body>+10% in this level. See? This is better! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Auditory":
                        respuesta = "<html><body>+10% in this level. Repeat: This is progressing! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Kinesthetic":
                        respuesta = "<html><body>+10% in this level. Experiencing and growing up. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                else:
                    respuesta = "<html><body>Good job! Your progress advances +10% in this level! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                    return HttpResponse(respuesta)

            else:
                student.level += 1
                student.percent_in_level = 0
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        respuesta = "<html><body>New level! Congratulations! Let's go! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Socializer":
                        respuesta = "<html><body>Congratulations! New level! And more friends! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Killer":
                        respuesta = "<html><body>New level! Let's go! Let's go! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Explorer":
                        respuesta = "<html><body>Congratulations! New level, new world! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        respuesta = "<html><body>Congratulations! New level, new challenges! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Converging":
                        respuesta = "<html><body>Congratulations! New level, new info that needs order! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Accommodating":
                        respuesta = "<html><body>Congratulations! New level, new ground for practice! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Assimilating":
                        respuesta = "<html><body>Congratulations! New level, new things to investigate and analyze. </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        respuesta = "<html><body>Congratulations! A new level is before your eyes! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Auditory":
                        respuesta = "<html><body>Congratulations! You have reached a new level! It sounds good, right? </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Kinesthetic":
                        respuesta = "<html><body>Congratulations! You have reached a new level! Enjoy! </br> Now you are at level %s.</body></html>" % student.level
                        return HttpResponse(respuesta)

                else:
                    respuesta = "<html><body>Congratulations! You have reached a new level! </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==12:
            # The student complete the level with an only action.
            student.level += 1
            student.percent_in_level = 0
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body>Fantastic job! You have reached a new level! </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body>Congratulations! Tell your friends! </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body>Great! You have reached a new level that you must completed. </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body>Congratulations! You have reached a new level! Know it! </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body>New level! Are you ready to accept new challenges? </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body>New level! New fresh information! </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body>Congratulations! New level, new ground for practice </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body>Congratulations! New level, new things to investigate and analyze. </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body>Congratulations! A new level is before your eyes! </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body>Congratulations! You have reached a new level! It sounds good, right? </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body>Congratulations! You have reached a new level! Enjoy! </br> Now you are at level %s.</body></html>" % student.level
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Congratulations! You have reached a new level! </br> Now you are at level %s.</body></html>" % student.level
                return HttpResponse(respuesta)

# ///// ACTIONS THAT TAKE AWAY POINTS /////

        elif action.id==13:
            if student.points > 10:
                student.points -= 10
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        respuesta = "<html><body>-10 points. Concentrate. You can do it. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.player_type=="Socializer":
                        rrespuesta = "<html><body>-10 points, don't worry, nobody is looking. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.player_type=="Killer":
                        respuesta = "<html><body>-10 points, this should not happen. Cheer up! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.player_type=="Explorer":
                        respuesta = "<html><body>-10 points, small mistake, don't lose your curiosity. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        respuesta = "<html><body>-10 points. Don't worry, use your imagination. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Converging":
                        respuesta = "<html><body>-10 points, no rush. Observe! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Accommodating":
                        respuesta = "<html><body>-10 points, don't worry and keep experimenting! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Assimilating":
                        respuesta = "<html><body>-10 points, your plan has gone wrong this time. Don't worry. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        respuesta = "<html><body>-10 points, Cheer up! Don't lose sight of the objective. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Auditory":
                        respuesta = "<html><body>-10 points, don't worry, it sounds worse than it really is. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Kinesthetic":
                        respuesta = "<html><body>-10 points, don't worry, experiencing obstacles is part of the way. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                else:
                    respuesta = "<html><body>Ouch! You have lost 10 points. Cheer up! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            else:
                student.points = 0
                student.save()
                return HttpResponse("Your scores is 0. Cheer up! Fall seven times and stand up eight!")

# /////////////////////////////////////////

        elif action.id==14:
            if student.points > 20:
                student.points -= 20
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        respuesta = "<html><body>-20 points. Hurry up! Work hard and you could be a winner. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.player_type=="Socializer":
                        respuesta = "<html><body>-20 points. Come on! It doesn't talk good about you. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.player_type=="Killer":
                        respuesta = "<html><body>-20 points. Really? </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.player_type=="Explorer":
                        respuesta = "<html><body>-20 points. Cheer up! High scores open doors. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        respuesta = "<html><body>Oh! -20 points, change your perspective. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Converging":
                        respuesta = "<html><body>-20 points, calm, there is time for thinking! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Accommodating":
                        respuesta = "<html><body>-20 points, trial and error. Cheer up! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Assimilating":
                        respuesta = "<html><body>-20 points, don't worry and be rational. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        respuesta = "<html><body>-20 points, Cheer up! Don't lose sight of the objective. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Auditory":
                        respuesta = "<html><body>-20 points, don't worry, it sounds worse than it really is. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Kinesthetic":
                        respuesta = "<html><body>-20 points, don't worry, experiencing obstacles is part of the way. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                else:
                    respuesta = "<html><body>Ouch! You have lost 20 points. Cheer up! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)
            else:
                student.points = 0
                student.save()
                return HttpResponse("Your scores is 0. Cheer up! Fall seven times and stand up eight!")

# /////////////////////////////////////////

        elif action.id==15:
            if student.points > 50:
                student.points -= 50
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        respuesta = "<html><body>-50 points. Take a rest and come back with force! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.player_type=="Socializer":
                        respuesta = "<html><body>-50 points. This is not going to like your friends. Cheer up! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.player_type=="Killer":
                        respuesta = "<html><body>-50 points. This isn't the way. Cheer up! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.player_type=="Explorer":
                        respuesta = "<html><body>-50 points. Cheer up! High scores open doors. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        respuesta = "<html><body>Ouch... -50 points! A brainstorm? </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Converging":
                        respuesta = "<html><body>-50 points, don't worry and take your time! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Accommodating":
                        respuesta = "<html><body>-50 points. Cheer up! Practice and get better. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Assimilating":
                        respuesta = "<html><body>-50 points. Time to reflection. Cheer up! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        respuesta = "<html><body>-50 points, but don't worry, visualize the right track. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Auditory":
                        respuesta = "<html><body>-50 points, but listen to youself: I CAN! </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Kinesthetic":
                        respuesta = "<html><body>-50 points, big achievements require big efforts. </br> Your score is: %s.</body></html>" % student.points
                        return HttpResponse(respuesta)

                else:
                    respuesta = "<html><body>Ouch! You have lost 50 points. Cheer up! Cheer up! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)
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
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        respuesta = "<html><body>-5% in this level. Cheer up! You can flip over your streak. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Socializer":
                        respuesta = "<html><body>-5% in this level. Come on! Keep your reputation up. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Killer":
                        respuesta = "<html><body>-5% in this level. Come on! Are not you a winner? </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Explorer":
                        respuesta = "<html><body>-5% in this level. That is the wrong way. Cheer up! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        respuesta = "<html><body>-5% in this level. Be careful. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Converging":
                        respuesta = "<html><body>-5% in this level. Look out! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Accommodating":
                        respuesta = "<html><body>-5% in this level. Don't worry and be impulsive! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Assimilating":
                        respuesta = "<html><body>-5% in this level. The challenges don't always go well. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        respuesta = "<html><body>-5% in this level. Calm, it seems little and can be recovered. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Auditory":
                        respuesta = "<html><body>-5% in this level. Don't listen it and concentrate! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Kinesthetic":
                        respuesta = "<html><body>-5% in this level. Don't back down. You can retrieve it. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                else:
                    respuesta = "<html><body>-5% in your progress. Come on! You can do better! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                    return HttpResponse(respuesta)

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
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        respuesta = "<html><body>-10% in this level. Cheer up! You can improve it! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Socializer":
                        respuesta = "<html><body>-10% in this level. It doesn't seem something to be proud of. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Killer":
                        respuesta = "<html><body>-10% in this level. Come on! Change the chip! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.player_type=="Explorer":
                        respuesta = "<html><body>-10% in this level. Do you like to advance, right? Cheer up! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        respuesta = "<html><body>-10% in this level. This isn't cool! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Converging":
                        respuesta = "<html><body>-10% in this level. Stop, take a breath, observe, analize, proceed. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Accommodating":
                        respuesta = "<html><body>-10% in this level. Looking on the bright side and you will improve! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Assimilating":
                        respuesta = "<html><body>-10% in this level. Don't worry and inquire into the problem. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        respuesta = "<html><body>-10% in this level. Don't worry, we learn from mistakes. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Auditory":
                        respuesta = "<html><body>-10% in this level. Listen to yourself and you will recover it. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                    elif student.learning_style=="Kinesthetic":
                        respuesta = "<html><body>-10% in this level. You should recover the good feelings. </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                        return HttpResponse(respuesta)

                else:
                    respuesta = "<html><body>-10% in your progress. Come on! You can do better! </br> Your progress in this level is %s %.</body></html>" % student.percent_in_level
                    return HttpResponse(respuesta)

            else:
                student.percent_in_level = 0
                student.save()
                return HttpResponse("Your progress is 0% in this level, cheer up! You can do better!")

# ////////// ANOTHER ACTIONS /////////////

        elif action.id==18:
            # Feedback and 10 points for visit
            student.points += 10
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body>Nice visit, right? Thanks you, +10 points! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Thank you for your visit. +10 points! </br> Your score is: %s.</body></html>" % student.points
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==19:
            # Feedback and 10 points for click
            student.points += 10
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":
                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body>+10 points for your click! </br> Your score is: %s.</body></html>" % student.points

                elif student.learning_style=="Converging":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Thank you for click here. +10 points! </br> Your score is: %s.</body></html>" % student.points
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==20:
            # Feedback and 10 points for vote
            student.points += 20
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Thank you for your vote. +20 points! </br> Your score is: %s.</body></html>" % student.points
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==21:
            # Feedback and 10 points for comment
            student.points += 20
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Thank you for your comment. +10 points! </br> Your score is: %s.</body></html>" % student.points
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==22:
            # Feedback and 10 points for upload a file
            student.points += 10
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Your file has been successfully uploaded. +10 points! </br> Your score is: %s.</body></html>" % student.points
                return HttpResponse(respuesta)

# /////////////////////////////////////////

        elif action.id==23:
            # Feedback and 10 points for watch a video
            student.points += 20
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Socializer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Killer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.player_type=="Explorer":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Converging":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Accommodating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Assimilating":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    respuesta = "<html><body> ... </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

            else:
                respuesta = "<html><body>Great video, right? +20 points! </br> Your score is: %s.</body></html>" % student.points
                return HttpResponse(respuesta)
