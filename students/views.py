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
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
                    return HttpResponse("")

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
                    return HttpResponse("Good job! +10 points, go on!")

                elif student.player_type=="Socializer":
                    return HttpResponse("Yes! +10 points, tell your friends it!")

                elif student.player_type=="Killer":
                    return HttpResponse("+10 points, no bad. But do you conform with that?")

                elif student.player_type=="Explorer":
                    return HttpResponse("Good! +10 points, step by step knowledge comes...")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("+10 points, this is getting exciting!")

                elif student.learning_style=="Converging":
                    return HttpResponse("+10 points, that is a good job!")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
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
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("Great job! +20 points, that is the way!")

                elif student.player_type=="Socializer":
                    return HttpResponse("Good! +20 points, You will make many friends if you keep this up!")

                elif student.player_type=="Killer":
                    return HttpResponse("+20 points, really no bad!")

                elif student.player_type=="Explorer":
                    return HttpResponse("Great! +20 points, go on, you still have much to discover.")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("+20 points, exciting experience, right?!")

                elif student.learning_style=="Converging":
                    return HttpResponse("+20 points, great analysis!")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
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
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("Awesome! +50 points!")

                elif student.player_type=="Socializer":
                    return HttpResponse("Great! +50 points, your friends will be proud of you!")

                elif student.player_type=="Killer":
                    return HttpResponse("+50 points. Show who is the boss!")

                elif student.player_type=="Explorer":
                    return HttpResponse("Great! +50 points, go on and be curious.")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("Great! +50 points, keep it up!")

                elif student.learning_style=="Converging":
                    return HttpResponse("+50 points, thinking before acting is a great idea!")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("+50 points! This looks really good.")

                elif student.learning_style=="Auditory":
                    respuesta = "<html><body>+50 points! Repeat it yourself: I'm working really well! </br> Your score is: %s.</body></html>" % student.points
                    return HttpResponse(respuesta)

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("+50 points... this deserves a dance!")

            else:
                return HttpResponse("Well done, +50 points!! ")

# /////////////////////////////////////////

        elif action.id==7:
            student.bronze_badges += 1
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("Great! +1 bronze badge, the gold will soon arrive.")

                elif student.player_type=="Socializer":
                    return HttpResponse("Great! +1 bronze badge, good topic to start a conversation!")

                elif student.player_type=="Killer":
                    return HttpResponse("+1 bronze badge, better than nothing, right?")

                elif student.player_type=="Explorer":
                    return HttpResponse("Great! +1 bronze badge, the search yields results!")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("+1 bronze badge! New experiences await you.")

                elif student.learning_style=="Converging":
                    return HttpResponse("+1 bronze badge! This is just the beginning, keep practicing.")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("Great! +1 bronze badge, your intuition works!")

                elif student.learning_style=="Assimilating":
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
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("+1 silver badge, it's fantastic! But there are better badges yet.")

                elif student.player_type=="Socializer":
                    return HttpResponse("+1 silver badge, with it is easier make new friends!")

                elif student.player_type=="Killer":
                    return HttpResponse("+1 silver badge, but you prefer the golden badges, right?")

                elif student.player_type=="Explorer":
                    return HttpResponse("+1 silver badge, it demonstrates your experience.")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("Great! +1 silver badge. Go on, even greater challenges await you!")

                elif student.learning_style=="Converging":
                    return HttpResponse("Great! +1 silver badge. Organize and win.")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("Wow! +1 silver badge. Imagine when your friends see it.")

                elif student.learning_style=="Auditory":
                    return HttpResponse("Wow! +1 silver badge! That sounds so good!.")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("Wow! +1 silver badge! Do you want touch it, right?")

            else:
                return HttpResponse("Great! You have earned a silver badge! ")

# /////////////////////////////////////////

        elif action.id==9:
            student.golden_badges += 1
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("+1 golden bagde, this is the reward for an amazing job!")

                elif student.player_type=="Socializer":
                    return HttpResponse("Great! +1 golden bagde. This is the most prestigious badge.")

                elif student.player_type=="Killer":
                    return HttpResponse("Yes! +1 golden bagde! Show them who is the boss.")

                elif student.player_type=="Explorer":
                    return HttpResponse("Great! +1 golden bagde, a recognition of your experience and knowledge.")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("Wow! +1 golden bagde, are you excited? You should!")

                elif student.learning_style=="Converging":
                    return HttpResponse("Great! +1 golden badge. A good analysis pays off!")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("+1 golden bagde! Amazing! Take a photo!")

                elif student.learning_style=="Auditory":
                    return HttpResponse("+1 golden bagde! Amazing! Tell your friends!")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("+1 golden bagde! Amazing! Can you feeling that?")

            else:
                return HttpResponse("Congratulations, you have earned a golden badge! ")

