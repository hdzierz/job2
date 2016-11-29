"""job2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
import lbm.views as views 
import master_files.views as mviews

urlpatterns = [
    url(r'^$', views.page_home, name='page_home'),    
    url(r'^admin/', admin.site.urls),
    url(r'^lbm/jobsCurrent', views.page_lbm, name='page_lbm'),
    url(r'^lbm/jobBooking', views.page_lbm_jobBooking, name='page_lbm_jobBooking'),
    url(r'^lbm/jobRoutes/(?P<job_id>[0-9]*)/$', views.page_lbm_jobRoutes, name='page_lbm_jobRoutes'),
    #url(r'^lbm/test', views.page_test, name='page_test'),
    url(r'^reports/lbm/jobDetails', views.page_reports_lbm_jobDetails, name='page_reports_lbm_jobDetails'),
    url(r'^master_files/route/$', mviews.page_route_list),
    url(r'^test/$', mviews.page_data_table),

]
