from django.shortcuts import render


# render pages
def homepage(request):
    return render(request,'portfolio/homepage.html')

def work_history(request):
    return render(request, 'portfolio/work_history_page.html')

def certifications(request):
    return render(request, 'portfolio/certifications_page.html')

def alma_maters(request):
    return render(request, 'portfolio/alma_maters_page.html')