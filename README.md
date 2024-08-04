## Run Postgres Docker container if not currently running:

`sudo docker start postgresql`

## Run fastapi backend:
- go to `app` dir and run

`uvicorn main:app`

or

`gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker main:api --workers=2`

## Run frontend:

do not forget to:  `npm install` first, then:

- go to `frontend` folder and run:

`npm run serve`