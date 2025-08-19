# Supabase Setup (Backend)

Follow these steps to prepare Supabase for the Attendance Management backend:

1) Apply schema and policies
- Open assets/supabase.md in this repo.
- Copy the "SQL: Schema and Policies" section and run it in your Supabase project's SQL editor.
- Seed an admin user and corresponding profiles row.

2) Configure Auth
- Authentication > URL Configuration
  - Site URL: production URL (or http://localhost:3000 for local)
  - Redirect URLs:
    - http://localhost:3000/**
    - https://<your-domain>/**
- Enable Email / Password provider.

3) Environment variables (required by backend)
- SUPABASE_URL
- SUPABASE_ANON_KEY
- SUPABASE_SERVICE_ROLE_KEY
- SUPABASE_JWT_SECRET

These are read by src/api/dependencies.py. Endpoints requiring Supabase will error if missing.

4) Next implementation tasks
- Replace stubbed endpoints in src/api/routers with real Supabase queries.
- Use service role key only on server-side operations.
- Validate JWTs in backend if required, or rely on Supabase's PostgREST+RLS for direct access patterns.

Troubleshooting:
- If RLS blocks initial seeding, use service role key or temporarily disable RLS during seed, then re-enable.
