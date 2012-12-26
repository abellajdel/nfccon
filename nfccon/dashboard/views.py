from django.template.response import TemplateResponse
from main.models import Item 
from django.contrib.auth.decorators import login_required

@login_required
def items_list(request, template='dashboard/itemslist.html'):
    print request.user
    items = Item.objects.filter(user=request.user)
    context = {'items': items}
    return TemplateResponse(request, template, context)

def one_item(request, id=None, template='dashboard/oneitem.html'):
    return TemplateResponse(request, template, {})


def item_edit(request, template='dashboard/itemedit.html'):
    pass
