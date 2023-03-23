from rest_framework.response import Response
from rest_framework.decorators import api_view

from heros.models import Hero
from heros.serializers import HeroSerializer

# @api_view(['GET'])
# def api_home(request):
#     instance = Hero.objects.all().order_by('?').first()
#     data = {}
#     if instance:
#         data = HeroSerializer(instance).data
#     return Response(data)

@api_view(['POST'])
def api_home(request):
    serializer = HeroSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=400)