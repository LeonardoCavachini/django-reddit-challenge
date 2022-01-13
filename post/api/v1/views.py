"""
API V1: Comment Views
"""
###
# Libraries
###
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import (
    permissions,
    viewsets,
)

from . import serializers
from post.models import Post
#from comment.models import Comment

###
# Filters
###


###
# Viewsets
###
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        post = self.get_object()
        serializer = serializers.PostSerializer(post.comment.all(), many=True)
        
        return Response( serializer.data)

class PostTopicViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(topic__URLName=self.kwargs['topic_URLName'])