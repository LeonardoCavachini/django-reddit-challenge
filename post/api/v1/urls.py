"""
API V1: Topic Urls
"""
###
# Libraries
###
from django.urls.conf import path
from django.conf.urls import include
from rest_framework import routers
from post.api.v1 import views

router = routers.SimpleRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]