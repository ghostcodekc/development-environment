# aws-environment

This repo contains a [Cloudformation template](./dev-server-template.yaml) to deploy infrastructure and an EC2 Instance for software development.

## Requirements

- VSCode with Remote-SSH extension installed and configured.
  - powerOnDevServer.py will update the config file with the dev machine IP.
- AWS Account
  - Configured AWS CLI on your local machine
- EC2 Keypair
- Python 3 installed on your local machine

## What's in the box?

This will deploy a Amazon Linux EC2 instance, a VPC with subnets, and an Instance Profile granting admin access, and a cloudwatch alarm to turn off the instance after 10 minutes of inactivity.

## What do I do with it?

Write and deploy code!

I recommend making desired changes to this AMI and burning a new AMI with your preferred configurations built in. For example, you could install your favorite version of python, securely store credentials, configure your dotfiles.

## How much will it cost me?

Leaving this instance stopped for a month will incur about an $0.80 bill in us-east-1. The reason for this is the 8 GB EBS volume that is provisioned: `$0.10 per GB-month of General Purpose SSD (gp2) provisioned storage - US East (Northern Virginia)`

Small instances however, are very cheap to run. You can usually get a machine big enough for your development needs for under $0.01 an hour. [Here is the EC2 Instance Pricing page.](https://aws.amazon.com/ec2/pricing/on-demand/)

## How Do I Get Started?

- Log into you AWS console and go to CloudFormation
- Deploy the dev-server-template.yaml
  - Turn off the server in the AWS EC2 Console.
- After the infrastructure deployment is complete, run the following command:
  - pip install -r Automation\requirements.txt\
- Run "powerOnDevServer.py"

That's it! VSCode is now ready to connect to the machine using Remote-SSH
