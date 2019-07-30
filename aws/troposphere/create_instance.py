from troposphere import Ref, Template
import troposphere.ec2 as ec2

t = Template()
instance = ec2.Instance("myinstance")

# https://cloud-images.ubuntu.com/locator/ec2/
instance.ImageId = "ami-0499a641a2a0e5da9"
instance.InstanceType = "t1.micro"
t.add_resource(instance)

f = open("ec2.yml", "w+")
f.write(t.to_yaml())

f.close()