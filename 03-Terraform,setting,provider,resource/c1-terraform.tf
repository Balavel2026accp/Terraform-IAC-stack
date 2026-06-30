##########################################################################
# Terraform setting block
terraform {
  required_version = "~> 0.14.8" # it will allow only form 14.8 not below version.
  required_providers {
   aws ={                        # local name of the provider its prefre to use the offical give name from provider document.
    source  = "hashicorp/aws"
    version = "~>6.0"
   }
  }
}   
##terraform here is block {} aws is map aws = {}
/*
######Why and how to choose the profile in the provider configuration.####


[ec2-user@ip-172-31-37-246 aws]$ aws configure list
NAME       : VALUE                    : TYPE             : LOCATION
profile    : <not set>                : None             : None
access_key : ****************R254     : shared-credentials-file :
secret_key : ****************buad     : shared-credentials-file :
region     : ap-south-1               : config-file      : ~/.aws/config
[ec2-user@ip-172-31-37-246 aws]$ cat ~/.aws/config
[default]
region = ap-south-1
output = json
[ec2-user@ip-172-31-37-246 aws]$
[ec2-user@ip-172-31-37-246 aws]$



 */

 provider "aws" {
    region = "ap-south-1"
   # profile = default   # it is not mandatory when we use the default profile for api communucation with aws. 
 }