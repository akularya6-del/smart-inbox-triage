import re
from app.models.email import Email
from app.models.rule import Rule

def evaluate_condition(email: Email, condition: dict) -> bool:
    """Evaluates a single condition like {'field': 'subject', 'operator': 'contains', 'value': 'invoice'}"""
    field = condition.get("field")
    operator = condition.get("operator")
    value = condition.get("value", "").lower()
    
    email_val = getattr(email, field, "")
    if not isinstance(email_val, str):
        email_val = str(email_val)
    email_val = email_val.lower()
    
    if operator == "contains":
        return value in email_val
    elif operator == "equals":
        return value == email_val
    elif operator == "starts_with":
        return email_val.startswith(value)
    elif operator == "ends_with":
        return email_val.endswith(value)
    elif operator == "regex":
        try:
            return bool(re.search(value, email_val))
        except re.error:
            return False
    return False

def evaluate_rule(email: Email, rule: Rule) -> bool:
    """Evaluates a full rule with AND/OR logic"""
    # Assuming conditions format: {"type": "AND", "rules": [{field:...}, {field:...}]}
    # Or simple list of conditions (implicit AND)
    conditions = rule.conditions
    
    if isinstance(conditions, list):
        # Implicit AND
        return all(evaluate_condition(email, cond) for cond in conditions)
    elif isinstance(conditions, dict):
        cond_type = conditions.get("type", "AND").upper()
        rules = conditions.get("rules", [])
        if cond_type == "AND":
            return all(evaluate_condition(email, cond) for cond in rules)
        elif cond_type == "OR":
            return any(evaluate_condition(email, cond) for cond in rules)
    return False

def find_matching_rule(email: Email, rules: list[Rule]) -> Rule | None:
    """Returns the highest priority matching rule"""
    # rules should be ordered by priority ASC (1 is highest)
    for rule in sorted(rules, key=lambda x: x.priority):
        if not rule.enabled:
            continue
        if evaluate_rule(email, rule):
            return rule
    return None
