# Vercel Deployment Guide for KSP Crime Intelligence AI

## Overview

This guide covers deploying your full-stack KSP Crime Intelligence AI project on Vercel.

**Important**: Vercel is optimized for frontend and serverless backends. Since this project has a Python FastAPI backend with persistent databases, we recommend a **hybrid deployment approach**.

---

## Deployment Architecture

### Frontend: Vercel ✅
- React + Vite application
- Hosted on Vercel edge network
- Auto-deploys from GitHub

### Backend + Databases: External Service
- Python FastAPI backend
- MSSQL, Neo4j, ChromaDB databases
- Deploy to: Railway, Render, Fly.io, AWS, or Docker service

---

## Step 1: Deploy Frontend to Vercel

### Prerequisites
- GitHub account (repo already connected)
- Vercel account: https://vercel.com

### Steps

1. **Go to Vercel Dashboard**
   - Visit https://vercel.com/dashboard
   - Click "Add New..." → "Project"

2. **Import Your Repository**
   - Search for `Intelligent_conversational_ai`
   - Click "Import"

3. **Configure Project**
   - **Framework Preset**: Vite (auto-detected)
   - **Root Directory**: `./` (or leave blank)
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Output Directory**: `frontend/dist`
   - **Install Command**: `npm install`

4. **Add Environment Variables**
   - Click "Environment Variables"
   - Add: `VITE_API_BASE_URL` = `https://your-backend-url.com` (you'll set this later)
   - Click "Deploy"

5. **Deploy**
   - Click "Deploy" button
   - Wait for build to complete (2-3 minutes)
   - Your frontend will be live at: `https://your-project.vercel.app`

---

## Step 2: Deploy Backend (Choose One Option)

### Option A: Railway (Easiest with Docker) ⭐ RECOMMENDED

1. **Go to Railway**
   - Visit https://railway.app
   - Sign up with GitHub
   - Create new project

2. **Connect Docker Compose**
   - Select "Deploy from GitHub"
   - Choose your repository
   - Railway auto-detects `docker-compose.yml`

3. **Configure Environment**
   - Add variables from `.env.example`:
     - `OPENAI_API_KEY` (get from OpenAI)
     - `SECRET_KEY` (generate random string)
     - `DATABASE_URL` (use Railway's MSSQL service)

4. **Set Up Databases**
   - Create MSSQL service in Railway
   - Create Neo4j service in Railway
   - Update DATABASE_URL in environment

5. **Deploy**
   - Railway auto-deploys from GitHub
   - Backend URL: `https://your-backend.railway.app`

### Option B: Render (Docker Deployment)

1. **Go to Render**
   - Visit https://render.com
   - Connect GitHub account

2. **Create Web Service**
   - New → Web Service
   - Choose repository
   - Set runtime to Docker
   - Build Command: `docker build -t backend ./backend`

3. **Configure Environment**
   - Add all variables from `.env.example`
   - Connect PostgreSQL/MSSQL service

4. **Deploy**
   - Render auto-deploys
   - Backend URL: `https://your-backend.onrender.com`

### Option C: Fly.io (Container Platform)

1. **Install Fly CLI**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Deploy Backend**
   ```bash
   fly launch --dockerfile backend/Dockerfile
   fly secrets set OPENAI_API_KEY=xxx
   fly deploy
   ```

3. **Databases**
   - Use external services (Azure SQL, Neo4j Aura, etc.)
   - Update DATABASE_URL accordingly

---

## Step 3: Connect Frontend to Backend

Once both are deployed:

1. **Update Frontend Environment Variable**
   - Go to Vercel dashboard
   - Project settings → Environment Variables
   - Update `VITE_API_BASE_URL` = `https://your-backend-url.com`

2. **Redeploy Frontend**
   - Vercel auto-redeployed when env changes
   - Or trigger redeploy manually

3. **Test Connection**
   - Open frontend URL
   - Open browser DevTools → Network tab
   - Check if API calls go to backend URL

---

## Database Services

### Option 1: Azure SQL Database (MSSQL)
```
1. Create Azure account
2. Create SQL Database
3. Get connection string
4. Add to backend environment: DATABASE_URL
```

### Option 2: AWS RDS (MSSQL/PostgreSQL)
```
1. AWS Console → RDS
2. Create MSSQL instance
3. Copy endpoint
4. Configure security groups for access
```

### Option 3: Neo4j Aura (Graph Database)
```
1. https://neo4j.com/cloud/aura/
2. Create cloud instance
3. Get connection URI
4. Add to NEO4J_URI environment
```

### Option 4: ChromaDB
```
1. Self-host or use open-source Docker image
2. Set CHROMA_URL in backend environment
```

---

## Environment Variables Needed

### Frontend (.env files already created)
```
VITE_API_BASE_URL=https://your-backend-url.com
```

### Backend (Set in your hosting platform)
```
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
SECRET_KEY=generate_random_string_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=mssql+pyodbc://user:password@host/database
OPENAI_API_KEY=sk-your-key-here
CHROMA_URL=http://chromadb-service:8000
NEO4J_URI=bolt+s://neo4j-service:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your-password
```

---

## Troubleshooting

### Frontend builds but shows blank page
- Check browser console for errors
- Verify `VITE_API_BASE_URL` is correct
- Check CORS settings in backend

### API calls fail
- Verify backend URL is accessible
- Check backend logs in hosting platform
- Ensure firewall allows connections

### Database connection errors
- Verify connection strings
- Check IP whitelist on database service
- Test connection locally first

### Build fails on Vercel
```bash
# Test locally
cd frontend
npm install
npm run build

# Check output
ls frontend/dist
```

---

## File Changes Summary

The following files were added to support Vercel deployment:

- `vercel.json` - Vercel configuration
- `frontend/.env.production` - Production environment
- `frontend/.env.development` - Development environment
- `.vercelignore` - Files to ignore in deployment

---

## Quick Deployment Checklist

- [ ] Frontend deployed to Vercel
- [ ] Backend deployed to Railway/Render/Fly.io
- [ ] Database services set up
- [ ] Environment variables configured
- [ ] Frontend connected to backend
- [ ] Tested API connectivity
- [ ] Secure secrets in environment (not in code)

---

## Next Steps

1. Set up backend hosting (Railway recommended)
2. Configure database services
3. Add environment variables
4. Test full application flow
5. Monitor logs and performance
6. Set up CI/CD pipeline

---

## Support

- **Vercel Docs**: https://vercel.com/docs
- **FastAPI Deployment**: https://fastapi.tiangolo.com/deployment/
- **Railway Docs**: https://docs.railway.app
- **Docker Documentation**: https://docs.docker.com

---

Last Updated: 2026-07-21
