
import botoß 
import logging
From botocore.exceptions import ClientError
elb = boto3.client('elbv2')
tg_arn = "<TG-ARN>"
iplist = elb.describe_target_health(TargetGroupArn=tg_arn)["TargetHealthDescriptions"]
currenttargets = []
unhealthytargets = []
for i in iplist:
  if (1["TargetHealth"]["State"] != "healthy"): 
    unhealthytargets.append (i["Target"]["Id"])
  else:
    currenttargets append (1["Target"]["Id"])
print(iplist)

def register_targets (newtargets):
  for ip in newtargets:
    if ip in currenttargets:
      print ("Target already registered")
    else:
      print("Registering new target (}". format (newtargets))
      targetreponse = elb.register_targets(
        TargetGroupArn=tg_arn,
        Targets=[
          {
          'Id': ip,
          'Port': 443
          },
        ]
      )
      try:
        waiter = elb.get_waiter( 'target_in_service')
        waiter.wait(
          TargetGroupArn=tg_arn,
          Targets=[
            {    
            'Id': ip,
            'Port': 443
            }
          ],
            
