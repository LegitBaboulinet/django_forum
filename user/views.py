from django.shortcuts import render
from django.http import HttpResponseRedirect
from hashlib import sha256

# Forms
from pip._internal import resolve

from .forms import loginForm

# Models
from .models import User


def login(req):
    print(req)
    if req.method == 'GET':
        return render(req, 'login.html')
    elif req.method == 'POST':
        form = loginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            qs = User.objects.filter(username=username)

            if qs.count() == 1:
                user = qs.first()

                password_salt = str.encode(password + user.salt)

                if sha256(password_salt).hexdigest() == user.hash:
                    req.session['username'] = user.username
                    return HttpResponseRedirect('/dashboard')
                else:
                    print('Mauvais nom d\'utilisateur ou mot de passe #3')
                    # TODO: Gérér le cas ou le mot de passe de ne correspond pas
            else:
                print('Mauvais nom d\'utilisateur ou mot de passe #2')
                # TODO: Gérer le cas ou l'utilisateur n'existe pas
        else:
            print('Mauvais nom d\'utilisateur ou mot de passe #1')
            # TODO: Gérer le cas ou le formulaire n'est pas valide


def dashboard(req):
    if 'username' in req.session:
        return render(req, 'dashboard.html', {'username': req.session['username']})
    else:
        return HttpResponseRedirect('/login')
