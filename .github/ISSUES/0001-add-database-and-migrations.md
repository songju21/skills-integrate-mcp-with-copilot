---
title: Add database persistence and migrations
labels: enhancement, backend
---

Currently activities are stored in-memory. Persist activities, users, and signups
to a database (e.g., PostgreSQL) and add Alembic/FastAPI migrations or equivalent
so data survives restarts. Include seed data and instructions.

Suggested tasks:
- Add SQLAlchemy models for `User`, `Activity`, `Signup`, `Role`
- Add migration scripts and a `migrations` workflow
- Provide seed data and `docker-compose` for local DB