# /////////////////////////////////////////

        elif action.id==10:
            # The percentage completed at this level is increased by 5 units
            if student.percent_in_level <= 95:
                student.percent_in_level += 5
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        return HttpResponse("+5% in this level. A little closer!")

                    elif student.player_type=="Socializer":
                        return HttpResponse("+5% in this level. When you progress people are interested in you.")

                    elif student.player_type=="Killer":
                        return HttpResponse("+5% in this level. Hurry up! More rhythm!")

                    elif student.player_type=="Explorer":
                        return HttpResponse("+5% in this level. Strange new things are coming.")

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        return HttpResponse("+5% in this level. Go for it!")

                    elif student.learning_style=="Converging":
                        return HttpResponse("+5% in this level. Observe, analyze, forward.")

                    elif student.learning_style=="Accommodating":
                        return HttpResponse("")

                    elif student.learning_style=="Assimilating":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("+5% in this level. If progress grows up is all good.")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("+5% in this level. Listen how this goes on!")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("+5% in this level. Good sensations, right?")

                else:
                    return HttpResponse("Good job! Your progress advances +5% in this level!")

            else:
                student.level += 1
                student.percent_in_level = 0
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        return HttpResponse("New level! Congratulations! Let's go!")

                    elif student.player_type=="Socializer":
                        return HttpResponse("Congratulations! New level! And more friends!")

                    elif student.player_type=="Killer":
                        return HttpResponse("New level! Let's go! Let's go!")

                    elif student.player_type=="Explorer":
                        return HttpResponse("Congratulations! New level, new world!")

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        return HttpResponse("Congratulations! New level, new challenges!")

                    elif student.learning_style=="Converging":
                        return HttpResponse("Congratulations! New level, new info that needs order!")

                    elif student.learning_style=="Accommodating":
                        return HttpResponse("")

                    elif student.learning_style=="Assimilating":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("Congratulations! A new level is before your eyes!")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("Congratulations! You have reached a new level! It sounds good, right?")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("Congratulations! You have reached a new level! Enjoy!")

                else:
                    return HttpResponse("Congratulations! You have reached a new level!")

# /////////////////////////////////////////

        elif action.id==11:
            # The percentage completed at this level is increased by 10 units
            if student.percent_in_level <= 90:
                student.percent_in_level += 10
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        return HttpResponse("+10% in this level. That's a big step! Go on!")

                    elif student.player_type=="Socializer":
                        return HttpResponse("+10% in this level. A little effort and then socialize.")

                    elif student.player_type=="Killer":
                        return HttpResponse("+10% in this level. You know that this is the way.")

                    elif student.player_type=="Explorer":
                        return HttpResponse("+10% in this level. Discover the next level is nearer.")

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        return HttpResponse("+10% in this level. What a breakthrough!")

                    elif student.learning_style=="Converging":
                        return HttpResponse("+10% in this level. Good analyze, good job.")

                    elif student.learning_style=="Accommodating":
                        return HttpResponse("")

                    elif student.learning_style=="Assimilating":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("+10% in this level. See? This is better!")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("+10% in this level. Repeat: This is progressing!")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("+10% in this level. Experiencing and growing up.")

                else:
                    return HttpResponse("Good job! Your progress advances +10% in this level!")

            else:
                student.level += 1
                student.percent_in_level = 0
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        return HttpResponse("New level! Congratulations! Let's go!")

                    elif student.player_type=="Socializer":
                        return HttpResponse("Congratulations! New level! And more friends!")

                    elif student.player_type=="Killer":
                        return HttpResponse("New level! Let's go! Let's go!")

                    elif student.player_type=="Explorer":
                        return HttpResponse("Congratulations! New level, new world!")

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        return HttpResponse("Congratulations! New level, new challenges!")

                    elif student.learning_style=="Converging":
                        return HttpResponse("Congratulations! New level, new info that needs order!")

                    elif student.learning_style=="Accommodating":
                        return HttpResponse("")

                    elif student.learning_style=="Assimilating":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("Congratulations! A new level is before your eyes!")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("Congratulations! You have reached a new level! It sounds good, right?")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("Congratulations! You have reached a new level! Enjoy!")

                else:
                    return HttpResponse("Congratulations! You have reached a new level!")

