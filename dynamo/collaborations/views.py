from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin, UpdateView, DeleteView
from itertools import chain
from chat.forms import CollaborationMessageForm
from chat.models import Message
from collaborations.models import Collaboration, CollaborationTask, CollaborationMilestone
from groups.models import Group


@method_decorator(login_required, name="dispatch")
class CollaborationCreateView(CreateView):
    """
    Allows users to create a new collaboration
    """

    template_name = "collaborations/collaboration_create.html"
    model = Collaboration
    fields = (
        "name",
        "description",
    )

    def get_initial(self):
        group = Group.objects.get(slug=self.kwargs.get("group_slug"))
        return {"related_group": group}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group"] = Group.objects.get(slug=self.kwargs.get("group_slug"))
        return context

    def form_valid(self, form):
        """
        We override the form valid to add the user as admin and creator
        """

        # 1. Get user
        user = self.request.user
        if not user.is_authenticated:
            raise PermissionError
        form.instance.created_by = user

        form.instance.related_group = Group.objects.get(
            slug=self.kwargs.get("group_slug")
        )

        return super(CollaborationCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "collaboration-detail",
            kwargs={"slug": self.object.slug},
        )


class CollaborationDetailView(FormMixin, DetailView):
    """
    Shows all information regarding a collaboration, as well as
        - Chat Messages
        - Tasks /Milestones
    """

    template_name = "collaborations/collaboration_detail.html"
    model = Collaboration
    form_class = CollaborationMessageForm

    def get_context_data(self, **kwargs):
        """
        We override get_context_data to populate the search field choices
        """

        context = super(CollaborationDetailView, self).get_context_data(**kwargs)

        collaboration = self.get_object()

        context.update(
            {
                "chat_messages": Message.objects.filter(collaboration=collaboration),
                "chat_form": CollaborationMessageForm(
                    initial={"collaboration": collaboration}
                ),
                "elements": self.get_all_elements()
            },
        )

        return context

    def get_all_elements(self):
        tasks = CollaborationTask.objects.all()
        milestones = CollaborationMilestone.objects.all()
        element_list = sorted(
            chain(tasks, milestones),
            key=lambda element: element.position, reverse=True)
        return element_list


@method_decorator(login_required, name="dispatch")
class CollaborationUpdateView(UpdateView):
    """
    Allows the user to update multiple fields on a collaboration which they are the admin/creator of.
    """

    template_name = "collaborations/collaboration_update.html"
    model = Collaboration
    fields = [
        "name",
        "description",
    ]

    def get_success_url(self):
        return reverse_lazy(
            "collaboration-detail",
            kwargs={"slug": self.object.slug},
        )


@method_decorator(login_required, name="dispatch")
class CollaborationDeleteView(DeleteView):
    template_name = "collaborations/collaboration_delete.html"
    model = Collaboration

    def get_success_url(self):
        return reverse_lazy(
            "group-detail",
            kwargs={"slug": self.object.related_group.slug},
        )
