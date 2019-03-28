import pusher
import RTI.configs
from RTI.Database.cpu import *
from RTI.Database.memory import *
from RTI.Database.disk import *
from RTI.Database.battery import *
from apscheduler.schedulers.background import BackgroundScheduler


def per_cpu_upload_sched():
  cpu_per = get_processor_usage('percent')
  per_cpu_upload(cpu_per)
  pusher_client.trigger('rti-cpu-channel', 'cpu-perform', {'p': cpu_per})


def per_memory_upload_sched():
  memoryused = get_memory_usage('used')
  memoryunused = get_memory_usage('unused')
  memorypercent = get_memory_usage('percent')
  per_memory_upload(memoryused, memoryunused, memorypercent)
  pusher_client.trigger('rti-memory-channel', 'memory-perform', {'mused': memoryused, 'munused': memoryunused, 'mper': memorypercent})

def per_disk_upload_sched():
  diskused = get_disk_status('used')
  diskunused = get_disk_status('unused')
  disksize = get_disk_status('size')
  diskpercent = get_disk_status('percent')
  per_disk_upload(diskpercent, diskused, diskunused, disksize)
  pusher_client.trigger('rti-disk-channel', 'disk-perform', {'dper': diskpercent, 'dused': diskused, 'dunused': diskunused, 'dsize': disksize})

def per_battery_upload_sched():
  batterypercent = get_battery_status('percent')
  batterystatus = get_battery_status('status')
  per_battery_upload(batterypercent, batterystatus)
  pusher_client.trigger('rti-battery-channel', 'battery-perform', {'p': batterypercent, 's': batterystatus})


cpu_upload_sched = BackgroundScheduler()
cpu_upload_sched.add_job(per_cpu_upload_sched, 'interval', seconds=2)
cpu_upload_sched.start()

memory_upload_sched = BackgroundScheduler()
memory_upload_sched.add_job(per_memory_upload_sched, 'interval', seconds=2)
memory_upload_sched.start()

disk_upload_sched = BackgroundScheduler()
disk_upload_sched.add_job(per_disk_upload_sched, 'interval', seconds=30)
disk_upload_sched.start()

battery_upload_sched = BackgroundScheduler()
battery_upload_sched.add_job(per_battery_upload_sched, 'interval', seconds=60)
battery_upload_sched.start()


pusher_client = pusher.Pusher(
  app_id=RTI.configs.PUSHER_APP_ID,
  key=RTI.configs.PUSHER_KEY,
  secret=RTI.configs.PUSHER_SECRET,
  cluster=RTI.configs.PUSHER_CLUSTER,
  ssl=True
)

