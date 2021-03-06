"""game_gauger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

from reviews import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^reviews/$', views.index, name='index'),

    url(r'^reviews/about', views.about, name='about'),

    url(r'^reviews/featured', views.featured,name='featured'),

    url(r'^reviews/signin/$',views.user_login, name='signin'),

    url(r'^reviews/signup/$', views.register, name='signup'),

    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^reviews/addgame',views.addgame,name='addgame'),

    url(r'^reviews/categories',views.categories,name='categories'),

    url(r'^reviews/(?P<game_name_slug>[\w\-]+)/$',
        views.detail, name='detail'),

    url(r'^reviews/action',views.cataction,name='action'),

    url(r'^reviews/actionadventure',views.catactionadventure,name='actionadventure'),

    url(r'^reviews/adventure',views.catadventure,name='adventure'),

    url(r'^reviews/rpg',views.catrpg,name='rpg'),

    url(r'^reviews/simulation',views.catsim,name='simulation'),

    url(r'^reviews/sport',views.catsport,name='sport'),

    url(r'^reviews/puzzle',views.catpuzzle,name='puzzle'),

    url(r'^reviews/misc',views.catmisc,name='misc'),

    url(r'^admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error handlers
handler404 = views.error_404
handler500 = views.error_500
