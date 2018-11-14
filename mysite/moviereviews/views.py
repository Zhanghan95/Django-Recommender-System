from django.shortcuts import render
from .models import Review, Movie

def review_list(request):
    lastest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'lastest_review_list': lastest_review_list}
    return render(request, 'review_list.html', context)

def review_detail(request):
    review = get_object_or_404(Review, id=pk)
    return render(request, 'review_detail.html', {'review': review})

def movie_list(request):
    movie_list = Movie.objects.order_by('-title')[:20]
    context = {'movie_list': movie_list}
    return render(request, 'movie_list.html', context)

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    return render(request, 'movie_detail.html', {'movie': movie})

