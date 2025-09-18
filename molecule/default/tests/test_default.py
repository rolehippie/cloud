import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("executable", [
    "/usr/bin/s5cmd",
    "/usr/bin/eksctl",
    "/usr/bin/hcloud",
    "/usr/bin/az"
])
def test_is_installed(host, executable):
    file = host.file(executable)
    assert file.is_file
