from rest_framework import serializers
from .models import Comments

class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['id', 'car_id', 'comment_text', 'rating_score', 'comment_date', 'client_name']