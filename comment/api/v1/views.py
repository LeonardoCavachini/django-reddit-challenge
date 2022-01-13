"""
API V1: Comment Views
"""
###
# Libraries
###

from rest_framework import (
    permissions,
    viewsets,
)

from . import serializers
from comment.models import Comment

###
# Filters
###


###
# Viewsets
###
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

