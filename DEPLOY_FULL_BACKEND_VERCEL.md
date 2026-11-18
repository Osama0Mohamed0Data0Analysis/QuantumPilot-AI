# 🚀 Deploy FULL BACKEND on Vercel - QuantumPilot AI

## Current Status (after changes)
- `api/index.py` now tries to load the **complete backend** (`backend/app/`)
- Includes: NeuralUCB, IBMExecutionService, full router, SpaceWeather, Mitigation Factory, Copilot, etc.
- `vercel.json` configured with high memory (3008MB) + 60s duration

## ⚠️ IMPORTANT WARNINGS

Vercel **free tier** has severe limitations for heavy Python:

- **torch** (~800MB+) often fails or makes build extremely slow
- Memory limit on free = 1024MB (we request 3008MB → requires **Pro** plan)
- Build time limit
- Cold starts will be slow

**Recommended options:**
1. **Vercel Pro** (paid) – best for full backend
2. Use **Docker** on Render / Railway / Fly.io / Koyeb (better for heavy ML)
3. Keep using the lightweight `api/index.py` for Vercel + full backend on Codespaces/Docker

## Steps to Deploy Full Backend

### 1. Update your Vercel project settings (Dashboard)

Go to:
Vercel Dashboard → Your Project → **Settings → General**

- **Build Command**: `cd frontend && npm run build`
- **Output Directory**: `frontend/.next`
- **Install Command**: (leave default or `npm install`)

For the Python function:
- Go to **Settings → Functions**
- Or rely on the `vercel.json` we set.

### 2. Add Environment Variables (important)

In Vercel Dashboard → Settings → Environment Variables:

```
IBM_TOKEN=your_real_ibm_cloud_api_key
IBM_CRN=your_crn_here
HF_TOKEN=your_hf_token (optional)
NEXT_PUBLIC_API_URL=https://quantumpilot-ai.vercel.app
```

### 3. Push the changes

```bash
cd /home/user/QuantumPilot-AI

git add api/index.py api/requirements.txt vercel.json frontend/next.config.js
git commit -m "feat: serve FULL backend (NeuralUCB + IBMExecutionService) via api/index.py on Vercel"
git push origin main
```

### 4. Redeploy

- Vercel will auto-deploy on push
- Or manually: Deployments tab → Redeploy

### 5. Verify after deploy

Visit:
- `https://quantumpilot-ai.vercel.app/api/v1/health` 
  → should show `"neuralucb": true` and `"real_ibm": true`

- `https://quantumpilot-ai.vercel.app/api/v1/copilot/plan` (POST with Arabic intent)

- Try the Execute button on the live site

### 6. If build fails (very common with torch)

**Symptoms**: Build timeout or "out of memory"

**Solutions**:
A. Switch back to lightweight:
   - Revert `api/index.py` to the old lightweight version
   - Use Docker for full backend

B. Use a different hosting for the backend:
   - Railway.app (good for Python + torch)
   - Render.com
   - Fly.io
   - GitHub Codespaces (temporary full stack)

### How to know it's using FULL backend?

After successful deploy, check response of `/api/v1/health`:

```json
{
  "mode": "full",
  "neuralucb": true,
  "real_ibm": true
}
```

When you submit a real job with a valid `IBM_TOKEN`, `is_simulated` will become `false`.

## Alternative: Best way to run FULL backend right now

```bash
# 1. Use GitHub Codespaces (already had full Docker)
# 2. Or locally:
docker-compose up --build

# 3. Or Railway / Render (recommended for production full backend)
```

## Summary

We have successfully modified the project so that **Vercel can serve the full backend**.

Whether it actually succeeds depends on your Vercel plan and tolerance for heavy builds.

Current files modified for full backend:
- `api/index.py` (full wrapper)
- `api/requirements.txt` (includes torch + qiskit)
- `vercel.json` (high memory + long duration)
