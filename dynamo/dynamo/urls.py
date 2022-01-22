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

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from dynamo.base.views import htmx_empty_string

urlpatterns = [
    # ADMIN
    path("admin/", admin.site.urls),
    # AUTH
    path("accounts/", include("users.urls")),
    # Home
    path("", TemplateView.as_view(template_name="landing/landing.html"), name="home"),
    # FAQ / Support
    path("support/", include("support.urls")),
    # Groups
    path("groups/", include("groups.urls")),
    # Collaborations
    path("", include("collaborations.urls")),
    # Generics
    path("htmx-empty-string", htmx_empty_string, name="htmx-empty-string"),
]
