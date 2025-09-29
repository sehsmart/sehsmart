app_name = "sehsmart"
app_title = "SEHSmart"
app_publisher = "Surateyehospital"
app_description = "SEHSmart System"
app_email = "surateyehospital.it@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sehsmart",
# 		"logo": "/assets/sehsmart/logo.png",
# 		"title": "SEHSmart",
# 		"route": "/sehsmart",
# 		"has_permission": "sehsmart.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sehsmart/css/sehsmart.css"
# app_include_js = "/assets/sehsmart/js/sehsmart.js"

# include js, css files in header of web template
# web_include_css = "/assets/sehsmart/css/sehsmart.css"
# web_include_js = "/assets/sehsmart/js/sehsmart.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sehsmart/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sehsmart/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sehsmart.utils.jinja_methods",
# 	"filters": "sehsmart.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sehsmart.install.before_install"
# after_install = "sehsmart.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sehsmart.uninstall.before_uninstall"
# after_uninstall = "sehsmart.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sehsmart.utils.before_app_install"
# after_app_install = "sehsmart.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sehsmart.utils.before_app_uninstall"
# after_app_uninstall = "sehsmart.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sehsmart.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# custom_app/hooks.py


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sehsmart.tasks.all"
# 	],
# 	"daily": [
# 		"sehsmart.tasks.daily"
# 	],
# 	"hourly": [
# 		"sehsmart.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sehsmart.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sehsmart.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sehsmart.install.before_tests"

# Overriding Methods
# ------------------------------
#



#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sehsmart.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------





# after_request = ["sehsmart.utils.after_request"]

# Job Events
# ----------
# before_job = ["sehsmart.utils.before_job"]
# after_job = ["sehsmart.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sehsmart.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [

    {
        "dt": "DocType",

        "filters":[["name","in",["Operative","Operative Table28","Operative Table29","Operative Table30","Operative Table31","Operative Table32","Operative Table33","Operative Table34","Operative Table35","Operative Table36","Operative Table37","Operative Table38","Operative Table39","Operative Table40","Operative Table41","Operative Table42","Operative Table43","Operative Table44","Operative Table45","Operative Note For","Operative Table1","Operative Table2","Operative Table3","Operative Table4","Operative Table5","Operative Table6","Operative Table7","Operative Table8","Operative Table9","Operative Table10","Operative Table11","Operative Table12","Operative Table13","Operative Table14","Operative Table15","Operative Table16","Operative Table17","Operative Table18","Operative Table19","Operative Table20","Operative Table21","Operative Table22","Operative Table23","Operative Table24","Operative Table25","Operative Table26","Operative Table27","Operative Retina Surgery","Operative Retina Surgery Table1","Operative Retina Surgery Table2","Operative Retina Surgery Table3","Operative Retina Surgery Table4","Operative Retina Surgery Table5","Operative Retina Surgery Table6","Operative Retina Surgery Table7","Operative Retina Surgery Table8","Operative Retina Surgery Table10","Operative Retina Surgery Table11","Eye Surgery Nursing Record","Eye Surgery Nursing Record Table1","Eye Surgery Nursing Record Table2","Eye Surgery Nursing Record Table3","Eye Surgery Nursing Record Table4","Eye Surgery Nursing Record Table5","Eye Surgery Nursing Record Table6","Eye Surgery Nursing Record Table7","Eye Surgery Nursing Record Table8","Eye Surgery Nursing Record Table10","Eye Surgery Nursing Record Table11","Eye Surgery Nursing Record Table12","Eye Surgery Nursing Record Table13","Eye Surgery Nursing Record Table14","Eye Surgery Nursing Record Table15","Eye Surgery Nursing Record Table16","Eye Surgery Nursing Record Table17","Eye Surgery Nursing Record Table18","Eye Surgery Nursing Record Table19","Eye Surgery Nursing Record Table20","Surgical Safety Checklist","EYE Medication Record","Outpatient Medication Table","Inpatient Medication Table","Operating Room Medication Table","Pre PRK Medication Table","Pre Trans PRK Medication Table","Pre FEMTO Relex Medication Table","Post Lasik Refractive Medication Table","General Surgical Nursing Record","General Surgical Nursing Record Table1","General Surgical Nursing Record Table2","General Surgical Nursing Record Table3","General Surgical Nursing Record Table4","General Surgical Nursing Record Table5","General Surgical Nursing Record Table6","General Surgical Nursing Record Table7","General Surgical Nursing Record Table8","General Surgical Nursing Record Table9","General Surgical Nursing Record Table10","General Surgical Nursing Record Table11","General Surgical Nursing Record Table12","General Surgical Nursing Record Table13","General Surgical Nursing Record Table14","General Surgical Nursing Record Table15","General Surgical Nursing Record Table16","General Surgical Nursing Record Table17","General Surgical Nursing Record Table18","Minutes Of The Meeting","Minutes Of The Meeting Listname Table","Meeting Participants Table","Meeting Agenda Table","Meeting Agenda Table1","Meeting Agenda Table2","Meeting Agenda Table3"]]]
    },

    {
        "dt": "Client Script",
        "filters": [["name", "in", ["General Surgical Nursing Record", "Surgical Safety Checklist", "Operative Retina Surgery", "Operative Note For", "Operative", "Eye Surgery Nursing Record"]]]
    },

    {
        "dt": "Print Format",
        "filters": [["name","in",["Description of Pars Plana Vitrectomy","Operative Note for Strabismus Surgery","Operative Note","Operative Record for Pterygium Surgery","department","Operative Retina Surgery","แบบฟอร์มทางการพยาบาลผู้ป่วย","Surgical Safety Checklist","Laser Refractive Surgery Safety Checklist","Surgery Safety Checklist FEMTO Cataract","Full Operative"]]]
    }

    
]