TCOPY
=====

tcopy is a template aware copy tool.

The primary usage of this tool would be to use in bash-configured Packer files.

You might also use it with github.com/mpdehaan/strider.

Installation
============

    pip install tcopy

Usage
=====

    tcopy --input foo.conf.j2 --data answers.yml --output /etc/foo.conf

License
=======

Apache 2.  Program (C) Michael DeHaan, 2015
