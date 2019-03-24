from flask import Flask

app = Flask(__name__)

__import__('RTI.Database')
__import__('RTI.Feature')
__import__('RTI.Resource')

app.run(port=5000, debug=True)
