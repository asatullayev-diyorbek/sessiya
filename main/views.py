from django.shortcuts import render, redirect
from django.utils.html import linebreaks
from django.views import View
from .models import Note

class Dashboard(View):
    def get(self, request):
        notes = Note.objects.all()  # Barcha yozuvlarni olish
        return render(request, 'dashboard.html', context={'notes': notes})

    def post(self, request):
        text = request.POST.get('text')  # Formadagi matn
        file = request.FILES.get('file')  # Formadagi fayl

        if text or file:
            text_with_linebreaks = linebreaks(text) # Agar matn yoki fayl bo'lsa, ma'lumotni saqlaymiz
            Note.objects.create(text=text_with_linebreaks, file=file)
            return redirect('main:dashboard')

        return render(request, 'dashboard.html', {'error': 'Matn yoki fayl kiritilmagan.'})
