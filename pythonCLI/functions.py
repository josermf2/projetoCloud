import os
import shutil
import json
import subprocess

parent_dir = "/".join(str(os.getcwd()).split('/')[:-1])

def cria_instancia(variables):
    try:
        dirname = f"terraform-aws/{variables['ec2_name']}-ec2Instace"
        path = os.path.join(parent_dir, dirname)
        main_orig_file = os.path.join(parent_dir, "cloudOptions/createEC2Instance/main.tf")
        os.makedirs(path)
        shutil.copy(main_orig_file, path)
    except:
        print("O nome da sua instancia já existe, por favor escolha outro")
        return
    var_file = {
        "variable" : {
            "instance_type" : {
                "default" : variables['ec2_type']
            },
            "name" : {
                "default" : variables['ec2_name']
            },
            "security_group_id" : {
                "default" : None
            },
            "subnet_id" : {
                "default" : None
            }
        } 
    }
    if variables['ec2_secGrp'] == "Yes":
        try:
            with open(os.path.join(parent_dir, f"terraform-aws/{variables['ec2_secGrp_name']}-secGrp", "terraform.tfstate"), "r") as f:
                secGrp_id = json.load(f)["resources"][0]["instances"][0]["attributes"]["id"]
            var_file["variable"]["security_group_id"] = {
                "default" : [secGrp_id]
            }
        except:
            print("Security Group not found")
    json_object = json.dumps(var_file, indent=4)
    with open(str(path)+"/variables.tf.json", "w") as f:
        f.write(json_object)
    result = subprocess.run("terraform init", cwd=path, shell=True)
    result = subprocess.run("terraform apply -auto-approve", cwd=path, shell=True)
    if result.returncode != 0:
        shutil.rmtree(str(path))	
    return

def cria_VPC(variables):
    try:
        dirname = f"terraform-aws/{variables['vpc_name']}-vpc"
        path = os.path.join(parent_dir, dirname)
        main_orig_file = os.path.join(parent_dir, "cloudOptions/createVPC/main.tf")
        os.makedirs(path)
        shutil.copy(main_orig_file, path)
    except:
        print("O nome da sua vpc já existe, por favor escolha outro")
        return   
    var_file = {
        "variable" : {
            "cidr_block" : {
                "default" : variables['vpc_cidr_block']
            },
            "name" : {
                "default" : variables['vpc_name']
            }
        } 
    }
    json_object = json.dumps(var_file)
    with open(str(path)+"/variables.tf.json", "w") as f:
        f.write(json_object)
    result = subprocess.run("terraform init", cwd=path, shell=True)
    result = subprocess.run("terraform apply -auto-approve", cwd=path, shell=True)
    if result.returncode != 0:
        shutil.rmtree(str(path))	
    return

def cria_VPC_Subnet(variables):
    try:
        dirname = f"terraform-aws/{variables['vpc_name']}-vpc-subnet"
        path = os.path.join(parent_dir, dirname)
        main_orig_file = os.path.join(parent_dir, "cloudOptions/createVPC_Subnet/main.tf")
        os.makedirs(path)
        shutil.copy(main_orig_file, path)
    except:
        print("O nome da sua vpc já existe, por favor escolha outro")
        return
    var_file = {
        "variable" : {
            "cidr_block" : {
                "default" : variables['vpc_cidr_block']
            },
            "name" : {
                "default" : variables['vpc_name']
            },
            "subnet_cidr_block" : {
                "default" : variables['subnet_cidr_block']
            },
            "subnet_name" : {
                "default" : variables['subnet_name']
            }
        } 
    }
    json_object = json.dumps(var_file)
    with open(str(path)+"/variables.tf.json", "w") as f:
        f.write(json_object)
    result = subprocess.run("terraform init", cwd=path, shell=True)
    result = subprocess.run("terraform apply -auto-approve", cwd=path, shell=True)
    if result.returncode != 0:
        shutil.rmtree(str(path))	
    return

def cria_VPC_Subnet_InternetGateway(variables):
    try:
        dirname = f"terraform-aws/{variables['vpc_name']}-vpc-subnet-ig"
        path = os.path.join(parent_dir, dirname)
        main_orig_file = os.path.join(parent_dir, "cloudOptions/createVPC_Subnet_InternetGateway/main.tf")
        os.makedirs(path)
        shutil.copy(main_orig_file, path)
    except:
        print("O nome da sua vpc já existe, por favor escolha outro")
        return
    var_file = {
        "variable" : {
            "cidr_block" : {
                "default" : variables['vpc_cidr_block']
            },
            "name" : {
                "default" : variables['vpc_name']
            },
            "subnet_cidr_block" : {
                "default" : variables['subnet_cidr_block']
            },
            "subnet_name" : {
                "default" : variables['subnet_name']
            }, 
            "IG_name" : {
                "default" : variables['IG_name']
            }
        } 
    }
    json_object = json.dumps(var_file)
    with open(str(path)+"/variables.tf.json", "w") as f:
        f.write(json_object)
    result = subprocess.run("terraform init", cwd=path, shell=True)
    result = subprocess.run("terraform apply -auto-approve", cwd=path, shell=True)
    if result.returncode != 0:
        shutil.rmtree(str(path))	
    return

