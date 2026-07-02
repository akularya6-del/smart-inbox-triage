**Product Requirements Document (PRD)**
=======================================

**Smart Inbox Triage Dashboard**
--------------------------------

### **Version 1.0 (Implementation Specification)**

### **Audience**

*   Human Software Engineer
    
*   AI Coding Agent (Google Antigravity)
    
*   Designers
    
*   QA Engineers
    

**Executive Summary**
=====================

**Product Name**
----------------

**Smart Inbox Triage Dashboard**

**One-line Description**
------------------------

A local-first productivity dashboard that connects securely to Gmail, intelligently classifies emails into actionable categories, proposes tasks/events, requires human approval for important actions, and maintains a complete audit trail.

**Vision**
==========

Email has become an overloaded task manager.

People spend hours every week:

*   deleting newsletters
    
*   finding receipts
    
*   replying late
    
*   forgetting bills
    
*   missing deadlines
    
*   manually creating calendar reminders
    
*   manually copying emails into Notion
    

The Smart Inbox Dashboard becomes an intelligent email operations center that performs the repetitive work while always keeping the human in control.

The product is **NOT** an AI email assistant.

It is an **automation platform with human approval**.

Safety is more important than automation.

**Product Goals**
=================

Primary goals:

*   Reduce time spent organizing email
    
*   Never lose important messages
    
*   Reduce manual task creation
    
*   Require approval before risky actions
    
*   Maintain complete transparency
    
*   Work locally
    
*   Own your data
    

Secondary goals:

*   Learn user preferences over time
    
*   Become extensible
    
*   Support additional integrations
    
*   Be deployable by anyone
    

**Non Goals**
=============

The application will NOT:

*   Send emails automatically
    
*   Delete emails permanently
    
*   Auto-reply
    
*   Train cloud AI models on user email
    
*   Upload mailbox contents to external servers
    
*   Replace Gmail
    

**Success Metrics**
===================

User should:

Reduce inbox processing time by 60%

Miss fewer important emails

Approve >90% of suggested actions

Spend under 10 minutes/day reviewing queue

Average dashboard load:

<500ms

Email sync:

<5 seconds

Task creation:

<3 seconds

**User Personas**
=================

**Persona 1 — Student**
-----------------------

Needs:

Assignment reminders

Professor emails

Internship applications

Scholarships

University announcements

Pain points:

Misses deadlines

Loses emails

Inbox clutter

**Persona 2 — Professional**
----------------------------

Needs:

Meeting reminders

Invoices

Client emails

Project discussions

Action tracking

Pain points:

Manual task creation

Email overload

Missed follow-ups

**Persona 3 — Freelancer**
--------------------------

Needs:

Invoices

Payments

Contracts

Client communication

Pain points:

Forgotten invoices

Late replies

Scattered workflow

**Product Principles**
======================

**Local First**
---------------

Everything runs locally.

Email content remains local.

Database remains local.

Logs remain local.

**Human in Control**
--------------------

High-risk actions require approval.

Automation should never surprise users.

**Transparent**
---------------

Every decision is explainable.

Every action is logged.

Nothing hidden.

**Recoverable**
---------------

Every failure can be retried.

Every operation is idempotent.

Nothing disappears.

**Functional Requirements**
===========================

**User Authentication**
=======================

**FR-001**
----------

User can connect Gmail.

Acceptance Criteria

*   OAuth login
    
*   Refresh token stored securely
    
*   Access token refreshed automatically
    
*   Reconnect flow
    

**FR-002**
----------

User can disconnect Gmail.

Acceptance

*   Remove tokens
    
*   Remove cached credentials
    
*   Keep local processed history
    

**Email Synchronization**
=========================

**FR-003**
----------

Scheduler fetches emails every X minutes.

Configurable.

Default:

5 minutes

**FR-004**
----------

Manual Sync button

Acceptance

User clicks Sync

Immediately starts job

Progress displayed

**FR-005**
----------

Incremental sync

Only fetch:

Unread

or

Last N hours

or

History ID changes

**FR-006**
----------

Pagination

Continue until:

No next page

OR

Configured limit reached

**Email Storage**
=================

Every email normalized.

Schema:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Email  id  gmail_message_id  thread_id  subject  sender_name  sender_email  snippet  body_text  body_html  labels  internal_date  received_at  processed_at  classification  confidence  status  hash  created_at  updated_at   `

**Classification Engine**
=========================

Categories

Ignore

Newsletter

Receipt

Promotion

Meeting

Needs Reply

Follow Up

Calendar Event

Task

Important

Unknown

Spam Candidate

Each email receives

Category

Confidence

Reason

Rule matched

Example

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Invoice from Stripe  ↓  Receipt  Confidence 96%  Reason:  Sender matched billing domain   `

