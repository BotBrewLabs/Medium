import boto3

def list_public_s3_buckets():
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()['Buckets']
    
    for bucket in buckets:
        try:
            acl = s3.get_bucket_acl(Bucket=bucket['Name'])
            for grant in acl['Grants']:
                if 'URI' in grant['Grantee']:
                    if 'http://acs.amazonaws.com/groups/global/AllUsers' in grant['Grantee']['URI']:
                        print(f"Publicly Accessible Bucket Found: {bucket['Name']}")
        except Exception as e:
            print(f"Error checking bucket {bucket['Name']}: {e}")

def list_ec2_security_groups():
    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups()

    for sg in response['SecurityGroups']:
        print(f"Security Group: {sg['GroupName']} ({sg['GroupId']})")
        for rule in sg['IpPermissions']:
            if '0.0.0.0/0' in str(rule.get('IpRanges')):
                print(f"  Inbound rule allowing public access: {rule}")

if __name__ == '__main__':
    print("Checking AWS Infrastructure for vulnerabilities...\n")
    
    print("S3 Buckets:")
    list_public_s3_buckets()
    
    print("\nEC2 Security Groups:")
    list_ec2_security_groups()
