from django.shortcuts import render
from .models import Members


def view_members(request):
    """ A view that renders the club members page """

    members = Members.objects.all()

    context = {
        "members": members
    }
    return render(request, 'members/members.html', context)
