from django.urls import path, include

from . import views, feeds

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('post/<int:year>/<int:month>', views.ArchiveView.as_view(), name='archives'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='categories'),
    path('tag/<int:pk>', views.TagView.as_view(), name='tags'),
    path('all/rss', feeds.AllPostsRssFeed(), name='rss'),
    path('search/', include('haystack.urls'))
]


