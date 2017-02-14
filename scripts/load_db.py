from lbm.models import *


def run():
    for client in Client.objects.using('coural').raw("SELECT client_id as id, client.* FROM client"):
        client.save(using="default")


    for j in Job.objects.using('coural').raw('SELECT job_id as id, job.* FROM job'):
        client = CLient.objects.get(pk=j.client_id)
        pub,created = Publication.objetcs.get_or_create(client=client,
                name=j.publication)

        j.publication = pub
        j.client = client

        j.save(using='default')



    for r in Route.objects.using('coural').raw('SELECT route_id as id,route.* FROM route'):
        r.save(using='default')

    for r in JobRoute.objects.using('coural').raw('SELECT job_route_id as id,job_route.* FROM  job_route' ):
        r.save(using='default')


