filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()

# Traceback (most recent call last):
#   File "D:\drs\Python\PythonCrashCourse2\ch10\alice.py", line 3, in <module>
#     with open(filename, encoding='utf-8') as f:
#          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'