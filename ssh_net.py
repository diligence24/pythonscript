#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yangzhefeng'

from fabric.api import env, lcd, local, cd, sudo, local, put, settings, task, execute, run, get
from fabric.contrib.files import exists
from os.path import expanduser


env.hosts = ["10.0.1.2", "10.0.1.24", "10.0.1.132", "10.0.1.227", "10.0.1.241", "10.0.1.53", "10.0.1.204", "10.0.1.159",
"10.0.1.80", "10.0.1.124", "10.0.1.165", "10.0.1.26"]
env.user = "root"
env.password = 'xxxx'

jump_machine_ssh_key = 'xxxx'
sudoers_mod = 'admin   ALL=\(ALL\)       NOPASSWD: ALL'

@task
def add_user():
	run("useradd admin")
	run("echo -e 'Terminus123\nTerminus123' | passwd admin")

@task
def ssh_key_gen():
	with cd("/home/admin"):
		run("sudo -u admin -H sh -c 'ssh-keygen -t rsa -N \"\" -f /home/admin/.ssh/id_rsa'")
		with cd("/home/admin/.ssh"):
			run("sudo -u admin -H sh -c 'cp id_rsa.pub authorized_keys'")
			run("chmod 600 authorized_keys")
			run("echo {jump_machine_ssh_key} > authorized_keys".format(jump_machine_ssh_key = jump_machine_ssh_key))


@task
def mod_sudoers():
	run("chmod 740 /etc/sudoers")
	run("echo {sudoers_mod} >> /etc/sudoers".format(sudoers_mod = sudoers_mod))


@task(default=True)
def ssh_net():
	add_user()
	ssh_key_gen()
	mod_sudoers()
