from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from .forms import Robowars_Form, Mecha_Form, Sky_Form, Crepido_Form, Para_Form, Turboflux_Form, Animazione_Form, \
    Cryptocrux_Form, Posterolic_Form, Wall_Form, Boss_Form, Freako_Form, Counter_Form, NFS_Form, Fifa_Form, Techno_Form, \
    FeedForm, Autobot_Form, Mobile_Form, Android_Form, Aquahunt_Form, Baker_Form, SelfBal_Form, Manualrobo_Form, \
    Electro_Form, Ornitho_Form, Kartavya_Form,  Architech_Form,  Designo_Form, Photoscope_Form, Brain_Form, Coll_Form, \
    Laser_Form
from .models import RobowarsRegistration, MechaRegistration, SkyRegistration, CrepidoRegistration, ParaRegistration, \
    TurbofluxRegistration, AnimazioneRegistration, CryptocruxRegistration, PosterolicRegistration, \
    WallstreetRegistration, WhosTheBossRegistration, FreakoRegistration, CounterStrikeRegistration, NFSRegistration, \
    FifaRegistration, TechnoDocxRegistration, FeedbackMessage, AutobotRegistration, MobileRegistration, \
    AndroidRegistration, AquahuntRegistration, BakerRegistration, SelfBalRegistration, ManualroboRegistration, \
    ElectroRegistration, OrnithoRegistration, KartavyaRegistration, ArchitechRegistration, DesignoRegistration, \
    PhotoscopeRegistration, BrainRegistration, CollRegistration, LaserRegistration
from django.core.mail import EmailMessage


def index(request):
    return render(request, "main/index.html")


def amish(request):
    return render(request, "main/attr/amish.html")


def inaug(request):
    return render(request, "main/attr/Inaug.html")


def afishal(request):
    return render(request, "main/attr/afishal.html")


def google(request):
    return render(request, "main/google6f282865ac0ed8e0.html")


def sitemap(request):
    return render(request, "main/sitemap.xml")


def first(request):
    return render(request, "main/first.html")


def events(request):
    return render(request, "main/events.html")


def contact(request):
    return render(request, "main/contact.html")


def workshops(request):
    return render(request, "main/workshops.html")


def android(request):
    return render(request, "main/workshops/android.html")


def ornitho(request):
    return render(request, "main/workshops/ornitho.html")


def mobile(request):
    return render(request, "main/workshops/mobile.html")


def selfbal(request):
    return render(request, "main/workshops/selfbal.html")


def attractions(request):
    return render(request, "main/attractions.html")


def socialini(request):
    return render(request, "main/socini.html")


def teamct(request):
    return render(request, "main/team/teamct.html")


def core(request):
    return render(request, "main/team/core.html")


def profs(request):
    return render(request, "main/team/profs.html")


def publicity(request):
    return render(request, "main/team/publicity.html")


def webt(request):
    return render(request, "main/team/webteam.html")


def sponsors(request):
    return render(request, "main/sponsors.html")


def colors(request):
    return render(request, "main/socini/colors.html")


def envday(request):
    return render(request, "main/socini/envday.html")


def nosmoke(request):
    return render(request, "main/socini/nosmoke.html")


def blood(request):
    return render(request, "main/socini/blood.html")


def mad(request):
    return render(request, "main/socini/mad.html")


def robowars(request):
    return render(request, "main/events/anr/robowars.html")


def aquahunt(request):
    return render(request, "main/events/anr/aquahunt.html")


def autobot(request):
    return render(request, "main/events/anr/autobot.html")


def robocup(request):
    return render(request, "main/events/anr/robo-saviour.html")


def sky(request):
    return render(request, "main/events/cnd/aquaskylark.html")


def crepido(request):
    return render(request, "main/events/cnd/crepido.html")


def mechatryst(request):
    return render(request, "main/events/anr/mechatryst.html")


def devise(request):
    return render(request, "main/events/cnd/devise.html")


def paradiegma(request):
    return render(request, "main/events/cnd/paradiegma.html")


def turbo(request):
    return render(request, "main/events/cnd/turboflux.html")


