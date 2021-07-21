import mimetypes
import traceback

from linebot import LineBotApi
from linebot.exceptions import LineBotApiError
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselTemplate, \
    ImageCarouselColumn, URITemplateAction, PostbackTemplateAction, ButtonsTemplate, FlexSendMessage, BubbleContainer, \
    BoxComponent, URIAction, ImageComponent, TextComponent


def _line_push_message(line_channel_access_token, line_user_id, base_message):
    """
    Sends a single message to a single user using the LINE api
    :param line_channel_access_token: token to access LINE api
    :param line_user_id: id of LINE user
    :param base_message: of type BaseMessage
    """
    line_bot_api = LineBotApi(line_channel_access_token)

    try:
        line_bot_api.push_message(
            line_user_id,
            base_message
        )
    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)


def _line_send_multicast(line_channel_access_token, user_list, base_message):
    print("made it to _line_send_multicast")

    """
    Sends a multicast message using LINE api
    :param end_user_info:
    :param user_list: list of line_user ids limited to a max size of 150
    :param base_message: of type BaseMessage
    """
    if len(user_list) > 150:
        raise AttributeError('user_list argument exceeded the magimum size of 150 users!')
    line_bot_api = LineBotApi(line_channel_access_token)
    try:
        line_bot_api.multicast(
            user_list,
            base_message
        )

    except LineBotApiError as e:
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)


def _chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def _line_send_bulk_message(line_channel_access_token, user_list, message, message_type):
    # build id_list using line_user_id
    id_list = [i.get_attribute_json('line_user_id') for i in user_list]
    # send out messages in chunks no larger than 150 users
    chunked_list = list(_chunks(id_list, 150))

    for chunk in chunked_list:
        if message_type.name == "text":
            _line_send_multicast(line_channel_access_token, chunk, TextSendMessage(text=message))
        if message_type.name == "image":
            _line_send_multicast(line_channel_access_token, chunk, _format_image_message_for_line(url=message))
        if message_type.name == "file":
            _line_send_multicast(line_channel_access_token, chunk, _format_file_message_for_line(url=message))


def line_send_message(line_channel_access_token, recipients, message, options, type='text'):
    if isinstance(recipients, str) or isinstance(recipients, int):
        _line_push_message(line_channel_access_token, recipients, message)
    elif isinstance(recipients, list):
        _line_send_bulk_message(line_channel_access_token, recipients, message)


"""
Push Message functions that push a single messages to a single user
"""


def line_text_send_message(access_token, end_user, message):
    line_user_id = end_user.get_attribute_json('line_user_id')

    _line_push_message(
        access_token,
        line_user_id,
        TextSendMessage(text=message)
    )


def line_image_send_message(access_token, end_user, content_json):
    line_user_id = end_user.get_attribute_json('line_user_id')

    _line_push_message(access_token, line_user_id, _format_image_message_for_line(url=content_json))


def line_file_send_message(access_token, end_user, content_json):
    line_user_id = end_user.get_attribute_json('line_user_id')

    _line_push_message(access_token, line_user_id, _format_file_message_for_line(url=content_json))


def line_option_send_message(access_token, end_user, message, options):
    line_user_id = end_user.get_attribute_json('line_user_id')

    action_list = []
    actions = options
    for action in actions:
        action_obj = PostbackTemplateAction(
            label=action["title"],
            data=action["payload"]
        )
        action_list.append(action_obj)

    if len(action_list) >= 4:
        action_list = action_list[0:4]

    buttons_template_message = TemplateSendMessage(
        alt_text='SELECT Button',
        template=ButtonsTemplate(
            text=message,
            actions=action_list
        )
    )

    _line_push_message(
        access_token,
        line_user_id,
        buttons_template_message
    )


def _format_image_message_for_line(url):
    mimetype, encoding = mimetypes.guess_type(url)

    # if ".JPEG" in url or ".jpeg" in url or ".JPG" in url or ".jpg" in url:
    # LINE doesn't directly support animated image types and will parse them as static instead
    if mimetype and mimetype.startswith('image'):
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
    else:
        image_message = TemplateSendMessage(
            alt_text='File View',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url=url,
                        action=URITemplateAction(
                            label='View on Web',
                            uri=url,
                        )
                    )
                ]
            )
        )

    return image_message


def _format_file_message_for_line(url):
    # todo proper validation
    file_name = url.split("/")[-1]

    file_message = FlexSendMessage(
        alt_text="hello",
        contents=BubbleContainer(
            direction='ltr',
            action=URIAction(label=file_name, uri=url),
            body=(BoxComponent(
                layout='horizontal',
                paddingAll='80px',
                contents=[ImageComponent(
                    url="https://s3.ap-northeast-1.amazonaws.com/data.local.smartby.ai/media/nchat/147/file_icon.png",
                    size="xxs",
                    margin="none",
                    align="start",
                    flex=0
                ),
                TextComponent(
                    text=file_name,
                    size='md',
                    align='start',
                    wrap=True,
                    margin="md",
                    gravity="center",
                    flex=1
                )]
                )
            )
        )
    )

    return file_message
