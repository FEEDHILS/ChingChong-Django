from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from account.models import User
from posts.models import *
import json
from datetime import datetime

@csrf_exempt
def search_city(req):
    query = req.GET.get('city', None)
    if query:
        query = req.GET.get('city', '')
        # Выполнение поиска по базе
        results = Cities.objects.filter(city__icontains=query).values('adress')[:5]
        return JsonResponse({'results': list(results)})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

# Я бы лучше переделал бы это с формой, но у меня нет времени!!!
def profile_update(req):
    if req.method == "POST":
        data = json.loads(req.body)
        print(data)
        user = req.user  # Получаем текущего аутентифицированного пользователя
        if 'birth' in data and data['birth'] is not '':
            user.birthday = datetime.strptime(data['birth'], '%Y-%m-%d').date()
        if 'phone' in data:
            user.number = data['phone']
        if 'email' in data :
            if not get_user_model().objects.filter(email=data['email']).exclude(email=user.email).exists():
                user.email = data['email']
            else:
                return JsonResponse({'success': False, 'error': 'This email is already used'})
        if 'food' in data:
            user.food = data['food']
        if 'about' in data:
            user.aboutMe = data['about']

            user.save()  # Сохраняем обновленного пользователя

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Something went wrong'})
        


def like_or_dislike(request, post_id, rating):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    rating = int(rating)

    # Обновляем оценку пользователя
    PostInfo.set_user_rating(post, user, rating)

    return JsonResponse({
        'likes': post.likes,
        'dislikes': post.dislikes,
    })