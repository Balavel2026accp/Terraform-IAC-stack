##demo creation
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

## terraform values
variable "terraform_ec2_region" {
    default = "ap-south-1" 
}

variable "instance_type" {
    default = "t3.micro" 
}

##main.tf 
resource "aws_instance" "Terraform_demo" {
  ami = "ami-0011550b539717e2a"
  region = var.terraform_ec2_region
  instance_type = var.instance_type

  tags = {
    Name = "test-ins"
  }
}