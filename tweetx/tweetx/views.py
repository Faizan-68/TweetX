from django.shortcuts import render,redirect,get_object_or_404

def reset_complete(request):
    return render(request, 'registration/password-reset-complete.html')