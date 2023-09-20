from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
      #  fields = '__all__'
        # fields = ['todo_title']
        exclude = ['created_at', 'updated_at', 'u_id']