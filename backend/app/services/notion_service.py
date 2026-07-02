from app.config import settings
from app.core.exceptions import ActionExecutionError
import httpx
import structlog

logger = structlog.get_logger(__name__)

async def create_notion_task(title: str, description: str, priority: str = "Medium"):
    if not settings.NOTION_API_KEY or not settings.NOTION_DATABASE_ID:
        raise ActionExecutionError("Notion integration is not configured.")
        
    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {settings.NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    # Truncate description if too long
    if description and len(description) > 2000:
        description = description[:1997] + "..."
        
    data = {
        "parent": {"database_id": settings.NOTION_DATABASE_ID},
        "properties": {
            "Name": {
                "title": [{"text": {"content": title}}]
            },
            "Status": {
                "status": {"name": "Not started"}
            },
            "Priority": {
                "select": {"name": priority}
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": description or "No description provided."}}]
                }
            }
        ]
    }
    
    async with httpx.AsyncClient() as client:
        resp = await client.post(url, headers=headers, json=data)
        if resp.status_code != 200:
            logger.error(f"Notion API error: {resp.text}")
            raise ActionExecutionError(f"Notion API returned {resp.status_code}")
        
    return resp.json().get("id")
