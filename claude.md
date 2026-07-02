# SMART INBOX TRIAGE DASHBOARD — FULL AUTONOMOUS BUILD DIRECTIVE

## MISSION PARAMETERS

You are operating in FULL AUTONOMOUS MODE. There will be NO human approvals, NO pauses for confirmation, NO interactive prompts. You will read the PRD at `./PRD.md`, decompose it into atomic implementation units, and execute them sequentially and in parallel where possible until every single functional requirement, acceptance criterion, and definition-of-done item is satisfied.

This is a Ralph-style autonomous agent loop. You will:
1. Parse the PRD completely
2. Generate a task graph with dependencies
3. Execute tasks in topological order
4. Self-verify each completed task against PRD acceptance criteria
5. Log progress continuously
6. Never stop until the project is complete or you hit an unrecoverable error (in which case, log it and attempt workaround)

## SKILL LOADING DIRECTIVE

The following skills are installed and available. You MUST actively use every single one where applicable — not just acknowledge them:

### Skill 1: Ralph (snarktank/ralph)
- **Purpose**: Autonomous agent loop that runs repeatedly until all PRD items are complete
- **How to use**: After completing each milestone, re-read the PRD, check off completed items, identify remaining items, and continue the loop. Never exit the loop early. Maintain a `.ralph-progress.md` file tracking every PRD item's status: `[ ]` incomplete, `[~]` in-progress, `[x]` verified complete.

### Skill 2: Ruflo (ruvnet/ruflo)
- **Purpose**: Workflow orchestration and flow management
- **How to use**: Use ruflo patterns for managing the multi-step email processing pipeline (fetch → normalize → classify → review → execute → audit). Each pipeline stage should be a discrete, testable flow unit.

### Skill 3: Andrej Karpathy Skills (multica-ai/andrej-karpathy-skills)
- **Purpose**: Deep implementation rigor, first-principles thinking, build-from-scratch mental models
- **How to use**: When building the classification engine, rule engine, and state machine, apply Karpathy-style thinking — understand WHY each design decision is made, implement from first principles, never cargo-cult. Write clean, readable code with clear variable names and comments explaining the reasoning.

### Skill 4: GSD Core (@opengsd/gsd-core)
- **Purpose**: Get Stuff Done — execution framework, task decomposition, progress tracking
- **How to use**: Decompose each PRD section into concrete files-to-create and code-to-write. Track in `.gsd-tasks.json`. Before writing any code, the task must exist in that file with a clear definition of done.

### Skill 5: UI/UX Pro Max Skill (nextlevelbuilder/ui-ux-pro-max-skill)
- **Purpose**: Professional-grade UI/UX implementation
- **How to use**: The dashboard must look and feel like a production SaaS product. Apply:
  - Consistent spacing system (4px grid)
  - Professional color palette with semantic colors (success=green, warning=amber, error=red, info=blue)
  - Proper typography hierarchy
  - Smooth transitions and micro-interactions
  - Responsive layout (sidebar + main content)
  - Empty states, loading states, error states for EVERY view
  - Toast notifications for actions
  - Proper form validation with inline errors
  - Data tables with sorting, filtering, pagination
  - Card-based layouts for widgets
  - Proper iconography using Lucide icons
  - Dark/light theme support
  - Accessibility: proper ARIA labels, keyboard navigation, focus management

### Skill 6: Find Skills (vercel-labs/skills/find-skills)
- **Purpose**: Dynamically discover additional skills when needed
- **How to use**: If at any point you encounter a domain you're not expert in (e.g., OAuth flows, WebSocket patterns, Docker optimization), use find-skills to locate and load relevant additional capabilities.

### Skill 7: Superpowers (obra/Superpowers)
- **Purpose**: Enhanced reasoning, planning, and code generation capabilities
- **How to use**: Apply superpowers-level thinking to architectural decisions. The system architecture in the PRD is a guide, but you should make optimal decisions about file structure, module boundaries, error handling patterns, and API design. Think beyond the PRD where it's underspecified.

### Skill 8: Claude Mem (thedotmack/claude-mem)
- **Purpose**: Persistent memory across sessions
- **How to use**: After every significant milestone completion, write a memory checkpoint to `.claude-mem/memory.md` containing: what was built, key decisions made, files created/modified, any issues encountered and their solutions. This enables recovery if the session is interrupted.

### Skill 9: Impeccable (pbakaus/impeccable)
- **Purpose**: Flawless code quality — no shortcuts, no TODOs left behind, production-grade output
- **How to use**: Every file you create must be:
  - Complete (no placeholder functions, no `pass`, no `// TODO`)
  - Properly typed (TypeScript strict mode, Python type hints everywhere)
  - Properly error-handled (no uncaught exceptions possible)
  - Properly structured (single responsibility, clear module boundaries)
  - Import-complete (all imports resolve, no circular dependencies)
  - Lint-ready (consistent style, no dead code)

### Skill 10: One Skill to Rule Them All (rebelytics/one-skill-to-rule-them-all)
- **Purpose**: Meta-skill that ensures all other skills are properly coordinated and utilized
- **How to use**: This is the orchestrator. Before each major phase, pause (internally) and verify all applicable skills are being applied. Use it as a checklist: Ralph loop active? UI/UX quality applied? Impeccable standards met? Memory checkpointed? GSD tasks tracked?

---

## PROJECT STRUCTURE TO CREATE

