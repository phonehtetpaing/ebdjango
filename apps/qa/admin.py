from django.contrib import admin

# Register your models here.
from apps.qa.models.plan import Plan
admin.site.register(Plan)
from apps.qa.models.service import Service
admin.site.register(Service)
from apps.qa.models.vendor_plan import VendorPlan
admin.site.register(VendorPlan)
from apps.qa.models.vendor_service import VendorService
admin.site.register(VendorService)
from apps.qa.models.vendor_user import VendorUser
admin.site.register(VendorUser)
from apps.qa.models.message import Message
admin.site.register(Message)
from apps.qa.models.ma_trigger_type import MaTriggerType
admin.site.register(MaTriggerType)
from apps.qa.models.questionnaire import Questionnaire
admin.site.register(Questionnaire)
from apps.qa.models.questionnaire_template import QuestionnaireTemplate
admin.site.register(QuestionnaireTemplate)
from apps.qa.models.questionnaire_template_question import QuestionnaireTemplateQuestion
admin.site.register(QuestionnaireTemplateQuestion)
from apps.qa.models.question import Question
admin.site.register(Question)
from apps.qa.models.senbay_user import SenbayUser
admin.site.register(SenbayUser)
from apps.qa.models.vendor_business_partner import VendorBusinessPartner
admin.site.register(VendorBusinessPartner)
from apps.qa.models.vendor_business_partner_tag import VendorBusinessPartnerTag
admin.site.register(VendorBusinessPartnerTag)
from apps.qa.models.product_category import ProductCategory
admin.site.register(ProductCategory)
from apps.qa.models.stock_space import StockSpace
admin.site.register(StockSpace)
from apps.qa.models.product import Product
admin.site.register(Product)
from apps.qa.models.stock import Stock
admin.site.register(Stock)
from apps.qa.models.receiving_history import ReceivingHistory
admin.site.register(ReceivingHistory)
from apps.qa.models.shipping_history import ShippingHistory
admin.site.register(ShippingHistory)
