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
    sudo("add route ppp0 192.168.1.63")

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




