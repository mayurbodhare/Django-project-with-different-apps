from django.shortcuts import render

# Create your views here.
from .models import Editor
from .forms import EditorForm
def index(request):
    form=EditorForm()
    return render(request,'blog_to_html/index.html',{'form':form})