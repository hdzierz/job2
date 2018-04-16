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
import reports.views as rviews
import invoice.views as iviews

from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', views.page_home, name='page_home'),    
    url(r'^admin/', admin.site.urls),
    url(r'^lbm/jobsCurrent', views.page_lbm, name='page_lbm'),
    url(r'^lbm/jobBooking/$', views.page_lbm_jobBooking, name='page_lbm_jobBooking'),
    url(r'^lbm/jobBooking/(?P<job_id>[0-9]*)/$', views.page_lbm_jobBooking, name='page_lbm_jobBooking'),
    url(r'^lbm/jobRoutes/(?P<job_id>[0-9]*)/$', views.page_lbm_jobRoutes, name='page_lbm_jobRoutes'),
    #url(r'^lbm/test', views.page_test, name='page_test'),
    url(r'^reports/lbm/jobDetails', views.page_reports_lbm_jobDetails, name='page_reports_lbm_jobDetails'),
    url(r'^reports/lbm/sumdeliveryins', rviews.SummaryDeliveryInstructions.as_view(),
        name='page_summary_delivery_instructions'),


    url(r'^reports/archived/pmpupdated', rviews.PmpUpdated.as_view(), name='page_reports_archived_pmpupdated'),
    url(r'^reports/archived/Distpmpupdatedby', rviews.DistPmpUpdated.as_view(), name='page_reports_archived_Distpmpupdatedby'),
    url(r'^reports/archived/addressDetails', rviews.AddressDetails.as_view(), name='page_reports_archived_addressDetails'),
    url(r'^reports/archived/distBible', rviews.DistBible.as_view(), name='page_reports_archived_distBible'),
    url(r'^reports/archived/regionBible', rviews.RegionBible.as_view(), name='page_reports_archived_regionBible'),

	url(r'^invoice', iviews.page_invoice, name='page_invoice'),

    url(r'^master_files/(?P<model>[a-zA-Z0-9_]*)/$', mviews.page_list,
        name='master_files_routes'),
    url(r'^master_files/route/create/$', mviews.RouteCreate.as_view()),
    url(r'^master_files/route/update/(?P<pk>[0-9]*)$', mviews.RouteUpdate.as_view()),
    url(r'^master_files/route/delete/(?P<pk>[0-9]*)$',
        mviews.RouteDelete.as_view()),

    url(r'^master_files/region/create/$', mviews.RegionCreate.as_view()),
    url(r'^master_files/region/update/(?P<pk>[0-9]*)$',
        mviews.RegionUpdate.as_view()),
    url(r'^master_files/region/delete/(?P<pk>[0-9]*)$',
        mviews.RegionDelete.as_view()), 

    url(r'^master_files/area/create/$', mviews.AreaCreate.as_view()),
    url(r'^master_files/area/update/(?P<pk>[0-9]*)$',
                mviews.AreaUpdate.as_view()),
    url(r'^master_files/area/delete/(?P<pk>[0-9]*)$',
                mviews.AreaDelete.as_view()),

    url(r'^master_files/address/create/$', mviews.AddressCreate.as_view()),
    url(r'^master_files/address/update/(?P<pk>[0-9]*)$',
                mviews.AddressUpdate.as_view()),
    url(r'^master_files/address/delete/(?P<pk>[0-9]*)$',
                mviews.AddressDelete.as_view()), 
                
    url(r'^master_files/client/create/$', mviews.ClientCreate.as_view()),
    url(r'^master_files/client/update/(?P<pk>[0-9]*)$', mviews.ClientUpdate.as_view()),
    url(r'^master_files/client/delete/(?P<pk>[0-9]*)$',
        mviews.ClientDelete.as_view()),

    url(r'^master_files/user/create/$', mviews.UserCreate.as_view()),
    url(r'^master_files/user/update/(?P<pk>[0-9]*)$',
                mviews.UserUpdate.as_view()),

    url(r'^master_files/config/create/$', mviews.ConfigCreate.as_view()),
    url(r'^master_files/config/update/(?P<pk>[0-9]*)$',
                        mviews.ConfigUpdate.as_view()),

    url(r'^master_files/route_aff/create/$', mviews.RouteAffCreate.as_view()),
    url(r'^master_files/route_aff/update/(?P<pk>[0-9]*)$',
                        mviews.RouteAffUpdate.as_view()),


    url(r'^reports/monthly_job_report/$', rviews.MonthlyJobReport.as_view()),
    url(r'^reports/weekly_job_report/$', rviews.WeeklyReport.as_view()),
    url(r'^reports/summary_delivery/$', rviews.SummaryDeliveryInstructions.as_view()),
    
    url(r'^ajax_data_table/(?P<model>[a-zA-Z0-9]*)$', mviews.ajax_data_table),
    url(r'^test/$', rviews.bible_send),
    # url(r'^sweet/(?P<do_id>[0-9]+)/(?P<job_id>[0-9]+)/$', gssviews.api_get_gss_image),
]
