from django.shortcuts import render

from participant.forms import TestForm

def index(request):
    return render(request, 'participant/index.html', {'form': TestForm})


def test_score_page(request):
    return render(request, 'participant/test_score.html')