from rest_framework import serializers
from .models import TodoDetails
from datetime import datetime

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoDetails
        fields = ('id', 'state', 'due_date', 'text')

    def validate_state(self, state):
        return state

    def validate_due_date(self, value):
        return value

    def validate_text(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Text length should be more than 10")
        return value