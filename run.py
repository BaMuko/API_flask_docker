from flask.cli import FlaskGroup

from device_registry.app import app

cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()