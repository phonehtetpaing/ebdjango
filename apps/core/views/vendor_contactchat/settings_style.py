import ast
import json
import boto3
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings


# import models
from apps.core.models.vendor import Vendor

# import views
from apps.core.views.vendor_common.login_user_info import *


@login_required
def index(request):
    """ list """
    user_obj = get_login_user_objects(request)

    # fetch css string from vendor object
    vendor_branch = user_obj["vendor_branch"]
    vendor = Vendor.objects.filter(id=vendor_branch.vendor.id).first()
    css_string = vendor.contactchat_css

    # convert css string to dict
    if css_string:
        css_dict = ast.literal_eval(css_string)
    else:
        css_dict = {}

    if request.method == "POST":
        robottextcolor = request.POST['--robottextcolor']
        robotbubblecolor = request.POST['--robotbubblecolor']
        usertextcolor = request.POST['--usertextcolor']
        userbubblecolor = request.POST['--userbubblecolor']
        chatbackgroundcolor = request.POST['--chatbackgroundcolor']
        submitbuttoncolor = request.POST['--submitbuttoncolor']

        roboticon = request.POST['--roboticon']
        usericon = request.POST['--usericon']

        fontsize = request.POST['--fontsize']
        fontfamily = request.POST['--fontfamily']
        fontstyle = request.POST['--fontstyle']

        css_dict['robottextcolor'] = robottextcolor
        css_dict['robotbubblecolor'] = robotbubblecolor
        css_dict['usertextcolor'] = usertextcolor
        css_dict['userbubblecolor'] = userbubblecolor
        css_dict['chatbackgroundcolor'] = chatbackgroundcolor
        css_dict['submitbuttoncolor'] = submitbuttoncolor
        css_dict['usericon'] = usericon
        css_dict['roboticon'] = roboticon
        css_dict['fontsize'] = fontsize
        css_dict['fontfamily'] = fontfamily
        css_dict['fontstyle'] = fontstyle

        json_dump = json.dumps(css_dict)
        vendor.contactchat_css = json_dump
        vendor.save()

        # save css to S3 bucket under vendor identifier
        save_css(create_css(css_dict), vendor.contactchat_access_url_part)

    cc_base_url = settings.CONTACTCHAT_BASE_URL

    context = {
        "title": "Vendor Settings",
        "path": ["Settings", "Style Settings"],
        "vendor": user_obj["vendor_branch"].vendor,
        "css_dict": css_dict,
        "cc_base_url": cc_base_url,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor_contactchat/settings_style.html", context)


def save_css(file, name):
    # Create an S3 client
    s3 = boto3.resource('s3')

    filename: str = f'{name}.css'
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    # uploads a file to s3 and sets file type and cache control
    s3.Bucket(bucket_name).put_object(Key=f'cc/css/{filename}', Body=file, ContentType='text/css',
                                      CacheControl='max-age=86400', ACL='public-read')


def create_css(value_map):
    css_template_string = """
    :root {{
      --robottextcolor: #{robottextcolor};
      --robotbubblecolor: #{robotbubblecolor};
      --usertextcolor: #{usertextcolor};
      --userbubblecolor: #{userbubblecolor};
      --chatbackgroundcolor: #{chatbackgroundcolor};
      --submitbuttoncolor: #{submitbuttoncolor};
      --usericon: url({usericon});
      --roboticon: url({roboticon});
      --fontsize: {fontsize};
      --fontfamily: {fontfamily};
      --fontstyle: {fontstyle};
    }}
    
    .custom-theme .conversational-form {{
      font-size: var(--fontsize) !important;
    }}
    .custom-theme .conversational-form-inner {{
      background-color: var(--chatbackgroundcolor);
    }}
    
    .custom-theme .conversational-form cf-chat-response.robot text {{
      color: var(--robottextcolor) !important;
    }}
    .custom-theme .conversational-form cf-chat-response.robot text > p {{
      color: var(--robottextcolor) !important;
      background: var(--robotbubblecolor);
      font-family: var(--fontfamily) !important;
      font-style: var(--fontstyle) !important;
    }}
    
    .custom-theme .conversational-form cf-chat-response.robot thumb {{
      background-color: var(--robotbubblecolor);
    }}
    
    .custom-theme .conversational-form cf-chat-response.user text {{
      color: var(--usertextcolor) !important;
    }}
    .custom-theme .conversational-form cf-chat-response.user text > p {{
      color: var(--usertextcolor) !important;
      background: var(--userbubblecolor);
      font-family: var(--fontfamily) !important;
      font-style: var(--fontstyle) !important;
    }}
    .custom-theme .conversational-form cf-chat-response.user thumb {{
      background-color: var(--userbubblecolor);
    }}
    
    .custom-theme.conversational-form cf-input-button {{
        background: var(--robotbubblecolor);
        height: 42px;
        width: 42px;
        border: none;
    }}
    .custom-theme.conversational-form.cf-button {{
        color: var(--robottextcolor);
        background - color: var(--robotbubblecolor);
        border - color:  # dddddd;
    }}
    .custom-theme .conversational-form cf-input-button {{
      background: var(--submitbuttoncolor);
      height: 32px;
      width: 32px;
      border: none;
      bottom: 8px;
    }}
    
    .custom-theme .conversational-form cf-chat-response.user thumb {{
      background-image: var(--usericon) !important;
      background-color: var(--userbubblecolor);
      background-size: 20px 20px;
      background-repeat: no-repeat;
    }}
    .custom-theme .conversational-form cf-chat-response.robot thumb {{
      background-image: var(--roboticon) !important;
      background-color: var(--robotbubblecolor);
      background-size: 20px 20px;
      background-repeat: no-repeat;
    }}
    
    """.format_map(value_map)

    return css_template_string