# /////////////////////////////////////////

        elif action.id==12:
            # The student complete the level with an only action.
            student.level += 1
            student.percent_in_level = 0
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("Fantastic job! You have reached a new level!")

                elif student.player_type=="Socializer":
                    return HttpResponse("Congratulations! Tell your friends!")

                elif student.player_type=="Killer":
                    return HttpResponse("Great! You have reached a new level that you must completed.")

                elif student.player_type=="Explorer":
                    return HttpResponse("Congratulations! You have reached a new level! Know it!")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("New level! Are you ready to accept new challenges?")

                elif student.learning_style=="Converging":
                    return HttpResponse("New level! New fresh information!")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("Congratulations! A new level is before your eyes!")

                elif student.learning_style=="Auditory":
                    return HttpResponse("Congratulations! You have reached a new level! It sounds good, right?")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("Congratulations! You have reached a new level! Enjoy!")

            else:
                return HttpResponse("Congratulations! You have reached a new level!")

# ///// ACTIONS THAT TAKE AWAY POINTS /////

        elif action.id==13:
            if student.points > 10:
                student.points -= 10
                student.save()
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        return HttpResponse("-10 points. Concentrate. You can do it.")

                    elif student.player_type=="Socializer":
                        return HttpResponse("-10 points, don't worry, nobody is looking.")

                    elif student.player_type=="Killer":
                        return HttpResponse("-10 points, this should not happen. Cheer up!")

                    elif student.player_type=="Explorer":
                        return HttpResponse("-10 points, small mistake, don't lose your curiosity.")

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        return HttpResponse("-10 points. Don't worry, use your imagination.")

                    elif student.learning_style=="Converging":
                        return HttpResponse("-10 points, no rush. Observe!")

                    elif student.learning_style=="Accommodating":
                        return HttpResponse("-10 points, don't worry and keep experimenting!")

                    elif student.learning_style=="Assimilating":
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
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        return HttpResponse("-20 points. Hurry up! Work hard and you could be a winner.")

                    elif student.player_type=="Socializer":
                        return HttpResponse("-20 points. Come on! It doesn't talk good about you.")

                    elif student.player_type=="Killer":
                        return HttpResponse("-20 points. Really?")

                    elif student.player_type=="Explorer":
                        return HttpResponse("-20 points. Cheers up! High scores open doors.")

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        return HttpResponse("Oh! -20 points, change your perspective.")

                    elif student.learning_style=="Converging":
                        return HttpResponse("-20 points, calm, there is time for thinking!")

                    elif student.learning_style=="Accommodating":
                        return HttpResponse("")

                    elif student.learning_style=="Assimilating":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("-20 points, Cheer up! Don't lose sight of the objective.")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("-20 points, don't worry, it sounds worse than it really is.")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("-20 points, don't worry, experiencing obstacles is part of the way.")

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
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        return HttpResponse("-50 points. Take a rest and come back with force!")

                    elif student.player_type=="Socializer":
                        return HttpResponse("-50 points. This is not going to like your friends. Cheer up!")

                    elif student.player_type=="Killer":
                        return HttpResponse("-50 points. This isn't the way. Cheer up!")

                    elif student.player_type=="Explorer":
                        return HttpResponse("-50 points. Cheers up! High scores open doors.")

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        return HttpResponse("Ouch... -50 points! A brainstorm?")

                    elif student.learning_style=="Converging":
                        return HttpResponse("-50 points, don't worry and take your time!")

                    elif student.learning_style=="Accommodating":
                        return HttpResponse("")

                    elif student.learning_style=="Assimilating":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("-50 points, but don't worry, visualize the right track.")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("-50 points, but listen to youself: I CAN!")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("-50 points, big achievements require big efforts.")

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
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        return HttpResponse("-5% in this level. Cheer up! You can flip over your streak.")

                    elif student.player_type=="Socializer":
                        return HttpResponse("-5% in this level. Come on! Keep your reputation up.")

                    elif student.player_type=="Killer":
                        return HttpResponse("-5% in this level. Come on! Are not you a winner?")

                    elif student.player_type=="Explorer":
                        return HttpResponse("-5% in this level. That is the wrong way. Cheer up!")

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        return HttpResponse("-5% in this level. Be careful.")

                    elif student.learning_style=="Converging":
                        return HttpResponse("-5% in this level. Look out!")

                    elif student.learning_style=="Accommodating":
                        return HttpResponse("")

                    elif student.learning_style=="Assimilating":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("-5% in this level. Calm, it seems little and can be recovered.")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("-5% in this level. Don't listen it and concentrate!")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("-5% in this level. Don't back down. You can retrieve it.")

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
                if student.learning_style=="Undefined" and student.player_type!="Undefined":

                    #  PLAYER TYPES MECHANICS - BARTLE
                    if student.player_type=="Achiever":
                        return HttpResponse("-10% in this level. Cheer up! You can improve it!")

                    elif student.player_type=="Socializer":
                        return HttpResponse("-10% in this level. It doesn't seem something to be proud of.")

                    elif student.player_type=="Killer":
                        return HttpResponse("-10% in this level. Come on! Change the chip!")

                    elif student.player_type=="Explorer":
                        return HttpResponse("-10% in this level. Do you like to advance, right? Cheer up!")

                elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                    # LEARNING STYLES MECHANICS - KOLB
                    if student.learning_style=="Diverging":
                        return HttpResponse("-10% in this level. This isn't cool!.")

                    elif student.learning_style=="Converging":
                        return HttpResponse("-10% in this level. Stop, take a breath, observe, analize, proceed.")

                    elif student.learning_style=="Accommodating":
                        return HttpResponse("")

                    elif student.learning_style=="Assimilating":
                        return HttpResponse("")

                    # LEARNING STYLES MECHANICS - PNL
                    elif student.learning_style=="Visual":
                        return HttpResponse("-10% in this level. Don't worry, we learn from mistakes.")

                    elif student.learning_style=="Auditory":
                        return HttpResponse("-10% in this level. Listen to yourself and you will recover it.")

                    elif student.learning_style=="Kinesthetic":
                        return HttpResponse("-10% in this level. You should recover the good feelings.")

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
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("Nice visit, right? Thanks you, +10 points!")

                elif student.learning_style=="Converging":
                    return HttpResponse("")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
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
            if student.learning_style=="Undefined" and student.player_type!="Undefined":
                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("+10 points for your click!")

                elif student.learning_style=="Converging":
                    return HttpResponse("")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
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
            student.points += 20
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("")

                elif student.learning_style=="Converging":
                    return HttpResponse("")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Thank you for your vote. +20 points!")