```
smart-inbox-triage/
├── PRD.md                          # (already exists)
├── README.md                       # Full setup instructions, <10 min install
├── .ralph-progress.md              # Ralph loop progress tracker
├── .gsd-tasks.json                 # GSD task tracking
├── .claude-mem/
│   └── memory.md                   # Session memory checkpoints
├── docker-compose.yml              # Full stack orchestration
├── Dockerfile.backend              # Python FastAPI backend
├── Dockerfile.frontend             # React frontend
├── .env.example                    # All required env vars documented
├── Makefile                        # Common commands
│
├── backend/
│   ├── pyproject.toml              # Dependencies with pinned versions
│   ├── alembic.ini                 # DB migrations config
│   ├── alembic/
│   │   ├── env.py
│   │   └── versions/               # Migration files
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI app entry, CORS, lifespan
│   │   ├── config.py               # Pydantic Settings, all configuration
│   │   ├── database.py             # SQLAlchemy engine, session, Base
│   │   ├── models/                 # SQLAlchemy ORM models
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── oauth_token.py
│   │   │   ├── email.py
│   │   │   ├── email_label.py
│   │   │   ├── rule.py
│   │   │   ├── classification.py
│   │   │   ├── review_queue.py
│   │   │   ├── task.py
│   │   │   ├── calendar_event.py
│   │   │   ├── job.py
│   │   │   ├── job_log.py
│   │   │   ├── retry_queue.py
│   │   │   ├── audit_log.py
│   │   │   └── setting.py
│   │   ├── schemas/                # Pydantic request/response schemas
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── email.py
│   │   │   ├── rule.py
│   │   │   ├── review.py
│   │   │   ├── task.py
│   │   │   ├── calendar.py
│   │   │   ├── job.py
│   │   │   ├── log.py
│   │   │   └── setting.py
│   │   ├── api/                    # Route handlers
│   │   │   ├── __init__.py
│   │   │   ├── router.py           # Main router aggregating all sub-routers
│   │   │   ├── auth.py             # POST /auth/google/start, GET /callback, POST /disconnect
│   │   │   ├── emails.py           # POST /sync/start, GET /emails, GET /emails/{id}, GET /emails/search
│   │   │   ├── review.py           # GET /review, POST /review/{id}/approve|reject|edit
│   │   │   ├── rules.py            # CRUD /rules
│   │   │   ├── jobs.py             # GET /jobs, POST /jobs/{id}/retry|cancel
│   │   │   ├── logs.py             # GET /logs, GET /audit
│   │   │   └── settings.py         # GET /settings, PUT /settings
│   │   ├── services/               # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── oauth_service.py    # Google OAuth flow, token management, encryption
│   │   │   ├── gmail_service.py    # Gmail API: fetch, paginate, incremental sync
│   │   │   ├── email_normalizer.py # Raw Gmail → normalized Email model
│   │   │   ├── classification_engine.py  # Rule-based + heuristic classification
│   │   │   ├── rule_engine.py      # User-defined rules, priority ordering, matching
│   │   │   ├── review_service.py   # Queue management, status transitions
│   │   │   ├── action_executor.py  # Dispatch actions: Notion, Calendar, Labels, etc.
│   │   │   ├── notion_service.py   # Notion API: database selection, task creation
│   │   │   ├── calendar_service.py # Google Calendar: event creation
│   │   │   ├── scheduler_service.py # APScheduler config, job management
│   │   │   ├── retry_service.py    # Exponential backoff retry logic
│   │   │   └── notification_service.py # Desktop notifications
│   │   ├── core/                   # Shared utilities
│   │   │   ├── __init__.py
│   │   │   ├── security.py         # Token encryption, secret masking
│   │   │   ├── logging.py          # Structlog configuration, JSON logs
│   │   │   ├── exceptions.py       # Custom exception hierarchy
│   │   │   └── utils.py            # Hashing, deduplication helpers
│   │   └── tasks/                  # Background task definitions
│   │       ├── __init__.py
│   │       ├── sync_task.py        # Email sync background job
│   │       ├── classify_task.py    # Classification pipeline job
│   │       └── action_task.py      # Action execution job
│   └── tests/
│       ├── conftest.py
│       ├── test_oauth_service.py
│       ├── test_gmail_service.py
│       ├── test_email_normalizer.py
│       ├── test_classification_engine.py
│       ├── test_rule_engine.py
│       ├── test_review_service.py
│       ├── test_action_executor.py
│       ├── test_retry_service.py
│       ├── test_scheduler_service.py
│       ├── test_api_auth.py
│       ├── test_api_emails.py
│       ├── test_api_review.py
│       ├── test_api_rules.py
│       └── test_api_jobs.py
│
└── frontend/
    ├── package.json
    ├── vite.config.ts
    ├── tsconfig.json
    ├── tailwind.config.ts
    ├── postcss.config.js
    ├── index.html
    ├── public/
    │   └── favicon.svg
    └── src/
        ├── main.tsx
        ├── App.tsx
        ├── index.css                 # Tailwind imports + custom CSS variables
        ├── vite-env.d.ts
        ├── lib/
        │   ├── api.ts                # Axios/fetch client, base URL config
        │   ├── query-client.ts       # TanStack Query client setup
        │   ├── utils.ts              # cn() helper, formatters
        │   └── types.ts              # Shared TypeScript types
        ├── hooks/
        │   ├── use-auth.ts
        │   ├── use-emails.ts
        │   ├── use-review.ts
        │   ├── use-rules.ts
        │   ├── use-jobs.ts
        │   ├── use-logs.ts
        │   ├── use-settings.ts
        │   └── use-websocket.ts      # Real-time job updates
        ├── components/
        │   ├── ui/                   # ShadCN components (button, card, dialog, table, input, select, badge, toast, dropdown-menu, tabs, skeleton, tooltip, popover, command, separator, scroll-area, sheet, avatar, switch, label, textarea, checkbox)
        │   ├── layout/
        │   │   ├── AppLayout.tsx     # Sidebar + main content shell
        │   │   ├── Sidebar.tsx       # Navigation sidebar with icons
        │   │   ├── Header.tsx        # Top bar with user info, sync button
        │   │   └── MobileNav.tsx     # Mobile responsive navigation
        │   ├── dashboard/
        │   │   ├── DashboardPage.tsx
        │   │   ├── StatsCards.tsx    # Unread today, tasks, events, pending, failed
        │   │   ├── ActivityFeed.tsx  # Recent activity timeline
        │   │   ├── ProcessingChart.tsx # Processing time visualization
        │   │   └── QuickActions.tsx  # Sync now, view queue, etc.
        │   ├── inbox/
        │   │   ├── InboxPage.tsx
        │   │   ├── EmailList.tsx
        │   │   ├── EmailRow.tsx
        │   │   ├── EmailDetail.tsx   # Slide-out panel or modal
        │   │   ├── EmailSearch.tsx
        │   │   ├── EmailFilters.tsx
        │   │   └── BulkActions.tsx
        │   ├── review/
        │   │   ├── ReviewPage.tsx
        │   │   ├── ReviewCard.tsx    # Email preview + suggested action + buttons
        │   │   ├── ReviewBulkActions.tsx
        │   │   └── ConfidenceFilter.tsx
        │   ├── rules/
        │   │   ├── RulesPage.tsx
        │   │   ├── RuleEditor.tsx    # Create/edit rule form
        │   │   ├── RuleList.tsx
        │   │   └── RulePrioritySelector.tsx
        │   ├── history/
        │   │   ├── HistoryPage.tsx
        │   │   ├── HistoryTimeline.tsx
        │   │   └── HistoryDetail.tsx
        │   ├── jobs/
        │   │   ├── JobsPage.tsx
        │   │   ├── JobList.tsx
        │   │   ├── JobDetail.tsx     # Logs for a specific job
        │   │   └── JobStatusBadge.tsx
        │   ├── logs/
        │   │   ├── LogsPage.tsx
        │   │   ├── LogViewer.tsx     # Structured log display with severity filtering
        │   │   └── AuditTrail.tsx    # State transition table
        │   ├── settings/
        │   │   ├── SettingsPage.tsx
        │   │   ├── OAuthSettings.tsx
        │   │   ├── SchedulerSettings.tsx
        │   │   ├── RetrySettings.tsx
        │   │   ├── IntegrationSettings.tsx  # Notion + Calendar API keys
        │   │   ├── ThemeSettings.tsx
        │   │   ├── BackupSettings.tsx
        │   │   └── DangerZone.tsx
        │   └── auth/
        │       ├── LoginPage.tsx
        │       ├── GoogleCallback.tsx
        │       └── DisconnectConfirm.tsx
        └── pages/
            └── index.tsx             # Route definitions using React Router
```

