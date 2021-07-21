import json
from django.shortcuts import render, redirect
from django.http import HttpResponse

# import models
from apps.core.models.tmp_entry import TmpEntry
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.end_user import EndUser
from apps.core.models.end_user_line import EndUserLINE

# import views
from apps.core.views.vendor_common.recome.welcome_message import *
from apps.core.views.bot_common.tag_settings import *

def user_registration_update(request):
    try:
        tmp_entry_id = int(request.POST["tmp_entry_id"])
        end_user_id = int(request.POST["end_user_id"])
        is_register = int(request.POST["is_register"])

        # Retrieve update data
        tmp_entry = TmpEntry.objects.filter(id=tmp_entry_id).first()
        branch_cd = tmp_entry.branch_code

        vendor_branch = VendorBranch.objects.filter(id=branch_cd).first()
        end_user = EndUser.objects.filter(id=end_user_id).first()
        end_user_line = EndUserLINE.objects.filter(end_user_id=end_user_id).first()
        # check if click "Yes"
        if is_register == 1:
            # Update end_user branch
            if vendor_branch and end_user:
                end_user.vendor_branch = vendor_branch
                end_user.save()

                # Add Tags
                set_tag(end_user, tmp_entry)

                # Send Thank you message
                if end_user_line:
                    thankyou_message(end_user.id)

                    # Close Page
                    context = {
                        "message": "ありがとうございます！",
                        "line_url":"https://line.me/R/ti/p/%40cxv4122b"
                    }

                else:
                    # Close Page
                    context = {
                        "message": "Try it again.",
                        "line_url": "https://line.me/R/ti/p/%40cxv4122b"
                    }

        else:
            if vendor_branch and end_user:
                sorry_message(end_user.id)

            # Close Page
            context = {
                "message": "ありがとうございます！",
                "line_url": "https://line.me/R/ti/p/%40cxv4122b"
            }

        # Delete tmp entry record
        TmpEntry.objects.filter(id=tmp_entry_id).delete()

        return render(request, "common/close.html", context)

    except Exception as e:
        context = {
            "message": "Try it again.",
            "line_url": "https://line.me/R/ti/p/%40cxv4122b"
        }
        return render(request, "common/close.html", context)
