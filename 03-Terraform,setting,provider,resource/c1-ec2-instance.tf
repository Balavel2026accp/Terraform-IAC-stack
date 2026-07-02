####### resouce creation ec2-instance #####
resource "aws_instance" "Lab1" {
    ami = "ami-0011550b539717e2a"
    instance_type = "t3.micro"
    user_data = file("${path.module}/app1-install.sh")
    key_name = "terraform-key"

    tags = {
      Name = "lab1-server"
    }
} 