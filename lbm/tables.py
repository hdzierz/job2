import django_tables2 as tables
from  django_tables2.utils import A
from .models import LBMJob, LBMJobRoute, Route


class RouteTable(tables.Table):
   class Meta:
        model=Route
        template="django_tables2/bootstrap3.html"
        fields = (
                'island',
                'region',
                'area',
                'code',
                'dest_type',
                )
 
class JobRouteTable(tables.Table):
   def render_region(self, value):
        print(value)

   edit = tables.LinkColumn('item_edit', args=[A('pk')], orderable=False)
   #sel = tables.CheckBoxColumn('sel', orderable=False)


   class Meta:
        model=LBMJobRoute
        template="django_tables2/bootstrap3.html"
        fields = (
                'route.island',
                'route.region',
                'route.area',
                'route.code',
                'dest_type',
                'version',
                'amount',
                )


class JobTable(tables.Table):
    action = tables.Column(accessor="pk", empty_values=())
    finished = tables.Column(empty_values=())

    def render_action(self, value):
        return """ 
           <a href="" class="tipB" title="" data-original-title="View"><i class="glyphicon glyphicon-eye-open"></i></a>
           <a href="/lbm/jobBooking/{}" class="tipB" title="" data-original-title="Edit"><i class="glyphicon glyphicon-pencil"></i></a>
           <a href="" class="tipB active" title="" data-original-title="Reopen"><i class="glyphicon glyphicon-ban-circle"></i></a>
           <a href="" class="tipB active" title="" data-original-title="Start again"><i class="glyphicon glyphicon-ok"></i></a>
           <a href="" class="tipB" title="" data-original-title="Delete"><i class="glyphicon glyphicon-trash"></i></a>
    """.format(value)

    def render_yes_no(self, value):
        if value == 'Y':                                                                         
            return '<span href="" class="tipB active" title="" data-original-title="This job is finished"><i class="glyphicon glyphicon-ok"></i></span>'
        elif not value:
            return '<span href="" class="tipB active" title="" data-original-title="This job is cancelled"><i class="glyphicon glyphicon-ban-circle"></i></span>'
        else:
            return '<span href="" class="tipB active" title="" data-original-title="This job is cancelled"><i class="glyphicon glyphicon-ban-circle"></i></span>'

    def render_finished(self, value):
        return self.render_yes_no(value)

    def render_cancelled(self, value):
        return self.render_yes_no(value)

    class Meta:
        model=LBMJob
        template="django_tables2/bootstrap3.html" 
        fields = (
                'action',
                'finished', 
                'cancelled', 
                'client', 
                'publication', 
                'delivery_date', 
                'job_no', 
                'invoice_no', 
                'purchase_no',
                'weight',
                'dest_type',
                )
