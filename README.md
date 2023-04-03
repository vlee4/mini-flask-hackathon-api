# Global Hack Week Python-Flask api

A minimalist API made in Python with Flask.
`#CreateYourOwnAPI`

## Run virtual environment

On Windows, run:
`tutorial-env\Scripts\activate.bat`

On Unix or MacOS, run:
`source tutorial-env/bin/activate`

## Run server

With your virtual environment running, in the terminal enter:
`FLASK_APP=./app.py flask run`

OR
`flask run`

OR

for updates on refresh, use:
`flask run --reload`

The server will run on `http://127.0.0.1:5000/`

## Stop server

Type `CTRL + C` into the terminal

## Deactivate virtual environment

`deactivate`

## Make a POST request on a locally run server

Using POSTMAN, make a request to `http://localhost:5000/hackathons`. An example JSON body you send with the request is:

```
   {
    "Name": "hackathon 4",
    "theme": "Aesthetics",
    "start_date": "2023-04-19 12:00:00",
    "end_date": "2023-04-23 12:00:00",
    "location": "Somewhere",
    "Type": "In-person"
}
```
