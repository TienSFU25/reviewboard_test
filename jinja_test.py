# -*- coding: utf-8 -*-
import os, os.path as path

from jinja2 import Template, Environment, Undefined, DebugUndefined
from jinja2.runtime import Context
from jinja2 import BaseLoader, PackageLoader, PrefixLoader
from jinja2 import BytecodeCache, FileSystemBytecodeCache

# ud=Undefined(obj)

class MyLoader(PackageLoader):
	def get_source(self, env, template_name):
		return "Hello //name||\n\nUndefined junk down here\n\n//ud||", "who cares about this path again?", False

def finalize(var):
	if var is None:
		return str(Environment().undefined(obj=str, name="None"))
	else:
		return var

class MyCache(FileSystemBytecodeCache):
    def load_bytecode(self, bucket):
    	# import pdb
    	# pdb.set_trace()
# {'directory': '/Users/tien/Documents/reviewboard_test/tmp/jinja_cache', 'pattern': '__jinja2__%s.cache'}
# {'environment': <jinja2.environment.Environment object at 0x102654110>, 'checksum': 'edfc577fbaf1e11957fe13094f6b8286fc745a28', 'code': None, 'key': 'af146353c55a03a5b2629604ac8e0b3b00fffa70'}
        filename = path.join(self.directory, bucket.key)
        # print bucket.key
        # print self.directory
        # print filename
        # print "-----------"
        if path.exists(filename):
            with open(filename, 'rb') as f:
                bucket.load_bytecode(f)
                # AFTER THIS CODE IS NO LONGER NONE, bucket.bytecode_to_string() prints some junk
                self.dump_bytecode(bucket)

    # this seems to never get called
    def dump_bytecode(self, bucket):
        filename = path.join(self.directory, bucket.key)
        with open(filename, 'wb') as f:
        	# print f.read()
            bucket.write_bytecode(f)

p = "".join([os.getcwd(), "/tmp/jinja_cache"])
print p
bcc = MyCache(p, "__jinja2__%s.cache")

env = Environment(loader=
	PrefixLoader({
		'app1': PackageLoader('some_app', 'templates'),
		'app2': MyLoader('some_app', 'templates')
	}), 
	variable_start_string="//", 
	variable_end_string="||",
	# undefined=Undefined,
	undefined=DebugUndefined,
	finalize=finalize,
	cache_size=0,
	extensions=['jinja2.ext.autoescape'],
	bytecode_cache=bcc)
	# )

# template = Template('Hello {{name}}')
template = env.get_template('app2/template1.html', parent="clgt")
ud=env.undefined(obj=int, name=708932)
print ud
print env.list_templates()
print Context.environment
# env.compile_templates("some_dir")

print template.render(name=u'Pokémon', ud=ud)

# print env.globals