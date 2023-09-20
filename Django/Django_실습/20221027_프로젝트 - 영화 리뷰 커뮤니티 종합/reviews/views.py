from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'reviews/index.html')

@login_required
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, '글 작성이 완료되었습니다.')
            return redirect('reviews:community')
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'reviews/create.html', context=context)

def community(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/community.html', context)

def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review': review,
        'comment': review.comment_set.all(),
        }
    return render(request, 'reviews/detail.html', context)

# @login_required
# def update(request, pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.user == review.user:
#         if request == 'POST':
#             review_form = ReviewForm(request.POST, request.FILES, instance=review)
#             if review_form.is_valid():
#                 review_form.save()
#                 messages.success(request, '글이 수정되었습니다.')
#                 return redirect('reviews:detail', review.pk)
#         else:
#             review_form = ReviewForm(instance=review)
#         context = {
#             'review_form': review_form
#         }
#         return render(request, 'reviews/create.html', context)
#     else:
#         return HttpResponseForbidden()

@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:

        if request.method == 'POST':
            # POST : input 값 가져와서, 검증하고, DB에 저장
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
                review_form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('reviews:detail', review.pk)
            # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
        else:
            # GET : Form을 제공
            review_form = ReviewForm(instance=review)
        context = {
            'review_form': review_form
        }
        return render(request, 'reviews/create.html', context)

def delete(request, pk):
    get_object_or_404(Review, pk=pk).delete()
    return redirect('reviews:community')

@login_required
def comment_create(request, pk):
    print(request.POST)
    article = get_object_or_404(Review, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment_form.save() # 모델 인스턴스의 save()
        context = {
            'content': comment.content,
            'userName': comment.user.username
        }
    return JsonResponse(context)

def comment_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)

@login_required
def like(request, pk):
  review = get_object_or_404(Review, pk=pk)
  if request.user in review.like_users.all(): 
    # 좋아요 삭제
    review.like_users.remove(request.user)
    is_liked = False
  else:
    # 좋아요 추가
    review.like_users.add(request.user)
    is_liked = True
  # 상세 페이지로 redirect
  context = {'isLiked': is_liked, 
             'likeCount': review.like_users.count(),
            }
  return JsonResponse(context)

