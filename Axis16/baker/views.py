from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from main.models import BakerRegistration
from .models import Baker_Questions
from django.core.checks.security import csrf
from django.template import RequestContext
from .forms import LoginForm
import datetime

# Create your views here.


def logindisp(request):
    return render(request, "baker/blogin.html")


def login2(request):
    if request.POST:
        name = request.POST['fname']
        mail = request.POST['fmail']
        idn = request.POST['idnum']
        if BakerRegistration.objects.filter(fname=name, fmail=mail, idnum=idn).exists():
            succ = True
            level = BakerRegistration.objects.get(idnum=idn).level
            if level < 48:
                request.session['name'] = name
                request.session['idnum'] = idn
                request.session['level'] = level
                request.session['res'] = True
                response = render_to_response('baker/welcome.html', {'name': name, 'level': level, 'succ': succ})
                return response
            else:
                return HttpResponseRedirect("/")

        else:
            succ = False
            # return HttpResponse("wrong")
            return render(request, "baker/blogin.html", context={'succ': succ})

    else:
        return HttpResponse("Go back and reload the page.")


def ques(request):
    # name = request.COOKIES['name']
    if "name" in request.session:
        name = request.session['name']
        level = request.session['level']
        res = request.session['res']
        if level < 48:
            quesn = Baker_Questions.objects.get(level=level)
            users = BakerRegistration.objects.all()
            # users = users.extra(order_by='level')
            return render(request, "baker/ques.html", context={'name': name, 'level': level,
                                                               'quesn': quesn, 'res': res, 'users': users})
        else:
            del request.session['name']
            del request.session['level']
            del request.session['res']
            del request.session['idnum']
            return HttpResponseRedirect("/")

    else:
        return HttpResponse("no session")


def check(request):
    if request.POST:
        level = request.session['level']
        ans = Baker_Questions.objects.get(level=level).answer
        pans = request.POST['answer']
        if str(ans.lower()) == str(pans.lower()):
            name = request.session['name']
            idn = request.session['idnum']
            user = BakerRegistration.objects.get(fname=name, idnum=idn)
            user.level += 1
            user.lastSubmit = datetime.datetime.now()
            request.session['res'] = True
            request.session['level'] = user.level
            level = request.session['level']
            user.save()
            if level > 47:
                del request.session['name']
                del request.session['level']
                del request.session['idnum']
                del request.session['res']
                return HttpResponseRedirect("/")
            else:
                name = request.session['name']
                quesn = Baker_Questions.objects.get(level=user.level)
                users = BakerRegistration.objects.order_by('-level', 'lastSubmit')
                # users = users.extra(order_by='level')
                return render(request, "baker/ques.html", context={'level': level, 'quesn': quesn, 'users': users,
                                                                   'name': name})
        else:
            quesn = Baker_Questions.objects.get(level=level)
            request.session['res'] = False
            res = request.session['res']
            users = BakerRegistration.objects.order_by('-level')
            return render(request, "baker/ques.html", context={'level': level, 'quesn': quesn, 'res': res, 'users': users})
    else:
        return render(request, 'baker/ques.html')


def sofar(request):
    level = request.session['level']
    quesns = Baker_Questions.objects.order_by('level')[:int(level)]
    return render(request, "baker/sofar.html", context={'level': level, 'quesns': quesns})

