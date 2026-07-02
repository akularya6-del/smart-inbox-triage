from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.rule import Rule
from pydantic import BaseModel
from typing import List, Dict, Any, Optional

router = APIRouter(prefix="/rules", tags=["Rules"])

class RuleCreate(BaseModel):
    user_id: str
    name: str
    enabled: bool = True
    priority: int = 1
    conditions: Dict[str, Any]
    action: str

class RuleResponse(RuleCreate):
    id: str
    
    class Config:
        from_attributes = True

@router.get("/", response_model=List[RuleResponse])
def list_rules(user_id: str, db: Session = Depends(get_db)):
    return db.query(Rule).filter(Rule.user_id == user_id).order_by(Rule.priority).all()

@router.post("/", response_model=RuleResponse)
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    db_rule = Rule(**rule.model_dump())
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule

@router.delete("/{rule_id}")
def delete_rule(rule_id: str, db: Session = Depends(get_db)):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    db.delete(rule)
    db.commit()
    return {"status": "deleted"}
