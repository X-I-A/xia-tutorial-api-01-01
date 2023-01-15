from __future__ import annotations
from xia_fields import StringField
from xia_engine import Document, EmbeddedDocument, EmbeddedDocumentField
from xia_api import XiaActionResult


class Address(EmbeddedDocument):
    address: str = StringField(description="Address", sample="M. Name \n 888, Road Name")
    city: str = StringField(description="City", sample="Paris")
    post_code: str = StringField(description="Post code", sample="75016")


class PurchaseOrder(Document):
    _actions = {"set_paid": {"out": XiaActionResult}}

    po_number: str = StringField(description="Purchase Order Number")
    order_status: str = StringField(description="Purchase Order Status",
                                    required=True,
                                    default="new",
                                    choices=["new", "paid", "delivered"])
    delivery_address = EmbeddedDocumentField(document_type=Address)

    def set_paid(self, _acl=None):
        self.update(order_status="paid")
        self.reload()
        if self.order_status == "paid":
            return XiaActionResult(successful=True, message="Order status successfully changed")
        else:
            return XiaActionResult(successful=False, message="Something goes wrong")
