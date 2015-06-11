# reload-on-change
A simple chrome extension + flask service to reload a given webpage on files change.


## What is this

A simple chrome extension that you can toggle to refresh a page when any file
in the folder that you specify changes.

You specify the folder to keep an eye on on a small flask service that tells
the extension whether any file in the folder has been changed or not.

This is just a first stab to the problem but good enough for me to use, use at
your own risk.

## How to run

In chrome you'll need to "Load unpacked extension..." the `reload-on-change/extension/` path

For the server you can do the following:

    $ cd reload-on-change/server/
    $ virtualenv reload-on-change
    $ source reload-on-change/bin/activate
    (reload-on-change) $ pip install -r requirements.txt
    (reload-on-change) $ python server.py /path/to/watch/

Just click the reload-like icon to toggle the magic.

## Motivation

I was looking for an app/extension/whatever that allows me to automatically
reload a web page that I was developing. I couldn't fine any that suits my
needs so I made a very simple one myself.

The current existing ones are for other platforms different than Linux, don't
work anymore or do a simple reload every X time.