# /////////////////////////////////////////

        elif action.id==21:
            # Feedback and 10 points for comment
            student.points += 20
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("")

                elif student.learning_style=="Converging":
                    return HttpResponse("")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
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
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("")

                elif student.learning_style=="Converging":
                    return HttpResponse("")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
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
            student.points += 20
            student.save()
            if student.learning_style=="Undefined" and student.player_type!="Undefined":

                #  PLAYER TYPES MECHANICS - BARTLE
                if student.player_type=="Achiever":
                    return HttpResponse("")

                elif student.player_type=="Socializer":
                    return HttpResponse("")

                elif student.player_type=="Killer":
                    return HttpResponse("")

                elif student.player_type=="Explorer":
                    return HttpResponse("")

            elif student.player_type=="Undefined" and student.learning_style!="Undefined":

                # LEARNING STYLES MECHANICS - KOLB
                if student.learning_style=="Diverging":
                    return HttpResponse("")

                elif student.learning_style=="Converging":
                    return HttpResponse("")

                elif student.learning_style=="Accommodating":
                    return HttpResponse("")

                elif student.learning_style=="Assimilating":
                    return HttpResponse("")

                # LEARNING STYLES MECHANICS - PNL
                elif student.learning_style=="Visual":
                    return HttpResponse("")

                elif student.learning_style=="Auditory":
                    return HttpResponse("")

                elif student.learning_style=="Kinesthetic":
                    return HttpResponse("")

            else:
                return HttpResponse("Great video, right? +20 points!")
