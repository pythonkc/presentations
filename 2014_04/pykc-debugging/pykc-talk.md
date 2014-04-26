#Debugging Python
##PyKC Monthly Meetup
###Thursday, April 24, 2014

#[Caleb Hyde](https://twitter.com/hedonistica)
##at Alight Analytics

#Approach
Just use `print()` statements!

#The CLI and iterative development
- Build incrementally, fail often
- [iPython](http://ipython.org/) -- Not just for the browser!

#Stack traces
- source file, line number
- On Exceptions (only)

#Debuggery
- [pdb (python debugger)](https://docs.python.org/2/library/pdb.html)
- [pudb: visual debugger for the terminal](https://pypi.python.org/pypi/pudb)
- Navigating the call stack

#Related
- log files 
- Exception (dis)handling
- [Tests](https://docs.python.org/2/library/unittest.html)
- [Call-stack visualtizations](http://pycallgraph.slowchop.com/en/master/)
  - Example: [microsearch](./pycallgraph.png)

#Further topics
- remote, network, and client-server debugging
- [mobile device debugging](https://developers.google.com/chrome-developer-tools/docs/remote-debugging)
- Django debugging
  - [Debug toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar)
  - Example: [PyKC Website](https://github.com/pythonkc/pythonkc.com)

#fin
![and thanks](http://i.imgur.com/gytCGgu.jpg)
