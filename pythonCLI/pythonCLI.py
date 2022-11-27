from PyInquirer import prompt
import time
from functions import *
from questions import *

rodando = True

print("------------------WARNING------------------")
print("FOR THIS AWS CLI TO WORK, YOU NEED TO HAVE") 
print("LOADED YOUR AWS CREDENTIALS IN YOUR TERMINAL")
print("------------------WARNING------------------")
print("\n")
time.sleep(5)
print('------------------------------------------')
print('     Welcome to the AWS-TERRAFORM CLI'     )
print('------------------------------------------')
time.sleep(2)
while rodando:
    action = prompt(first_options)
    if (action['action'] == 'Create an AWS VPC'):
        vpc_answers1 = prompt(vpc_questions1)
        if (vpc_answers1['create_subnet'] == 'Yes'):
            vpc_answers2 = prompt(vpc_questions2)
            variables = vpc_answers1 | vpc_answers2
            if (vpc_answers2['create_IG'] == 'Yes'):
                vpc_answers3 = prompt(vpc_questions3)
                variables = variables | vpc_answers3
                cria_VPC_Subnet_InternetGateway(variables)
            else:
                cria_VPC_Subnet(variables)
        else:
            cria_VPC(vpc_answers1)
    if (action['action'] == 'Create an AWS Security Group'):
        secGrp_answers = {'name': '', 'ingress': [], 'egress': []}
        secGrp_answers1 = prompt(secGrp_questions1)
        secGrp_answers['name'] = secGrp_answers1['secGrp_name']
        while True:
            secGrp_answers2 = prompt(secGrp_questions2)
            if (secGrp_answers2['create_ingress'] == 'Yes'):
                secGrp_answers3 = prompt(secGrp_questions3)
                secGrp_answers['ingress'].append(secGrp_answers3)
            else:
                break
        while True:
            secGrp_answers4 = prompt(secGrp_questions4)
            if (secGrp_answers4['create_egress'] == 'Yes'):
                secGrp_answers5 = prompt(secGrp_questions5)
                secGrp_answers['egress'].append(secGrp_answers5)
            else:
                break
        cria_security_group(secGrp_answers)
    if (action['action'] == 'Create an AWS Instance'):
        ec2_variables = prompt(ec2_options)
        if (ec2_variables['ec2_secGrp'] == "Yes"):
            ec2_variables2 = prompt(ec2_options2)
            ec2_variables = ec2_variables | ec2_variables2
        cria_instancia(ec2_variables)
    if (action['action'] == 'Create an AWS IAM User'):
        user_variables = prompt(user_options)
        cria_IAM_user(user_variables)
    if (action['action'] == 'Delete an AWS Instance'):
        ec2_variables = prompt(ec2_delete)
        if (ec2_variables['ec2_delete_confirm'] == "Yes"):
            deleta_instancia(ec2_variables)
    if (action['action'] == 'Delete an AWS VPC'):
        vpc_variables = prompt(vpc_delete)
        if (vpc_variables['vpc_delete_confirm'] == "Yes"):
            deleta_vpc(vpc_variables)
    if (action['action'] == 'Delete an AWS Security Group'):
        secGrp_variables = prompt(secGrp_delete)
        if (secGrp_variables['secGrp_delete_confirm'] == "Yes"):
            deleta_secgrp(secGrp_variables)
    if (action['action'] == 'Delete an AWS IAM User'):
        user_variables = prompt(user_delete)
        if (user_variables['user_delete_confirm'] == "Yes"):
            deleta_user(user_variables)
    if (action['action'] == 'List all AWS Resources'):
        list_all()
    if (action['action'] == 'Quit AWS CLI'):
        rodando = False