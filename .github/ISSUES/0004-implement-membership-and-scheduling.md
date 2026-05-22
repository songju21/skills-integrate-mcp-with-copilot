---
title: Implement membership/subscription lifecycle and scheduled jobs
labels: enhancement, backend
---

Add membership plans, subscription state (active/expired), and background jobs
to check expirations and notify users.

Suggested tasks:
- Add membership model and subscription endpoints
- Add background scheduler (cron, APScheduler, or Celery beat) for periodic
  tasks
- Add email notifications for renewals/expirations
