<div align="center">

# smart-inbox-triage

**AI-powered email triage dashboard. Automatically classifies incoming emails, routes action items for human review, and integrates with Notion and Google Calendar.**

![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-15-black?style=flat-square&logo=next.js)
![Python](https://img.shields.io/badge/Python-3.12-3776ab?style=flat-square&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ed?style=flat-square&logo=docker&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178c6?style=flat-square&logo=typescript&logoColor=white)

</div>

---

## Overview

Stop drowning in email. Smart Inbox Triage syncs your Gmail, classifies every message into actionable categories (RECEIPT, TASK, NEEDS_REPLY, CALENDAR_EVENT, NEWSLETTER, etc.), and surfaces ambiguous items in a review queue — letting you approve or reject AI-suggested actions with one click.

High-confidence, low-risk emails (newsletters, receipts) are handled automatically. High-stakes actions go through human review before executing. Every state transition is logged to a full audit trail.

## Features

- **Gmail OAuth sync** — Incremental sync via Gmail history API, deduplication by message hash
- **Rule-based classification engine** — 12 categories with confidence scoring and explainable reasons
- **User-defined rules** — Create/edit/reorder classification rules with AND/OR condition builders
- **Review queue** — Approve, reject, or edit AI-suggested actions before execution
- **Notion integration** — Auto-creates tasks in your Notion database from action emails
- **Google Calendar integration** — Auto-creates events from meeting/scheduling emails
- **Exponential backoff retry** — Failed downstream actions retry with configurable delays
- **Structured audit trail** — Immutable log of every state transition in the system
- **Full Docker Compose stack** — One command to start the entire application

## Tech Stack

| Layer | Tech |
|---|---|
| Backend | FastAPI, SQLAlchemy, Alembic, APScheduler |
| Frontend | Next.js 15, React, TypeScript, Tailwind CSS |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Auth | Google OAuth 2.0 with AES-256-GCM token encryption |
| Integrations | Gmail API, Notion API, Google Calendar API |
| Infrastructure | Docker Compose |

## Quick Start

```bash
git clone https://github.com/akularya6-del/smart-inbox-triage
cd smart-inbox-triage
cp .env.example .env
# Fill in GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, ENCRYPTION_KEY
docker compose up
```

Open [http://localhost:3000](http://localhost:3000), connect your Gmail, and start triaging.

## Architecture

```
smart-inbox-triage/
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI route handlers
│   │   ├── services/     # Gmail, Notion, Calendar, OAuth, Retry
│   │   ├── models/       # SQLAlchemy ORM models
│   │   └── tasks/        # Background jobs (sync, classify, execute, retry)
│   └── alembic/          # Database migrations
└── frontend/
    └── src/
        ├── components/   # Dashboard, Inbox, Review, Rules, Jobs, Logs, Settings
        └── hooks/        # TanStack Query data hooks
```

## Environment Variables

```env
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
ENCRYPTION_KEY=          # Random 32-byte hex string
NOTION_API_KEY=          # Optional
DATABASE_URL=sqlite:///./data/app.db
SYNC_INTERVAL_MINUTES=5
```

## Features

- fastapi
- nextjs
- ai
- email
- triage
- docker
- python
- typescript

## Getting Started

Clone the repo and follow the setup instructions in the code.
