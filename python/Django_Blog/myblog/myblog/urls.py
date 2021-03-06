"""myblog URL Configuration

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
from codeserver import views as codeserver_views
from runcode import views as runcode_views

if __name__ == '__main__':
    main()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^code/(\S{8})$',codeserver_views.codeserverIndex,name="codeserverIndex"),
    url(r'^codeup/',codeserver_views.codeup),
    url(r'^codeupdate/',codeserver_views.codeupdate),
    url(r'^runcode/',runcode_views.runcode),
    url(r'^$',runcode_views.index)
]
