first_options = [
    {
        'type': 'list',
        'name': 'action',
        'message': 'What do you want to do?',
        'choices': [
            'Create an AWS VPC',
            'Create an AWS Security Group',
            'Create an AWS IAM User',
            'Create an AWS Instance',
            'Delete an AWS Instance',
            'Delete an AWS VPC',
            'Delete an AWS Security Group',
            'Delete an AWS IAM User',
            'List all AWS Resources',
            'Quit AWS CLI'
        ]
    }
]

ec2_options = [
    {
        'type': 'input',
        'name': 'ec2_name',
        'message': 'What is the name of your instance?',
    },
    {
        'type': 'list',
        'name': 'ec2_type',
        'message': 'What is the type of your instance?',
        'choices': [
            "t2.micro", 
            "t2.small",
        ]
    },
    {
        'type': 'list',
        'name': 'ec2_secGrp',
        'message': 'Do you want to attach a security group to your instance?',
        'choices': [
            "Yes", 
            "No"
        ]
    }
]

ec2_options2 = [
    {
        'type': 'input',
        'name': 'ec2_secGrp_name',
        'message': 'What is the name of your security group?'
    }
]

ec2_options3 = [
    {
        'type': 'list',
        'name': 'ec2_subnet',
        'message': 'Do you want to attach a subnet to your instance?',
        'choices': [
            "Yes",
            "No"
        ]
    }
]

ec2_options4 = [
    {
        'type': 'input',
        'name': 'ec2_vpc_name',
        'message': 'What is the name of your VPC?'
    },
    {
        'type': 'list',
        'name': 'ec2_vpc_type',
        'message': 'What is the type of your VPC?',
        'choices': [
            "vpc", 
            "vpc-subnet",
            "vpc-subnet-ig"
        ]
    },
    {
        'type': 'input',
        'name': 'ec2_subnet_name',
        'message': 'What is the name of your subnet?'
    }
]

ec2_delete = [
    {
        'type': 'input',
        'name': 'ec2_name',
        'message': 'What is the name of the instance you wish to delete?',
    },
    {
        'type': 'list',
        'name': 'ec2_delete_confirm',
        'message': 'Do you really wish to delete this instance?',
        'choices': [
            "Yes", 
            "No"
        ]
    },
]

vpc_delete = [
    {
        'type': 'input',
        'name': 'vpc_name',
        'message': 'What is the name of the VPC you wish to delete?',
    },
    {
        'type': 'list',
        'name': 'vpc_type',
        'message': 'What is the type of your VPC?',
        'choices': [
            "vpc", 
            "vpc-subnet",
            "vpc-subnet-ig"
        ]
    },
    {
        'type': 'list',
        'name': 'vpc_delete_confirm',
        'message': 'Do you really wish to delete this VPC?',
        'choices': [
            "Yes", 
            "No"
        ]
    },
]

vpc_questions1 = [
    {
        'type': 'input',
        'name': 'vpc_name',
        'message': 'What is the name your VPC?',
    },
    {
        'type': 'input',
        'name': 'vpc_cidr_block',
        'message': 'What is the cidr_block of your VPC?',
    },
    {
        'type': 'list',
        'name': 'create_subnet',
        'message': 'Do you wish to create a subnet in this vpc?',
        'choices': [
            "Yes", 
            "No"
        ]
    }
]

vpc_questions2 = [
    {
        'type': 'input',
        'name': 'subnet_name',
        'message': 'What is the name your subnet?',
    },
    {
        'type': 'input',
        'name': 'subnet_cidr_block',
        'message': 'What is the cidr_block of your subnet?',
    },
    {
        'type': 'list',
        'name': 'create_IG',
        'message': 'Do you wish to create internet gateway to your vpc?',
        'choices': [
            "Yes", 
            "No"
        ]
    }
]

vpc_questions3 = [
    {
        'type': 'input',
        'name': 'IG_name',
        'message': 'What is the name your Internet Gateway?',
    }
]

secGrp_questions1 = [
    {
        'type': 'input',
        'name': 'secGrp_name',
        'message': 'What is the name your Security Group?',
    }
]

secGrp_questions2 = [
    {
    'type': 'list',
    'name': 'create_ingress',
    'message': 'Do you wish to an ingress rule to your Security Group?',
    'choices': [
        "Yes", 
        "No"
        ]
    }
]

secGrp_questions3 = [
    {
        'type': 'input',
        'name': 'port',
        'message': 'What is the port of your ingress rule?',
    },
    {
        'type': 'input',
        'name': 'cidr_blocks',
        'message': 'What is the cidr_block of your ingress rule?',
    },
    {
        'type': 'input',
        'name': 'protocol',
        'message': 'What is the protocol of your ingress rule?',
    }
]

secGrp_questions4 = [
    {
    'type': 'list',
    'name': 'create_egress',
    'message': 'Do you wish to an egress rule to your Security Group?',
    'choices': [
        "Yes", 
        "No"
        ]
    }
]

secGrp_questions5 = [
    {
        'type': 'input',
        'name': 'port',
        'message': 'What is the port of your egress rule?',
    },
    {
        'type': 'input',
        'name': 'cidr_blocks',
        'message': 'What is the cidr_block of your egress rule?',
    },
    {
        'type': 'input',
        'name': 'protocol',
        'message': 'What is the protocol of your egress rule?',
    }
]

secGrp_delete = [
    {
        'type': 'input',
        'name': 'secGrp_name',
        'message': 'What is the name of the Security Group you wish to delete?',
    },
    {
        'type': 'list',
        'name': 'secGrp_delete_confirm',
        'message': 'Do you really wish to delete this Security Group?',
        'choices': [
            "Yes", 
            "No"
        ]
    },
]

user_options = [
    {
        'type': 'input',
        'name': 'user_name',
        'message': 'What is the name of your IAM User?',
    }
]

user_delete = [
    {
        'type': 'input',
        'name': 'user_name',
        'message': 'What is the name of the IAM User you wish to delete?',
    },
    {
        'type': 'list',
        'name': 'user_delete_confirm',
        'message': 'Do you really wish to delete this IAM User?',
        'choices': [
            "Yes", 
            "No"
        ]
    },
]
