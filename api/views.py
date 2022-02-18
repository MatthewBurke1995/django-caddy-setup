from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import Episode
from django.template import loader


def rss(request):
    episodes = Episode.objects.order_by("-pub_date")
    template = loader.get_template("api/podcast.rss")
    context = {
        "episodes": episodes,
    }
    return HttpResponse(template.render(context, request))


