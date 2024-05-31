from django.http import HttpResponse
from django.shortcuts import render
from cv.models import Profile
from django.template import loader


def members(request):
  mymembers = Profile.objects.all().values()
  template = loader.get_template('profile.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Profile.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

# from django.http import HttpResponse
# from django.template import loader
#
# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())
# from django.shortcuts import render
# from django.http import HttpResponse

# def members(request):
#     return HttpResponse("Hello world!")