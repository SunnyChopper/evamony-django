from django.core import serializers
from django.http import JsonResponse
from .models import Family

def get(request):
	if request.method == 'GET':
		families = Family.objects.all()
		json = serializers.serialize('json', families)
		return JsonResponse(json, safe = False)
	else:
		return 'Error'