from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AmishRegistrations, FeedBackFromAndroid, NotifsAndroid
from .serializers import AmishSerializers, FeedSerializers, NotifsSerializers
from django.core.mail import EmailMessage
from .forms import Amish_Form


def amishreg(request):
    if request.POST:
        name = request.POST['params']
        mail = request.POST['mail']
        city = name["city"]
        college = request.POST['college']
        contact = request.POST['contact']
        regi = AmishRegistrations(name=name, mail=mail, contact=contact, college=college, city=city)
        regi.save()
        serializer = AmishSerializers(regi, many=True)
        return Response(serializer.data)
    else:
        return Response("None")


def getnotifs(request):
    if request.GET:
        regs = NotifsAndroid.objects.all().order_by("-id")[0]
        return Response(regs.title)
    else:
        return Response("error.")


class RegList(APIView):

    def get(self, request):
        regs = AmishRegistrations.objects.all()
        serializer = AmishSerializers(regs, many=True)
        return Response(serializer.data)

    def post(self, request):
        regs = AmishRegistrations.objects.all()
        serializer = AmishSerializers(regs,  many=True)
        form = Amish_Form(request.POST)
        if form.is_valid():
            tname = form.cleaned_data['name']
            tmail = form.cleaned_data['mail']
            tcontact = form.cleaned_data['contact']
            tcity = form.cleaned_data['city']
            tcollege = form.cleaned_data['college']
            idnum = "AXIS16AMI" + str(1000 + AmishRegistrations.objects.count())
            regi = AmishRegistrations(name=tname, mail=tmail, city=tcity, college=tcollege, contact=tcontact,
                                      idnum=idnum)
            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 GUEST LECTURE BY AMISH TRIPATHI. " \
                      "<br>Your event registration id" \
                      " is <b>" + idnum + "</b> . <br>Collect your pass at the Student's Activity Centre, VNIT Nagpur from 4pm to 9pm. <br> Please bring a snapshot of this mail and identity proof while collecting the pass. <br>For more details contact on these number : 7875352622.<br> " \
                                          "<br>Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[tmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            regi.save()
            s = "success"
            return Response(s)
        else:
            s = "error"
            return Response(s)


class FeedList(APIView):

    def get(self, request):
        regs = FeedBackFromAndroid.objects.all()
        serializer = FeedSerializers(regs, many=True)
        return Response(serializer.data)

    def post(self, request):
        regs = FeedBackFromAndroid.objects.all()
        serializer = FeedSerializers(regs,  many=True)
        form = Feed_form(request.POST)
        if form.is_valid():
            tname = request.POST['name']
            tmail = request.POST['mail']
            tcontact = request.POST['contact']
            tmsg = request.POST['msg']
            regi = FeedBackFromAndroid(name=tname, mail=tmail, contact=tcontact, msg=tmsg)
            regi.save()
            return Response(serializer.data)
        else:
            return Response("error.")


class Notifs(APIView):

    def get(self, request):
       regs = NotifsAndroid.objects.all()
       serializer = NotifsSerializers(regs, many=True)
       a = NotifsAndroid.objects.order_by('-id')[0]
       title = a.title
       msg = a.msg
       return Response({'title': title, 'msg': msg})

    def post(self, request):
        regs = NotifsAndroid.objects.all()
        serializer = NotifsSerializers(regs,  many=True)
        title = request.POST['title']
        msg = request.POST['msg']
        regi = NotifsAndroid(title=title, msg=msg)
        regi.save()
        return Response(serializer.data)




