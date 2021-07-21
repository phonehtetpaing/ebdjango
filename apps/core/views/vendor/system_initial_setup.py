from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db import transaction
import string
import random
import datetime
from django.conf import settings

# import models
from django.contrib.auth.models import User
from apps.core.models.vendor import Vendor
from apps.core.models.vendor_branch import VendorBranch
from apps.core.models.auto_message_condition import AutoMessageCondition
from apps.core.models.auto_message_type import AutoMessageType
from apps.core.models.tag_category import TagCategory
from apps.core.models.vendor_event_settings import VendorEventSettings
from apps.core.models.end_user_story import EndUserStory
from apps.core.models.end_user_story_template_category import EndUserStoryTemplateCategory
from apps.core.models.end_user_story_template import EndUserStoryTemplate
from apps.core.models.payload import Payload
from apps.core.models.end_user_state import EndUserState
from apps.core.models.messaging_api_type import MessagingAPIType
from apps.core.models.message_block import MessageBlock
from apps.core.models.message_sequence import MessageSequence

# import views
from apps.core.views.vendor_common.login_user_info import *
from apps.core.views.vendor_common.oem_setup import *


@login_required
def list(request):
    """ vendor list """
    if not is_setup_approved(request):
        return redirect("/")

    namespace = get_namespace(request)
    service_id = get_service_id(request)

    try:
        if service_id is not None:
            if in_group(request.user, "system") and is_oem_admin(request):
                vendor_list = get_oem_vendor_list(request)
                vendors = Vendor.objects.filter(service_id=service_id, id__in=vendor_list, is_delete=False).order_by(
                    "-regist_dt").all()

            elif in_group(request.user, "system") and is_oem_admin(request)==False:
                vendors = Vendor.objects.filter(service_id=service_id, is_delete=False).order_by("-regist_dt").all().order_by("-regist_dt").all()

            else:
                return redirect("/")

        else:
            return redirect("/")

    except Exception as e:
        return redirect("/")

    context = {
        "vendors": vendors,
        "namespace": namespace
    }

    return render(request, "vendor/system_initial_setup_list.html", context)


@login_required
def detail(request, vendor_id=None):
    """ Vendor detail """
    if not is_setup_approved(request):
        return redirect("/")

    namespace = get_namespace(request)
    service_id = get_service_id(request)
    oem_url = get_oem_url(request)

    if is_initial_setup(request, vendor_id):

        vendor = Vendor.objects.filter(id=vendor_id).first()
        vendor_branch = VendorBranch.objects.filter(vendor=vendor).first()
        auto_message_conditions = AutoMessageCondition.objects.filter(vendor_branch=vendor_branch,
                                                                      is_delete=False).all()

        line_access_url = settings.ROOT_URL + "/" + oem_url + "/line/" + vendor.line_access_url_part + "/"
        fbms_access_url = settings.ROOT_URL + "/" + oem_url + "/fbms/" + vendor.fbms_access_url_part + "/"

        vendor_user = VendorUser.objects.filter(vendor_branch=vendor_branch, is_delete=False).order_by(
            "regist_dt").first()

        login_text = """
=========================
【ログイン情報】

[URL] 
   {login_url}

[Username]
   {username}

[Password]

=========================
         """.format(login_url=settings.ROOT_URL, username=vendor_user.email).strip()

        if is_oem_admin(request):
            oem_admin_flg = True
            vendor_list = get_oem_vendor_list(request)
            vendors = Vendor.objects.filter(service_id=service_id, id__in=vendor_list, is_delete=False).order_by(
                "-regist_dt").all()
        else:
            oem_admin_flg = False
            vendors = Vendor.objects.filter(service_id=service_id, is_delete=False).order_by("-regist_dt").all()

        context = {
            "vendors": vendors,
            "vendor": vendor,
            "vendor_branch": vendor_branch,
            "auto_message_conditions": auto_message_conditions,
            "login_text": login_text,
            "line_access_url": line_access_url,
            "fbms_access_url": fbms_access_url,
            "oem_admin_flg": oem_admin_flg,
            "namespace": namespace
        }

        return render(request, "vendor/system_initial_setup_detail.html", context)

    else:
        return redirect("/")