---

## EXECUTION PHASES — DETAILED INSTRUCTIONS

### PHASE 1: FOUNDATION (Files → Code → Verify)

**1.1 Project Scaffolding**
- Create the entire directory structure above
- Initialize `backend/` as a Python project with `pyproject.toml` containing ALL dependencies:
  - fastapi, uvicorn[standard], sqlalchemy, alembic, pydantic, pydantic-settings
  - google-auth, google-auth-oauthlib, google-auth-httplib2, google-api-python-client
  - httpx, aiohttp (for async HTTP)
  - apscheduler
  - structlog, python-json-logger
  - cryptography (for token encryption)
  - python-dotenv
  - pytest, pytest-asyncio, pytest-cov, httpx (for test client)
  - waitress (production ASGI server)
- Initialize `frontend/` with `npm create vite@latest . -- --template react-ts`
- Install ALL frontend dependencies:
  - tailwindcss, postcss, autoprefixer, @tailwindcss/typography
  - react-router-dom, @tanstack/react-query, @tanstack/react-query-devtools
  - axios
  - lucide-react
  - date-fns
  - recharts (for dashboard charts)
  - clsx, tailwind-merge
  - shadcn/ui (initialize and add ALL components listed above)
  - sonner (toast notifications)
  - cmdk (command palette)
- Create `.env.example` with every required variable documented
- Create `Makefile` with commands: `dev`, `dev-backend`, `dev-frontend`, `build`, `test`, `test-frontend`, `lint`, `migrate`, `docker-up`, `docker-down`

**1.2 Database Models**
- Create EVERY model listed in the PRD database schema section
- Each model MUST have: `id` (UUID primary key), `created_at`, `updated_at`
- Email model must match the EXACT schema from the PRD (gmail_message_id, thread_id, subject, sender_name, sender_email, snippet, body_text, body_html, labels, internal_date, received_at, processed_at, classification, confidence, status, hash)
- All relationships properly defined with SQLAlchemy `relationship()`
- Generate initial Alembic migration
- Verify: `alembic upgrade head` runs without error

