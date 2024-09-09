from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
# Menampilkan nama aplikasi, dan nama serta kelas
    context = {
        'app': 'Dilly Dolly',  
        'nama': 'Fakhriyah Ghania Putri',  
        'kelas': 'PBP B' 
    }

    return render(request, "main.html", context)