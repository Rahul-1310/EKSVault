{
  "source": ["aws.ec2"],
  "detail": (
    "awsRegion": ["us-east-1"],
    "responseElements":
      "networkInterface":
        "networkInterfaceId": [{
          "exists": true
        }]
        }
    },
  "eventSource": ["ec2.amazonaws.com"],
  "eventName" : ["CreateNetworkInterface"],
  "userIdentity": {
    "sessionContext": {
      "sessionIssuer": {
        "userName": ["AWSServiceRoleForAmazonEKS"]
      }
    }
  },
  "request Parameters": {
    "description": ["Amazon EKS ‹your clustername›"]
I    }
}
}
