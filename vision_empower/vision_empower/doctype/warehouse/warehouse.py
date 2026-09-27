# Copyright (c) 2026, JPMC-VisionEmpower and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Warehouse(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		active: DF.Check
		address: DF.SmallText | None
		warehouse_name: DF.Data
		warehouse_type: DF.Literal["Physical", "Digital"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Warehouse"
