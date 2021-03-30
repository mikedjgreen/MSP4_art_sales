from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages


from .models import Members, Subs
from .forms import MemberForm, SubsForm


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
            short_msg='Failed to update member. Please ensure form is valid.'
            messages.error(request, short_msg)
    else:
        form = MemberForm(instance=member)
        messages.info(request, f'You are editing {member.full_name}')

    template = 'members/edit_member.html'
    context = {
        'form': form,
        'member': member,
    }

    return render(request, template, context)


@login_required
def delete_member(request, member_id):
    """ Delete a member from the club """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only club admin can do that.')
        return redirect(reverse('home'))

    member = get_object_or_404(Members, pk=member_id)
    member.delete()
    messages.success(request, 'Member deleted!')
    return redirect(reverse('view_members'))


@login_required
def pay_subs(request):
    """  Signed In Member can pay annual club subscription """
    usn = request.user.username
    rate = settings.CLUB_SUBSCRIPTION

    if usn:
        member = get_object_or_404(Members, username=usn)
        template = 'members/pay_subs.html'
        context = {
            'member': member,
            'user': usn,
            'rate': rate,
        }
        return render(request, template, context)


@login_required
def add_subs(request):
    """ Add a subscription for a member """

    if request.method == 'POST':
        form = SubsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added annual subscription')
            return redirect(reverse('members'))
        else:
            messages.error(request,
                           'Failed to add subscription.\
                            Please ensure the form is valid.')
    else:
        form = SubsForm()

    template = 'members/add_subs.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
