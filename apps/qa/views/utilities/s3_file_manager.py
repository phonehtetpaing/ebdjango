import boto3
import traceback
from django.conf import settings


def save_css(file, name):
    # Create an S3 client
    s3 = boto3.resource('s3')

    filename: str = f'{name}.css'
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    if settings.MODE == 'LOCAL':
        # saves file locally
        with open(filename, "w+") as f:
            f.write(file)

    else:
        try:
            # uploads a file to s3 and sets file type and cache control
            s3.Bucket(bucket_name).put_object(Key=f'cc/css/{filename}', Body=file, ContentType='text/css',
                                          CacheControl='max-age=86400', ACL='public-read')
        except Exception as e:
            print("Exception, unable to save CSS to S3: " + str(e))
            print(traceback.format_exc())




def save_static_text(file, name):
    # Create an S3 client
    s3 = boto3.resource('s3')

    filename: str = f'{name}.json'
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    if settings.MODE == 'LOCAL':
        with open(filename, "w+") as f:
            f.write(file)

    else:
        try:
            # uploads a file to s3 and sets file type and cache control
            s3.Bucket(bucket_name).put_object(Key=f'cc/json/{filename}', Body=file, ContentType='application/json',
                                      CacheControl='max-age=86400', ACL='public-read')
        except Exception as e:
            print("Exception, unable to save static text to S3: " + str(e))
            print(traceback.format_exc())

def read_static_text(name):
    # Create an S3 client
    s3 = boto3.resource('s3')

    filename: str = f'{name}.json'
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    if settings.MODE == 'LOCAL':
        try:
            with open(filename, "r") as f:
                return f.read()
        except Exception as e:
            print("Exception, unable to open static text: " + str(e))
            return None
    else:
        try:
            # returns a file from s3
            content_object = s3.Object(bucket_name, f'cc/json/{filename}')
            return content_object.get()['Body'].read().decode('utf-8')

        except Exception as e:
            print("Exception, unable to open static text on S3: " + str(e))
            print(traceback.format_exc())

def create_contactchat_css(value_map):
    css_template_string = """
    :root {{
      --robottextcolor: #{robottextcolor};
      --robotbubblecolor: #{robotbubblecolor};
      --usertextcolor: #{usertextcolor};
      --userbubblecolor: #{userbubblecolor};
      --chatbackgroundcolor: #{chatbackgroundcolor};
      --submitbuttoncolor: #{submitbuttoncolor};
      --windowcolor: #{windowcolor};
      --infotextcolor: #{infotextcolor};
      --usericon: url({usericon});
      --roboticon: url({roboticon});
      --fontsize: {fontsize};
      --fontfamily: {fontfamily};
      --fontstyle: {fontstyle};
    }}

    .widget-custom {{
      color: var(--infotextcolor) !important;
      background-color: var(--windowcolor) !important;
      background: var(--windowcolor) !important;
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