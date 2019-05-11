from RTI import app
import RTI.configs
from RTI.feature.battery import *
from RTI.database.trainlogs import train_logs_upload
from flask import request
import pusher
import datetime

pusher_client = pusher.Pusher(
  app_id=RTI.configs.PUSHER_APP_ID,
  key=RTI.configs.PUSHER_KEY,
  secret=RTI.configs.PUSHER_SECRET,
  cluster=RTI.configs.PUSHER_CLUSTER,
  ssl=True
)


@app.route('/train', methods=['POST'])
def upload_train():
    data = request.get_json()
    logs = data['logs']
    epoch = data['epoch']
    loss=data['loss']
    accuracy=data['accuracy']
    t = datetime.datetime.now()
    train_logs_upload(logs, epoch, loss, accuracy, t)
    pusher_client.trigger('rti-train-channel', 'train-perform', {'logs': logs, 'epoch': epoch, 'loss': loss, 'accuracy': accuracy, 't': str(t)})
    return "", 200