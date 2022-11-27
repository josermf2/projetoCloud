terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 4.39.0"
    }
  }
}

provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "web" {
    ami = "ami-0ee23bfc74a881de5"
    instance_type = var.instance_type
    vpc_security_group_ids = var.security_group_id
    subnet_id = var.subnet_id

    tags = {
        Name = var.name
    }
}