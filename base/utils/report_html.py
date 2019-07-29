import os
import time
import datetime
from functools import wraps
import traceback
import inspect
import html
import json
import pprint

import jsonpickle

from base.utils.settings import Environments
from base.utils.slack_notifier import SlackNotifier, SlackOptions


def decorator_loader(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(getattr(cls, attr)))
        return cls
    return decorate


def error_logger(func):
    @wraps(func)
    def wrap(self, *args, **kwargs):
        return wrap


def get_context(self):
    context = inspect.trace()[-1][0].f_locals
    if "self" in list(context):
        del context["self"]
    context = json.loads(jsonpickle.encode(context, max_depth=4))
    self_variables = {}
    for attr in dir(self):
        attr_value = getattr(self, attr)
        if not inspect.ismethod(attr_value) and not attr.startswith("_") and type(attr_value) in(
                bool, int, float, str, list, dict, tuple, set, type(None)):
            self_variables[attr] = getattr(self, attr)
    context_self = json.loads(jsonpickle.encode(self_variables, max_depth=4))
    context["self"] = context_self
    filter_keys(context, ["settings", "chrome_options", "driver", "py/object", "wait"])
    return context


def parse_browser_console_log(self):
    browser_log = self.driver.get_log("browser")
    log_output = ""
    for log in browser_log:
        log_output += log['level'] + " - " + log['message'] + " | Source: " + log['source'] + "<br>"
    return log_output


def create_error_html(self, error_log):
    with open(os.path.join(self.settings.project_dir,
                           "base", "utils", "error_records", "error_template.html"), "r") as file:
        data = file.read()
    data = data.replace("{case_name}", error_log['case_name'])
    data = data.replace("{timestamp}", error_log['timestamp'])
    data = data.replace("{error_message}", error_log['error_message'])
    data = data.replace("{img_src}", error_log['img_name'])
    data = data.replace("{case_title}", error_log['case_name'].split(" ")[0])
    data = data.replace("{console_log}", error_log['console_log'])
    data = data.replace("{context}", error_log['context'])
    html_location = os.path.join(self.settings.get_project_dir(),
                                 "base", "utils", "error_records", error_log['html_name'])
    with open(html_location, "w") as file:
        file.write(data)
        if self.settings.env in (Environments.JENKINS_TEST, Environments.JENKINS_DEPLOYMENT):
            print_html_dir = (self.settings.env_variables["JOB_URL"] + "ws/base/utils/error_records/" +
                              error_log['html_name'])
        else:
            print_html_dir = "file://" + html_location
        print(print_html_dir)


def filter_keys(obj, bad):
    if isinstance(obj, dict):
        for k in list(obj.keys()):
            if k in bad:
                del obj[k]
            else:
                filter_keys(obj[k], bad)
    elif isinstance(obj, list):
        for i in reversed(range(len(obj))):
            if obj[i] in bad:
                del obj[i]
            else:
                filter_keys(obj[i], bad)
