from django.shortcuts import render
from django.http import HttpResponseRedirect
from hashlib import sha256

import random, string

# Forms
from .forms import loginForm, signupForm

# Models
from .models import User


def login(req):
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


def signup(req):
    if req.method == 'GET':
        return render(req, 'signup.html')
    elif req.method == 'POST':
        form = signupForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            salt = generate_salt()
            hash = sha256(str.encode(password + salt)).hexdigest()

            user = User(username=username, email=email, hash=hash, salt=salt)
            user.save(force_update=False)

            if user.id is not None:
                req.session['username'] = username
                return HttpResponseRedirect('/dashboard')
            else:
                print('Save did not work')
                # TODO: Gérér le cas ou la sauvegarde ne se passe pas bien
        else:
            print('Formulaire invalide')
            # TODO: Gérér le cas ou le formulaire est invalide


def dashboard(req):
    if 'username' in req.session:
        return render(req, 'dashboard.html', {
            'username': req.session['username'],

        })
    else:
        return HttpResponseRedirect('/login')


# Functions
def generate_salt():
    return ''.join(
        [
            random.choice(string.ascii_letters + string.digits) for n in range(40)
        ]
    )
