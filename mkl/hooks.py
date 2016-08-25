# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mkl"
app_title = "MKL Document"
app_publisher = "myme"
app_description = "For Storing MKL Document"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "technical.erpsonic@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mkl/css/mkl.css"
# app_include_js = "/assets/mkl/js/mkl.js"

# include js, css files in header of web template
# web_include_css = "/assets/mkl/css/mkl.css"
# web_include_js = "/assets/mkl/js/mkl.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "mkl.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mkl.install.before_install"
# after_install = "mkl.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mkl.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mkl.tasks.all"
# 	],
# 	"daily": [
# 		"mkl.tasks.daily"
# 	],
# 	"hourly": [
# 		"mkl.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mkl.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mkl.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mkl.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mkl.event.get_events"
# }

