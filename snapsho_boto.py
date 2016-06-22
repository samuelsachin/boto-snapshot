
import boto3

ec2 = boto3.resource('ec2',region_name='eu-west-1')

s1 = ec2.create_snapshot(VolumeId='vol-id', Description='discription')
