import pytest
from app.services.rule_engine import evaluate_condition, evaluate_rule, find_matching_rule
from app.models.email import Email
from app.models.rule import Rule

def test_evaluate_condition_contains():
    email = Email(subject="Invoice for July", sender_email="test@example.com")
    cond = {"field": "subject", "operator": "contains", "value": "invoice"}
    assert evaluate_condition(email, cond) is True

def test_evaluate_condition_starts_with():
    email = Email(subject="URGENT: Action required", sender_email="test@example.com")
    cond = {"field": "subject", "operator": "starts_with", "value": "urgent"}
    assert evaluate_condition(email, cond) is True

def test_evaluate_rule_and():
    email = Email(subject="Invoice for July", sender_email="test@example.com")
    rule = Rule(
        conditions={"type": "AND", "rules": [
            {"field": "subject", "operator": "contains", "value": "invoice"},
            {"field": "sender_email", "operator": "equals", "value": "test@example.com"}
        ]}
    )
    assert evaluate_rule(email, rule) is True

def test_find_matching_rule():
    email = Email(subject="Urgent issue", sender_email="boss@corp.com")
    rule1 = Rule(priority=2, enabled=True, action="MoveToFinance", conditions=[{"field": "subject", "operator": "contains", "value": "invoice"}])
    rule2 = Rule(priority=1, enabled=True, action="MoveToUrgent", conditions=[{"field": "subject", "operator": "contains", "value": "urgent"}])
    
    match = find_matching_rule(email, [rule1, rule2])
    assert match is rule2
