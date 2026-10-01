import six
print("six._version_ =", six._version_)
print("six._file_   =", six,_file_)

print("PY2?", six.PY2, "| PY3?", six.PY3)
print("six.moves.range(3) ->", list(six.moves.range(3)))

import sys
print("sys.path[0] =", sys.path[0])

import site
print("site-packages:", site.getsitepackages())