"""
API V1: Topic Serializers
"""
###
# Libraries
###
from topic.models import Topic
from rest_framework import serializers
###
# Serializers
###
class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'
        read_only_fields = ("author",)

