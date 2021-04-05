from aws_cdk import core as cdk
from aws_cdk.aws_ec2 import (
    Peer,
    Port,
    Protocol,
    SecurityGroup,
    SubnetConfiguration,
    SubnetType,
    Vpc
)


class CdkNowIGetItStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str,
                 vpc_cidr: str, jump_host: str, mgmt_ports: list,
                 subnet_len: int, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # args:
        # - vpc_cidr (str): The CIDR range for the VPC.
        # - jump_host (str): An optional IP address for the jump host. If this
        #                    is not specified, te Security Group will not be
        #                    created.
        # - mgmt_ports (list): A list of TCP ports which the jump host is
        #                      allowed to connect to.
        # - subnet_len (int): The prefix length for subnet CIDR addresses.

        # Create the VPC resource. The VPC does not have an internet gateway,
        # or NAT gateway. Subnets are created in 2 zones.
        subnets = [SubnetConfiguration(name="MyVPC-Private",
                                 subnet_type=SubnetType.ISOLATED,
                                 cidr_mask=subnet_len)]
        self._vpc = Vpc(self, "MyVPC", cidr=vpc_cidr,
                        max_azs=2,
                        nat_gateways=None,
                        subnet_configuration=subnets)

        # Security Group only created if the jump host parameter was
        # specified.
        if len(jump_host) > 0:
            self.create_sg(jump_host, mgmt_ports)

    def create_sg(self, jump_host, mgmt_ports):
        # Create a Security Group within the VPC that is used to allow
        # management traffic from designated jump hosts.
        self._sg = SecurityGroup(self, "MySG", vpc=self._vpc,
                                 allow_all_outbound=False,
                                 description="Management traffic from jump boxes",
                                 security_group_name="jumpbox-mgmt-traffic")

        # Add ingress rules to the Security Group for the jump host
        # TCP/22 and TCP/3389.
        for port in mgmt_ports:
            self._sg.add_ingress_rule(peer=Peer.ipv4(jump_host),
                                      connection=Port(protocol=Protocol.TCP,
                                                      string_representation="jump",
                                                      from_port=int(port),
                                                      to_port=int(port)))

