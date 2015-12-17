from django.shortcuts import render, get_object_or_404
# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import ChoreList, Chore
from django.template import loader, RequestContext

'''
def index(request):
    lists = ChoreList.objects.all()
    template = loader.get_template('chores/index.html')
    context = RequestContext(request, {
        'chorelists': lists
    })
    return HttpResponse(template.render(context))'''


def index(request):
    lists = ChoreList.objects.all()
    context = {'chorelists': lists}
    return render(request, 'chores/index.html', context)


# list of chores of the chorelist with id=chorelist_id with links to choredetail
def detail(request, chorelist_id):
    list = get_object_or_404(ChoreList, pk=chorelist_id)
    return render(request, 'chores/chorelistdetail.html', {'chorelist': list})


# details of chore 'chore_id' of the chorelist 'chorelist_id'
def choredetail(request, chorelist_id, chore_id):
    chorelist = get_object_or_404(ChoreList, pk=chorelist_id)
    chore = get_object_or_404(Chore, pk=chore_id)
    return render(request, 'chores/choredetail.html', {'chorelist': chorelist, 'chore': chore})


def updatechore(request, chorelist_id, chore_id):
    chorelist = get_object_or_404(ChoreList, pk=chorelist_id)
    chore = get_object_or_404(Chore, pk=chore_id)
    if 'complete' in request.POST:
        chore.complete = True
    else:
        chore.complete = False

    chore.save()
    return HttpResponseRedirect('/main/' + chorelist_id + '/chores/' + chore_id)

def newlist(request):
    if request.POST:
        list = ChoreList(name=request.POST['name'], due_date=request.POST['duedate'])
        list.save()
        return HttpResponseRedirect('/main')
    else:
        return render(request, 'chores/newlist.html', {})