@login_required
def edit(request, vendor_id=None):
    """ edit """
    if not is_setup_approved(request):
        return redirect("/")

    oem_url = get_oem_url(request)

    if is_initial_setup(request, vendor_id):

        vendor = Vendor.objects.filter(id=vendor_id).first()
        vendor.company_name = request.POST["company_name"]
        vendor.fbms_access_token = request.POST["fbms_access_token"]
        vendor.line_access_token = request.POST["line_access_token"]
        vendor.line_verify_token = request.POST["line_verify_token"]

        if "oem_service_url" in request.POST:
            oem_service_url = request.POST["oem_service_url"]
            if len(oem_service_url) == 0:
                vendor.oem_service_url = None
                vendor.oem_service_namespace = None

            else:
                vendor.oem_service_url = oem_service_url
                vendor.oem_service_namespace = oem_service_url

        else:
            vendor.oem_service_url = None
            vendor.oem_service_namespace = None

        if "fbms_public_url" in request.POST and "line_public_url" in request.POST:
            vendor.fbms_public_url = request.POST["fbms_public_url"]
            vendor.line_public_url = request.POST["line_public_url"]

        # Replace MessageBlock / Sequence
        template_id = None
        if "template_id" in request.POST:
            if len(request.POST["template_id"]) != 0:
                template_id = int(request.POST["template_id"])
        # if a template was selected copy message blocks
        if template_id:
            vendor_branch = VendorBranch.objects.filter(cd="00001", vendor_id=vendor_id).first()
            copy_message_sequence(template_id, vendor_branch)

        vendor.save()

        return redirect("/" + oem_url + "/system/initial/setup/")

    else:
        return redirect("/")


@login_required
def new(request):
    if not is_setup_approved(request):
        return redirect("/")

    namespace = get_namespace(request)
    service_id = get_service_id(request)

    """ new """
    if in_group(request.user, "system"):
        auto_message_types = AutoMessageType.objects.filter(is_delete=False).all()
        if in_group(request.user, "system") and is_oem_admin(request):
            vendor_list = get_oem_vendor_list(request)
            vendors = Vendor.objects.filter(service_id=service_id, id__in=vendor_list, is_delete=False).order_by(
                "-regist_dt").all()

        elif in_group(request.user, "system"):
            vendors = Vendor.objects.filter(service_id=service_id, is_delete=False).order_by("-regist_dt").all()

        # create vendor data
        mmddhhmm = datetime.datetime.now().strftime('%m%d-%H%M')
        vendor_code = mmddhhmm
        vendor_branch_code = "00001"
        vendor_branch_name = "branch_" + vendor_branch_code

        # set default value
        default_registration_dt_name = "登録日時"

        # create password
        password = random_character(10)

        # create access a part of URL
        fbms_access_url_part = ""
        line_access_url_part = ""
        fbms_verify_token = ""

        while (True):
            fbms_access_url_part = "fb" + random_character(48)
            line_access_url_part = random_numbers(9)
            fbms_verify_token = random_character(10)

            # check if exists
            vendor_fb = Vendor.objects.filter(fbms_access_url_part=fbms_access_url_part).first()
            vendor_ln = Vendor.objects.filter(line_access_url_part=line_access_url_part).first()
            if (not vendor_fb) and (not vendor_ln):
                break

        if is_oem_admin(request):
            oem_admin_flg = True
        else:
            oem_admin_flg = False

        context = {
            "vendors": vendors,
            "vendor_code": vendor_code,
            "vendor_branch_code": vendor_branch_code,
            "vendor_branch_name": vendor_branch_name,
            "auto_message_types": auto_message_types,
            "default_registration_dt_name": default_registration_dt_name,
            "password": password,
            "fbms_access_url_part": fbms_access_url_part,
            "line_access_url_part": line_access_url_part,
            "fbms_verify_token": fbms_verify_token,
            "oem_admin_flg": oem_admin_flg,
            "namespace": namespace
        }

        return render(request, "vendor/system_initial_setup_new.html", context)

    else:
        return redirect("/")


