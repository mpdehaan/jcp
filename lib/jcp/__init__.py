# Copyright 2015 Michael DeHaan <michael.dehaan/gmail>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import yaml
import jinja2
import sys


class JCopyException(Exception):
    pass


class JCopy(object):
    def __init__(self, answers=None):
        self.answers = answers

    def write(self, input, output_stream):
        # verify the answers file exists and read it
        answers = self.answers
        if not os.path.exists(answers):
            raise JCopyException("%s does not exist" % answers)
        answer_data = open(answers).read()
        try:
            answer_data = yaml.load(answer_data)
        except Exception, e:
            raise JCopyException(str(e))

        if not type(answer_data) == dict:
            raise JCopyException("expecting %s to describe a YAML dictionary" % answers)

        # verify the input file exists
        if not os.path.exists(input):
            raise JCopyException("%s does not exist" % input)

            # prep the template engine
        loader = jinja2.FileSystemLoader(searchpath="/")
        jenv = jinja2.Environment(loader=loader, undefined=jinja2.StrictUndefined)
        template = jenv.get_template(os.path.abspath(input))

        # render and write the template
        contents = template.render(**answer_data)
        output_stream.write(contents)

        return 0

    def copy(self, input, output):
        if output:
            # verify the output file directory exists, if not, make it
            dirname = os.path.dirname(os.path.abspath(output))
            if not os.path.exists(dirname):
                os.makedirs(dirname)

            with open(output, "w") as fh:
                result = self.write(input, fh)
        else:
            # No output path specified, let's write to stdout
            result = self.write(input, sys.stdout)

        return result
