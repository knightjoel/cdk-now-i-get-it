from aws_cdk import core as cdk
from aws_cdk.aws_ec2 import (
    Peer,
    Port,
    Protocol,
    SecurityGroup,
    Vpc
)


class CdkNowIGetItStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the VPC resource.
        self._vpc = Vpc(self, "MyVPC", cidr="10.10.0.0/16")
        # Create a Security Group within the VPC that is used to allow
        # management traffic from designated jump hosts.
        self._sg = SecurityGroup(self, "MySG", vpc=self._vpc,
                                 allow_all_outbound=False,
                                 description="Management traffic from jump boxes",
                                 security_group_name="jumpbox-mgmt-traffic")

        # Add ingress rules to the Security Group for the jump host
        # 10.255.0.10 to TCP/22 and TCP/3389.
        self._sg.add_ingress_rule(peer=Peer.ipv4("10.255.0.10/32"),
                                  connection=Port(protocol=Protocol.TCP,
                                                  string_representation="host1",
                                                  from_port=22,
                                                  to_port=22))
        self._sg.add_ingress_rule(peer=Peer.ipv4("10.255.0.10/32"),
                                  connection=Port(protocol=Protocol.TCP,
                                                  string_representation="host1",
                                                  from_port=3389,
                                                  to_port=3389))

