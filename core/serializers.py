from rest_framework import serializers
from core.models import (Game, Map,)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        exclude = ('map',)
