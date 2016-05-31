# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from apps.recommender.models import Movie, Person
from settings import db


class MovieDetailView(DetailView):

    model = Movie


class MovieListView(ListView):

    model = Movie


class PersonDetailView(DetailView):
    model = Person


class PersonListView(ListView):
    model = Person


def index(request):
    return render_to_response('recommender/index.html', {},
                              context_instance=RequestContext(request))
