import django_tables2 as tables
from  django_tables2.utils import A
from lbm.models import LBMJob

class InvoiceTable(tables.Table):
    invoice_selection = tables.CheckBoxColumn(accessor="pk", attrs = { 
	                                        "th__input": {"onclick": "toggle(this)"}, 
										    "td__input": {"name": "invoice_selection[]"}
										},
                                        orderable=False)
	
    class Meta:
        attrs = {'table-name': 'invoice_table'}
        model=LBMJob
        template="django_tables2/bootstrap3.html" 
        fields = (
                'invoice_selection', 'job_no', 'invoice_no', 'purchase_order_no', 'client.name', 'publication.name', 'delivery_date'
                )
