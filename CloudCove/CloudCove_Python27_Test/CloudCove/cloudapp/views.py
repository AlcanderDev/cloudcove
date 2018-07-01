from django.shortcuts import render_to_response
from django.template import RequestContext
from models import UserDetails
import datetime

def index(request):
    if request.method == 'POST':
       # save new post
       username = request.POST['username']
       password = request.POST['password']
       address = request.POST['address']

       post = UserDetails(username=username)
       post.password = password
       post.last_update = datetime.datetime.now() 
       post.address = address
       post.save()

    # Get all posts from DB
    posts = UserDetails.objects 
    return render_to_response('index.html', {'UserDetails': posts},
                              context_instance=RequestContext(request))


def update(request):
    id = eval("request." + request.method + "['id']")
    post = UserDetails.objects(id=id)[0]
    
    if request.method == 'POST':
        # update field values and save to mongo
        post.username = request.POST['username']
        post.password = request.POST['password']
        post.last_update = datetime.datetime.now() 
        post.address = request.POST['address']
        post.save()
        template = 'index.html'
        params = {'UserDetails': UserDetails.objects} 

    elif request.method == 'GET':
        template = 'update.html'
        params = {'post':post}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request):
    id = eval("request." + request.method + "['id']")
    if request.method == 'POST':
        post = UserDetails.objects(id=id)[0]
        post.delete() 
        template = 'index.html'
        params = {'UserDetails': UserDetails.objects} 
    elif request.method == 'GET':
        template = 'delete.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))
                              
    
