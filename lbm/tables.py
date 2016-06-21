import django_tables2 as tables
from .models import Job


class JobTable(tables.Table):
    action = tables.Column(empty_values=())
    finished = tables.Column(empty_values=())

    def render_action(self, value):
        return """ 
           <a href="" class="tipB" title="" data-original-title="View"><i class="glyphicon glyphicon-eye-open"></i></a>
                                <a href="CO-lbm-jobs-edit.php" class="tipB" title="" data-original-title="Edit"><i class="glyphicon glyphicon-pencil"></i></a>
                                                        <a href="" class="tipB active" title="" data-original-title="Reopen"><i class="glyphicon glyphicon-ban-circle"></i></a>
                                                                                <a href="" class="tipB active" title="" data-original-title="Start again"><i class="glyphicon glyphicon-ok"></i></a>
                                                                                                        <a href="" class="tipB" title="" data-original-title="Delete"><i class="glyphicon glyphicon-trash"></i></a>
    """

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
        model=Job
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
