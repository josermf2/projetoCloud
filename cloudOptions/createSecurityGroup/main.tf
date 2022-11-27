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

resource "aws_security_group" "attrs" {
  name = local.name

  dynamic "ingress" {
    for_each = local.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }

  dynamic "egress" {
    for_each = local.egress_rules
    content {
      from_port   = egress.value.port
      to_port     = egress.value.port
      protocol    = egress.value.protocol
      cidr_blocks = egress.value.cidr_blocks
    }

  }
  
  tags = {
    Name : local.name
  }
}
