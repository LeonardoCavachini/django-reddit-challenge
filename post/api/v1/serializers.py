"""
API V1: Post Serializers
"""
###
# Libraries
###
from post.models import Post
from rest_framework import serializers
###
# Serializers
###
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'



