from django.contrib import admin

# Register your models here.
from apps.core.models.service import Service
admin.site.register(Service)
from apps.core.models.vendor import Vendor
admin.site.register(Vendor)
from apps.core.models.vendor import Preset
admin.site.register(Preset)
from apps.core.models.vendor_branch import VendorBranch
admin.site.register(VendorBranch)
from apps.core.models.vendor_event_settings import VendorEventSettings
admin.site.register(VendorEventSettings)
from apps.core.models.vendor_user import VendorUser
admin.site.register(VendorUser)
from apps.core.models.payload import Payload
admin.site.register(Payload)
from apps.core.models.end_user_state import EndUserState
admin.site.register(EndUserState)
from apps.core.models.end_user import EndUser
admin.site.register(EndUser)
from apps.core.models.end_user_facebook import EndUserFacebook
admin.site.register(EndUserFacebook)
from apps.core.models.end_user_line import EndUserLINE
admin.site.register(EndUserLINE)
from apps.core.models.end_user_auto_message import EndUserAutoMessage
admin.site.register(EndUserAutoMessage)
from apps.core.models.end_user_story import EndUserStory
admin.site.register(EndUserStory)
from apps.core.models.end_user_story_history import EndUserStoryHistory
admin.site.register(EndUserStoryHistory)
from apps.core.models.end_user_story_template_category import EndUserStoryTemplateCategory
admin.site.register(EndUserStoryTemplateCategory)
from apps.core.models.end_user_story_template import EndUserStoryTemplate
admin.site.register(EndUserStoryTemplate)
from apps.core.models.tag_category import TagCategory
admin.site.register(TagCategory)
from apps.core.models.tag import Tag
admin.site.register(Tag)
from apps.core.models.todo_action_status import TodoActionStatus
admin.site.register(TodoActionStatus)
from apps.core.models.event_category import EventCategory
admin.site.register(EventCategory)
from apps.core.models.event import Event
admin.site.register(Event)
from apps.core.models.event_reservation import EventReservation
admin.site.register(EventReservation)
from apps.core.models.event_reservation_status import EventReservationStatus
admin.site.register(EventReservationStatus)
from apps.core.models.messaging_api_type import MessagingAPIType
admin.site.register(MessagingAPIType)
from apps.core.models.auto_message_type import AutoMessageType
admin.site.register(AutoMessageType)
from apps.core.models.auto_message_condition import AutoMessageCondition
admin.site.register(AutoMessageCondition)
from apps.core.models.auto_message_trigger import AutoMessageTrigger
admin.site.register(AutoMessageTrigger)
from apps.core.models.auto_message_controller import AutoMessageController
admin.site.register(AutoMessageController)
from apps.core.models.auto_message_history import AutoMessageHistory
admin.site.register(AutoMessageHistory)
from apps.core.models.manual_message_overview import ManualMessageOverview
admin.site.register(ManualMessageOverview)
from apps.core.models.manual_message_controller import ManualMessageController
admin.site.register(ManualMessageController)
from apps.core.models.manual_message_history import ManualMessageHistory
admin.site.register(ManualMessageHistory)
from apps.core.models.worker_sqs_status import WorkerSQSStatus
admin.site.register(WorkerSQSStatus)
from apps.core.models.tmp_entry import TmpEntry
admin.site.register(TmpEntry)
from apps.core.models.tmp_registration_entry import TmpRegistrationEntry
admin.site.register(TmpRegistrationEntry)
from apps.core.models.affiliate import Affiliate
admin.site.register(Affiliate)
