# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0036_question_question_options'),
    ]

    operations = [
        migrations.RunSQL('ALTER TABLE qa_coupon DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_coupon CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_couponclaim DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_couponclaim CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_coupontype DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_coupontype CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_enduserquestionnaire DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_enduserquestionnaire CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_matrigger DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_matrigger CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_matriggertype DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_matriggertype CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_message DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_message CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_notificationservice DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_notificationservice CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_notificationsetting DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_notificationsetting CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_plan DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_plan CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_question DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_question CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_questionnaire DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_questionnaire CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_questionnairequestion DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_questionnairequestion CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_questiontype DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_questiontype CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_response DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_response CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_senbayuser DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_senbayuser CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_service DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_service CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_vendorplan DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_vendorplan CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_vendorservice DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_vendorservice CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_vendoruser DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_vendoruser CONVERT TO CHARACTER SET utf8;'),

        # other tables

        migrations.RunSQL('ALTER TABLE qa_product DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_product CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_productcategory DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_productcategory CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_receivinghistory DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_receivinghistory CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_shippinghistory DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_shippinghistory CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_stock DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_stock CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_stockspace DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_stockspace CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_vendorbusinesspartner DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_vendorbusinesspartner CONVERT TO CHARACTER SET utf8;'),

        migrations.RunSQL('ALTER TABLE qa_vendorbusinesspartnertag DEFAULT CHARACTER SET utf8;'),
        migrations.RunSQL('ALTER TABLE qa_vendorbusinesspartnertag CONVERT TO CHARACTER SET utf8;'),
    ]
