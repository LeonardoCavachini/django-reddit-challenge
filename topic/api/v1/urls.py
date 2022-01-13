"""
API V1: Topic Urls
"""
###
# Libraries
###
from urllib.request import urlretrieve
from django.urls.conf import path
from django.conf.urls import include,url
from rest_framework_nested import routers
from topic.api.v1.views import TopicViewSet
from post.api.v1.views import PostTopicViewSet
from comment.api.v1.views import CommentViewSet

router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet)

topicPost_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
topicPost_router.register(r'posts', PostTopicViewSet, basename='topic-post')

postComments_router = routers.NestedSimpleRouter(topicPost_router, r'posts', lookup='post')
postComments_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    url('', include(router.urls)),
    url('', include(topicPost_router.urls)),
    url('', include(postComments_router.urls)),
]