def anim(request):
    return render(request, "main/events/sne/animazion.html")


def crypto(request):
    return render(request, "main/events/sne/cryptocrux.html")


def inso(request):
    return render(request, "main/events/sne/insomnia.html")


def poster(request):
    return render(request, "main/events/sne/posterolic.html")


def js(request):
    return render(request, "main/events/se/js.html")


def dexter(request):
    return render(request, "main/events/se/dexter.html")


def wall(request):
    return render(request, "main/events/mno/wallstreet.html")


def boss(request):
    return render(request, "main/events/mno/whosdboss.html")


def baker(request):
    return render(request, "main/events/mno/221baker.html")


def freako(request):
    return render(request, "main/events/mno/freakomatrix.html")


def games(request):
    return render(request, "main/events/mno/gamesutra.html")


def informals(request):
    return render(request, "main/events/mno/informals.html")


def coll(request):
    return render(request, "main/events/xxx/coll.html")


def kart(request):
    return render(request, "main/events/xxx/kart.html")


def techno(request):
    return render(request, "main/events/xxx/technodocx.html")


def brain(request):
    return render(request, "main/events/new/brain.html")


def laser(request):
    return render(request, "main/events/new/laser.html")


def minute(request):
    return render(request, "main/events/new/minute.html")


def robowarsreg(request):
    if request.POST:
        form = Robowars_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            finame = form.cleaned_data['finame']
            ficollege = form.cleaned_data['ficollege']
            fimail = form.cleaned_data['fimail']
            ficon = form.cleaned_data['ficon']
            ficity = form.cleaned_data['ficity']
            siname = form.cleaned_data['siname']
            sicollege = form.cleaned_data['sicollege']
            simail = form.cleaned_data['simail']
            sicon = form.cleaned_data['sicon']
            sicity = form.cleaned_data['sicity']
            regid = "AXIS16ROBO" + str(1000 + RobowarsRegistration.objects.count())
            regi = RobowarsRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        finame=finame, ficollege=ficollege, fimail=fimail, ficon=ficon, ficity=ficity,
                                        siname=siname, sicollege=sicollege, simail=simail, sicon=sicon, sicity=sicity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT ROBOWARS. " \
                      "<br>Your event registration id" \
                      " is <b>"+regid+"</b> . <br>Contact the respective event manager for confirmation and more " \
                      "queries. <br>Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)

            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Robowars_Form()
        context = {'form': form}
        return render_to_response('main/events/anr/robowars.html', context)


def mechareg(request):
    if request.POST:
        form = Mecha_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            finame = form.cleaned_data['finame']
            ficollege = form.cleaned_data['ficollege']
            fimail = form.cleaned_data['fimail']
            ficon = form.cleaned_data['ficon']
            ficity = form.cleaned_data['ficity']
            regid = "AXIS16MECHA" + str(1000 + MechaRegistration.objects.count())
            regi = MechaRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        finame=finame, ficollege=ficollege, fimail=fimail, ficon=ficon, ficity=ficity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT MECHATRYST. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Mecha_Form()
        context = {'form': form}
        return render_to_response('main/events/anr/mechatryst.html', context)


def autobotreg(request):
    if request.POST:
        form = Autobot_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            finame = form.cleaned_data['finame']
            ficollege = form.cleaned_data['ficollege']
            fimail = form.cleaned_data['fimail']
            ficon = form.cleaned_data['ficon']
            ficity = form.cleaned_data['ficity']
            regid = "AXIS16AUTO" + str(1000 + AutobotRegistration.objects.count())
            regi = AutobotRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        finame=finame, ficollege=ficollege, fimail=fimail, ficon=ficon, ficity=ficity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT AUTOBOT. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries. <br>Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Autobot_Form()
        context = {'form': form}
        return render_to_response('main/events/anr/autobot.html', context)


