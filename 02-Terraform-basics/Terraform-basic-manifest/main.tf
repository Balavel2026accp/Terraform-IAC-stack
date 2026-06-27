resource "aws_instance" "terraform_node" {
    ami = "ami-0011550b539717e2a"
    instance_type = var.intance_type
    region = var.region

    #key_name = "terraform-key"

    tags = {
       Name = "Terraform-node"
    }
  
}