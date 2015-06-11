import sys
import os

from flask import Flask
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

app = Flask(__name__)
app.config.from_object(__name__)

# Disable requests logs
import logging
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.ERROR)


class CallbackObserver(FileSystemEventHandler):
    """Very simple observer that runs a callback on any event."""

    def __init__(self, callback):
        self._callback = callback

    def dispatch(self, event):
        self._callback()


class FileWatcher(object):

    def __init__(self, path):
        self._path = path
        self.modified = False

    def start(self):
        self._observer = Observer()
        obs = CallbackObserver(self.mark)
        self._observer.schedule(obs, self._path, recursive=True)
        self._observer.start()

    def stop(self):
        self._observer.stop()
        self._observer.join()

    def mark(self):
        self.modified = True

    def unmark(self):
        self.modified = False


@app.route('/haschanged', methods=['GET', 'POST'])
def has_changed():
    # if request.method == 'POST':
    #     url = request.form['url']

    if watcher.modified:
        watcher.unmark()
        refresh = 'true'
        print 'Some file has changed, reload response has been given.'
    else:
        refresh = 'false'

    return refresh

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path_to_watch = os.path.realpath(sys.argv[1])
    else:
        print "Path to watch is needed"
        sys.exit()

    watcher = FileWatcher(path_to_watch)
    watcher.start()

    try:
        app.run(host='0.0.0.0', port=8801)
    finally:
        watcher.stop()
        print 'Server and watcher stopped'