def skyreg(request):
    if request.POST:
        form = Sky_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            regid = "AXIS16SKY" + str(1000 + SkyRegistration.objects.count())
            regi = SkyRegistration(team=team,
                                   fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                   sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                   idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT AQUA SKYLARK. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Sky_Form()
        context = {'form': form}
        return render_to_response('main/events/cnd/aquaskylark.html', context)


def aquahuntreg(request):
    if request.POST:
        form = Aquahunt_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            finame = form.cleaned_data['foname']
            ficollege = form.cleaned_data['focollege']
            fimail = form.cleaned_data['fomail']
            ficon = form.cleaned_data['focon']
            ficity = form.cleaned_data['focity']
            regid = "AXIS16AQU" + str(1000 + AquahuntRegistration.objects.count())
            regi = AquahuntRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        finame=finame, ficollege=ficollege, fimail=fimail, ficon=ficon, ficity=ficity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT AQUAHUNT. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send()
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Aquahunt_Form()
        context = {'form': form}
        return render_to_response('main/events/anr/aquahunt.html', context)


def crepidoreg(request):
    if request.POST:
        form = Crepido_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            regid = "AXIS16CREP" + str(1000 + CrepidoRegistration.objects.count())
            regi = CrepidoRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT CREPIDO. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Crepido_Form()
        context = {'form': form}
        return render_to_response('main/events/cnd/crepido.html', context)


def parareg(request):
    if request.POST:
        form = Para_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            regid = "AXIS16PARA" + str(1000 + ParaRegistration.objects.count())
            regi = ParaRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT PARADEIGMA. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Para_Form()
        context = {'form': form}
        return render_to_response('main/events/cnd/paradiegma.html', context)


def turboreg(request):
    if request.POST:
        form = Turboflux_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            regid = "AXIS16TURBO" + str(1000 + TurbofluxRegistration.objects.count())
            regi = TurbofluxRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                         idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT TURBOFLUX. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Para_Form()
        context = {'form': form}
        return render_to_response('main/events/cnd/turboflux.html', context)


def animreg(request):
    if request.POST:
        form = Animazione_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            regid = "AXIS16ANIM" + str(1000 + AnimazioneRegistration.objects.count())
            regi = AnimazioneRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                          idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT ANIMAZIONE. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Animazione_Form()
        context = {'form': form}
        return render_to_response('main/events/sne/animazion.html', context)


def cryptoreg(request):
    if request.POST:
        form = Cryptocrux_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            regid = "AXIS16CRYPT" + str(1000 + CryptocruxRegistration.objects.count())
            regi = CryptocruxRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                          idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT CRYPTOCRUX. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Cryptocrux_Form()
        context = {'form': form}
        return render_to_response('main/events/sne/cryptocrux.html', context)


def posterreg(request):
    if request.POST:
        form = Posterolic_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            regid = "AXIS16POSTER" + str(1000 + PosterolicRegistration.objects.count())
            regi = PosterolicRegistration(fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                          idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT POSTEROLIC. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Posterolic_Form()
        context = {'form': form}
        return render_to_response('main/events/sne/posterolic.html', context)


def wallreg(request):
    if request.POST:
        form = Wall_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            regid = "AXIS16WALL" + str(1000 + WallstreetRegistration.objects.count())
            regi = WallstreetRegistration(fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                          idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT WALLSTREET. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Wall_Form()
        context = {'form': form}
        return render_to_response('main/events/mno/wallstreet.html', context)


def bossreg(request):
    if request.POST:
        form = Boss_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            regid = "AXIS16BOSS" + str(1000 + WhosTheBossRegistration.objects.count())
            regi = WhosTheBossRegistration(fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                           idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT WHO'S THE BOSS. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Boss_Form()
        context = {'form': form}
        return render_to_response('main/events/mno/whosdboss.html', context)


def freakoreg(request):
    if request.POST:
        form = Freako_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            regid = "AXIS16FREAKO" + str(1000 + FreakoRegistration.objects.count())
            regi = FreakoRegistration(team=team,
                                     fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                     sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                      idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT FREAK O MATIX. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Freako_Form()
        context = {'form': form}
        return render_to_response('main/events/mno/freakomatrix.html', context)


def csreg(request):
    if request.POST:
        form = Counter_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            finame = form.cleaned_data['finame']
            ficollege = form.cleaned_data['ficollege']
            fimail = form.cleaned_data['fimail']
            ficon = form.cleaned_data['ficon']
            ficity = form.cleaned_data['ficity']
            regid = "AXIS16CS" + str(1000 + CounterStrikeRegistration.objects.count())
            regi = CounterStrikeRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        finame=finame, ficollege=ficollege, fimail=fimail, ficon=ficon, ficity=ficity,
                                             idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT GAMESUTRA - COUNTER STRIKE. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)

            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Counter_Form()
        context = {'form': form}
        return render_to_response('main/events/mno/gamesutra.html', context)


def nfsreg(request):
    if request.POST:
        form = NFS_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            regid = "AXIS16NFS" + str(1000 + NFSRegistration.objects.count())
            regi = NFSRegistration(fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                   idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT GAMESUTRA- NEED FOR SPEED. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = NFS_Form()
        context = {'form': form}
        return render_to_response('main/events/mno/gamesutra.html', context)


def fifareg(request):
    if request.POST:
        form = Fifa_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            regid = "AXIS16FIFA" + str(1000 + FifaRegistration.objects.count())
            regi = FifaRegistration(fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                    idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT GAMESUTRA - FIFA. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                            'the form is not valid. Kindly refill the form and submit again." ))' \
                            '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Fifa_Form()
        context = {'form': form}
        return render_to_response('main/events/mno/gamesutra.html', context)


def technoreg(request):
    if request.POST:
        form = Techno_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            regid = "AXIS16TECHNO" + str(1000 + TechnoDocxRegistration.objects.count())
            regi = TechnoDocxRegistration(team=team,
                                     fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                     sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                          idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT TECHNO.DOCX. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Techno_Form()
        context = {'form': form}
        return render_to_response('main/events/xxx/technodocx.html', context)


def mobilereg(request):
    if request.POST:
        form = Mobile_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            finame = form.cleaned_data['finame']
            ficollege = form.cleaned_data['ficollege']
            fimail = form.cleaned_data['fimail']
            ficon = form.cleaned_data['ficon']
            ficity = form.cleaned_data['ficity']
            regid = "AXIS16WMOBO" + str(1000 + MobileRegistration.objects.count())
            regi = MobileRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        finame=finame, ficollege=ficollege, fimail=fimail, ficon=ficon, ficity=ficity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 WORKSHOP REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 WORKSHOP on MOBILE BUILDING. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Mobile_Form()
        context = {'form': form}
        return render_to_response('main/workshops/mobile.html', context)


def selfbalreg(request):
    if request.POST:
        form = SelfBal_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            finame = form.cleaned_data['finame']
            ficollege = form.cleaned_data['ficollege']
            fimail = form.cleaned_data['fimail']
            ficon = form.cleaned_data['ficon']
            ficity = form.cleaned_data['ficity']
            regid = "AXIS16WSBRO" + str(1000 + SelfBalRegistration.objects.count())
            regi = SelfBalRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        finame=finame, ficollege=ficollege, fimail=fimail, ficon=ficon, ficity=ficity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 WORKSHOP REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 WORKSHOP on SELF BALANCING ROBOT. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = SelfBal_Form()
        context = {'form': form}
        return render_to_response('main/workshops/selfbal.html', context)


def ornithoreg(request):
    if request.POST:
        form = Ornitho_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            regid = "AXIS16WORN" + str(1000 + OrnithoRegistration.objects.count())
            regi = OrnithoRegistration(
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 WORKSHOP REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 WORKSHOP on ORNITHOCOPTER. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Ornitho_Form()
        context = {'form': form}
        return render_to_response('main/workshops/ornitho.html', context)


def androidreg(request):
    if request.POST:
        form = Android_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            regid = "AXIS16WANDRO" + str(1000 + AndroidRegistration.objects.count())
            regi = AndroidRegistration(fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                       idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 WORKSHOP on ANDROID APP " \
                      "DEVELOPMENT. <br> Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                            'the form is not valid. Kindly refill the form and submit again." ))' \
                            '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Android_Form()
        context = {'form': form}
        return render_to_response('main/workshops/android.html', context)


def bakerreg(request):
    if request.POST:
        form = Baker_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            regid = "AXIS16BAK" + str(1000 + BakerRegistration.objects.count())
            regi = BakerRegistration(fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                     idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 Event " \
                      "221B BAKER STREET <br> Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                            'the form is not valid. Kindly refill the form and submit again." ))' \
                            '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Baker_Form()
        context = {'form': form}
        return render_to_response('main/events/mno/221baker.html', context)


def manualroboreg(request):
    if request.POST:
        form = Manualrobo_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            finame = form.cleaned_data['finame']
            ficollege = form.cleaned_data['ficollege']
            fimail = form.cleaned_data['fimail']
            ficon = form.cleaned_data['ficon']
            ficity = form.cleaned_data['ficity']
            regid = "AXIS16MANRO" + str(1000 + ManualroboRegistration.objects.count())
            regi = ManualroboRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        finame=finame, ficollege=ficollege, fimail=fimail, ficon=ficon, ficity=ficity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT ROBO SAVIOUR. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Manualrobo_Form()
        context = {'form': form}
        return render_to_response('main/events/anr/robo-saviour.html', context)


def minutereg(request):
    if request.POST:
        form = Electro_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            regid = "AXIS16ELEC" + str(1000 + ElectroRegistration.objects.count())
            regi = ElectroRegistration(
                                   fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                   idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT ELECTROBLITZ. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Electro_Form()
        context = {'form': form}
        return render_to_response('main/events/new/minute.html', context)


def kartreg(request):
    if request.POST:
        form = Kartavya_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            regid = "AXIS16KAR" + str(1000 + KartavyaRegistration.objects.count())
            regi = KartavyaRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                         idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT KARTAVYA. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Kartavya_Form()
        context = {'form': form}
        return render_to_response('main/events/xxx/kart.html', context)


def architechreg(request):
    if request.POST:
        form = Architech_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            regid = "AXIS16ARCHT" + str(1000 + ArchitechRegistration.objects.count())
            regi = ArchitechRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                         idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT DEVISE-ARCHITECH. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Kartavya_Form()
        context = {'form': form}
        return render_to_response('main/events/cnd/devise.html', context)


def desigreg(request):
    if request.POST:
        form = Designo_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            regid = "AXIS16ARCHD" + str(1000 + DesignoRegistration.objects.count())
            regi = DesignoRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                         idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT DEVISE-DESIGNO. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Designo_Form
        context = {'form': form}
        return render_to_response('main/events/cnd/devise.html', context)


def photoscreg(request):
    if request.POST:
        form = Photoscope_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            regid = "AXIS16ARCHP" + str(1000 + PhotoscopeRegistration.objects.count())
            regi = PhotoscopeRegistration(
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                         idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT DEVISE-PHOTOSCOPE. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Photoscope_Form
        context = {'form': form}
        return render_to_response('main/events/cnd/devise.html', context)


def brainreg(request):
    if request.POST:
        form = Brain_Form(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            regid = "AXIS16NBR" + str(1000 + BrainRegistration.objects.count())
            regi = BrainRegistration(fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                         idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT BRAINSTORM. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries.<br> Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)
            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Brain_Form
        context = {'form': form}
        return render_to_response('main/events/new/brain.html', context)


def collreg(request):
    if request.POST:
        form = Coll_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            finame = form.cleaned_data['finame']
            ficollege = form.cleaned_data['ficollege']
            fimail = form.cleaned_data['fimail']
            ficon = form.cleaned_data['ficon']
            ficity = form.cleaned_data['ficity']
            siname = form.cleaned_data['siname']
            sicollege = form.cleaned_data['sicollege']
            simail = form.cleaned_data['simail']
            sicon = form.cleaned_data['sicon']
            sicity = form.cleaned_data['sicity']
            regid = "AXIS16COLL" + str(1000 + CollRegistration.objects.count())
            regi = CollRegistration(team=team,
                                        fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                        sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                        tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                        foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                        finame=finame, ficollege=ficollege, fimail=fimail, ficon=ficon, ficity=ficity,
                                        siname=siname, sicollege=sicollege, simail=simail, sicon=sicon, sicity=sicity,
                                        idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT COLL-IN-COLL. " \
                      "<br>Your event registration id" \
                      " is <b>"+regid+"</b> . <br>Contact the respective event manager for confirmation and more " \
                      "queries. <br>Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)

            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Coll_Form()
        context = {'form': form}
        return render_to_response('main/events/xxx/coll.html', context)


def laserreg(request):
    if request.POST:
        form = Laser_Form(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            fname = form.cleaned_data['fname']
            fcollege = form.cleaned_data['fcollege']
            fmail = form.cleaned_data['fmail']
            fcon = form.cleaned_data['fcon']
            fcity = form.cleaned_data['fcity']
            sname = form.cleaned_data['sname']
            scollege = form.cleaned_data['scollege']
            smail = form.cleaned_data['smail']
            scon = form.cleaned_data['scon']
            scity = form.cleaned_data['scity']
            tname = form.cleaned_data['tname']
            tcollege = form.cleaned_data['tcollege']
            tmail = form.cleaned_data['tmail']
            tcon = form.cleaned_data['tcon']
            tcity = form.cleaned_data['tcity']
            foname = form.cleaned_data['foname']
            focollege = form.cleaned_data['focollege']
            fomail = form.cleaned_data['fomail']
            focon = form.cleaned_data['focon']
            focity = form.cleaned_data['focity']
            finame = form.cleaned_data['finame']
            ficollege = form.cleaned_data['ficollege']
            fimail = form.cleaned_data['fimail']
            ficon = form.cleaned_data['ficon']
            ficity = form.cleaned_data['ficity']
            regid = "AXIS16LAS" + str(1000 + LaserRegistration.objects.count())
            regi = LaserRegistration(team=team,
                                     fname=fname, fcollege=fcollege, fmail=fmail, fcon=fcon, fcity=fcity,
                                     sname=sname, scollege=scollege, smail=smail, scon=scon, scity=scity,
                                     tname=tname, tcollege=tcollege, tmail=tmail, tcon=tcon, tcity=tcity,
                                     foname=foname, focollege=focollege, fomail=fomail, focon=focon, focity=focity,
                                     finame=finame, ficollege=ficollege, fimail=fimail, ficon=ficon, ficity=ficity,
                                     idnum=regid)
            regi.save()

            subject = "AXIS'16 EVENT REGISTRATION"
            message = "Congratulations !<br> You have successfully registered for AXIS'16 EVENT LASER LITT. " \
                      "<br>Your event registration id" \
                      " is <b>" + regid + "</b> . <br>Contact the respective event manager for confirmation and more " \
                                          "queries. <br>Please carry your college id during the event."
            email = EmailMessage(subject, message, to=[fmail])
            email.content_subtype = "html"
            email.send(fail_silently=False)

            return_script = '<script type="text/javascript">if (!alert("Congratulations!!! Registration Completed ' \
                            'Successfully. Registration details are mailed to your email address." ))' \
                            '{window.opener.location.reload(false);};window.close();</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Some information in the form might be repeated and ' \
                     'the form is not valid. Kindly refill the form and submit again." ))' \
                     '{location.reload(false);}</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = Laser_Form()
        context = {'form': form}
        return render_to_response('main/events/new/laser.html', context)


def feed(request):
    if request.POST:
        form = FeedForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            con = form.cleaned_data['con']
            msg = form.cleaned_data['msg']
            feed = FeedbackMessage(name=name, mail=mail, con=con, msg=msg)
            feed.save()

            return_script = '<script type="text/javascript">if (!alert("Your message ' \
                            'has been sent successfully" ))' \
                            '{window.location="first.html";};</script>'
            return HttpResponse(return_script)
        else:
            script = '<script type="text/javascript">if (!alert("Your message was not sent. ' \
                            'There is some error in  form." ))' \
                            '{window.location="contact.html";};</script>'
            # return render_to_response('main/events/mno/gamesutra.html', {'form': form})
            return HttpResponse(script)
    else:
        form = FeedForm()
        context = {'form': form}
        return render_to_response('main/contact.html', context)
