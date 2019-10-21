# NetlifyProject

This project building mini netflix api

## Run this projet in local

`git clone https://github.com/hadpro24/googlechallenge-phase-1-backend.git`

`cd googlechallenge-phase-1-backend.git`

## Use a environment execution
create virtual environment
`python -m venv env`

activate it:
`source ../env/bin/activate`

## Install all dependencies
`pip install -r requirements.txt`

## Development server

Run `python manage.py runserver` for a dev server. Navigate to `http://localhost:8000/`.


## API Endpoints

| Resource URL | Methods | Description |
| -------- | ------------- | --------- |
| `/api/v1/films/` | GET | View all films |
| `/api/v1/films/<int:pk>` | GET | Get a film with id equals pk |
| `/api/v1/films/?search=title_search` | GET | Search the films title contains |
| `/api/v1/films/favorites/?ids=1,3,5,8` | GET | Get all films with id in (1,3,5,8) |


### Credit : Harouna Diallo
