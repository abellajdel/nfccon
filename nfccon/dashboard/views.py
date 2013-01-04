from django.template.response import TemplateResponse
from main.models import Item 
from main.forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404

@login_required
def items_list(request, template='dashboard/itemslist.html'):
    items = get_list_or_404(Item, user=request.user)
    context = {'items': items}
    return render_to_response(template, context)

def one_item(request, id=None, template='dashboard/oneitem.html'):
    item = get_object_or_404(Item, id=int(id), user=request.user)
    context = {
        'item': item,
    }
    return render_to_response(template, context)


def item_edit(request, id=None, template='dashboard/itemedit.html'):
    instance = None
    if id:
        instance = get_object_or_404(Item, pk=id)

    if request.method == 'POST':
        if instance:
            form = ItemForm(data=request.POST, instance=instance)
            if form.is_valid(): 
                form.save()
        else:
            form = ItemForm(data=request.POST, user=request.user)
            if form.is_valid(): 
                form.save()
    else:
        if instance:
            form = ItemForm(instance=instance)
        else:
            form = ItemForm()
    context = {
        'form': form,
        'instance': instance
    }
    return TemplateResponse(request, template, context)
