from django.shortcuts import render, redirect

from .forms import ReviewForm, CommentForm
from reviews.models import Review, Comment

from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.


def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("reviews:detail", review.pk)
    else:
        form = ReviewForm()
    context = {
        "form": form,
    }
    return render(request, "reviews/create.html", context)


@login_required
def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        "review": review,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "reviews/detail.html", context)


@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("reviews:detail", review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        "form": form,
        "review": review,
    }
    return render(request, "reviews/update.html", context)


@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        review.delete()
        return redirect("reviews:index")
    else:
        from django.http import HttpResponseForbidden

        return HttpResponseForbidden


def search(request):
    all_data = Review.objects.order_by("-pk")
    search = request.GET.get("search", "")
    if search:
        search_list = all_data.filter(
            Q(title__icontains=search) | Q(movie_name__icontains=search)
        )

        context = {
            "search_list": search_list,
        }
    else:
        context = {}

    return render(request, "reviews/search.html", context)


@login_required
def comments_create(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        comments = []
        for a in review.comment_set.all():
            comments.append(
                [
                    a.content,
                    a.user.username,
                    a.create_at,
                    a.user.id,
                    request.user.id,
                    a.id,
                    a.review.id,
                ]
            )
        context = {"comments": comments}
        return JsonResponse(context)


@login_required
def comments_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect("reviews:detail", review_pk)


@login_required
def likes(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        is_Liked = False
    else:
        review.like_users.add(request.user)
        is_Liked = True
    context = {"isLiked": is_Liked, "likeCount": review.like_users.count()}
    return JsonResponse(context)
