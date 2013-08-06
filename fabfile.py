# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Created on 2013-5-16

@author: floyd
'''

from fabric.api import task, sudo, env, run, local, cd
import os,sys

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
    sudo("route delete -net 192.168.1.100 -interface ppp0")

    sudo("route add -net 192.168.1.24 -interface ppp0")
    sudo("route add -net 192.168.1.61 -interface ppp0")
    sudo("route add -net 192.168.1.170 -interface ppp0")
    sudo("route add -net 192.168.1.171 -interface ppp0")
    sudo("route add -net 192.168.1.100 -interface ppp0")

@task
def new_pyproject(name="test_py"):
    local("mkdir %s" % name)
    local("cd %s" % name)
    local("buildout init ./")

@task
def new_mavenproject(name="test_java", base="spring"):
    local("mkdir %s" % name)
    local("cd %s" % name)
    local("mvn archetype:create -DgroupId=com.floydshen.data -DartifactId=%s -DarchetypeArtifactId=appfuse-basic-spring" % name)

@task
def service():
    #TODO
    pass

@task
def install_pear():
    sudo("cd /usr/lib/php")
    sudo("sudo php install-pear-nozlib.phar")
    #include_path = ".:/usr/lib/php/pear"
    sudo("sudo pear channel-update pear.php.net")
    sudo("sudo pecl channel-update pecl.php.net")
    sudo("sudo pear upgrade-all")
    pass

@task
def help():
    run("echo ' -----------------------------------------------'")
    run("echo '|                                               |'")
    run("echo ' -----------------------------------------------'")

project_dir = "/Users/floyd/Desktop/devProjects/HaozuTest/Haozu/HaoZu2.0"
@task
def rename_haozu():
    def listdir(dir):
        list = os.listdir(dir)
        for line in list:
            filepath = os.path.join(dir,line)
            if os.path.isdir(filepath):
                listdir(filepath)
            elif os.path:
                tmp = line[0] + line[1]
                if tmp != "HZ":
                    if line.find("+") < 0 and line.find(".m") > -1 and line.find("AppDelegate") < 0:
                        newpath_m = os.path.join(dir,"HZ"+line)
                        filepath_h = os.path.join(dir,line[:-2]+".h")
                        newpath_h = os.path.join(dir,"HZ"+line[:-2]+".h")
                        run("rm -rf "+newpath_m)
                        run("rm -rf "+newpath_h)
                        run("mv "+filepath+" "+newpath_m)
                        run("mv "+filepath_h+" "+newpath_h)

                        #替换文件中className
                        with cd(project_dir):
                            run("find . -type f -name '*.h' -exec sed -i '' \"s/\ %s /\ HZ%s /g\" {} +" % (line[:-2], line[:-2]))
                            run("find . -type f -name '*.m' -exec sed -i '' \"s/\ %s /\ HZ%s /g\" {} +" % (line[:-2], line[:-2]))

                            run("find . -type f -name '*.h' -exec sed -i '' \"s/\ %s,/\ HZ%s,/g\" {} +" % (line[:-2], line[:-2]))
                            run("find . -type f -name '*.m' -exec sed -i '' \"s/\ %s,/\ HZ%s,/g\" {} +" % (line[:-2], line[:-2]))

                            run("find . -type f -name '*.h' -exec sed -i '' \"s/\ %s>/\ HZ%s>/g\" {} +" % (line[:-2], line[:-2]))
                            run("find . -type f -name '*.m' -exec sed -i '' \"s/\ %s>/\ HZ%s>/g\" {} +" % (line[:-2], line[:-2]))

                            run("find . -type f -name '*.h' -exec sed -i '' \"s/\ %s{/\ HZ%s{/g\" {} +" % (line[:-2], line[:-2]))
                            run("find . -type f -name '*.m' -exec sed -i '' \"s/\ %s{/\ HZ%s{/g\" {} +" % (line[:-2], line[:-2]))

                            run("find . -type f -name '*.h' -exec sed -i '' \"s/\ %s\.h/\ HZ%s\.h/g\" {} +" % (line[:-2], line[:-2]))
                            run("find . -type f -name '*.m' -exec sed -i '' \"s/\ %s\.h/\ HZ%s\.h/g\" {} +" % (line[:-2], line[:-2]))

                            run("find . -type f -name '*.h' -exec sed -i '' \"s/\"%s\.h/\"HZ%s\.h/g\" {} +" % (line[:-2], line[:-2]))
                            run("find . -type f -name '*.m' -exec sed -i '' \"s/\"%s\.h/\"HZ%s\.h/g\" {} +" % (line[:-2], line[:-2]))




    with cd(project_dir):
        listdir(project_dir)

