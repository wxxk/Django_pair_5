from django.shortcuts import render, redirect

import reviews

from .forms import ReviewForm
from .models import Review

from django.db.models import Q


# Create your views here.


def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("reviews:index")
    else:
        form = ReviewForm()
    context = {
        "form": form,
    }
    return render(request, "reviews/create.html", context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


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


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect("reviews:index")


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
