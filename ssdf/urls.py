from django.conf.urls import include, url
from django.conf.urls.defaults import patterns
from django.conf.urls.static import static
from django.contrib import admin

from django.conf import settings

from rest_framework_nested import routers

from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet, GCMDeviceAuthorizedViewSet

from api.events.views import EventViewSet, EventTrackViewSet, EventTrackLevelViewSet, ScheduleItemViewSet, ScheduleItemHoursViewSet
from api.guide.views import GuideItemViewSet, GuideItemHoursViewSet
from api.competitions.views import CompetitionViewSet
from api.feed.views import FeedViewSet
from api.feedback.views import EventTrackLevelRateViewSet, ScheduleItemRateViewSet

router = routers.DefaultRouter()
router.register(r'events', EventViewSet, base_name='events')
router.register(r'feed', FeedViewSet, base_name='feeds')
router.register(r'device/apns', APNSDeviceAuthorizedViewSet)
router.register(r'device/gcm', GCMDeviceAuthorizedViewSet)

event_router = routers.NestedSimpleRouter(router, r'events', lookup='event')
event_router.register(r'tracks', EventTrackViewSet, base_name='track')
event_router.register(r'guide', GuideItemViewSet, base_name='guide')
event_router.register(r'competitions', CompetitionViewSet, base_name='competition')

guide_router = routers.NestedSimpleRouter(event_router, 'guide', lookup='guide')
guide_router.register(r'hours', GuideItemHoursViewSet, base_name='hours')

tracks_router = routers.NestedSimpleRouter(event_router, r'tracks', lookup='track')
tracks_router.register(r'levels', EventTrackLevelViewSet, base_name='levels')

levels_router = routers.NestedSimpleRouter(tracks_router, r'levels', lookup='level')
levels_router.register(r'schedule', ScheduleItemViewSet, base_name='schedule')
levels_router.register(r'feedback', EventTrackLevelRateViewSet, base_name='feedback')

schedule_router = routers.NestedSimpleRouter(levels_router, r'schedule', lookup='schedule')
schedule_router.register(r'hours', ScheduleItemHoursViewSet, base_name='hours')
schedule_router.register(r'feedback', ScheduleItemRateViewSet, base_name='feedback')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(event_router.urls)),
    url(r'^', include(guide_router.urls)),
    url(r'^', include(tracks_router.urls)),
    url(r'^', include(levels_router.urls)),
    url(r'^', include(schedule_router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG is False:
    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
