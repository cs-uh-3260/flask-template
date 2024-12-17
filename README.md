# flask-api

An example flask rest API server.

## Pre-requisites

- python 3.10 or higher
- mongodb installed. Follow [https://www.mongodb.com/docs/manual/installation/](https://www.mongodb.com/docs/manual/installation/) to install mongodb locally. Select the right link for your operating system.

## Tech Stack

This flask web app uses:

- [flask-restx](https://flask-restx.readthedocs.io/en/latest/quickstart.html) for creating REST APIs. Directory structure following [this setup](https://flask-restx.readthedocs.io/en/latest/scaling.html)
- flask-restx automatically generates [OpenAPI specifications](https://swagger.io/docs/specification/v3_0/about/) for your API
- pymongodb for communicating with the the mongodb database
- pytest for testing (see [https://flask.palletsprojects.com/en/stable/testing/](https://flask.palletsprojects.com/en/stable/testing/) for more info specific to testing Flask applications)

## Running the server locally

This assumes you are already running MongoDB (e.g., through `brew services restart mongodb-community` on MacOs. Find the equivalent for your OS)

1. Run `make dev_env` to create a virtual environment and install dependencies
2. Run `make prod` to run the server. This will also run the test first. 

Go to [http://127.0.0.1:8000] to see it running!

You can use `ctr-c` ()`cmd-c` on MacOS) to stop the server.

Don't forget to run `deactivate` to deactivate the virtual environment once you are done working for the day!
