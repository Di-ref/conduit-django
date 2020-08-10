#from django.urls import path
from django.urls import include, path
#from django.conf.urls import url
#from django.conf.urls import include as includeurl
from rest_framework.routers import DefaultRouter
from .views import (ArticleViewSet,
                    CommentsListCreateAPIView,
                    CommentsDestroyAPIView,
                    ArticleFavoriteAPIView,
                    ArticlesFeedAPIView,
                    TagListAPIView,
                    )


router = DefaultRouter(trailing_slash=False)
router.register(r'articles', ArticleViewSet)

app_name = 'articles'

urlpatterns = [
    path('articles/feed/', ArticlesFeedAPIView.as_view()),
    path('articles/<slug:article_slug>/comments/', CommentsListCreateAPIView.as_view()),
    path('articles/<slug:article_slug>/comments/<comment_pk>)/', CommentsDestroyAPIView.as_view()),
    path('articles/<slug:article_slug>/favorite/',  ArticleFavoriteAPIView.as_view()),
    path('tags/', TagListAPIView.as_view()),
    path('', include(router.urls)),
    #url(r'^', includeurl(router.urls)),

]
