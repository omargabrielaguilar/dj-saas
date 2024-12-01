import pathlib

from django.shortcuts import render
from django.http import HttpResponse

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
  print(this_dir)
  
  title = "page"
  context = {
    "page_title" : title
  }
  
  html_template  = "home.html"
  return render(request, html_template)  


def old_home_page_view(request, *args, **kwargs):
  print(this_dir)
  
  html_ = ""
  html_file_path = this_dir / "home.html"
  html_ = html_file_path.read_text()  #important read_text method <>
  
  return HttpResponse(html_)