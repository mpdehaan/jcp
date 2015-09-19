JCP
=====

jcp is a template aware copy program.

The primary usage of this tool would be to use in something like bash-configured Packer files, or hack-and-slash
shell scripts.

If you are doing immutable systems builds, you might also be interested in http://github.com/mpdehaan/strider.

Installation
============

    pip install template-copy

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
