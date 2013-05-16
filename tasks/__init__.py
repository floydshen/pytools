# -*- coding: utf-8 -*-
#!/usr/bin/env python
from fabric.api import task, hosts, roles, run, local, sudo, env, execute

@task
def test():
    print "Test"
