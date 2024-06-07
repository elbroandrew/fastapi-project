## Run fastapi app:
- got to `app` dir and run

`uvicorn main:app --reload`

or

`gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker main:api --workers=2`