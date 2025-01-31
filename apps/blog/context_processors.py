# -*- coding: utf-8 -*-
import datetime
import json
from django.conf import settings
from .utils import (site_full_url, get_site_create_day)


# 自定义上下文管理器
def settings_info(request):
    site_create_day = get_site_create_day(settings.SITE_CREATE_DATE)
    return {
        'this_year': datetime.datetime.now().year,
        'site_create_date': site_create_day[0],
        'site_create_year': site_create_day[1],
        'site_logo_name': settings.SITE_LOGO_NAME,
        'site_end_title': settings.SITE_END_TITLE,
        'site_description': settings.SITE_DESCRIPTION,
        'site_keywords': settings.SITE_KEYWORDS,
        'tool_flag': settings.TOOL_FLAG,
        'api_flag': settings.API_FLAG,
        'cnzz_protocol': settings.CNZZ_PROTOCOL,
        '51la': settings.LA51_PROTOCOL,
        'beian': settings.BEIAN,
        'my_github': settings.MY_GITHUB,
        'site_verification': settings.MY_SITE_VERIFICATION,
        'site_url': site_full_url(),
        'private_links': json.loads(settings.PRIVATE_LINKS),
    }
