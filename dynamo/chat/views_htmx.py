from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from chat.forms import CollaborationMessageForm, GroupMessageForm
from chat.models import Message
from collaborations.models import Collaboration
from groups.models import Group
from groups.views import get_membership_level


@login_required()
def group_message_create_view(request, slug):
    """
    HTMX VIEW - Allows chat messages to be added
    """
    # TODO: Secure and set methods

    # Get  variables
    message = str(request.POST["message"])

    user = request.user
    group = Group.objects.get(slug=slug)

    Message.objects.create(group=group, user=user, message=message)
    messages = Message.objects.filter(group=group)
    membership_level = get_membership_level(request.user, group)

    return render(request, "app/group/partials/chat/main.html", {
        'membership_level': membership_level,
        "chat_messages": messages,
        "group": group,
        "chat_form": GroupMessageForm(
            initial={"group": group}
        )})


@login_required()
def group_message_delete_view(request, slug, pk):
    """
    HTMX VIEW - Allows chat messages to be deleted
    """

    # TODO: Secure and set methods

    # Get  variables
    message = Message.objects.get(pk=pk)
    user = request.user

    group = message.group
    message.delete()
    messages = Message.objects.filter(group=group)

    membership_level = get_membership_level(request.user, group)

    return render(request, "app/group/partials/chat/main.html", {
        'membership_level': membership_level,
        "chat_messages": messages,
        "group": group,
        "chat_form": GroupMessageForm(
            initial={"group": group}
        )})


@login_required()
def collaboration_message_create_view(request, slug):
    """
    HTMX VIEW - Allows chat messages to be added
    """
    # TODO: Secure and set methods

    # Get  variables
    message = str(request.POST["message"])

    user = request.user
    collaboration = Collaboration.objects.get(slug=slug)

    Message.objects.create(collaboration=collaboration, user=user, message=message)
    messages = Message.objects.filter(collaboration=collaboration)

    membership_level = get_membership_level(request.user, collaboration.related_group)

    return render(request, "app/collaborations/partials/chat/main.html", {
        'membership_level': membership_level,
        "chat_messages": messages,
        "collaboration": collaboration,
        "chat_form": CollaborationMessageForm(
            initial={"collaboration": collaboration}
        )})


@login_required()
def collaboration_message_delete_view(request, slug, pk):
    """
    HTMX VIEW - Allows chat messages to be deleted
    """

    # TODO: Secure and set methods

    # Get  variables
    message = Message.objects.get(pk=pk)
    user = request.user

    collaboration = message.collaboration
    message.delete()
    messages = Message.objects.filter(collaboration=collaboration)

    membership_level = get_membership_level(request.user, collaboration.related_group)

    return render(request, "app/collaborations/partials/chat/main.html", {
        'membership_level': membership_level,
        "chat_messages": messages,
        "collaboration": collaboration,
        "chat_form": CollaborationMessageForm(
            initial={"collaboration": collaboration}
        )})

