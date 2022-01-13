"""
API V1: Comment Serializers
"""
###
# Libraries
###
from comment.models import Comment
from rest_framework import serializers
###
# Serializers
###
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


