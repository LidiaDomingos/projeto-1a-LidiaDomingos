from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        content = request.POST.get('detalhes')
        add_nota(content)
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        return redirect('index')
    else:
        all_notes = Note.objects.last()
        return render(request, 'notes/index.html', {'notes': all_notes})

def add_nota(content):
    note = Note(content=content)
    note.save(note)