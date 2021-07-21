import ast
import json

from django import template
register = template.Library()

from apps.qa.models.end_user_questionnaire import EndUserQuestionnaire
from apps.qa.models.response import Response
from apps.core.models.end_user import EndUser


@register.filter("get_qa_response_count")
def get_qa_response_count(value):
    if value:
        end_user_questionnaire = EndUserQuestionnaire.objects.filter(id=value).first()
        if end_user_questionnaire:
            responses = Response.objects.filter(end_user_questionnaire=end_user_questionnaire).count()
            return responses
        else:
            return 0
    else:
        return 0


@register.filter("get_question_response")
def get_question_response(value):
    if value:
        response = value
        response_content = response.content
        if response.questionnaire_question.question.type.name == 'option':
            response_content_id = int(response_content[2])
            response_opt = ast.literal_eval(response.questionnaire_question.question.question_options)
            formatted_response = response_opt[response_content_id]
            return formatted_response
        elif response.questionnaire_question.question.type.name == 'multioption':
            json_format = response_content.replace("'", '"')
            json_response = ast.literal_eval(json_format)
            response_opt = ast.literal_eval(response.questionnaire_question.question.question_options)
            formatted_response = ''
            for response_val in json_response:
                formatted_response += response_opt[int(response_val)] + ','
            return formatted_response
        else:
            return response.content


@register.filter("loadjson")
def loadjson(data):
    if (data):
        return ast.literal_eval(data)