@login_required
def add(request):
    """ add """
    if not is_setup_approved(request):
        return redirect("/")
    
    oem_url = get_oem_url(request)
    namespace = get_namespace(request)
    service_id = get_service_id(request)

    if in_group(request.user, "system"):
        try:
            with transaction.atomic():
                # Vendor Data
                cd = request.POST["cd"]
                company_name = request.POST["company_name"]
                fbms_access_url_part = request.POST["fbms_access_url_part"]
                fbms_access_token = request.POST["fbms_access_token"]
                fbms_verify_token = request.POST["fbms_verify_token"]
                line_access_url_part = request.POST["line_access_url_part"]
                line_access_token = request.POST["line_access_token"]
                line_verify_token = request.POST["line_verify_token"]

                # Vendor Branch Data
                branch_cd = request.POST["branch_cd"]
                branch_name = request.POST["branch_name"]

                # Auto Message Condition Data
                auto_message_condition_list = []
                auto_message_types = AutoMessageType.objects.filter(is_delete=False).all()
                for auto_message_type in auto_message_types:
                    param = "ac_" + str(auto_message_type.id)
                    auto_message_condition_dict = {
                        "auto_message_type_id": auto_message_type.id,
                        "auto_message_condition_name": request.POST[param]
                    }
                    auto_message_condition_list.append(auto_message_condition_dict)

                # Vendor User
                first_name = request.POST["first_name"]
                last_name = request.POST["last_name"]
                email = request.POST["email"]
                password = request.POST["password"]

                # Create New Vendor
                vendor = Vendor()
                vendor.service_id = service_id
                vendor.cd = cd
                vendor.company_name = company_name

                base_url = "https://smartby.ai/"
                vendor.fbms_access_url_part = fbms_access_url_part
                vendor.fbms_public_url = (base_url + fbms_access_url_part)
                vendor.fbms_access_token = fbms_access_token
                vendor.fbms_verify_token = fbms_verify_token
                vendor.line_access_url_part = line_access_url_part
                vendor.line_public_url = (base_url + line_access_url_part)
                vendor.line_access_token = line_access_token
                vendor.line_verify_token = line_verify_token

                # OEM Adminの場合、oem_service_url は自分もものをセットする

                if "oem_service_url" in request.POST:
                    oem_service_url = request.POST["oem_service_url"]
                    if len(oem_service_url) == 0:
                        vendor.oem_service_url = None
                        vendor.oem_service_namespace = None

                    else:
                        vendor.oem_service_url = oem_service_url
                        vendor.oem_service_namespace = oem_service_url

                else:
                    vendor.oem_service_url = None
                    vendor.oem_service_namespace = None

                if "fbms_public_url" in request.POST and "line_public_url" in request.POST:
                    vendor.fbms_public_url = request.POST["fbms_public_url"]
                    vendor.line_public_url = request.POST["line_public_url"]

                vendor.save()

                # Create New Branch
                vendor_branch = VendorBranch()
                vendor_branch.vendor = vendor
                vendor_branch.cd = branch_cd
                vendor_branch.name = branch_name
                vendor_branch.is_google_calendar_ready = True
                vendor_branch.save()

                # Create Auto Message Conditions
                for ac in auto_message_condition_list:
                    auto_message_condition = AutoMessageCondition()
                    auto_message_condition.vendor_branch = vendor_branch
                    auto_message_condition.auto_message_type_id = ac["auto_message_type_id"]
                    auto_message_condition.name = ac["auto_message_condition_name"]
                    auto_message_condition.save()

                # Create Tag Category
                tag_category = TagCategory()
                tag_category.vendor_branch = vendor_branch
                tag_category.name = "dummy"
                tag_category.save()

                # Create VendorEventSettings
                vendor_event_settings = VendorEventSettings()
                vendor_event_settings.vendor_branch = vendor_branch
                vendor_event_settings.save()

                # Create Vendor User (Login User)
                auth_user = User.objects.create_user(username=email, email=email, password=password)
                auth_user.is_active = True
                auth_user.save()
                vendor_user = VendorUser()
                vendor_user.vendor_branch = vendor_branch
                vendor_user.auth_user = auth_user
                vendor_user.last_name = last_name
                vendor_user.first_name = first_name
                vendor_user.email = email
                vendor_user.save()

                # Create MessageBlock / Sequence
                template_id = None
                if "template_id" in request.POST:
                    if len(request.POST["template_id"]) != 0:
                        template_id = int(request.POST["template_id"])

                # if a template was selected copy message blocks
                if template_id:
                    copy_message_sequence(template_id, vendor_branch)
                # else init default
                else:
                    message_block = MessageBlock()
                    message_block.admin_text = "START"
                    message_block.messaging_api_param_json = "[]"
                    message_block.is_delete = False
                    message_block.vendor_branch = vendor_branch
                    message_block.save()

                    message_sequence = MessageSequence()
                    message_sequence.admin_text = "GET_STARTED"
                    message_sequence.is_delete = False
                    message_sequence.start_block = message_block
                    message_sequence.vendor_branch = vendor_branch
                    message_sequence.save()

        except Exception as e:
            print("ERROR:" + e)

        context = {
            "namespace": namespace
        }

        return redirect("/" + oem_url + "/system/initial/setup/")

    else:
        return redirect("/")


