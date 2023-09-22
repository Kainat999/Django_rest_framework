from rest_framework import serializers
from .models import Todo
import re

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
      #  fields = '__all__'
        fields = ['todo_title', 'todo_description', 'is_done']
        # exclude = ['created_at', 'updated_at', 'u_id']


        def velidate(self, validated_data):
            if validated_data.get('todo_title'):
                
                todo_title = validated_data['todo_title']  
                regex = re.compile(r'[~!@#$%^&*()_+|}{\][?><,./]')
                
                if not regex.search(todo_title) == None:
                  raise serializers.ValidationError('Todo title cannot contain specail charactors!')
            return validated_data     


