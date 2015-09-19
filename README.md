JCP
=====

jcp is a template aware copy program.

The primary usage of this tool would be to use in something like bash-configured Packer files, or hack-and-slash
shell scripts.  If you are defining an operating system configuration, often you want to have templates that only vary a
small amount between one system to another.  Most things you can do with bash - like tweak systemd configurations or
enable SELinux configurations, but templates are the one thing you need a tool for.

jcp provides that, and only that.  It's fast, really basic, and and there's not really a lot to it.
All the credit goes to the authors of Python, argparse, and Jinja2.

Advertising: If you are doing immutable systems builds, you might also be interested in http://github.com/mpdehaan/strider.
It's like Packer and Vagrant, just in Python, and also pretty fast and basic.

Installation
============

    pip install jcp

Usage
=====

    jcp --input foo.conf.j2 --data answers.yml --output /etc/foo.conf

Ideas
=====

Possibly good pull requests for unimplemented features:

   * If no "--output" parameter, dump to stdout
   * Support a "--engine" parameter to use things other than Jinja2
   * Support other important flags from "--cp" if any.
   * Python 3 compliance

License
=======

Apache 2.  Program (C) Michael DeHaan, 2015
