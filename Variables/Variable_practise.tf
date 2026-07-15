## Creating variable with primitive types

# Integer, 
variable "instance_count" {
    type = Integer
    description = "Define number of inetance"
    default = 1
} 

variable "environment" {
    type = string
    description  = "Type env to deploy"
    default = "rect"
    #validation
    validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be rect, dev, staging, or prod."
  }
} 

variable "avaliabilty_zone" {
   type = list(string)
   description = "Az-to deploy"
   default = ["ap-south-1", "ap-south-2", "ap-south-3"]
   ## validation condition
   validation {
    condition     = contains(["ap-south-1", "ap-south-2", "ap-south-3"], var.avaliabilty_zone)
    error_message = "Environment must be ap-south-1, ap-south-2, ap-south-3."
  }
}

## set delete on termination in EC2 
variable "Delete the volume" {
      type = bool
      default = true
}
    