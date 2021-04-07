#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from cdk_now_i_get_it.cdk_now_i_get_it_v1 import (
    CdkNowIGetIt as CdkNowIGetIt_v1
)
from cdk_now_i_get_it.cdk_now_i_get_it_v2 import (
    CdkNowIGetIt as CdkNowIGetIt_v2
)
from cdk_now_i_get_it.cdk_now_i_get_it_v3 import (
    CdkNowIGetIt as CdkNowIGetIt_v3
)


class MyStackv1(cdk.Stack):

    def __init__(self, scope: cdk.App, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self._network = CdkNowIGetIt_v1(self, "CdkNowIGetItv1")


class MyStackv2(cdk.Stack):

    def __init__(self, scope: cdk.App, id: str, vpc_cidr: str,
                 jump_host: str, ports: list, **kwargs):
        super().__init__(scope, id, **kwargs)

        self._network = CdkNowIGetIt_v2(self, "CdkNowIGetItv2",
                                        vpc_cidr,
                                        jump_host,
                                        ports)


class MyStackv3(cdk.Stack):

    def __init__(self, scope: cdk.App, id: str, vpc_cidr: str,
                 jump_host: str, ports: list, subnet_len: int, **kwargs):
        super().__init__(scope, id, **kwargs)

        self._network = CdkNowIGetIt_v3(self, "CdkNowIGetItv3",
                                        vpc_cidr,
                                        jump_host,
                                        ports,
                                        subnet_len)


def get_params_from_database():
    # Ok, this isn't exacty a database, but it makes the point. This could
    # also be a call to a relational DB, an API call to an IPAM system, or
    # anything else.
    import csv
    with open("network.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            if row[0] == "MyVPC":
                return {
                    "vpc_cidr": row[1],
                    "jump_host": row[2],
                    "ports": row[3].split(":")
                }


app = cdk.App()

stack_v1 = MyStackv1(app, "MyStackv1")

params = get_params_from_database()
stack_v2 = MyStackv2(app, "MyStackv2",
                     params["vpc_cidr"],
                     params["jump_host"],
                     params["ports"])

subnet_len = 24
stack_v3 = MyStackv3(app, "MyStackv3",
                     params["vpc_cidr"],
                     params["jump_host"],
                     params["ports"],
                     subnet_len)

app.synth()
