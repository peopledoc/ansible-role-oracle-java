.. image:: https://travis-ci.org/peopledoc/ansible-role-oracle-java.svg?branch=master
    :target: https://travis-ci.org/peopledoc/ansible-role-oracle-java


Install oracle-java role for ansible.

## Tests

Tests can be executed using:

```
$ molecule --debug test --driver-name docker
```

The dependencies are `ansible`, `molecule` and `docker-py` Python packages.

Role Variables
--------------

CA certificates can be added to the java keystore with the following variables::

  ca-certificates:
    certificates:
      - alias: cert
        path: /usr/local/share/ca-certificates/cert.crt
      - url: google.com
    password: changeit

Java Cryptography Extension can be installed with the ``install_cryptography_extension`` boolean variable.

Bouncycastle libs can be added with the ``add_bouncycastle`` boolean variable.
