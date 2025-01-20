from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
from random import randint
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_protect