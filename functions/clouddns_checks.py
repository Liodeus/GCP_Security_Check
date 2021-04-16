from functions.misc_functions_folder.clouddns_misc_functions import *


def clouddns_dnssec(cmd_list, report="False", lock="", severity="Major", mitigation_name="clouddns_dnssec.md"):
	"""
		Test for DNSSEC security
	"""
	dnssec = clouddns_reduce(cmd_list, "clouddns_dnssec", lock)
	report_print("Cloud DNS DNSSEC check", dnssec, report, mitigation_name, severity, lock)


def clouddns_rsasha1(cmd_list, report="False", lock="", severity="Critical", mitigation_name="clouddns_rsasha1.md"):
	"""
		Test for DNSSEC RSASHA1 weak algorithm
	"""
	rsasha1 = clouddns_reduce(cmd_list, "clouddns_rsasha1", lock)
	report_print("Cloud DNS RSASHA1 check", rsasha1, report, mitigation_name, severity, lock)
