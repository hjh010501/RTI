from flask import Flask

app = Flask(__name__)

__import__('RTI.database')
__import__('RTI.feature')
__import__('RTI.resource')
__import__('RTI.scheduler')

app.run(port=5000, debug=True, threaded=True)
