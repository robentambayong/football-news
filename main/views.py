from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406453594',
        'name': 'Roben Joseph B Tambayong',
        'class': 'KKI'
    }

    return render(request, "main.html", context)