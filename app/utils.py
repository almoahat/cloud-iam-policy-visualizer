# Helper functions

import boto3

def fetch_policy_from_aws(policy_arn):
    client = boto3.client("iam")
    response = client.get_policy(PolicyArn=policy_arn)
    default_version = response["Policy"]["DefaultVersionId"]

    version = client.get_policy_version(
        PolicyArn=policy_arn,
        VersionId=default_version
    )
    return version["PolicyVersion"]["Document"]
