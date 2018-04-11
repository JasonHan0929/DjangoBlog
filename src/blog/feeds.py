from django.contrib.syndication.views import Feed

from .models import Post

TITLE = 'Django Blog'
DESCRIPTION = 'A personal blog made by django'

class AllPostsRssFeed(Feed):
    title = TITLE
    description = DESCRIPTION
    link = '/'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body