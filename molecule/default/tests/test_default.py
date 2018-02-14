import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


# Good example:
# https://github.com/nephelaiio/ansible-role-rbenv/blob/4771cdc2ee559b78d29929ab0700e8fca15019ab/molecule/compile/tests/test_compile.py

rbenv_version = 'v0.33.1'

def test_rbenv_folders(host):
    f = host.file('/home/vagrant/.rbenv')

    assert f.exists
    assert f.user == 'vagrant'
    assert f.group == 'vagrant'