**Rule Engine**
===============

User can create rules.

Example:

IF sender contains amazon.com

THEN

Receipt

IF subject contains invoice

THEN

Receipt

IF sender = professor

THEN

Important

Rule priority:

1 Manual Rule

2 Learned Rule

3 AI Suggestion

4 Default

**Review Queue**
================

Every uncertain action enters queue.

Status

Pending

Approved

Rejected

Edited

Expired

User sees

Email

Suggested action

Confidence

Reason

Buttons

Approve

Reject

Modify

**Actions**
===========

Supported actions

Create Notion Task

Create Calendar Event

Add Gmail Label

Mark Read

Archive

Star

Reminder

Future

Slack

Discord

Todoist

Linear

Jira

**Notion Integration**
======================

User chooses database.

Task fields

Title

Description

Due date

Priority

Email link

Sender

Labels

**Google Calendar**
===================

Event

Title

Description

Date

Time

Duration

Reminder

Email reference

**Scheduler**
=============

Runs

Every 5 minutes

Configurable

Cron supported

States

Idle

Running

Retrying

Failed

Paused

Completed

**Retry Queue**
===============

Failures enter queue.

Retries

1 minute

5

15

30

60

180

Maximum attempts configurable.

**Logging**
===========

Every action logged.

Example

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Email fetched  ↓  Normalized  ↓  Classified  ↓  Review Queue  ↓  Approved  ↓  Task Created  ↓  Completed   `

**Audit Trail**
===============

Every state transition recorded.

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   EmailID  Old Status  New Status  Timestamp  Actor  Reason   `

**Notifications**
=================

Optional desktop notifications

Examples

New Important Email

Task Created

Sync Failed

OAuth Expiring

**Dashboard**
=============

Pages

Dashboard

Inbox

Review Queue

Rules

History

Jobs

Logs

Settings

**Dashboard Details**
=====================

**Dashboard**
-------------

Widgets

Unread today

Tasks created

Events created

Pending approvals

Failed jobs

Processing time

Recent activity

**Inbox**
---------

Search

Filter

Sort

Bulk actions

Preview

**Review Queue**
----------------

Approve

Reject

Edit

Bulk approve

Confidence filter

**Rules**
---------

Create

Edit

Delete

Enable

Disable

Priority ordering

**History**
-----------

Every processed email

Timeline

Search

Replay

**Jobs**
--------

Running jobs

Completed jobs

Retry jobs

Cancel

Restart

**Logs**
--------

Structured JSON logs

Severity

Search

Export

**Settings**
------------

OAuth

Scheduler

Retry policy

Database

API keys

Theme

Backup

**System Architecture**
=======================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML                `React Dashboard                         │            REST API / WebSocket                         │        FastAPI Backend (Python)                         │  ────────────────────────────────────  │ OAuth Manager                    │  │ Gmail Sync Engine                │  │ Classification Engine            │  │ Rule Engine                      │  │ Review Queue                     │  │ Action Executor                  │  │ Retry Queue                      │  │ Scheduler                         │  │ Logger                           │  ────────────────────────────────────             │             │          SQLite       File Storage             │     Gmail API / Notion API / Calendar API`

**Technology Stack**
====================

Frontend

React

TypeScript

Vite

TailwindCSS

ShadCN

TanStack Query

React Router

Backend

Python

FastAPI

SQLAlchemy

Pydantic

APScheduler

httpx

Database

SQLite (default)

Postgres optional

Auth

OAuth 2

Google OAuth

Background Jobs

APScheduler

Future:

Celery

Logging

Structlog

JSON logs

Testing

Pytest

React Testing Library

Playwright

Deployment

Docker

Docker Compose

Local executable

**Database Schema**
===================

Tables

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   users  oauth_tokens  emails  email_labels  rules  classifications  review_queue  tasks  calendar_events  jobs  job_logs  retry_queue  audit_logs  settings   `

Every table includes

UUID

CreatedAt

UpdatedAt

**State Machine**
=================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Fetched  ↓  Normalized  ↓  Classified  ↓  Needs Review?  ↓  Yes ---------------- No  ↓                     ↓  Pending Review      Execute Action  ↓  Approved?  ↓  Yes ---- No  ↓  Execute  ↓  Success?  ↓  Yes  Completed  ↓  No  Retry Queue  ↓  Failed   `

**Error Handling**
==================

OAuth expired

Refresh

Reconnect if needed

API unavailable

