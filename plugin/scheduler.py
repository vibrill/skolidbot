from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=1)
def timed_job():
    try:
        subprocess.call(["python3", "crawl/crawl.py"])
    except:
        print('gagal meluncurkan aplikasi')
    print('crawl running')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=7)
def scheduled_job():
    try:
        subprocess.call(["python3", "crawl/pusmenjar.py"])
        print('pusmenjar telah dijalankan')
    except:
        print('gagal meluncurkan aplikasi')
    print('This job is run everyday at 7 am.')

sched.start()