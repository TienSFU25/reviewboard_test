from jinja2 import *

env = Environment(
	trim_blocks=True,
	lstrip_blocks=True)

env2 = Environment()

with open('test2.txt', 'r') as f:
	template_str = f.read()

t1 = env.from_string(template_str)
t2 = env2.from_string(template_str)

print t1.render(a="abcd")
print('----')
print t2.render(a="abcd")



import urllib2
request = {'_Request__fragment': None,
 '_Request__original': 'http://localhost:8080/api/validation/diffs/',
 '_Request__r_host': '/api/validation/diffs/',
 '_Request__r_type': '//localhost:8080/api/validation/diffs/',
 '_tunnel_host': None,
 'data': '--===============1370781187457944688==\r\nContent-Disposition: form-data; name="repository"\r\n\r\ntestrepo\r\n--===============1370781187457944688==\r\nContent-Disposition: form-data; name="path"; filename="diff"\r\nContent-Type: application/octet-stream\r\n\r\ndiff --git a/t2 b/t2\nindex f6762c3..135b1aa 100644\n--- a/t2\n+++ b/t2\n@@ -1 +1 @@\n-Random text for t2\n+Random t2 text\n\r\n--===============1370781187457944688==--\r\n\r\n',
 'headers': {'Content-length': '410',
             'Content-type': 'multipart/form-data; boundary================1370781187457944688=='},
 'host': 'localhost:8080',
 'method': 'POST',
 'origin_req_host': 'localhost',
 'port': None,
 'timeout': None,
 'type': 'http',
 'unredirected_hdrs': {'Cookie': 'rbsessionid=h2kfyr0ozs26r7hlq64w1dkx618e6qe0',
                       'Host': 'localhost:8080',
                       'User-agent': 'RBTools/0.7alpha0'},
 'unverifiable': False}

urllib2.urlopen(request)