Retry

Duplicate email

Ignore

Duplicate task

Skip

Rate limit

Exponential backoff

Database failure

Rollback transaction

**Security**
============

Encrypt refresh tokens

Never log email bodies

Mask secrets

HTTPS localhost callback

CSRF protection

Validate OAuth state

Input validation

SQL injection protection

XSS protection

**Performance Targets**
=======================

Dashboard

<500ms

Sync

<5s

Classification

<100ms/email

Search

<300ms

Memory

<300MB

**Future AI Features**
======================

Local LLM

Suggested replies

Automatic rule generation

Semantic search

Receipt OCR

Attachment summarization

Daily digest generation

Learning approval patterns

Priority prediction

**Milestones**
==============

**Phase 1**
-----------

Project setup

Database

Authentication

Dashboard shell

**Phase 2**
-----------

Gmail integration

Pagination

Incremental sync

Normalization

**Phase 3**
-----------

Rule engine

Classification

Review queue

**Phase 4**
-----------

Notion

Calendar

Action execution

Retry queue

**Phase 5**
-----------

Logging

Audit

Scheduler

Settings

**Phase 6**
-----------

Testing

Docker

Documentation

Performance optimization

**Testing Strategy**
====================

**Unit Tests**
--------------

*   OAuth manager
    
*   Rule engine
    
*   Classification logic
    
*   Retry logic
    
*   State transitions
    

**Integration Tests**
---------------------

*   Gmail OAuth flow
    
*   Gmail sync with pagination
    
*   Notion task creation
    
*   Calendar event creation
    
*   Database persistence
    

**End-to-End Tests**
--------------------

*   First-time user setup
    
*   Manual sync
    
*   Review and approve workflow
    
*   Retry after downstream failure
    
*   Reconnect after token expiration
    

**Failure Simulation**
----------------------

*   Network timeout during Gmail fetch
    
*   Notion API unavailable
    
*   Calendar API rate limiting
    
*   Database locked during write
    
*   Power interruption during job execution (verify recovery on restart)
    

**API Design (Internal Backend)**
=================================

**Authentication**
------------------

*   POST /auth/google/start
    
*   GET /auth/google/callback
    
*   POST /auth/disconnect
    

**Email**
---------

*   POST /sync/start
    
*   GET /emails
    
*   GET /emails/{id}
    
*   GET /emails/search
    

**Review Queue**
----------------

*   GET /review
    
*   POST /review/{id}/approve
    
*   POST /review/{id}/reject
    
*   POST /review/{id}/edit
    

**Rules**
---------

*   GET /rules
    
*   POST /rules
    
*   PUT /rules/{id}
    
*   DELETE /rules/{id}
    

**Jobs**
--------

*   GET /jobs
    
*   POST /jobs/{id}/retry
    
*   POST /jobs/{id}/cancel
    

**Logs**
--------

*   GET /logs
    
*   GET /audit
    

**Settings**
------------

*   GET /settings
    
*   PUT /settings
    

**Acceptance Criteria (MVP)**
=============================

The MVP is considered complete when:

*   A user can authenticate with Gmail via OAuth 2.0.
    
*   The application synchronizes unread or recent emails on a configurable schedule.
    
*   Emails are normalized into the local database with deduplication by Gmail message ID.
    
*   A configurable rule engine classifies emails into action categories with confidence scores.
    
*   Ambiguous or high-risk actions are placed into a review queue.
    
*   Approved actions successfully create a Notion task or Google Calendar event.
    
*   All workflow transitions are written to structured logs and audit records.
    
*   Failed downstream operations are retried using exponential backoff without creating duplicate tasks.
    
*   The dashboard exposes inbox metrics, job history, retry queue, logs, and settings.
    
*   The application runs fully on the user’s machine using Docker Compose or a local development environment.
    

**Definition of Done**
======================

A release is considered production-ready when:

*   All functional requirements are implemented.
    
*   Critical user flows pass automated end-to-end tests.
    
*   Unit test coverage is at least 80% for backend business logic.
    
*   No high-severity security issues remain open.
    
*   API documentation is complete (OpenAPI/Swagger).
    
*   A developer can install and run the project in under 10 minutes using the provided documentation.
    
*   The system gracefully recovers from interrupted jobs and partial failures.
    
*   Logging, monitoring, and backup/restore procedures have been verified.
    
*   User documentation includes setup, OAuth configuration, rule creation, troubleshooting, and deployment instructions.
    

This PRD is intentionally implementation-oriented so it can serve as both a product specification for human developers and a detailed execution blueprint for an AI coding agent such as Google Antigravity.