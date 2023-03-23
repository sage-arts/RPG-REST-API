from rest_framework import serializers
from .models import Hero

class HeroSerializer(serializers.ModelSerializer):
     buff = serializers.SerializerMethodField(read_only=True)
     class Meta:
          model = Hero
          fields = [
               'name',
               'description',
               'hp',
               'armor',
               'energy',
               'crit_hit',
               'buff'
          ]
     
     def get_buff(self, obj):
          if not hasattr(obj, 'id'):
               return None
          if not isinstance(obj, Hero):
               return None
          return obj.get_buff()
          # try:
          #      return obj.get_buff()
          # except:
          #      return None