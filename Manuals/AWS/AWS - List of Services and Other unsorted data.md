![[Images/Pasted image 20211217182212.png]]

Regions and Zones of AWS - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions

ASW S3 Portal - https://aws.amazon.com/s3/

Simple Storage Service (S3)

Configure a profile ASIA file 
* aws configure --profile {profileName}

Adds data to
* .aws/config
* aws/credential

List all buckets assigned to creditals harvested: 
* aws s3 ls --profile {profileName}

 few other common AWS reconnaissance techniques are:
Finding the Account ID belonging to an access key:
* aws sts get-access-key-info --access-key-id AKIAEXAMPLE 

Determining the Username the access key you're using belongs to
* aws sts get-caller-identity --profile PROFILENAME

Listing all the EC2 instances running in an account
* aws ec2 describe-instances --output text --profile PROFILENAME

Listing all the EC2 instances running in an account in a different region
* aws ec2 describe-instances --output text --region us-east-1 --profile PROFILENAME

AWS ARNs
arn:aws:<service>:<region>:<account_id>:<resource_type>/<resource_name>
	
	