def cria_security_group(variables):
    try:
        dirname = f"terraform-aws/{variables['name']}-secGrp"
        path = os.path.join(parent_dir, dirname)
        main_orig_file = os.path.join(parent_dir, "cloudOptions/createSecurityGroup/main.tf")
        os.makedirs(path)
        shutil.copy(main_orig_file, path)
    except:
        print("O nome do seu security group já existe, por favor escolha outro")
        return
    var_file = {
        "locals": {
            "name" :  variables['name'],
            "ingress_rules" : [
                
            ],
            "egress_rules" : [

            ]
        } 
    }
    for rule in variables['ingress']:
        rule['cidr_blocks'] = [rule['cidr_blocks']]
        var_file["locals"]['ingress_rules'].append(rule)
    for rule in variables['egress']:
        rule['cidr_blocks'] = [rule['cidr_blocks']]
        var_file["locals"]['egress_rules'].append(rule)
    json_object = json.dumps(var_file)
    with open(str(path)+"/variables.tf.json", "w") as f:
        f.write(json_object)
    result = subprocess.run("terraform init", cwd=path, shell=True)
    result = subprocess.run("terraform apply -auto-approve", cwd=path, shell=True)
    if result.returncode != 0:
        shutil.rmtree(str(path))	
    return

def cria_IAM_user(variables):
    try:
        dirname = f"terraform-aws/{variables['user_name']}-user"
        path = os.path.join(parent_dir, dirname)
        main_orig_file = os.path.join(parent_dir, "cloudOptions/createIAMUser/main.tf")
        os.makedirs(path)
        shutil.copy(main_orig_file, path)
    except:
        print("Já existe um IAM User com esse nome, por favor escolha outro")
        return
    var_file = {
        "variable" : {
            "name" : {
                "default" : variables['user_name']
            }
        } 
    }
    json_object = json.dumps(var_file)
    with open(str(path)+"/variables.tf.json", "w") as f:
        f.write(json_object)
    result = subprocess.run("terraform init", cwd=path, shell=True)
    result = subprocess.run("terraform apply -auto-approve", cwd=path, shell=True)
    if result.returncode != 0:
        shutil.rmtree(str(path))	
    return

def deleta_user(variables):
    try:
        dirname = f"terraform-aws/{variables['user_name']}-user"
        path = os.path.join(parent_dir, dirname)
        os.system(f"""
        cd {str(path)}
        terraform destroy -auto-approve 
        """)
        shutil.rmtree(str(path))	
    except:
        print("O nome do seu IAM User não existe, por favor verifique")
    return

def deleta_secgrp(variables):
    try:
        dirname = f"terraform-aws/{variables['secGrp_name']}-secGrp"
        path = os.path.join(parent_dir, dirname)
        subprocess.run("terraform destroy -auto-approve", cwd=path, shell=True)
        shutil.rmtree(str(path))	
    except:
        print("O nome do seu security group não existe, por favor verifique")
    return

def deleta_vpc(variables):
    try:
        dirname = f"terraform-aws/{variables['vpc_name']}-{variables['vpc_type']}"
        path = os.path.join(parent_dir, dirname)
        subprocess.run("terraform destroy -auto-approve", cwd=path, shell=True)
        shutil.rmtree(str(path))	
    except:
        print("O nome da sua vpc não existe, por favor verifique")
    return

def deleta_instancia(variables):
    try:
        dirname = f"terraform-aws/{variables['ec2_name']}-ec2Instace"
        path = os.path.join(parent_dir, dirname)
        subprocess.run("terraform destroy -auto-approve", cwd=path, shell=True)
        shutil.rmtree(str(path))	
    except:
        print("O nome da sua instancia não existe, por favor verifique")
    return

def listSecurityGroup(path):
    with open(path, 'r') as f:
        f = json.load(f)
        for resource in f['resources']:
            print("---------------------------------------------")
            print("Name: {}".format(resource["instances"][0]["attributes"]["tags"]["Name"]))
            print("ID: {}".format(resource["instances"][0]["attributes"]["id"]))
            print("Region: us-east-1")
        try:
            for egress in resource["instances"][0]["attributes"]["egress"]:
                print("-- Egress Rule --")
                print("Cidr_blocks: {}".format(egress["cidr_blocks"][0]))
                print("From_port: {}".format(egress["from_port"]))
                print("To_port: {}".format(egress["to_port"]))
                print("Protocol: {}".format(egress["protocol"]))
        except:
            pass
        try:
            for ingress in resource["instances"][0]["attributes"]["ingress"]:
                print("-- Ingress Rule --")
                print("Cidr_blocks: {}".format(ingress["cidr_blocks"][0]))
                print("From_port: {}".format(ingress["from_port"]))
                print("To_port: {}".format(ingress["to_port"]))
                print("Protocol: {}".format(ingress["protocol"]))
        except:
            pass        
        print("---------------------------------------------")  

def list_all():
    path = os.path.join(parent_dir, "terraform-aws")
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "terraform.tfstate":
                if ('secGrp' in root.split('/')[-1]):
                    listSecurityGroup(os.path.join(root, file))
                else:
                    with open(os.path.join(root, file), 'r') as f:
                        f = json.load(f)
                        for resource in f['resources']:
                            print("---------------------------------------------")
                            print("Name: {}".format(resource["instances"][0]["attributes"]["tags"]["Name"]))
                            print("ID: {}".format(resource["instances"][0]["attributes"]["id"]))
                            print("Region: us-east-1")
                            print("---------------------------------------------")                