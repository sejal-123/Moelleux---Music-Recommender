from django.shortcuts import render, redirect
from .models import SearchModel, FeedbackModel
from django.contrib.auth.models import User

"""
from .forms import SearchForm
import requests
import datetime
import sqlite3
from sqlite3 import Error
"""
# Create your views here.


def home(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			print('This is POST')
			song_name = request.POST.get('song_name')
			song_artist = request.POST.get('song_artist')
			print(song_name, song_artist)
			new = SearchModel(song_name=song_name, song_artist = song_artist, user = request.user)
			new.save()
			"""
			ins = SearchModel(song_name = song_name, song_artist = song_artist)
			ins.save()
			"""
		else:
			print('hell')
		return render(request, 'home.html')

	else:
		return redirect("ulogin")
"""
def home(request):
	if request.user.is_authenticated:
		return render(request, 'home.html')
	else:
		return redirect('ulogin')
def search(request):
	if request.user.is_authenticated:
		user=request.user
		if request.method=="POST":
			f=SearchForm(request.POST)
			f.save()
			fm=SearchForm()
			return render(request, 'home.html', {'fm':fm})
		else:
			fm=SearchForm(initial={'user':request.user})
			return render(request, 'home.html', {'fm':fm})
			"""
def showhistory(request):
	data=SearchModel.objects.filter(user=request.user)
	return render(request, 'showhistory.html', {'data':data})

def feedback(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			print('This is POST')
			feedback = request.POST.get('feedback')
			rating = request.POST.get('rating')
			print(feedback, rating)
			new = FeedbackModel(feedback = feedback, rating = rating, user = request.user)
			new.save()
			
		else:
			print('hell')
		return render(request, 'feedback.html')

	else:
		return redirect("ulogin")
	return render(request, 'feedback.html')

def contact(request):
	return render(request, 'contact.html')
