
resource "aws_instance" "ubuntu_server" {
  ami = "ami-0786adace1541ca80"
  instance_type = "t2.micro"
  key_name = "201152448000"
  tags = {
    
    Name = "Autojar-Ubuntu-Server-C"
    Environment = "Lab-D417"
    Owner = "MayPwintPhyu_012334391"
  }
  root_block_device {
    volume_type = "gp2" #General purpose SSD
    volume_size = 8
  }
  lifecycle {
    ignore_changes = [
      tags,
      tags_all,
      root_block_device[0].tags
    ]
  }
}