from django.shortcuts import render
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from rest_framework import status, renderers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Image
from .serializers import ImageSerializer
import urllib.request
from storage import settings
import os

# Create your views here.
class ImageList(APIView):
    '''Main page with all links to images.
      '''

    def get(self, request):
        image_list = Image.objects.all()
        serializer = ImageSerializer(image_list, many=True)
        return Response(serializer.data)

    def post(self, request):

        

        img_url = request.data['image_url']  
        img_id = request.data['id']      
        filename = img_url.split("/")[-1]
        path = settings.MEDIA_ROOT
        urllib.request.urlretrieve(img_url, path+filename)
        #request.data['download_url'] = f'http://{request.get_host()}/media/{filename}'
        request.data['download_url'] = f'http://{request.get_host()}/{img_id}/download'

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ImageDetails(APIView):

    def get_object(self, id):
        try:
            return Image.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        image = self.get_object(id)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def delete(self, request, id):
        image = self.get_object(id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ImageDownload(APIView):
    '''Download an image by click on 'download_url' link'''

    def get_object(self, id):
        try:
            return Image.objects.get(id=id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        img_url = self.get_object(id)  
        download_link = img_url.image_url
        filename = download_link.split("/")[-1]
        urllib.request.urlretrieve(img_url.image_url, filename)
        return HttpResponseRedirect(f'/{id}')
        


    


        
    
    