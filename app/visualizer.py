# Generates Mermaid graph syntax from IAM policy

def generate_mermaid_graph(parsed_policy):
    mermaid_lines = ["graph TD"]

    for i, stmt in enumerate(parsed_policy):
        actions = stmt.get("Action", [])
        resources = stmt.get("Resource", [])
        effect = stmt.get("Effect", "Unknown")
        condition = stmt.get("Condition", {})

        for action in actions:
            for resource in resources:
                user_node = f'User{i}["User or Role {i+1} ({effect})"]'
                action_node = f'Action{i}_{action.replace(":", "_")}["{action}"]'
                resource_node = f'Resource{i}_{resource.replace("*", "ALL")}["{resource}"]'

                mermaid_lines.append(f'{user_node} --> {action_node} --> {resource_node}')

                if condition:
                    cond_text = str(condition).replace('"', '').replace("'", "")
                    condition_node = f'Condition{i}["Condition: {cond_text}"]'
                    mermaid_lines.append(f'{action_node} --- {condition_node}')

    return "\n".join(mermaid_lines)
