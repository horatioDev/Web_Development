from django.shortcuts import render

# Import forms module
from django import forms

from django.http import HttpResponseRedirect

from django.urls import reverse

# Django Form
class NewTaskForm(forms.Form):
  # Input fields:
  # <input type='text' name='task' required id="id_task">
  # <input type="number" name="priority" min="1" max="10" required id="id_priority">
  task = forms.CharField(label='New Task')

# Create your views here.
def index(request):
  # Check if task in session
  if 'tasks' not in request.session:
    request.session['tasks'] = []
  return render(request, 'tasks/index.html',
  {'tasks': request.session['tasks']})

# Add tasks view
def add(request):
  # Check if form request is 'POST'
  if request.method == 'POST':
    # Create form w/ submitted data
    form = NewTaskForm(request.POST)
    # Check if form is valid
    if form.is_valid():
      # Get access to all data submitted if form is valid
      task = form.cleaned_data['task']
      # Add new task
      request.session['tasks'] += [task]
      # Redirect to tasks homepage
      return HttpResponseRedirect(reverse('tasks:index'))
    # Else return existing form data
    else:
      return render(request, 'tasks/add.html',
      {'form': form})
  # If method is GET
  return render(request, 'tasks/add.html', {'form': NewTaskForm()})