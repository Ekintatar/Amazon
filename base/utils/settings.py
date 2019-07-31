import configparser
import os


class Environments(enumerate):
    JENKINS_TEST = "JENKINS_TEST"
    JENKINS_DEPLOYMENT = "JENKINS_DEPLOYMENT"
    TEST_MACHINE = "TEST"
    LOCAL = "LOCAL"


class Settings:
    project_name = "Amazon"
    test_env_variable_name = "TEST_ENV"

    def __init__(self):
        self.env_variables = self.get_env_variables()
        self.env = self.get_env()
        self.project_dir = self.get_project_dir()
        self._settings = self.read_settings()

    def get_project_dir(self):
        project = self.project_name
        if self.env in (Environments.JENKINS_TEST, Environments.JENKINS_DEPLOYMENT):
            project = self.env_variables["JOB_NAME"]
        curent_path_splitted = os.path.realpath(__file__).split(os.sep)
        last_project_name_index = len(curent_path_splitted) - 1 - curent_path_splitted[::-1].index(project)
        return os.path.join(os.sep.join(curent_path_splitted[:last_project_name_index + 1]))

    def get_env_variables(self):
        env_variables = {}
        for env_key in os.environ:
            env_variables[env_key] = os.getenv(env_key)
        return env_variables

    def get_env(self):
        if self.test_env_variable_name not in self.env_variables:
            return Environments.LOCAL
        else:
            return self.env_variables[self.test_env_variable_name]

    def read_settings(self):
        if self.env in (Environments.JENKINS_TEST, Environments.JENKINS_DEPLOYMENT, Environments.TEST_MACHINE):
            ini_file_location = "/etc/atlas_settings.ini"
        else:
            ini_file_location = os.path.join(self.project_dir, "base", "utils", "settings.ini")

        if not os.path.isfile(ini_file_location):
            raise Exception("Please make settings.ini copy from settings.ini.example to {}".format(ini_file_location))

        config = configparser.ConfigParser()
        config.read(ini_file_location)

        settings = {}
        for option in config.options("ALL"):
            settings[option] = config.get("ALL", option)
        if self.env in (Environments.JENKINS_DEPLOYMENT, Environments.JENKINS_TEST):
            ini_env = "JENKINS"
        else:
            ini_env = self.env
        for option in config.options(ini_env):
            settings[option] = config.get(ini_env, option)
        return settings

    def get(self, settings_key):
        if settings_key in self._settings:
            return self._settings[settings_key]
        else:
            raise Exception("{} not found in settings.ini".format(settings_key))


class SettingKeys(enumerate):

    USER_MAIL = 'user_mail'
    USER_PASSWORD = 'user_password'
    SITE_URL = 'site_url'
    USER_NAME = 'user_name'

    PARTNER_ID = "partner_id"
    PANEL_USER = "panel_user"
    PANEL_PASSWORD = "panel_password"
    PARTNER_NAME = "partner_name"
    PARTNER_PANEL_URL = "partner_panel_url"
    PARTNER_SITE_URL = "partner_site_url"
    GACHAPON_PARTNER = "gachapon_partner"
    GACHAPON_URL = "gachapon_url"
    COLLABORATE_MAIL = "collaborate_mail"
    COLLABORATE_PASSWORD = "collaborate_password"
    VIEW_ONLY_MAIL = "view_only_mail"
    VIEW_ONLY_PASSWORD = "view_only_password"
    OUTSOURCE_MAIL = "outsource_mail"
    OUTSOURCE_PASSWORD = "outsource_password"
    NOROLE_MAIL = "norole_mail"
    NOROLE_PASSWORD = "norole_password"
    NOROLE_DEACTIVE_MAIL = "norole_deactive_mail"
    NOROLE_DEACTIVE_PASSWORD = "norole_deactive_password"
    HASROLE_DEACTIVE_MAIL = "hasrole_deactive_mail"
    HASROLE_DEACTIVE_PASSWORD = "hasrole_deactive_password"
    SELENIUM_MAIL = "selenium_mail"
    SELENIUM_PASSWORD = "selenium_password"
    LOCK_MAIL = "lock_mail"
    LOCK_PASSWORD = "lock_password"
    THRESHOLD_MAIL = "threshold_mail"
    THRESHOLD_PASSWORD = "threshold_password"
    CONTACT_API_KEY = "contact_api_key"
    GOOGLE_MAP_APIS_KEY = "google_map_apis_key"
    MAIL_API_KEY = "mail_api_key"
    QA_GMAIL = "qa_gmail"
    QA_GMAIL_PASSWORD = "qa_gmail_password"
    QA_GMAIL_IMAP_SERVER = "qa_gmail_imap_server"
    RESET_MAIL = "reset_mail"
    RESET_MAIL_PASSWORD = "reset_mail_password"
    FB_EMAIL = "fb_email"
    FB_PASSWORD = "fb_password"
    INSIDER_URL = "insider_url"
    CONFLUENCE_URL = "confluence_url"
    JIRA_URL = "jira_url"
    JIRA_TOKEN = NONE = "jira_token= none"
    MAIL_URL = "mail_url"
    DB_HOST = "db_host"
    DB_USER = "db_user"
    DB_PASSWORD = "db_password"
    DB_NAME = "db_name"
    DB_NAME_USEINSIDER = "db_name_useinsider"
    READER_DB_HOST = "reader_db_host"
    READER_DB_PASSWORD = "reader_db_password"
    READER_DB_USER = "reader_db_user"
    TOKEN_DB_HOST = "token_db_host"
    TOKEN_DB_USER = "token_db_user"
    TOKEN_DB_PASSWORD = "token_db_password"
    TOKEN_DB_PORT = "token_db_port"
    QA_DB_HOST = "qa_db_host"
    QA_DB_USER = "qa_db_user"
    QA_DB_PASSWORD = "qa_db_password"
    QA_DB_PORT = "qa_db_port"
    QA_DB_SCHEMA = "qa_db_schema"
    REMOTE_DRIVER = "remote_driver"
    HUB_IP = "hub_ip"
    GITHUB_URL = "github_url"
    GITHUB_TOKEN = "github_token"
    SLACK_WEBHOOK_URL = "slack_webhook_url"
    CONFLUENCE_GENERATE_PAGE_ID = "confluence_generate_page_id"
