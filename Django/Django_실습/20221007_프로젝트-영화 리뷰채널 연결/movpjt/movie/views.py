from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'movie/index.html', context)

def home(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'movie/community.html', context)

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('movie:home')
    else:        
        review_form = ReviewForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'movie/create.html', context=context)

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review
    }
    return render(request, 'movie/detail.html', context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('movie:home')

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('movie:detail', review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        'review_form': review_form
    }
    return render(request, 'movie/update.html', context)