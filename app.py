from flask import Flask, make_response, jsonify
from flask_auth_middleware import login_required
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config["SECRET_KEY"] = "1234567890"
secret_key = "1234567890"
toolbar = DebugToolbarExtension(app)


@app.route("/public")
def public():
    response = make_response(jsonify({"message": "This is public resource"}), 200)
    return response


@app.route("/private")
@login_required(secret_key=secret_key)
def private(decoded_payload):
    # pdb.set_breakpoint()
    respone = make_response(jsonify({"message": "This is private resource"}), 200)
    return respone


# The __name__ == "__main__" check is used to determine if the code is being run as the main program or being imported as a module.

# Some key points about this:

# - When running the file directly, __name__ will be equal to "__main__". This is the main entry point of the program.

# - When importing the file as a module in another file, __name__ will be set to the name of the module (in this case "app").

# - The app.run() call starts the development web server. We only want to do this if running as the main program, not when imported.

# So in summary, the __name__ check allows app.run() to be called when running the file directly, but not when imported.

# Some other ways we could handle this:

# - Move the app.run() call outside the __name__ check, and instead do:


if __name__ == "__main__":
    app.run(debug=True, port=5001)

# - Use an environment variable to control running the server:

#   import os

#   if os.environ.get("RUN_SERVER"):
#      app.run(debug=True, port=5001)

# - Create a separate file like run.py that imports app and calls app.run().

# So in general, we want to separate the application code from the code that runs the server, and the __name__ check is a handy way to do that in Python.
