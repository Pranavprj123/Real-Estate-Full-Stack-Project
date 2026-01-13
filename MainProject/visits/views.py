from django.shortcuts import render, redirect

# Create your views here.


def book_visit(request, id):
    if not request.user.is_authenticated:
        return redirect('login_user')

    return render(request, 'book.html', {'id': id})


def visit_success(request):
    return render(request, "visits/success.html")
