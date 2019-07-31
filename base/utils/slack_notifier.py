import json
import requests
import time


class SlackOptions(object):
    """ Includes some styles of Slack messages"""
    alert = ":radioactive_sign:"
    error = ":name_badge:"
    success = ":heavy_check_mark:"
    black = "#000000"
    blue = "#0000FF"
    green = "#00FF00"
    red = "#FF0000"
    yellow = "#FFFF00"
    white = "#FFFFFF"


class SlackNotifier:
    """
    This class includes all necessary functions to make connection
    between Atlas automation project and Slack API during catching exceptions
    Usage::
    Object = SlackNotifer(hook_url and channel_name)
    Object.create_configurations('desired configs')
    Object.prepare_attachment('desired configs')
    Object.send_alert_to_channel(config, attachment)
    """
    def __init__(self, webhook, channel_name):
        self.config = {}
        self.attachment = {}
        self.webhook_url = webhook
        self.channel_name = channel_name

    def create_config(self, username=None, icon_emoji=None):
        """
        Creates default configurations as a dictionary to use it when user sends the hook
        @Usage: You should give channel with '#' and choose an emoji from SlackOptions class.
        :param channel: Channel name that user want to see message on.
        :param username: The name appears as Username
        :param icon_emoji: Emoji of the user
        Minimum requirements: All variables should be filled
        """
        self.config = {
            "attachments": [],
            "channel": self.channel_name,
            "link_names": 1,
            "username": username,
            "icon_emoji": icon_emoji
        }
        return self.config

    def prepare_attachment(self, title_message="", details_url="", image_url="", text="", color="", footer="",
                           footer_icon=""):
        """
        Converts the given data to a correct shape for the attachment in the post message
        @Usage: All variables should be string, and URLs must include http or https.
        :param title_message: Appears as the title of message
        :param details_url: Lands user to given URL when they click on it
        :param image_url: The image link that is wanted to appear in message
        :param text: The main context of message
        :param color: Font color
        :param footer: Message that appears on bottom with a small font size compare than context
        :param footer_icon: The icon of footer
        Minimum requirements: title_message or text should be filled if you want to send a basic message to channel
        """
        self.attachment = {
            "fallback": "An error occured while retrieving error message",
            "title": title_message,
            "title_link": details_url,
            "image_url": image_url,
            "text": text,
            "color": color,
            "footer": footer,
            "footer_icon": footer_icon,
            "ts": round(time.time())
        }
        return self.attachment

    def send_webhook_to_slack(self):
        """ Sends a webhook to a channel via using Slack API """
        headers = {"Content-Type": "application/json"}
        if self.config == {} or self.attachment == {}:
            return "Please create configs and prepare an attachment"
        self.config['attachments'] = [self.attachment]
        data = json.dumps(self.config)
        if self.webhook_url != 'None':
            response = requests.post(url=self.webhook_url, headers=headers, data=data)
            if response.text is not 'ok':
                print(response.text)

