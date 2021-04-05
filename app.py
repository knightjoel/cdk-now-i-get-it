#!/usr/bin/env python3
import os

from aws_cdk import core as cdk

from cdk_now_i_get_it.cdk_now_i_get_it_v1_stack import (
    CdkNowIGetItStack as CdkNowIGetItStack_v1
)
from cdk_now_i_get_it.cdk_now_i_get_it_v2_stack import (
    CdkNowIGetItStack as CdkNowIGetItStack_v2
)
from cdk_now_i_get_it.cdk_now_i_get_it_v3_stack import (
    CdkNowIGetItStack as CdkNowIGetItStack_v3
)


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
stack_v1 = CdkNowIGetItStack_v1(app, "CdkNowIGetItStackv1")

params = get_params_from_database()
stack_v2 = CdkNowIGetItStack_v2(app, "CdkNowIGetItStackv2",
                                params["vpc_cidr"],
                                params["jump_host"],
                                params["ports"])

subnet_len = 24
stack_v3 = CdkNowIGetItStack_v3(app, "CdkNowIGetItStackv3",
                                params["vpc_cidr"],
                                params["jump_host"],
                                params["ports"],
                                subnet_len)

app.synth()
