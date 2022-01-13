"""
API V1: Accounts Views
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
from topic.models import Topic

###
# Filters
###


###
# Viewsets
###
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = serializers.TopicSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'URLName'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    