import ast
import json
import boto3
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse

import os
# import models
from apps.core.models.vendor import Vendor, Preset

# import views
from apps.core.views.vendor_common.login_user_info import *

def get_presets(request, preset_id=None):
    presets={}
    presets[1] = {"robottextcolor": "#2e1414", "robotbubblecolor": "#000000", "usertextcolor": "#000000", "userbubblecolor": "#000000", "chatbackgroundcolor": "#8e2525", "submitbuttoncolor": "#000000", "usericon": "https://upload.wikimedia.org/wikipedia/commons/2/27/Emojione_1F464.svg", "roboticon": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Emojione_1F916.svg", "fontfamily": "Arial", "fontstyle": "normal", "preset": "1"}
    presets[2] = {"robottextcolor": "#2e1414", "robotbubblecolor": "#000000", "usertextcolor": "#000000", "userbubblecolor": "#000000", "chatbackgroundcolor": "#000000", "submitbuttoncolor": "#ffff00", "usericon": "https://upload.wikimedia.org/wikipedia/commons/2/27/Emojione_1F464.svg", "roboticon": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Emojione_1F916.svg", "fontfamily": "Arial", "fontstyle": "normal", "preset": "2"}
    presets[3] = {"robottextcolor": "#2e1414", "robotbubblecolor": "#000000", "usertextcolor": "#000000", "userbubblecolor": "#000000", "chatbackgroundcolor": "#007bff", "submitbuttoncolor": "#6c757d", "usericon": "https://upload.wikimedia.org/wikipedia/commons/2/27/Emojione_1F464.svg", "roboticon": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Emojione_1F916.svg", "fontfamily": "Arial", "fontstyle": "normal", "preset": "3"}
    presets[4] = {"robottextcolor": "#2e1414", "robotbubblecolor": "#000000", "usertextcolor": "#000000", "userbubblecolor": "#000000", "chatbackgroundcolor": "#8e2525", "submitbuttoncolor": "#000000", "usericon": "https://upload.wikimedia.org/wikipedia/commons/2/27/Emojione_1F464.svg", "roboticon": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Emojione_1F916.svg", "fontfamily": "Arial", "fontstyle": "normal", "preset": "4"}
    preset_values=presets[preset_id];
    if not preset_values:
        return JsonResponse({"status": "match_not_found"})

    return JsonResponse(
        {
            "status": "match_found",
            "preset": {
                "chatbackgroundcolor": preset_values["chatbackgroundcolor"],
                "submitbuttoncolor": preset_values["submitbuttoncolor"],
            }
        }
    )


@login_required
def index(request):
    """ list """
    user_obj = get_login_user_objects(request)

    # fetch css string from vendor object
    vendor_branch = user_obj["vendor_branch"]
    vendor = Vendor.objects.filter(id=vendor_branch.vendor.id).first()
    css_string = vendor.contactchat_css
    presets = Preset.objects.all()

    # convert css string to dict
    if css_string:
        css_dict = ast.literal_eval(css_string)
    else:
        css_dict = {}

    if request.method == "POST":
        preset_id = request.POST['--preset']
        if preset_id != "0":
            css_dict['preset_id'] = preset_id
        else:
            # robottextcolor = '#' + request.POST['--robottextcolor']
            # robotbubblecolor = '#' + request.POST['--robotbubblecolor']
            # usertextcolor = '#' + request.POST['--usertextcolor']
            # userbubblecolor = '#' + request.POST['--userbubblecolor']
            # chatbackgroundcolor = '#' + request.POST['--chatbackgroundcolor']
            # submitbuttoncolor = '#' + request.POST['--submitbuttoncolor']
            robottextcolor = request.POST['--robottextcolor']
            robotbubblecolor = request.POST['--robotbubblecolor']
            usertextcolor = request.POST['--usertextcolor']
            userbubblecolor = request.POST['--userbubblecolor']
            chatbackgroundcolor = request.POST['--chatbackgroundcolor']
            submitbuttoncolor = request.POST['--submitbuttoncolor']
            roboticon = request.POST['--roboticon']
            usericon = request.POST['--usericon']

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
        "presets": presets,
        "cc_base_url": cc_base_url,
        "namespace": user_obj["service_namespace"]
    }

    return render(request, "vendor_contactchat/settings_style.html", context)


def save_css(file, name):
    # Create an S3 client
    # s3 = boto3.resource('s3')

    filename: str = f'{name}.css'
    # bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    # # uploads a file to s3 and sets file type and cache control
    # s3.Bucket(bucket_name).put_object(Key=f'cc/css/{filename}', Body=file, ContentType='text/css',
    #                                   CacheControl='max-age=86400', ACL='public-read')

    if os.path.exists('/Users/yp/Sites/projects/Javascript/ContactChat/public/css/accessurl00001.css'):
        os.remove('/Users/yp/Sites/projects/Javascript/ContactChat/public/css/accessurl00001.css')
        f = open(filename, "w")
        f.write(file)
        f.close()

        f = open(filename, "r")

        fs = FileSystemStorage(location=('/Users/yp/Sites/projects/Javascript/ContactChat/public/css'))
        fs.save(filename, f)
    else:
        f = open(filename, "a")
        f.write(file)
        f.close()

        f = open(filename, "r")

        fs = FileSystemStorage(location=('/Users/yp/Sites/projects/Javascript/ContactChat/public/css'))
        fs.save(filename, f)


def create_css(value_map):
    if value_map['preset_id']:
      preset_url=Preset.objects.filter(id=value_map['preset_id']).first().preset_url
      value_map['preset_url']=preset_url
      css_template_string = """
      @import url({preset_url});
      """.format_map(value_map)
    else:
      css_template_string = """
      :root {{
        --robottextcolor: {robottextcolor};
        --robotbubblecolor: {robotbubblecolor};
        --usertextcolor: {usertextcolor};
        --userbubblecolor: {userbubblecolor};
        --chatbackgroundcolor: {chatbackgroundcolor};
        --submitbuttoncolor: {submitbuttoncolor};
        --usericon: url({usericon});
        --roboticon: url({roboticon});
        --fontfamily: {fontfamily};
        --fontstyle: {fontstyle};
      }}
      
      .custom-theme .conversational-form-inner {{
        background-color: var(--chatbackgroundcolor);
      }}
      
      .custom-theme .conversational-form cf-chat-response.robot text {{
        color: var(--robottextcolor);
      }}
      .custom-theme .conversational-form cf-chat-response.robot text > p {{
        background: var(--robotbubblecolor);
        font-family: var(--fontfamily) !important;
        font-style: var(--fontstyle) !important;
      }}
      
      .custom-theme .conversational-form cf-chat-response.robot thumb {{
        background-color: var(--robotbubblecolor);
      }}
      
      .custom-theme .conversational-form cf-chat-response.user text {{
        color: var(--usertextcolor);
      }}
      .custom-theme .conversational-form cf-chat-response.user text > p {{
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
