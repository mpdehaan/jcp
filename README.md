JCP
=====

jcp is a template aware copy program.

The primary usage of this tool would be to use in something like bash-configured Packer files, or hack-and-slash
shell scripts.  

If you are defining an operating system configuration, often you want to have templates that only vary a
small amount between one system to another.  Most things you can do with bash - like tweak systemd configurations or
enable SELinux configurations, but templates are the one thing you need a tool for.

jcp provides that, and only that.  It's fast, really basic, and and there's not really a lot to it.
All the credit goes to the authors of Python, argparse, and Jinja2.

Advertising: If you are doing immutable systems builds, you might also be interested in http://github.com/mpdehaan/strider.
It's like Packer and Vagrant, just in Python (AWS only at this point), and also pretty fast and basic.

Installation
============

    pip install jcp

Usage
=====

The following example uses a template file, 'foo.conf.j2' in Jinja2 format, feeds in variables from 'answers.yml' and
saves the results in '/etc/foo.conf':

    jcp --input foo.conf.j2 --answers answers.yml --output /etc/foo.conf

Ok, that was easy.  Currently there aren't any more flags than that.  That's it!

Jinja2
======

For how Jinja2 templates work, I recommend the template engine documentation at http://jinja.pocoo.org/docs/dev/templates/.

Assume answers.yml looked like this:

    ---
    dog: fido
    cat: delicious

Here's a really basic example of an input file.

    My dog is named {{ dog }} and the cat is {{ cat }}.
    
The output file would look like:

    My dog is named fido and the cat is delicious.
    
Of course, most likely  you're using this for config files. If you want more, read the Jinja2 docs.  It's easy, and it does
if conditionals, loops, and all sorts of nice things.
    
Ideas
=====

Possibly good pull requests for unimplemented features:

   * If no "--output" parameter, dump to stdout
   * Support a "--engine" parameter to use things other than Jinja2 (anything Python goes, shelling out to ruby for erb is cool too, I don't care!).  Actually this should probably go by the file extension and just default to Jinja, and be explicit only when --engine is specified.
   * Support other important flags from coreutils cp, if any are desired.
   * Support extra variables from the command line via --vars "key1=value1 key2=value2"
   * Python 3 compliance

License
=======

Apache 2.  Program (C) Michael DeHaan, 2015
