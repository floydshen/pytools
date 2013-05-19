# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Created on 2013-5-16

@author: floyd
'''

from fabric.api import task, sudo, env
env.user = 'floyd'
env.hosts = ['localhost']

# @task
# def test():
#     """
#     a test function
#     """
#     print "Test"

@task
def ajk_vpn():
    sudo("route delete -net 192.168.1.24 -interface ppp0")
    sudo("route delete -net 192.168.1.61 -interface ppp0")
    sudo("route delete -net 192.168.1.170 -interface ppp0")
    sudo("route delete -net 192.168.1.171 -interface ppp0")

    sudo("route add -net 192.168.1.24 -interface ppp0")
    sudo("route add -net 192.168.1.61 -interface ppp0")
    sudo("route add -net 192.168.1.170 -interface ppp0")
    sudo("route add -net 192.168.1.171 -interface ppp0")

@task
def new_pyproject():
    #TODO
    pass

@task
def new_mavenproject():
    #TODO
    pass

@task
def service():
    #TODO
    pass




