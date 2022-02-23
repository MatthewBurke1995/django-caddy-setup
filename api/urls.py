from django.urls import path
from ninja import NinjaAPI
import youtube_dl
from .models import Episode
from django.utils import timezone
from django.contrib.syndication.views import Feed

api = NinjaAPI()

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '128',
    }],
    'outtmpl': 'data/static/podcasts/audio/%(id)s.mp3'
}

@api.post("/add")
def add(request, youtube_video: str):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(youtube_video, download=False)
        title = info_dict["title"]
        id_ = info_dict["id"]
        url = f'https://matthewburke.xyz/static/podcasts/audio/{id_}.mp3'
        description = info_dict["description"]

        episode = Episode(title=title, pub_date=timezone.now(), description=description, length=10000, url=url)
        ydl.download([youtube_video])
        episode.save()
    return {"result": info_dict}



class LatestPostFeed(Feed):
    title = 'Matts listening'
    link = '/feed.rss'
    description = 'what im listening to'

    def items(self):
        return Episode.objects.order_by("-pub_date")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_pubdate(self, item):
        return item.pub_date

    def item_link(self, item):
        return item.url

    def item_extra_kwargs(self, item):
        return {'pubDate':item.pub_date}
    
    def item_enclosure_url(self,item):
        return item.url

    def item_enclosure_length(self,item):
        return item.length

    def item_enclosure_mime_type(self):
        return "audio/mpeg"

urlpatterns = [
    path("", api.urls),
    path('feed.rss', LatestPostFeed(), name='post_feed'),
]
