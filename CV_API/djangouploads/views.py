import os

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import JsonResponse

from scorer import final_score
from .models import Drink
from .serializer import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .settings import MEDIA_ROOT
import cv2

# def image(request, id):
#     img = ImageInfo.objects.get(pk=id)
#     if img is not None:
#         return render(request, 'images/images.html', {'image': img})
#     else:
#         raise Http404('Image not exist')


@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drink = Drink.objects.all()
        serializer = DrinkSerializer(drink, many=True)
        # serializer = DrinkSerializer(drink)

        return JsonResponse({'Drinks': serializer.data})

    if request.method == 'POST':
        print("Post method Called")
        serializer = DrinkSerializer(data=request.data)
        image = request.FILES["image"]

        path = default_storage.save('C:/Users/mangl/PycharmProjects/images/tmp/somename.jpg', ContentFile(image.read()))
        # tmp_file = os.path.join(MEDIA_ROOT, path)
        # img = cv2.imread(tmp_file)
        # cv2.imshow("Output", img)
        score = final_score(path)
        print(score)
        if serializer.is_valid():
            serializer.save()
            return Response([serializer.data,score], status=status.HTTP_201_CREATED)

        return Response({}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def drink_detail(request, id, format=None):
#     try:
#         drink = Drink.objects.get(pk=id)
#         # img = Drink.objects.get(pk=id)
#         # if img is not None:
#         #     return render(request, 'images/images.html', {'image': img})
#
#     except Drink.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = DrinkSerializer(drink)
#
#         return Response([serializer.data,score])
#
#     elif request.method == 'PUT':
#         serializer = DrinkSerializer(drink, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         drink.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
