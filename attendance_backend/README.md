# Attendance Backend (FastAPI)

This service provides REST APIs for authentication, class management, and attendance operations. Supabase integration is planned; current endpoints are stubbed and return HTTP 501 Not Implemented where applicable.

## Prerequisites

- Python 3.11+ recommended
- Virtual environment (optional but recommended)
- Installed dependencies:
  - pip install -r requirements.txt

## Required environment variables (Supabase)

The backend reads configuration from environment variables in src/api/dependencies.py. While the application can start without them for documentation and OpenAPI generation, any endpoint that actually requires Supabase will return a 500 if these are missing.

Set the following variables in your shell or a .env file loaded by your runner:

- SUPABASE_URL: Base URL of your Supabase project (e.g., https://<project>.supabase.co)
- SUPABASE_ANON_KEY: Public anonymous API key
- SUPABASE_SERVICE_ROLE_KEY: Service role key (server-side only; keep it secret)
- SUPABASE_JWT_SECRET: JWT secret configured in your Supabase project
- ENVIRONMENT: Optional. Defaults to development.

Behavior:
- App boot and OpenAPI generation do not require these values.
- Endpoints that depend on Supabase call settings.require() and will respond with 500 and a list of missing variables if not provided.

## Running the API locally

1) Create and activate a virtual environment (optional)
   - python -m venv .venv
   - source .venv/bin/activate   (Windows: .venv\Scripts\activate)

2) Install dependencies
   - pip install -r requirements.txt

3) Export environment variables (example using bash)
   - export SUPABASE_URL="https://YOUR_PROJECT.supabase.co"
   - export SUPABASE_ANON_KEY="YOUR_ANON_KEY"
   - export SUPABASE_SERVICE_ROLE_KEY="YOUR_SERVICE_ROLE_KEY"
   - export SUPABASE_JWT_SECRET="YOUR_JWT_SECRET"
   - export ENVIRONMENT="development"

4) Start the server with uvicorn
   - uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --reload

5) Access the API
   - OpenAPI/Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc
   - Health check: GET http://localhost:8000/

Notes:
- The routers are mounted under /api, e.g., /api/auth/login, /api/classes, /api/attendance/mark.
- Many endpoints currently return 501 Not Implemented while Supabase integration is being added.

## Regenerating the OpenAPI specification

The repository includes a script that exports the live OpenAPI schema from the FastAPI app to interfaces/openapi.json.

To regenerate:
1) Ensure dependencies are installed.
2) Run the generator script:
   - python -m src.api.generate_openapi

This will:
- Import the FastAPI app from src/api/main.py
- Generate the schema via app.openapi()
- Write the result to attendance_backend/interfaces/openapi.json

## Project structure (backend)

- src/api/main.py: FastAPI app setup, CORS, and health endpoint.
- src/api/dependencies.py: Settings loader reading Supabase-related environment variables and validation helpers.
- src/api/routers/: Routers for auth, classes, and attendance (currently stubbed).
- src/api/generate_openapi.py: Utility to emit OpenAPI to interfaces/openapi.json.
- interfaces/openapi.json: Generated OpenAPI document.
- requirements.txt: Python dependencies.

## Troubleshooting

- 500 Server is not fully configured. Missing environment variables:
  - Some endpoints require Supabase configuration. Provide the variables listed above and restart the server.
- 501 Not Implemented:
  - This is expected for stubbed endpoints until Supabase integration is completed.
