from app import create_app,db
from flask_apscheduler import APScheduler
app=create_app()
scheduler = APScheduler(app=app)

# @scheduler(trigger='interval', id='updateBook', hours=1)
# def updateBook():
#     pass


if __name__ == '__main__':
    scheduler.start()
    app.run(host='0.0.0.0', port=8011, debug=False, use_reloader=False)
