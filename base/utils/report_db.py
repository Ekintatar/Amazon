import time

import pymysql
from pypika.queries import QueryBuilder
from pypika import functions as sql_func, Table, Tables
from base.utils.settings import Settings, SettingKeys


#   required table sql

# create table atlas_reports
# (
# 	id int auto_increment,
# 	session_id varchar(13) null,
# 	failed int null,
# 	passed int null,
# 	skipped int null,
# 	xpassed int null,
# 	error int null,
# 	duration float null,
# 	logtime datetime null,
# 	constraint atlas_reports_pk
# 		primary key (id)
# );
#

# create table spPanel.atlas_case_reports
# (
#     id int auto_increment
#         primary key,
#     session_id int(13)      null,
#     case_name  varchar(500) null,
#     status     varchar(50)  null,
#     output     text         null,
#     duration   float        null,
#     logtime    datetime     null,
#     constraint atlas_case_reports_pk
#         primary key (id)
# );


class CaseResult:
    def __init__(self):
        self.session_id = None
        self.case_name = None
        self.status = None
        self.output = None
        self.duration = None
        self.settings = Settings()

    def get_qa_db_connection(self):
        """open connection to qa database"""
        return pymysql.connect(self.settings.get(SettingKeys.QA_DB_HOST),
                               self.settings.get(SettingKeys.QA_DB_USER),
                               self.settings.get(SettingKeys.QA_DB_PASSWORD),
                               self.settings.get(SettingKeys.QA_DB_SCHEMA))

    def collect_test_case_result(self, pytest_item, pytest_result):
        """collect test case info from pytest values"""
        session_id = pytest_item.config.cache.get("session_id", None)
        if session_id:
            self.session_id = session_id
        else:
            raise Exception("test_id not defined!")
        self.case_name = pytest_result.nodeid
        if pytest_result.failed:
            self.output = "{err}\n\n{stdout}".format(err=pytest_result.longreprtext, stdout=pytest_result.capstdout)
        else:
            self.output = pytest_result.capstdout
        self.status = pytest_result.outcome
        self.duration = pytest_result.duration

    def push_case_result_to_qa_db(self):
        """generate insert query for test case result"""
        db = self.get_qa_db_connection()
        cursor = db.cursor()
        try:
            case_report_table = Table('spPanel.atlas_case_reports')
            query = QueryBuilder(quote_char=None).into(case_report_table).columns(
                'session_id', 'case_name', 'status', 'output', 'duration', 'logtime'
            ).insert(
                self.session_id, self.case_name, self.status, self.output, self.duration, sql_func.Now()
            )
            cursor.execute(str(query))
            db.commit()
            db.close()
        except Exception as e:
            db.rollback()
            db.close()
            raise e

    def save_over_all_result(self, session_id):
        """
        get status counts of current session and push collected counts
        :param session_id int
        session_id is automation start epoch time
        """
        duration = time.time() - session_id / 1000
        db = self.get_qa_db_connection()
        cursor = db.cursor()
        case_report_table, report_table = Tables('spPanel.atlas_case_reports', 'spPanel.atlas_reports')
        query_grouped_by_cases = QueryBuilder(quote_char=None).from_(
            case_report_table).select(
                sql_func.Star()
            ).where(
                case_report_table.session_id == session_id
            ).groupby(case_report_table.case_name)
        query_status_counts = QueryBuilder(quote_char=None).from_(
            query_grouped_by_cases).select(
                "status", sql_func.Count("*")
            ).groupby("status")
        test_result_counts = {"failed": 0, "passed": 0, "skipped": 0, "xpassed": 0, "error": 0}
        try:
            cursor.execute(str(query_status_counts))
            results = cursor.fetchall()
            for row in results:
                test_result_counts[row[0]] = int(row[1])

            query_insert_overall_report = QueryBuilder(quote_char=None).into(report_table).columns(
                "session_id", "failed", "passed", "skipped", "xpassed", "error", "duration", "logtime"
            ).insert(
                session_id, test_result_counts["failed"], test_result_counts["passed"], test_result_counts["skipped"],
                test_result_counts["xpassed"], test_result_counts["error"], duration, sql_func.Now()
            )
            cursor.execute(str(query_insert_overall_report))
            db.commit()
            db.close()
        except Exception as e:
            db.rollback()
            db.close()
            raise e
