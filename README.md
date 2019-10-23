# difs-quad
Base project for DIFS L2 TP QuaD. Please, fork me!

# Create dev env
Run the following command: `pip install -r requirements.txt`

Restart any IDE in order to work properly.

# Run for development
Run the following command: `FLASK_ENV=development flask run`

The dev server will be listenning on the port 5000. So, open a web browser and go to the following url: `http://localhost:5000/`

# Run selenium tests
Must have Chrome install with the latest version.

Must have a running server on localhost:5000

Run the following command: `behave tests/features`
