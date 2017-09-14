"""tutorgame URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
#    url(r'^$', views.index, name='index'),
#    url(r'^regexapp', include('regexapp.urls')),
#    url(r'^admin/', admin.site.urls),
url(r'^ajax/question_hw/(?P<game_id>[\w]+)/$', views.question_hw, name='question_hw')
url(r'^ajax/check_homework/(?<game_id>[\w]+)/$', views.question_check_hw, name='check_hw'),
url(r'^ajax/question_test/(?<game_id>[\w]+)/$', views.question_test, name='question_test'),
url(r'^ajax/check_test/(?<game_id>[\w]+)/$', views.question_check_test, name='question_check_test'),
url(r'new_game/$', views.new_game, name='new_game'),
url(r'^index/(?p<game_id>[\w]+/$', views.index, name='game'),
url(r'^ajax/save/(?P<game_id>[\w]+)/$', views.save, name='save'),
]