**1.3 Configuration**
- `app/config.py` using Pydantic Settings with `.env` loading:
  - `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`
  - `NOTION_API_KEY`, `NOTION_DATABASE_ID`
  - `GOOGLE_CALENDAR_API_KEY`
  - `ENCRYPTION_KEY` (for token encryption)
  - `SYNC_INTERVAL_MINUTES` (default 5)
  - `SYNC_MAX_EMAILS` (configurable limit)
  - `RETRY_ATTEMPTS` (default 6)
  - `RETRY_DELAYS` (default [1, 5, 15, 30, 60, 180])
  - `DATABASE_URL` (default sqlite:///./data/app.db)
  - `CORS_ORIGINS`
  - `LOG_LEVEL`
  - `HOST`, `PORT`

**1.4 Core Utilities**
- `security.py`: AES-GCM encryption/decryption for OAuth refresh tokens, secret masking function
- `logging.py`: Structlog configured with JSON output, severity levels, request ID context
- `exceptions.py`: Custom exceptions: `OAuthError`, `GmailSyncError`, `ClassificationError`, `ActionExecutionError`, `RetryExhaustedError`, with proper HTTP status code mapping
- `utils.py`: Email content hashing (SHA-256 for deduplication), date formatting helpers

**1.5 FastAPI App Shell**
- `main.py` with:
  - Lifespan context manager (startup: init DB, start scheduler; shutdown: stop scheduler)
  - CORS middleware configured
  - All routers mounted at `/api/v1`
  - Global exception handlers mapping custom exceptions to HTTP responses
  - Health check endpoint `GET /health`
  - OpenAPI schema at `/docs`
- Verify: `uvicorn app.main:app --reload` starts without error, `/docs` shows all endpoints (even if not yet implemented)

**1.6 Frontend Shell**
- Configure Tailwind with the design system:
  - Colors: slate for neutrals, blue for primary, green/success, amber/warning, red/error
  - Font: Inter (from Google Fonts)
  - Border radius, spacing, shadow tokens
- `App.tsx` with React Router, TanStack Query provider, theme provider
- `AppLayout.tsx` with responsive sidebar (collapsible on desktop, sheet on mobile)
- Sidebar navigation with icons for: Dashboard, Inbox, Review Queue, Rules, History, Jobs, Logs, Settings
- All page components as placeholder shells that render their page title
- Verify: `npm run dev` starts, sidebar navigation works, all routes render

---

### PHASE 2: AUTHENTICATION (Complete OAuth Flow)

**2.1 Backend OAuth Service**
- `oauth_service.py`:
  - `start_google_oauth()` → generates authorization URL with proper scopes (gmail.readonly, calendar.events, calendar.readonly), state parameter (random, stored in cache/temp DB), redirect URI
  - `handle_callback(code, state)` → exchanges code for tokens, validates state, encrypts refresh token, stores in `oauth_tokens` table, creates/updates user record
  - `refresh_access_token(user_id)` → decrypts refresh token, calls Google token endpoint, updates access token, re-encrypts if rotated
  - `disconnect(user_id)` → deletes tokens, keeps user and processed email history
  - `get_valid_access_token(user_id)` → returns valid access token, refreshing if expired or within 60 seconds of expiry
- Token encryption MUST use AES-256-GCM with the ENCRYPTION_KEY from config

**2.2 Auth API Routes**
- `POST /api/v1/auth/google/start` → returns `{ authorization_url }`
- `GET /api/v1/auth/google/callback` → handles redirect, exchanges code, creates session or returns tokens
- `POST /api/v1/auth/disconnect` → removes tokens
- `GET /api/v1/auth/status` → returns current connection status (connected/disconnected, email address)
- Session management: simple API key or JWT token for frontend→backend auth after OAuth

**2.3 Frontend Auth**
- `LoginPage.tsx`: Clean, centered card with "Connect Gmail" button, Google icon, brief description of what permissions are requested and why (read-only, no sending)
- `GoogleCallback.tsx`: Handles OAuth redirect, calls backend callback, redirects to dashboard
- Auth context/hook that checks connection status on app load
- `OAuthSettings.tsx`: Shows current connection status, connected email, disconnect button with confirmation
- Protected route wrapper that redirects to login if not connected

**2.4 Verify**
- Test: Start backend, navigate to login, click connect, simulate callback (document the manual OAuth flow for real usage)

---

### PHASE 3: GMAIL INTEGRATION

**3.1 Gmail Service**
- `gmail_service.py`:
  - `fetch_emails(access_token, max_results=50, page_token=None, query=None)` → calls Gmail API `users.messages.list`, returns message IDs + snippets
  - `fetch_message(access_token, message_id)` → calls `users.messages.get` with format=full, returns raw message with headers, body, labels
  - `fetch_emails_incremental(access_token, history_id=None, max_results=50)` → uses `users.history.list` for incremental sync
  - `get_profile(access_token)` → returns current history ID for bookmarking
  - ALL calls use httpx async client with proper timeout and error handling
  - Rate limit handling: catch 429, parse `Retry-After` header, sleep accordingly

**3.2 Email Normalizer**
- `email_normalizer.py`:
  - `normalize_raw_message(raw_message, user_id)` → extracts:
    - `gmail_message_id` (from message.id)
    - `thread_id`
    - `subject` (decoded from headers)
    - `sender_name` and `sender_email` (parsed from From header)
    - `snippet`
    - `body_text` (decoded from payload parts, preferring text/plain)
    - `body_html` (from text/html part)
    - `labels` (list of label names)
    - `internal_date` (timestamp from Gmail)
    - `hash` (SHA-256 of message_id + internal_date for deduplication)
  - Handle MIME decoding, charset detection, multipart messages
  - Gracefully handle missing fields (default to empty string/null)

**3.3 Sync Task**
- `sync_task.py`:
  - `run_sync(user_id)`:
    1. Get valid access token
    2. Get last sync history_id from settings
    3. If history_id exists, do incremental sync; else full sync of recent emails
    4. For each message ID: fetch full message, normalize, check hash for deduplication, upsert into emails table
    5. Update last sync history_id in settings
    6. Create job record with status, timing, counts
    7. Log each step with structlog
    8. Handle errors per-message (skip and log, don't abort entire sync)
    9. Return summary: fetched, new, duplicates, errors

**3.4 Sync API**
- `POST /api/v1/sync/start` → triggers async sync job, returns job ID
- `GET /api/v1/sync/status` → returns current/last sync status

**3.5 Frontend Inbox**
- `InboxPage.tsx` with:
  - Search bar (searches subject, sender, snippet)
  - Filter dropdowns: classification, status, date range, label
  - Sort: date (newest/oldest), sender, subject
  - `EmailList.tsx`: Virtualized or paginated list of emails
  - `EmailRow.tsx`: Shows sender avatar (initials), sender name, subject, snippet (truncated), classification badge, received time, read/unread indicator
  - `EmailDetail.tsx`: Slide-out panel showing full email: headers, body (HTML rendered safely), classification info, associated actions/tasks, raw labels
  - `BulkActions.tsx`: Select multiple → archive, mark read, star, add label, classify manually
  - Manual "Sync Now" button in header with loading spinner and progress indication
  - Empty state when no emails synced yet
  - Loading skeleton states

**3.6 Verify**
- Write unit tests for normalizer with sample Gmail API responses
- Write unit tests for deduplication logic
- Test sync API endpoint with mocked Gmail service

---

### PHASE 4: CLASSIFICATION & RULES

**4.1 Classification Engine**
- `classification_engine.py`:
  - Categories enum: `IGNORE`, `NEWSLETTER`, `RECEIPT`, `PROMOTION`, `MEETING`, `NEEDS_REPLY`, `FOLLOW_UP`, `CALENDAR_EVENT`, `TASK`, `IMPORTANT`, `UNKNOWN`, `SPAM_CANDIDATE`
  - `classify_email(email: Email, rules: list[Rule]) -> Classification`:
    1. Check manual rules (highest priority) — exact match
    2. Check learned rules — pattern match
    3. Apply heuristic classification:
       - NEWSLETTER: list-unsubscribe header present, sender in known newsletter domains, "unsubscribe" in body
       - RECEIPT: sender contains (stripe, paypal, amazon, shopify, invoice, receipt, order confirmation), subject patterns
       - PROMOTION: marketing language, discount codes, "sale", "offer", "deal"
       - MEETING: calendar invite attachment, "meeting", "call", "zoom", "meet.google.com" in body
       - NEEDS_REPLY: question marks in body, direct address ("you"), "please", "respond", "reply", no list-unsubscribe
       - FOLLOW_UP: "following up", "checking in", "just wanted to", "reminder"
       - CALENDAR_EVENT: date/time patterns + action verbs, "schedule", "appointment"
       - TASK: imperative verbs, "please", "need you to", "action item", deadline mentions
       - IMPORTANT: sender in user's important contacts, high-priority patterns
       - SPAM_CANDIDATE: excessive caps, suspicious links, common spam patterns
       - IGNORE: auto-generated, no-reply, notifications with no action needed
    4. Fall back to UNKNOWN
    5. Calculate confidence score (0-100) based on match strength
    6. Record reason string explaining classification
  - Store result in `classifications` table

**4.2 Rule Engine**
- `rule_engine.py`:
  - `Rule` model fields: name, enabled, priority (1=highest), conditions (JSON), action (category to assign), created_by (manual/learned)
  - Condition types: `sender_contains`, `sender_equals`, `subject_contains`, `subject_matches_regex`, `body_contains`, `has_attachment`, `label_is`, `from_domain`
  - Multiple conditions combined with AND/OR logic
  - `evaluate_rule(email: Email, rule: Rule) -> bool`
  - `evaluate_rules(email: Email, rules: list[Rule]) -> Optional[RuleResult]`: evaluate in priority order, return first match
  - `learn_rule(email: Email, user_correction: str)`: when user manually changes classification, suggest creating a rule from the pattern

**4.3 Review Queue Logic**
- After classification:
  - If confidence >= 90 AND category is low-risk (IGNORE, NEWSLETTER, RECEIPT, PROMOTION) → auto-execute applicable actions
  - If confidence >= 90 AND category is high-risk (NEEDS_REPLY, TASK, CALENDAR_EVENT, IMPORTANT) → enter review queue
  - If confidence < 90 → enter review queue regardless of category
  - If category is UNKNOWN → enter review queue
- `review_service.py`: CRUD for review queue items, status transitions (PENDING → APPROVED/REJECTED/EDITED/EXPIRED)

**4.4 Rules API**
- Full CRUD: `GET /api/v1/rules`, `POST /api/v1/rules`, `PUT /api/v1/rules/{id}`, `DELETE /api/v1/rules/{id}`, `PATCH /api/v1/rules/{id}/toggle`
- `POST /api/v1/rules/reorder` → update priority ordering
- `POST /api/v1/rules/test` → test a rule against recent emails without saving

**4.5 Frontend Rules**
- `RulesPage.tsx` with:
  - `RuleList.tsx`: Table of rules with name, conditions (human-readable), action/category, priority, enabled toggle, edit/delete buttons
  - `RuleEditor.tsx`:
    - Name input
    - Dynamic condition builder: add/remove conditions, select type, enter value
    - AND/OR toggle between conditions
    - Category selector dropdown
    - Priority input
    - Save/Cancel buttons
  - `RulePrioritySelector.tsx`: Drag-and-drop or up/down buttons for reordering
  - "Test Rule" button that shows which recent emails would match
  - Empty state: "No rules yet. Create your first rule to automate email classification."

**4.6 Frontend Review Queue**
- `ReviewPage.tsx` with:
  - Summary bar: total pending, by category breakdown
  - `ConfidenceFilter.tsx`: slider or buttons to filter by confidence range
  - `ReviewCard.tsx` for each item:
    - Email preview (sender, subject, snippet)
    - Suggested classification with confidence bar and reason
    - Suggested action(s)
    - Approve (green), Reject (red), Edit (blue) buttons
    - Edit opens inline form to change classification/action
  - `ReviewBulkActions.tsx`: Select multiple → approve all, reject all
  - Auto-refresh when new items enter queue (WebSocket or polling)

**4.7 Verify**
- Unit tests for every classification heuristic with sample emails
- Unit tests for rule evaluation with various condition combinations
- Unit tests for review queue entry logic (confidence thresholds)
- Integration test: classify a batch of emails, verify correct queue placement

---

### PHASE 5: ACTION EXECUTION & INTEGRATIONS

**5.1 Action Executor**
- `action_executor.py`:
  - `execute_action(review_item: ReviewQueue, action_type: str, params: dict)`:
    - Dispatches to appropriate service based on action type
    - Wraps in try/except, returns success/failure
    - On failure: creates retry queue entry
    - On success: logs to audit trail, updates review item status
  - Action types: `CREATE_NOTION_TASK`, `CREATE_CALENDAR_EVENT`, `ADD_GMAIL_LABEL`, `MARK_READ`, `ARCHIVE`, `STAR`, `SET_REMINDER`

**5.2 Notion Service**
- `notion_service.py`:
  - `test_connection(api_key)` → calls Notion API to verify key and get user info
  - `list_databases(api_key)` → returns available databases for user to select
  - `get_database_schema(api_key, database_id)` → returns properties of selected database
  - `create_task(api_key, database_id, task_data: TaskCreateSchema)` → creates a page in the database with:
    - Title (from email subject)
    - Description (from email snippet/body, truncated)
    - Due date (extracted from email if present)
    - Priority (inferred from classification)
    - Email link (Gmail web URL)
    - Sender (email address)
    - Labels (from classification)
  - Maps PRD task fields to Notion properties dynamically based on database schema
  - Proper error handling for rate limits, invalid database, missing properties

**5.3 Calendar Service**
- `calendar_service.py`:
  - `create_event(access_token, event_data: CalendarEventCreateSchema)`:
    - Title (from email subject or extracted event name)
    - Description (email snippet + link to original email)
    - Date and time (extracted from email body using date patterns)
    - Duration (default 30 min if not specified, or inferred from context)
    - Reminder (default 15 min before)
    - Returns created event ID and link
  - `extract_datetime_from_email(body_text: str) -> Optional[datetime]`:
    - Pattern matching for common date formats
    - Relative date parsing ("tomorrow", "next monday", "in 2 hours")
    - Time zone handling (default to user's local timezone)

**5.4 Gmail Action Service**
- Part of `gmail_service.py` or separate `gmail_action_service.py`:
  - `add_label(access_token, message_id, label_name)` → create label if needed, apply to message
  - `mark_read(access_token, message_id)`
  - `archive(access_token, message_id)` → remove INBOX label
  - `star(access_token, message_id)` → add STAR label

**5.5 Action Task**
- `action_task.py`:
  - `execute_approved_actions()`:
    1. Query review queue for APPROVED items not yet executed
    2. For each: call action executor
    3. On success: mark as COMPLETED, create audit log
    4. On failure: create retry queue entry with error details
    5. Handle idempotency: check if action was already performed (e.g., Notion task already exists for this email)

**5.6 Retry Service**
- `retry_service.py`:
  - `process_retry_queue()`:
    1. Query retry queue for items where `next_retry_at <= now` and `attempts < max_attempts`
    2. For each: attempt the action again
    3. On success: mark as completed, remove from retry queue
    4. On failure: increment attempt count, calculate next retry time using exponential backoff from RETRY_DELAYS config
    5. If attempts exhausted: mark as FAILED, log final error
  - Ensure idempotency: before retrying, check if action was actually completed despite the error (e.g., network timeout but Notion task was created)

**5.7 Review API**
- `GET /api/v1/review` → list review queue items with filters (status, category, confidence range, pagination)
- `POST /api/v1/review/{id}/approve` → set status to APPROVED, trigger action execution
- `POST /api/v1/review/{id}/reject` → set status to REJECTED, log reason
- `POST /api/v1/review/{id}/edit` → update classification/action, re-approve

**5.8 Frontend Integration Settings**
- `IntegrationSettings.tsx`:
  - Notion section: API key input (masked), "Test Connection" button, database selector dropdown (populated after connection), database schema preview
  - Calendar section: shows "Connected via Gmail OAuth" status, no additional config needed
  - Status indicators: green dot + "Connected" or red dot + "Not configured"

**5.9 Verify**
- Unit tests for Notion service with mocked API responses
- Unit tests for Calendar service with mocked API responses
- Unit tests for retry logic with various failure scenarios
- Integration test: approve a review item → verify Notion task created
- Idempotency test: approve same item twice → verify only one task created

---

### PHASE 6: SCHEDULER, JOBS & LOGGING

**6.1 Scheduler Service**
- `scheduler_service.py`:
  - Uses APScheduler with AsyncIOScheduler
  - Jobs:
    - `email_sync_job`: runs every X minutes (configurable), calls `run_sync()` for each connected user
    - `classification_job`: runs after sync, classifies newly fetched unclassified emails
    - `action_execution_job`: runs every minute, processes approved review items
    - `retry_job`: runs every minute, processes retry queue
  - Job states tracked in `jobs` table: IDLE, RUNNING, RETRYING, FAILED, PAUSED, COMPLETED
  - Each job execution creates a `job_log` entry with start/end time, status, items processed, errors
  - Pause/resume/cancel capabilities
  - Configurable via Settings API

**6.2 Jobs API**
- `GET /api/v1/jobs` → list all jobs with filters (type, status, date range), pagination
- `GET /api/v1/jobs/{id}` → job detail with associated logs
- `POST /api/v1/jobs/{id}/retry` → retry a failed job
- `POST /api/v1/jobs/{id}/cancel` → cancel a running job

**6.3 Logging System**
- Structlog configured with:
  - JSON output format
  - Timestamps in ISO 8601
  - Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - Context binding: request_id, user_id, job_id, email_id
  - Console output for development
  - File output for persistence (rotating files)
- Every service function logs entry, exit, errors, and key decisions
- Log format example:
  ```json
  {
    "timestamp": "2025-01-15T10:30:00.000Z",
    "level": "info",
    "event": "email_classified",
    "email_id": "uuid",
    "classification": "RECEIPT",
    "confidence": 96,
    "reason": "Sender matched billing domain",
    "duration_ms": 12
  }
  ```

**6.4 Audit Trail**
- `audit_logs` table records every state transition:
  - `entity_type` (email, review_item, task, job, etc.)
  - `entity_id`
  - `old_status`
  - `new_status`
  - `actor` (system, user, scheduler)
  - `reason`
  - `metadata` (JSON blob with additional context)
- Every status change in the system MUST create an audit log entry
- Immutable: no updates or deletes on audit_logs

**6.5 Logs API**
- `GET /api/v1/logs` → structured logs with filters (level, source, date range, entity_id), pagination, search
- `GET /api/v1/audit` → audit trail with filters (entity_type, entity_id, actor, date range), pagination
- `GET /api/v1/logs/export` → download logs as JSON or CSV

**6.6 Frontend Jobs Page**
- `JobsPage.tsx`:
  - `JobList.tsx`: Table of jobs with type, status badge, start time, duration, items processed, error count
  - `JobDetail.tsx`: Expanded view with step-by-step log entries, error details, retry button
  - `JobStatusBadge.tsx`: Color-coded badges (RUNNING=blue animated, COMPLETED=green, FAILED=red, PAUSED=yellow)
  - Filter by job type and status
  - Auto-refresh for running jobs (polling every 5 seconds)

**6.7 Frontend Logs Page**
- `LogsPage.tsx`:
  - `LogViewer.tsx`: Virtualized log display with:
    - Color-coded severity levels
    - Collapsible JSON metadata
    - Search/filter bar (text search, level filter, date range)
    - Auto-scroll toggle
    - Export button
  - `AuditTrail.tsx`: Table view of state transitions with old→new status, actor, timestamp, reason

**6.8 Frontend Settings — Scheduler & Retry**
- `SchedulerSettings.tsx`:
  - Sync interval input (minutes, with presets: 1, 5, 15, 30, 60)
  - Max emails per sync
  - Enable/disable individual job types
  - Pause all jobs button
- `RetrySettings.tsx`:
  - Max retry attempts
  - Retry delays (editable list)
  - Current retry queue size and status

**6.9 Verify**
- Unit test scheduler job registration and execution
- Unit test audit log creation for every state transition
- Integration test: trigger sync → verify job created → verify logs written → verify audit trail
- Test retry: simulate failure → verify retry queued → verify exponential backoff timing

---

### PHASE 7: DASHBOARD, HISTORY & NOTIFICATIONS

**7.1 Dashboard API**
- `GET /api/v1/dashboard/stats` → returns:
  - `unread_today`: count of emails received today
  - `tasks_created_today`: count
  - `events_created_today`: count
  - `pending_approvals`: count of PENDING review items
  - `failed_jobs`: count of FAILED jobs in last 24h
  - `avg_processing_time_ms`: average classification + action time
  - `total_emails_processed`: all time
  - `classification_breakdown`: { category: count }
- `GET /api/v1/dashboard/activity` → recent activity feed (last 50 items across all entities)

**7.2 Frontend Dashboard**
- `DashboardPage.tsx`:
  - `StatsCards.tsx`: Grid of stat cards with icon, label, value, trend indicator (up/down arrow with percentage change vs yesterday)
  - `ActivityFeed.tsx`: Timeline of recent events (email classified, task created, job completed, etc.) with timestamps and icons
  - `ProcessingChart.tsx`: Line/bar chart showing processing volume over time (last 7 days by default, adjustable)
  - `QuickActions.tsx`: "Sync Now", "Review Queue (N pending)", "View Failed Jobs" buttons
  - Responsive grid layout: stats cards 2x3 on desktop, stacked on mobile

**7.3 History**
- `GET /api/v1/history` → paginated list of all processed emails with classification, status, timestamps
- `GET /api/v1/history/{email_id}` → full email detail with complete processing history (every state transition from this email)
- `POST /api/v1/history/{email_id}/replay` → re-process an email through classification and review (useful after adding new rules)

**7.4 Frontend History**
- `HistoryPage.tsx`:
  - `HistoryTimeline.tsx`: Visual timeline showing email processing flow for selected email
  - `HistoryDetail.tsx`: Full email content + processing history table
  - Search, filter by classification, status, date range
  - "Reprocess" button per email

**7.5 Notifications**
- `notification_service.py`:
  - Desktop notification support using `desktop-notifier` Python package or via WebSocket push to frontend
  - Notification types: NEW_IMPORTANT_EMAIL, TASK_CREATED, EVENT_CREATED, SYNC_FAILED, OAUTH_EXPIRING
  - User-configurable in settings (which notifications to enable)
- Frontend: Browser Notification API integration, permission request on first use, notification preferences in settings

**7.6 Verify**
- Dashboard API returns correct aggregate data
- Charts render with sample data
- History replay correctly re-classifies an email

---

### PHASE 8: POLISH, TESTING & DOCKER

**8.1 Frontend Polish (UI/UX Pro Max Skill — FULL APPLICATION)**
- Apply EVERY UI/UX principle:
  - Consistent 4px spacing grid across ALL components
  - Proper loading skeletons for every data-dependent view
  - Empty states for every list/table: illustration, message, CTA button
  - Error states: error boundary at page level, error messages with retry buttons
  - Smooth page transitions
  - Toast notifications for every mutation action (approved, rejected, created, deleted, etc.)
  - Form validation with inline error messages (no alert boxes)
  - Responsive design: test at 320px, 768px, 1024px, 1440px widths
  - Keyboard shortcuts: ` Cmd+K` for command palette, `Esc` to close modals
  - Command palette (using cmdk): search pages, actions, emails
  - Proper focus management: when modal opens, focus traps inside; when modal closes, focus returns to trigger
  - Dark theme: complete dark mode with proper contrast ratios
  - Table rows: hover state, selected state, zebra striping option
  - Pagination: show page numbers, items per page selector, total count
  - Breadcrumbs where appropriate (Settings > OAuth)
  - Tooltips on icon-only buttons
  - Confirmation dialogs for destructive actions (disconnect, delete rule, clear logs)

**8.2 Backend Unit Tests — 80% Coverage Target**
- `test_oauth_service.py`: token encryption/decryption, flow steps, error cases
- `test_gmail_service.py`: fetch with pagination, incremental sync, rate limit handling, error handling
- `test_email_normalizer.py`: various email formats, multipart, missing fields, encoding issues
- `test_classification_engine.py`: every category with multiple examples, confidence scoring, edge cases
- `test_rule_engine.py`: every condition type, AND/OR logic, priority ordering, regex matching
- `test_review_service.py`: queue entry logic, status transitions, expiration
- `test_action_executor.py`: dispatch to correct service, error handling, idempotency
- `test_retry_service.py`: backoff timing, attempt counting, exhaustion, success recovery
- `test_scheduler_service.py`: job registration, execution, pause/resume

**8.3 Backend Integration Tests**
- `test_api_auth.py`: full OAuth flow with mocked Google endpoints
- `test_api_emails.py`: sync trigger, email listing, search, pagination
- `test_api_review.py`: approve/reject/edit flow, bulk actions
- `test_api_rules.py`: CRUD, test, reorder
- `test_api_jobs.py`: job listing, retry, cancel

**8.4 Docker**
- `Dockerfile.backend`:
  - Python 3.12 slim base
  - Install system deps (build tools for cryptography)
  - Copy pyproject.toml, install deps
  - Copy app code
  - Create data directory for SQLite
  - Expose port 8000
  - CMD: uvicorn with workers
- `Dockerfile.frontend`:
  - Node 20 alpine base
  - Multi-stage: build → nginx serve
  - Proper nginx config for SPA routing
  - Expose port 3000
- `docker-compose.yml`:
  - backend service
  - frontend service
  - Volume for backend data persistence
  - Environment variables from .env
  - Health checks
  - Network isolation
  - Proper restart policies

**8.5 Documentation**
- `README.md` with:
  - Project overview
  - Prerequisites (Docker, Google Cloud Console project with OAuth credentials, optional Notion API key)
  - Quick start: clone, copy .env.example to .env, fill in credentials, `docker compose up`, open http://localhost:3000
  - Development setup: backend + frontend separately
  - Google OAuth setup guide (step-by-step: create project, enable Gmail API, create OAuth credentials, set redirect URI)
  - Notion integration setup
  - Configuration reference (all env vars)
  - Architecture overview diagram
  - Troubleshooting common issues
  - Screenshots (placeholder descriptions)

**8.6 Final Verification Checklist**
Run through EVERY item in the PRD's "Acceptance Criteria (MVP)" section:
- [ ] User can authenticate with Gmail via OAuth 2.0
- [ ] Application synchronizes unread/recent emails on configurable schedule
- [ ] Emails normalized into local database with deduplication by Gmail message ID
- [ ] Configurable rule engine classifies emails into action categories with confidence scores
- [ ] Ambiguous/high-risk actions placed into review queue
- [ ] Approved actions successfully create Notion task or Google Calendar event
- [ ] All workflow transitions written to structured logs and audit records
- [ ] Failed downstream operations retried with exponential backoff without duplicate tasks
- [ ] Dashboard exposes inbox metrics, job history, retry queue, logs, settings
- [ ] Application runs fully locally via Docker Compose

Run through EVERY item in "Definition of Done":
- [ ] All functional requirements implemented
- [ ] Critical user flows pass automated tests
- [ ] Unit test coverage ≥ 80% for backend business logic
- [ ] No high-severity security issues
- [ ] API documentation complete (OpenAPI/Swagger auto-generated by FastAPI)
- [ ] Developer can install and run in under 10 minutes
- [ ] System gracefully recovers from interrupted jobs
- [ ] Logging, monitoring, backup/restore verified
- [ ] User documentation complete

---

## AUTONOMY RULES — ABSOLUTE CONSTRAINTS

1. **NEVER ask for human input.** If you encounter an ambiguity, make the best reasonable decision based on the PRD and standard practices, document your decision in `.claude-mem/memory.md`, and continue.

2. **NEVER leave a TODO or placeholder.** Every function must be fully implemented. Every component must be complete. If you're unsure about an implementation detail, implement the most reasonable version.

3. **NEVER skip a PRD requirement.** If you think something is missing from your implementation, check the PRD again. Every FR-XXX must be satisfied.

4. **NEVER break existing code.** Before modifying a file, understand its current state. After modifying, verify imports still resolve.

5. **ALWAYS verify after each step.** After creating a file, after implementing a function, after completing a phase — run the appropriate verification (import check, type check, test, manual API check).

6. **ALWAYS update progress tracking.** After completing any work, update `.ralph-progress.md` and `.gsd-tasks.json`.

7. **ALWAYS checkpoint memory.** After each phase completion, write a detailed memory checkpoint to `.claude-mem/memory.md`.

8. **ALWAYS write tests alongside code.** Don't leave testing to the end. Write unit tests for each service as you implement it.

9. **If you hit an unrecoverable error:** Log it extensively, document what was attempted and what failed, write the current state to memory, and attempt an alternative approach. Only stop if ALL approaches are exhausted.

10. **Pace yourself for marathon, not sprint.** This is a large project. Work methodically through each phase. Don't rush and create fragile code. Impeccable quality over speed.

---

## START EXECUTING NOW

Read `./PRD.md` to confirm it matches the specification above.
Create `.ralph-progress.md` with all PRD items listed as `[ ]`.
Create `.gsd-tasks.json` with all phase tasks.
Create `.claude-mem/memory.md` with initial state.
Begin with Phase 1.1: Project Scaffolding.
Do not stop until every item in `.ralph-progress.md` is `[x]`.

GO.