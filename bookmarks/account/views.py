from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        # Create a form with data from request.POST.
        form = LoginForm(request.POST)
        # Check a validity of the form
        if form.is_valid():
            # Assign cleaned data which created in process of is_valid()
            cd = form.cleaned_datad
            # Authenticate user with cleaned data, return user or None
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            # Check user is authenticated and is activated
            if user is not None:
                if user.is_active:
                    # Login user, sets user in the current session
                    login(request, user)
                    return HttpResponse('Successfully Login')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm(request.POST)
        return render(request, 'account/login.html', {'form': form})