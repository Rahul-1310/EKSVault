
import botoß 
import logging
From botocore.exceptions import ClientError
elb = boto3.client('elbv2')
tg_arn = "arn:aws:elasticloadbalancing: eu-west-1:008155010674: targetgroup/siebelupgrade-E7-vaulttg-443/4c67a232341610a4"
iplist = elb.describe_target.
_health (TargetGroupArn=tg_arn) ["TargetHealthDescriptions"]
currenttargets = [1
unhealthytargets = ［］
for i in iplist:
if (1["TargetHealth"]["State"] != "healthy"): unhealthytargets.append (i["Target"]["Id"])
else:
currenttargets append (1["Target"]["Id"])
print(iplist)
I
def
register_targets (newtargets) :
For ip in newtargets:
if ip in currenttargets:
print ("Target already registered")
else:
print("Registering new target (}". format (newtargets) )
targetreponse = elb.register_targets(
TargetGroupArn=tg_arn,
Targets=[
'Id': ip,
"Port': 443
}
try:
waiter = elb.get_waiter( 'target_in_service')
waiter.wait(
TargetGroupArn=tg_arn,
Targets=[
｛
'Id': ip,
'Port': 443