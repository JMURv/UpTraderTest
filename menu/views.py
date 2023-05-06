from django.shortcuts import render, redirect


def index_view(request):
    return redirect('catalog')


def catalog_view(request):
    return render(request, "catalog.html", None)


def pc_components_view(request):
    return render(request, "pc_components.html", None)


def smartphones_view(request):
    return render(request, "smartphones.html", None)


def cameras_view(request):
    return render(request, "cameras.html", None)
