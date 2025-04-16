# Unit test for analyzer


from app.analyzer import parse_policy

def test_parse_policy():
    sample = {
        "Statement": {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        }
    }
    result = parse_policy(sample)
    assert result[0]["Action"] == ["s3:*"]
    assert result[0]["Effect"] == ["Allow"]
    assert result[0]["Resource"] == ["*"]
    assert result[0]["Action"] == []
    return result

def test_parse_single_statement():
    input_policy = {
        "Statement": {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "*"
        }
    }
    result = parse_policy(input_policy)
    assert isinstance(result, list)
    assert result[0]["Action"] == ["s3:ListBucket"]
    assert result[0]["Resource"] == ["*"]

def test_parse_multiple_actions():
    input_policy = {
        "Statement": {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject"],
            "Resource": ["arn:aws:s3:::mybucket/*"]
        }
    }
    result = parse_policy(input_policy)
    assert len(result[0]["Action"]) == 2

def test_parse_with_condition():
    input_policy = {
        "Statement": {
            "Effect": "Deny",
            "Action": "ec2:TerminateInstances",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:RequestedRegion": "us-west-2"
                }
            }
        }
    }
    result = parse_policy(input_policy)
    assert "Condition" in result[0]
    assert "StringNotEquals" in result[0]["Condition"]