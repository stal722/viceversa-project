from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	count = len(user_text.split())
	if  count > 1:
		count_words = 'has ' + str(count) + ' words'
	else:
		count_words = 'has ' + str(count) + ' word'
	reverse_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reverse_text, 'countwords':count_words})