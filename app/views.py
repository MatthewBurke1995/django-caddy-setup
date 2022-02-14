from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from .models import Post
from django.template import loader


def index(request):
    latest_post_list = Post.objects.order_by("-post_date")[:5]
    template = loader.get_template("app/index.html")
    context = {
        "latest_post_list": latest_post_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    template = loader.get_template("app/detail.html")
    tags = [str(t) for t in post.tag_set.all()]
    context = {"post": post, "tags": tags}
    return HttpResponse(template.render(context, request))
