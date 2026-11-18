#!/bin/bash
# Run this script from your local machine or GitHub Codespaces
# after cloning the repo

echo "=== QuantumPilot AI - Push Full Backend Update to GitHub ==="
echo ""

cd "$(dirname "$0")" || exit 1

echo "Current status:"
git status --short
echo ""

echo "Latest local commits:"
git log --oneline -3
echo ""

echo "Pushing to origin/main ..."
git push origin main

echo ""
echo "✅ Done! Check GitHub and then redeploy on Vercel."
