from rest_framework.response import Response
from rest_framework.decorators import api_view

from heros.models import Hero
from heros.serializers import HeroSerializer

# @api_view(['GET'])
# def api_home(request):
#     obj = Hero.objects.all().order_by('?').first()
#     data = {}
#     if obj:
#         data = HeroSerializer(obj).data
#     return Response(data)

@api_view(['POST'])
def api_home(request):
    serializer = HeroSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # obj = serializer.save()
        # print(obj)
        return Response(serializer.data)
    return Response({'invalid': 'not good data'}, status=400)