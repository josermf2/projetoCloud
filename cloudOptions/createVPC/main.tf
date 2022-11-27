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

resource "aws_vpc" "newVPC" {
 cidr_block = var.cidr_block
 
 tags = {
   Name = var.name
 }
}

