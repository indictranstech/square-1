
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
class Lead(Document):
	pass

@frappe.whitelist()
def make_order(source_name,target_doc= None,ignore_permissions=False):
	target_doc = get_mapped_doc("Lead", source_name,
		{"Lead": {
			"doctype": "Order Form",
			"field_map": {
				"name": "lead",
				"lead_name": "contact_display",
				"company_name": "customer_name",
				"email_id": "contact_email",
				"mobile_no": "contact_mobile"
			}
		}}, target_doc)

	return target_doc