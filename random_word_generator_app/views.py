# Create your views here.
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 1
    context = {
        'attempt_count': request.session['counter'],
        'random_word': get_random_string(length=14),
    }
    return render(request, 'index.html', context)


# BUGGY B/C IT DOESNT INCREMENT ON REFRESH LIKE PROMPT ASKS

def random_word(request):
    request.session['counter'] += 1
    return redirect('/')

def reset(request):
    request.session['counter'] = 0
    return redirect('/random_word')
