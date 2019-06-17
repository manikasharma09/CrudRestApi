from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Profile
from .serializers import ProfileSerializers
from rest_framework import generics
from .models import Profile
from .import serializers



# using the function based views and manually writing get post and delete
def first(request):
	if request.method=="GET":
		queryset=Profile.objects.all()
		serializer=ProfileSerializers(queryset,many=True)
		return JsonResponse(serializer.data,safe=False)


	elif request.method=="POST":
	    serializer=ProfileSerializers(data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return JsonResponse(serializer.data)	


def second(request,pk):
	if request.method=="GET":
		queryset=Profile.objects.get(pk=pk)
		serializer=ProfileSerializers(queryset)
		return JsonResponse(serializer.data,safe=False)

	elif request.method=="DELETE":
	    queryset=Profile.objects.get(pk=pk)
	    queryset.delete()
	    return HttpResponse(status=204)	



# using the generic views and accordingly change the urls.py also

#class ListCreate(generics.ListCreateAPIView):
#	queryset=Profile.objects.all()
#	serializer_class=serializers.ProfileSerializers


#class RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
 #   queryset=Profile.objects.all()
  #  serializer_class=serializers.ProfileSerializers
