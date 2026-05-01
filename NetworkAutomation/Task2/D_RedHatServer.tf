resource "aws_instance" "redhat_server" {
  ami           = "ami-026fc9b0dc11499dc" 
  instance_type = "t2.micro"
  key_name = "201152448000"
  tags = {
    Name        = "Autojor-RedHat-Server-D"
    Environment = "Lab-D417"
    Owner       = "MayPwintPhyu_012334391"
  }
  root_block_device {
    volume_type = "gp2"
    volume_size = 10
  }
  lifecycle {
    ignore_changes = [
      tags,
      tags_all,
      root_block_device[0].tags
    ]
  }
}