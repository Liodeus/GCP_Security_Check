from functions.gce_misc_functions import *


def gce_firewallrule_log(cmd_list, report="False", lock="", severity="Medium", mitigation_name="gce_firewallrule_log.md"):
	"""
		Test if firewall rule are enable
	"""
	firewall_rule_enable = gce_reduce(cmd_list, "gce_firewallrule_log", lock)

	# Print report for gce_firewallrule_log
	report_print("GCE firewallrule_log ", firewall_rule_enable, report, mitigation_name, severity, lock)


def gce_disk_location(cmd_list, report="False", lock="", severity="Major", mitigation_name="gce_disk_location.md"):
	"""
		Test for disk location compliance to GDPR
	"""
	disk_location_result = gce_reduce(cmd_list, "gce_disk_location", lock)

	# Print report for gce_disk_location
	report_print("GCE disk location", disk_location_result, report, mitigation_name, severity, lock)


def gce_instance_externalip(cmd_list, report="False", lock="", severity="Major", mitigation_name="gce_instance_externalip.md"):
	"""
		Test for external ip on GCE instance
	"""
	external_ip_result = gce_reduce(cmd_list, "gce_instance_externalip", lock)

	# Print report for gce_instance_externalip
	report_print("GCE instance external ip", external_ip_result, report, mitigation_name, severity, lock)


def gce_instance_location(cmd_list, report="False", lock="", severity="Major", mitigation_name="gce_instance_location.md"):
	"""
		Test for instance location compliance to GDPR
	"""
	location_result = gce_reduce(cmd_list, "gce_instance_location", lock)
	
	# Print report for gce_disk_location
	report_print("GCE instance location", location_result, report, mitigation_name, severity, lock)


def gce_instance_service_account(cmd_list, report="False", lock="", severity="Major", mitigation_name="gce_instance_service_account.md"):
	"""
		Test for instance default account
	"""
	location_result = gce_reduce(cmd_list, "gce_instance_service_account", lock)
	if "API_BILLING" in location_result:
		services_account = location_result
	else:
		services_account = gce_reduce_two(location_result, cmd_list, "gce_instance_service_account")

	# Print report for gce_instance_service_account
	report_print("GCE instance service account", services_account, report, mitigation_name, severity, lock)


def gce_ip_forwarding(cmd_list, report="False", lock="", severity="Critical", mitigation_name="gce_ip_forwarding.md"):
	"""
		Test for 
	"""
	location_result = gce_reduce(cmd_list, "gce_ip_forwarding", lock)
	if "API_BILLING" in location_result:
		services_account = location_result
	else:
		services_account = gce_reduce_two(location_result, cmd_list, "gce_ip_forwarding")

	# Print report for gce_instance_service_account
	report_print("GCE instance IP forwarding", services_account, report, mitigation_name, severity, lock)
		

def gce_network_name(cmd_list, report="False", lock="", severity="Major", mitigation_name="gce_network_name.md"):
	"""
		Test for 
	"""
	location_result = gce_reduce(cmd_list, "gce_network_name", lock)
	
	if "API_BILLING" in location_result:
		network_default = location_result
	else:
		network_default = gce_reduce_two(location_result, cmd_list, "gce_network_name")

	# Print report for gce_network_name
	report_print("GCE instance instance default network", network_default, report, mitigation_name, severity, lock)


def gce_shielded_instances(cmd_list, report="False", lock="", severity="Minor", mitigation_name="gce_shielded_instances.md"):
	"""
		Test if enableIntegrityMonitoring, enableSecureBoot,enableVtpm are enable on GCE instances
	"""
	location_result = gce_reduce(cmd_list, "gce_shielded_instances", lock)
	if "API_BILLING" in location_result:
		shield_result = location_result
	else:
		shield_result = gce_reduce_two(location_result, cmd_list, "gce_shielded_instances")

	# Print report for gce_shielded_instances
	report_print("GCE instance shielding", shield_result, report, mitigation_name, severity, lock)
