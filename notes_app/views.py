from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.models import ProFile

# Create your views here.


def all_notes(request):
    user = request.user
    all_notes = Note.objects.filter(user = user)
    if request.user.is_authenticated :
        profile = get_object_or_404(ProFile , user = user)
        context = {
            'all_notes' : all_notes ,
            'profile' : profile ,
        }
    else:
        context = {
            'all_notes' : all_notes ,
        }
    return render(request, 'all_notes.html', context)
    # return render(request, 'notes.html', context)


def detail(request, slug):
    note = Note.objects.get(slug = slug)
    if request.user.is_authenticated :
        user = request.user
        profile = get_object_or_404(ProFile , user = user)
        context = {
            'note': note ,
            'profile' : profile ,
        }
    else:
        context = {
            'note': note ,
        }
    return render(request, 'note_detail.html', context)
    # return render(request, 'one_note.html', context)


def note_add(request):
    user = request.user
    profile = get_object_or_404(ProFile , user = user)
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Note added successfuly.')
            return redirect('/')
    else:
        form = NoteForm()

    context = {
        'form': form ,
        'profile' : profile ,
    }
    return render(request , 'add.html', context)


def note_edit(request , slug):
    user = request.user
    profile = get_object_or_404(ProFile , user = user)
    note = get_object_or_404(Note, slug = slug)
    if request.method == 'POST':
        form = NoteForm(request.POST , instance = note)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Your Post updated Successfully.')
            return redirect('/notes/' + slug)
    else:
        form = NoteForm(instance = note)

    context = {
        'form' : form ,
        'profile' : profile ,
    }
    return render(request , 'edit.html', context)


def note_delete(request, slug):
    note = get_object_or_404(Note, slug = slug)
    try:
        print (request.method)
        if request.method == 'GET':
            form = NoteForm(request.GET , instance = note)
            note.delete()
            return redirect('/')

    except Exception as e:
        messages.success(request, 'The note could not be deleted : Error {}'.format(e))
