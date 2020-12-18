import boto3
import pprint
from sshconf import read_ssh_config
from os.path import expanduser

c = read_ssh_config(expanduser("~/.ssh/config"))
ec2 = boto3.resource('ec2')

def findDevelopmentInstance():
    for instance in ec2.instances.all():
            for tag in instance.tags:
                    if tag['Value'] == 'DevelopmentMachine':
                        instance.start()
                        instanceId = instance.instance_id 
    return instanceId

def updateSSHConfigFile(instanceId):        
    devInstance = ec2.Instance(instanceId)
    devInstance.wait_until_running()
    instancePublicIP = devInstance.public_ip_address
    print("aws-ec2 host", c.host("aws-ec2"))
    c.set("aws-ec2", Hostname=instancePublicIP)
    print("aws-ec2 host now", c.host("aws-ec2"))
    c.save()

developmentInstanceId = findDevelopmentInstance()
updateSSHConfigFile(developmentInstanceId)