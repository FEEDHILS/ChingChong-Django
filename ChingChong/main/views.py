from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
@csrf_exempt
def search_city(req):
    query = req.GET.get('city', None)
    if query:
        query = req.GET.get('city', '')
        # Выполнение поиска по базе
        results = Cities.objects.filter(city__icontains=query).values('adress')[:5]
        return JsonResponse({'results': list(results)})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)