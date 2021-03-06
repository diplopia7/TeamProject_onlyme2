import requests
from django.shortcuts import render


# Create your views here.

def game_info(request):
    return render(request, 'game_info.html')


def main_menu(request):
    return render(request, 'main_menu.html')


def character(request):
    returnPage = 'character.html'

    command = 0
    power = 0
    inteli = 0
    politics = 0
    innertrait = '없음'
    fighttrait = '없음'
    skill = '없음'
    status = '부장'
    hp = 100

    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        form = request.POST.dict()
        request.session['command'] = form['command']
        request.session['power'] = form['power']
        request.session['inteli']=form['inteli']
        request.session['politics']=form['politics']
        request.session['innertrait']=form['innertrait']
        request.session['fighttrait']=form['fighttrait']
        request.session['skill']=form['skill']
        request.session['portrait']=form['portrait']
        request.session['status']=status
        request.session['hp']=hp

        print(form)
        returnPage='characterok.html'

        return render(request, returnPage)

    context = {'command': command, 'power': power, 'inteli': inteli, 'politics': politics, 'innertrait': innertrait, 'fighttrait': fighttrait, 'skill': skill,
               'status':status,'hp':hp}

    return render(request, returnPage,context)


def story1(request):
    return render(request, 'story1.html')


def story2(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        form = request.POST.dict()
        request.session['dicenumber'] = form['dicenumber']
        request.session['success'] = form['success']
        request.session['command'] = form['command']
        request.session['power'] = form['power']
        request.session['inteli'] = form['inteli']
        request.session['politics'] = form['politics']
        request.session['innertrait'] = form['innertrait']
        request.session['fighttrait'] = form['fighttrait']
        request.session['skill'] = form['skill']
        request.session['status']=form['status']

        print(form)
        returnPage = 'story2ok.html'

        return render(request, returnPage)
    return render(request, 'story2.html')


def story3(request):
    return render(request, 'story3.html')


def 내정(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        form = request.POST.dict()
        request.session['gold']=form['goldinput']
        request.session['food']=form['foodinput']
        request.session['army']=form['armyinput']
        request.session['officer']=form['officerinput']
        request.session['officer']=form['officerinput']
        request.session['hp']=form['hpinput']
        request.session['item']=form['iteminput1']
        request.session['itemstat1']=form['iteminput2']
        request.session['itemstat2']=form['iteminput3']
        request.session['itemfullname']=form['itemfullname']

        request.session['command'] = form['command']
        request.session['power'] = form['power']
        request.session['inteli'] = form['inteli']
        request.session['politics'] = form['politics']
        request.session['innertrait'] = form['innertrait']
        request.session['fighttrait'] = form['fighttrait']
        request.session['skill'] = form['skill']

        print(form)
        returnPage = '내정ok.html'

        return render(request, returnPage)
    return render(request, '내정.html')


def 전투(request):
    return render(request, '전투.html')


def how_to_fight(request):
    return render(request,'how_to_fight.html')