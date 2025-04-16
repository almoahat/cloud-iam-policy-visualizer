# Entry point
import web.app

import json
from app.analyzer import parse_policy

with open("sample_policies/sample_iam_policy.json") as f:
    policy = json.load(f)

parsed = parse_policy(policy)
print(json.dumps(parsed, indent=2))
