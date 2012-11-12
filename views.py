from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from blog.models import Entry
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.template import RequestContext
from tagging.models import Tag

def entries_index(request, id=None):
    if id:
        tag = Tag.objects.get(id=id)
        entries = Entry.objects.filter(id__in=tag.items.all().values('object_id'))
    else:
        entries = Entry.objects.filter(status=1)

    paginator = Paginator(entries, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)

    ids = list(range(page - 3 if page - 3 >=1 else 1, page + 5 if page + 4 < paginator.num_pages else paginator.num_pages+1))
    if entries.count() == 0:
        ids = []


    return render_to_response('blog/entry_index.html', 
                {
                'user':request.user,
                'entry_list': contacts,
                'ids' : ids,
                'tag':tag.name if id else False,
                },
                context_instance=RequestContext(request))

def entry_detail(request, id):
    entry = get_object_or_404(Entry, id=id)
    entry.views = 1 + entry.views
    entry.save()
    return render_to_response('blog/entry_detail.html', {'user':request.user, 'entry': entry },
                context_instance=RequestContext(request))

