from django.shortcuts import render, redirect
from django.http import HttpResponse
from usc.models import Assembly,Packing,ShortageReport,Quote
from usc.forms import AssemblyForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



def index(request):
    context = {
        'index_text':"Welcome Index Page.",
        }
    return render(request, 'index.html', context)

@login_required
def addassembly(request):
    if request.method == "POST":
        form = AssemblyForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
            messages.success(request,("New Assembly has been Added!!!"))
            return redirect('assemblylist')
        else:
            messages.error(request,("Something went wrong Pls try again!"))
            return redirect('assemblylist')
    else:
        form = AssemblyForm(request.POST or None)
        return render(request, 'add_assembly_form.html', {'form': form})


@login_required
def assemblylist(request):    
        all_assemblies = Assembly.objects.filter(manage=request.user)
        paginator = Paginator(all_assemblies, 5)
        page = request.GET.get('pg')
        all_assemblies = paginator.get_page(page)

        return render(request, 'assembly_list.html', {'all_assemblies': all_assemblies})


@login_required
def detail(request,task_id):
    assembly = Assembly.objects.get(pk=task_id,)
    if  assembly.manage == request.user:        
        return render(request, 'assembly_detail.html', {'assembly': assembly})

@login_required
def delete_task(request, task_id):
    task = Assembly.objects.get(pk=task_id)
    if task.manage == request.user:
        if request.method == 'POST':
            task.delete()
            return redirect('assemblylist')
    else:
       messages.error(request,("Access Restricted, You Are Not Allowed."))

    task = Assembly.objects.get(pk=task_id)
    return render(request, 'assembly-delete-confirm.html',{'task':task})


@login_required
def edit_task(request, task_id):
    task = Assembly.objects.get(pk=task_id)
    form = AssemblyForm(request.POST or None, instance = task)           
    if form.is_valid():
        form.save()
        messages.success(request,("Assembly has been updated!"))
        return redirect('assemblylist')       
    return render(request, 'edit.html', {'form':form,'task': task})

@login_required
def packing(request):
    if  request.user.is_authenticated:          
        packings = Packing.objects.filter(manage=request.user,active=True)
        paginator = Paginator(packings, 5)
        page = request.GET.get('pg')
        packings = paginator.get_page(page)   
                       
    return render(request, 'packings.html', {'packings': packings})


@login_required
def shortage(request):    
    if  request.user.is_authenticated:          
        shortages = ShortageReport.objects.filter(manage=request.user,active=True)
        paginator = Paginator(shortages, 5)
        page = request.GET.get('pg')
        shortages = paginator.get_page(page)

    return render(request, 'shortages.html', {'shortages': shortages}) 



@login_required
def quote(request):
    if  request.user.is_authenticated: 
        quotes = Quote.objects.filter(manage=request.user,active=True)
        paginator = Paginator(quotes, 5)
        page = request.GET.get('pg')
        quotes = paginator.get_page(page)
         
    return render(request, 'quotes.html', {'quotes': quotes})


# def contact(request):
#     context = {
#         'contact_text':"Welcome Contact Page.",
#         }
#     return render(request, 'contact.html', context)

# def about(request):
#     context = {
#         'about_text':"Welcome About Page.",
#         }
#     return render(request, 'about.html', context)