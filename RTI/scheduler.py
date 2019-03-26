import pusher
import RTI.configs
from RTI.Database.cpu import *
from RTI.Database.memory import *
from RTI.Database.disk import *
from RTI.Database.battery import *
from apscheduler.schedulers.background import BackgroundScheduler

cpu_upload_sched = BackgroundScheduler()
cpu_upload_sched.add_job(per_cpu_upload, 'interval', seconds=2)
cpu_upload_sched.start()

memory_upload_sched = BackgroundScheduler()
memory_upload_sched.add_job(per_memory_upload, 'interval', seconds=2)
memory_upload_sched.start()

disk_upload_sched = BackgroundScheduler()
disk_upload_sched.add_job(per_disk_upload, 'interval', seconds=30)
disk_upload_sched.start()

battery_upload_sched = BackgroundScheduler()
battery_upload_sched.add_job(per_battery_upload, 'interval', seconds=60)
battery_upload_sched.start()


pusher_client = pusher.Pusher(
  app_id=RTI.configs.PUSHER_APP_ID,
  key=RTI.configs.PUSHER_KEY,
  secret=RTI.configs.PUSHER_SECRET,
  cluster=RTI.configs.PUSHER_CLUSTER,
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})