def copy_message_sequence(from_vendor_id, to_vendor):
    """
        First deletes all message sequences and blocks from a vendor and then
        copies all message blocks from one vendor to another and follows up
        by copying the first message sequence
    """
    # delete all existing message blocks
    MessageSequence.objects.filter(vendor_branch=to_vendor).all().delete()
    MessageBlock.objects.filter(vendor_branch=to_vendor).all().delete()

    # todo update this to keep multiple message sequences in mind when updating to multiple.
    # gather all blocks we want to use as a template
    message_sequence = MessageSequence.objects.filter(vendor_branch_id=from_vendor_id).first()
    # but exclude the start block
    message_blocks = MessageBlock.objects.filter(vendor_branch_id=from_vendor_id).exclude(id=message_sequence.start_block.id)

    # copy over the start sequence and the corrosponding start block
    if message_sequence:
        message_sequence.id = None

        tmp_start_block = message_sequence.start_block
        tmp_start_block.id = None
        tmp_start_block.vendor_branch = to_vendor
        tmp_start_block.save()

        message_sequence.start_block = tmp_start_block
        message_sequence.vendor_branch = to_vendor
        message_sequence.save()

    for block in message_blocks:
        block.id = None
        block.vendor_branch = to_vendor
        block.save()

    return


def in_group(user, team_name):
    if user.groups.filter(name=team_name).exists():
        return True
    else:
        return False


def create_end_user_story(vendor_branch_id, template_category_id):
    """
        ・事前準備：テンプレート種別テーブル作成
        ・json、payload、enduserステータス、apiタイプ名、TODOタイトル/フラグ を一つのテンプレートとしてテーブルに保存
        ・実装
            テーブルを元にして・・
            1. payload レコード作成 (return 名称とidの組み合わせ： payload["test"]⇛1がかえる）
            2. Stateレコード作成
            3. IDを使って、end_user_storyを作成
            """

    # TODO:
    end_user_story_template_category = EndUserStoryTemplateCategory.objects.filter(id=template_category_id).first()
    end_user_story_templates = EndUserStoryTemplate.objects.filter(
        end_user_story_template_category=end_user_story_template_category, is_delete=False).all()

    for end_user_story_template in end_user_story_templates:
        payload = get_payload(vendor_branch_id, end_user_story_template.payload)
        end_user_state = get_user_state(vendor_branch_id, end_user_story_template.end_user_state)
        next_end_user_state = get_user_state(vendor_branch_id, end_user_story_template.next_end_user_state)
        messaging_api_type = get_messageing_api_type(end_user_story_template.messaging_api_type)

        end_user_story = EndUserStory()
        end_user_story.messaging_api_param_json = end_user_story_template.messaging_api_param_json
        end_user_story.run_order_num = end_user_story_template.run_order_num
        end_user_story.end_user_state_id = int(end_user_state)
        end_user_story.next_end_user_state_id = int(next_end_user_state)
        end_user_story.messaging_api_type_id = int(messaging_api_type)
        end_user_story.next_end_user_state_id = int(next_end_user_state)
        end_user_story.payload_id = payload
        end_user_story.is_todo = end_user_story_template.is_todo
        end_user_story.todo_title = end_user_story_template.todo_title
        end_user_story.save()

    """
    SELECT
        '',
        core_payload.value,
        core_enduserstate.cd,
        core_messagingapitype.cd,
        messaging_api_param_json,
        run_order_num,
        is_todo,
        todo_title,
        '',
        '',
        '',
        1
    FROM messaging_platform.core_enduserstory
    left join core_payload
    on core_payload.id = core_enduserstory.payload_id
    left join core_enduserstate
    on core_enduserstate.id = core_enduserstory.end_user_state_id
    left join core_messagingapitype
    on core_messagingapitype.id = core_enduserstory.messaging_api_type_id
    order by payload_id, run_order_num

    """
    # ・Payload
    # ・EndUserStory
    # core_enduserstate

    return True


def get_payload(vendor_branch_id, payload_text):
    payload = Payload.objects.filter(vendor_branch_id=vendor_branch_id, value=payload_text).first()
    if payload:
        return payload.id

    else:
        payload = Payload()
        payload.value = payload_text
        payload.vendor_branch_id = vendor_branch_id
        # TODO: tag_name
        # payload.tag_name = ""
        payload.save()
        return payload.id


def get_user_state(vendor_branch_id, state_name):
    end_user_state = EndUserState.objects.filter(cd=state_name).first()
    if end_user_state:
        return end_user_state.id

    else:
        end_user_state = EndUserState()
        end_user_state.vendor_branch_id = vendor_branch_id
        end_user_state.cd = state_name
        end_user_state.save()
        return end_user_state.id


def get_messageing_api_type(messaging_api_type_name):
    messaging_api_type = MessagingAPIType.objects.filter(cd=messaging_api_type_name).first()
    if messaging_api_type:
        return messaging_api_type.id

    else:
        return None


def random_character(n):
    c = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([random.choice(c) for i in range(n)])


def random_numbers(n):
    c = string.digits
    return ''.join([random.choice(c) for i in range(n)])