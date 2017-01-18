from django.shortcuts import render, get_object_or_404, redirect
from .models import App
from django.utils import timezone
from .forms import AppForm

# Create your views here.

def app_list(request):
    apps = App.objects.filter(pubDate__lte=timezone.now()).order_by('pubDate')
    return render(request, "apprecog/app_list.html", {'apps': apps})

def app_detail(request, pk):
    app = get_object_or_404(App, pk=pk)
    print 'app detail info', app.appName, ":", app.summary
    return render(request, 'apprecog/app_detail.html', {'app': app})

def app_new(request):
    if request.method == 'POST':
        form = AppForm(request.POST)

        if form.is_valid():
            app = form.save(commit=False)
            app.author = request.user

            app.save()

            return redirect('app_detail', pk=app.pk)
    else:
        form = AppForm()

    return render(request, 'apprecog/app_edit.html', {'form': form})

def app_draft_list(request):
    apps = App.objects.filter(pubDate__isnull=True).order_by('regDate')
    return render(request, 'apprecog/app_draft_list.html', {'apps': apps})

def app_publish(request, pk):
    app = get_object_or_404(App, pk=pk)
    app.publish()
    return redirect('app_detail', pk=pk)