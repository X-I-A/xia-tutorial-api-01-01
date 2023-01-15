from xia_fields import StringField
from xia_engine import Document, EmbeddedDocument, EmbeddedDocumentField


class Address(EmbeddedDocument):
    address: str = StringField(description="Address", sample="M. Name \n 888, Road Name")
    city: str = StringField(description="City", sample="Paris")
    post_code: str = StringField(description="Post code", sample="75016")


class PurchaseOrder(Document):
    po_number: str = StringField(description="Purchase Order Number")
    order_status: str = StringField(description="Purchase Order Status",
                                    required=True,
                                    default="new",
                                    choices=["new", "paid", "delivered"])
    delivery_address = EmbeddedDocumentField(document_type=Address)
