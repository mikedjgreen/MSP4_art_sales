from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Members
from .forms import MemberForm


@login_required
def view_members(request):
    """  A view that renders the club members page """

    members = Members.objects.all()

    context = {
        "members": members
    }
    return render(request, 'members/members.html', context)


@login_required
def member_details(request, member_id):
    """ A view to show an individual member """

    member = get_object_or_404(Members, pk=member_id)

    context = {
        'member': member,
    }

    return render(request, 'members/member_details.html', context)


@login_required
def edit_member(request, member_id):
    """ Edit a member of the club """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only club admin can do that.')
        return redirect(reverse('home'))

    member = get_object_or_404(Members, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated member!')
            return redirect(reverse('member_details', args=[member.id]))
        else:
            messages.error(request, 'Failed to update member. \
                                     Please ensure form is valid.')
    else:
        form = MemberForm(instance=member)
        messages.info(request, f'You are editing {member.full_name}')

    template = 'members/edit_member.html'
    context = {
        'form': form,
        'member': member,
    }

    return render(request, template, context)
