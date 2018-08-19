from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets, renderers, status
from rest_framework.response import Response

from peach.apps.university.models import Metadata
from peach.apps.university.serializers.metadata import MetadataSerializer


class MetadataViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer
    renderer_classes = (renderers.JSONRenderer,)

    def list(self, request, *args, **kwargs):
        response = super(MetadataViewSet, self).list(request, *args, **kwargs)
        return response

    # def retrieve(self, request, *args, **kwargs):
    #     response = super(AssignmentViewSet, self).retrieve(request, *args, **kwargs)
    #     if request.accepted_renderer.format == 'html':
    #         return Response({'assignment': response.data}, template_name='assignment/get.html')
    #     return response
    #
    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         instance = self.get_object()
    #         instance.delete()
    #     except Http404:
    #         pass
    #     return HttpResponseRedirect(reverse("assignment-list"))
    #
    # def create(self, request, *args, **kwargs):
    #     serializer = AssignmentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         instance = serializer.save()
    #         return HttpResponseRedirect(redirect_to=reverse('assignment-detail', args=(instance.id, )))
    #     add_serializer_error_to_messages(request, serializer)
    #     return HttpResponseRedirect(reverse("assignment-new"))
    #
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = AssignmentSerializer(data=request.data, instance=instance)
    #     if serializer.is_valid():
    #         instance = serializer.save()
    #         return HttpResponseRedirect(redirect_to=reverse('assignment-detail', args=(instance.id, )))
    #     add_serializer_error_to_messages(request, serializer)
    #     return HttpResponseRedirect(reverse("assignment-edit"))
