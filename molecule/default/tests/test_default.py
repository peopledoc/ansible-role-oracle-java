import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):

    assert host.package('oracle-java8-installer').is_installed
    assert host.package('oracle-java8-set-default').is_installed
    assert host.package('oracle-java8-unlimited-jce-policy').is_installed


def test_binaries(host):

    # Check java availability and the default version
    run1 = host.run('java -version')
    run2 = host.run('/usr/lib/jvm/java-8-oracle/jre/bin/java -version')
    assert run1.rc == run2.rc == 0
    assert run1.stderr and run1.stderr == run2.stderr
    assert run1.stdout == run2.stdout == ''

    # Check 'javac' and 'java' must be the same version
    javac = host.run('javac -version')
    assert javac.rc == 0
    # expected output:
    # javac 1.8.0_161
    javac_version = javac.stderr.split()[1]

    # expected output:
    # java version "1.8.0_161"
    # Java(TM) SE Runtime Environment (build 1.8.0_161-b12)
    # Java HotSpot(TM) 64-Bit Server VM (build 25.161-b12, mixed mode)
    java_version = run1.stderr.split('\n')[0]  # first line

    # compare java and javac versions
    assert java_version == 'java version "%s"' % javac_version


def test_certificates(host):
    cmd = "keytool -list -storepass changeit "
    cmd += "-keystore /usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts"
    run = host.run(cmd)
    print(run.stdout)
    assert run.rc == 0
    assert "google.com" in run.stdout
    assert "dummy-test" in run.stdout
