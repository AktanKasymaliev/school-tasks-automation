from django.contrib.auth import authenticate, login
from django.http import HttpRequest

def auto_login(request: HttpRequest, **creds) -> None:
    user = authenticate(request, 
                **creds
            )
    try:
        login(request, user)
    except AttributeError:
        pass