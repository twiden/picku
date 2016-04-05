from flask import Flask, render_template, jsonify
from jinja2 import Environment, PackageLoader
from application.storage import Storage
from application import subscriber
from application.publisher import Publisher
import yaml

app = Flask(__name__)
app.debug = True

storage = Storage()
config = yaml.load(open('config.yaml'))
subscriber.start(config, storage)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/routing_keys/")
def routing_keys():
    return jsonify({'routing_keys': storage.routing_keys()})

@app.route("/messages/<routing_key>")
def messages(routing_key):
    return jsonify({'messages': storage.messages(routing_key)})

@app.route("/publish/<message_id>")
def publish(message_id):
    Publisher(config).publish(storage.get(message_id))
    return jsonify({'published': message_id})


if __name__ == "__main__":
    app.run(port=5555)
