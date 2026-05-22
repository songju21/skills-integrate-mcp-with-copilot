#!/usr/bin/env bash
# Create GitHub issues from files in .github/ISSUES using gh CLI.
# Requires: gh CLI installed and authenticated with repo access.

set -euo pipefail
REPO="songju21/skills-integrate-mcp-with-copilot"
ISSUES_DIR=".github/ISSUES"

for f in "$ISSUES_DIR"/*.md; do
  title=$(sed -n '2p' "$f" | sed 's/^title: //')
  gh issue create --repo "$REPO" --title "$title" --body-file "$f" --label "auto-created"
done

echo "All issues created (or attempted)."
