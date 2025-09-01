from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# from networkx import reverse
from django.urls import reverse
from .utils.unsplash import search_unsplash
from .models import Collection, Image
from .utils.unsplash import get_unsplash_image_detail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.



def index(request):
    query = request.GET.get("q", "nature")  # default search
    results = search_unsplash(query, per_page=12)

    return render(request, "collection/index.html", {"images": results.get("results", [])})


@login_required
def collection_list(request):
    collections = Collection.objects.filter(user=request.user)
    return render(request, "collection/collection_list.html", {"collections": collections})


@login_required
def add_to_collection(request):
    if request.method == "POST":
        image_id = request.POST.get("image_id")
        if not image_id:
            return JsonResponse({"success": False, "message": "No image ID provided."})

        collection, _ = Collection.objects.get_or_create(user=request.user)
        image, created = Image.objects.get_or_create(unsplash_id=image_id)
        if created:
            detail = get_unsplash_image_detail(image_id)
            image.url = detail['urls']['small']
            image.description = detail.get('description', '')
            image.save()

        if collection.images.filter(id=image.id).exists():
            return JsonResponse({"success": False, "message": "This image is already in your collection."})
        else:
            collection.images.add(image)
            return JsonResponse({"success": True})

    return JsonResponse({"success": False, "message": "Invalid request."})


@login_required
def delete_image_from_collection(request):
    if request.method == "POST":
        image_id = request.POST.get("image_id")
        collection_id = request.POST.get("collection_id")
        if not image_id or not collection_id:
            return JsonResponse({"success": False, "message": "Missing image or collection ID."})
        try:
            collection = Collection.objects.get(id=collection_id, user=request.user)
            image = Image.objects.get(id=image_id)
            collection.images.remove(image)
            return JsonResponse({"success": True})
        except Collection.DoesNotExist:
            return JsonResponse({"success": False, "message": "Collection not found."})
        except Image.DoesNotExist:
            return JsonResponse({"success": False, "message": "Image not found."})
    return JsonResponse({"success": False, "message": "Invalid request."})


def collection_detail(request):
    image_id = request.GET.get('image_id')
    image_detail = None
    if image_id:
        from .utils.unsplash import get_unsplash_image_detail
        image_detail = get_unsplash_image_detail(image_id)
    # collection = Collection.objects.get(id=collection_id)
    # images = collection.Images.all()
    return render(request, "collection/collection_detail.html", {
        "image": image_detail,
        # Add other context variables as needed
    })