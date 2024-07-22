## Run fastapi backend:
- go to `app` dir and run

`uvicorn main:app --reload`

or

`gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker main:api --workers=2`

## Run frontend:

- go to `frontend` folder and run:

`npm run serve`