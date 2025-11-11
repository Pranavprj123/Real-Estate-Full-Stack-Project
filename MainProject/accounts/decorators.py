from django.shortcuts import redirect

def agent_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.userprofile.role == "agent":
            return view_func(request, *args, **kwargs)
        return redirect("/")  # or show error page
    return wrapper
