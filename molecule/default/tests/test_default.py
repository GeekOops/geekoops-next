#!/usr/bin/python3
# -*- coding: utf-8 -*-


import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_pxe(host):
	# TODO: Extend the test coverage. 
	tftpboot = "/srv/tftpboot"
	cmd = host.run("curl -v --fail tftp://127.0.0.1/pxelinux.0 -o /tmp/pxelinux.0")
	print(cmd.stdout)
	assert cmd.succeeded
	cmd = host.run(f'diff {tftpboot}/pxelinux.0 /tmp/pxelinux.0')
	assert cmd.succeeded
