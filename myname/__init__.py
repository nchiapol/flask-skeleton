import os

from flask import Flask

def create_app(config = None):
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.from_mapping(config)

    if not app.config["DATABASE"][0] == "/":
        app.config["DATABASE"] = os.path.join(app.instance_path, app.config["DATABASE"])

    try:
        os.makedirs(app.instance_path)
    except FileExistsError:
        pass

    from . import db
    db.init_app(app)

    from . import myblue
    app.register_blueprint(myblue.bp)
    app.add_url_rule('/', endpoint='index')

    return app

