# Parses IAM policies

def parse_policy(policy_json):
    try:
        statements = policy_json.get("Statement", [])
        if isinstance(statements, dict):
            statements = [statements]

        parsed = []
        for stmt in statements:
            parsed.append({
                "Effect": stmt.get("Effect"),
                "Action": stmt.get("Action") if isinstance(stmt.get("Action"), list) else [stmt.get("Action")],
                "Resource": stmt.get("Resource") if isinstance(stmt.get("Resource"), list) else [stmt.get("Resource")],
                "Condition": stmt.get("Condition", {})
            })
        return parsed
    except Exception as e:
        print(f"Error parsing policy: {e}")
        raise
