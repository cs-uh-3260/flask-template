# flask-api

An example flask rest API server.

## Pre-requisites

- python 3.10 or higher
- mongodb installed. Follow [https://www.mongodb.com/docs/manual/installation/](https://www.mongodb.com/docs/manual/installation/) to install mongodb locally. Select the right link for your operating system.

## Running the server locally

1. Run `make dev_env` to create a virtual environment and install dependencies
2. Run `make prod` to run the server. This will also run the test first. 

Go to [http://127.0.0.1:8000] to see it running!

You can use [ctr-c] (cmd-c on MacOS) to stop the server.

Don't forget to run `deactivate` to deactivate the virtual environment once you are done working for the day!
