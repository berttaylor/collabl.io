"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from chat.views_htmx import collaboration_message_create_view, collaboration_message_delete_view
from collaborations.views import CollaborationCreateView, CollaborationDetailView
from .views_htmx import collaboration_task_toggle_view, collaboration_task_create_view, \
    collaboration_milestone_create_view, collaboration_task_update_view, collaboration_milestone_update_view, \
    collaboration_task_delete_view, collaboration_milestone_delete_view, collaboration_task_move_view, \
    collaboration_milestone_move_view, collaboration_task_notes_view, collaboration_elements_list_view, \
    collaboration_update_view, collaboration_image_view

urlpatterns = [
    # We use long URLs here because collaborations are created within groups and this probably make more sense
    # to the user in terms of data hierarchy.
    path(
        "groups/<slug>/create-collaboration/",
        CollaborationCreateView.as_view(),
        name="collaboration-create",
    ),
    path(
        "collaborations/<slug>/",
        CollaborationDetailView.as_view(),
        name="collaboration-detail",
    ),
    path(
        "collaborations/<slug>/update",
        collaboration_update_view,
        name="collaboration-update",
    ),
    path(
        "collaborations/<slug>/image",
        collaboration_image_view,
        name="collaboration-image",
    ),
    path(
        "collaborations/<slug>/elements",
        collaboration_elements_list_view,
        name="collaboration-elements-list",
    ),

    path(
        "collaborations/<slug>/tasks",
        collaboration_task_create_view,
        name="collaboration-task-create",
    ),
    path(
        "collaborations/<slug>/tasks/<pk>",
        collaboration_task_update_view,
        name="collaboration-task-update",
    ),
    path(
        "collaborations/<slug>/tasks/<pk>/delete",
        collaboration_task_delete_view,
        name="collaboration-task-delete",
    ),
    path(
        "collaborations/<slug>/tasks/<pk>/notes",
        collaboration_task_notes_view,
        name="collaboration-task-notes",
    ),
    path(
        "collaborations/<slug>/tasks/<pk>/toggle/<status>",
        collaboration_task_toggle_view,
        name="collaboration-task-toggle",
    ),
    path(
        "collaborations/<slug>/tasks/<pk>/move/<position>",
        collaboration_task_move_view,
        name="collaboration-task-move",
    ),

    path(
        "collaborations/<slug>/milestones",
        collaboration_milestone_create_view,
        name="collaboration-milestone-create",
    ),
    path(
        "collaborations/<slug>/milestones/<pk>",
        collaboration_milestone_update_view,
        name="collaboration-milestone-update",
    ),
    path(
        "collaborations/<slug>/milestones/<pk>/delete",
        collaboration_milestone_delete_view,
        name="collaboration-milestone-delete",
    ),
    path(
        "collaborations/<slug>/milestones/<pk>/move/<position>",
        collaboration_milestone_move_view,
        name="collaboration-milestone-move",
    ),
    path(
        "collaborations/<slug>/messages",
        collaboration_message_create_view,
        name="collaboration-message-create",
    ),
    path(
        "collaborations/<slug>/messages/<pk>/delete",
        collaboration_message_delete_view,
        name="collaboration-message-delete",
    ),
]
