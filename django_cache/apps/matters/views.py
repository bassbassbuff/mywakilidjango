from django.shortcuts import render

from rest_framework import viewsets

from .serializers import MatterSerializer
from .models import Matter, File
from django.core.exceptions import PermissionDenied

class MatterViewSet(viewsets.ModelViewSet):
    serializer_class = MatterSerializer
    queryset = Matter.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    def perform_update(self, serializer):
        '''Update only matters created by user'''
        obj = self.get_object()

        if self.request.user != obj.created_by:
            raise PermissionDenied('Wrong object owner')

        serializer.save()