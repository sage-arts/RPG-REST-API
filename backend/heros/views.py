from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404

from .models import Hero
from .serializers import HeroSerializer

class HeroDetailAPIView(generics.RetrieveAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    # lookup_field = pk

hero_detail_view = HeroDetailAPIView.as_view()

class HeroListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description')
        if description is None:
            description = name
        serializer.save(description=description)

hero_list_create_view = HeroListCreateAPIView.as_view()

class HeroUpdateAPIView(generics.UpdateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    # lookup_field = pk

    def perform_update(self, serializer):
        obj = serializer.save()
        if not obj.description:
            obj.description = obj.name

hero_update_view = HeroUpdateAPIView.as_view()

class HeroDeleteAPIView(generics.DestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def perform_destroy(self, obj):
        super().perform_destroy(obj)

hero_delete_view = HeroDeleteAPIView.as_view()

# @api_view(['GET', 'POST'])
# def hero_alt_view(request, pk=None):
#     if request.method == 'GET':
#         if pk is None:
#             queryset = Hero.objects.all()
#             serializer = HeroSerializer(queryset, many=True)
#             return Response(serializer.data)
#         obj = get_object_or_404(Hero, pk=pk)
#         serializer = HeroSerializer(obj)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = HeroSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             name = serializer.validated_data.get('name')
#             description = serializer.validated_data.get('description')
#             if description is None:
#                 description = name
#             serializer.save(description=description)
#             return Response(serializer.data)
#         return Response({'invalid': 'not good data'}, status=400)