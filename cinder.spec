#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cinder
Version  : 7.0.1
Release  : 23
URL      : http://tarballs.openstack.org/cinder/cinder-7.0.1.tar.gz
Source0  : http://tarballs.openstack.org/cinder/cinder-7.0.1.tar.gz
Source1  : cinder.tmpfiles
Summary  : OpenStack Block Storage
Group    : Development/Tools
License  : Apache-2.0
Requires: cinder-bin
Requires: cinder-python
Requires: cinder-config
Requires: cinder-data
BuildRequires : Babel
BuildRequires : Jinja2
BuildRequires : Mako
BuildRequires : MarkupSafe
BuildRequires : MySQL-python
BuildRequires : Paste
BuildRequires : PasteDeploy
BuildRequires : PyYAML
BuildRequires : Pygments
BuildRequires : Routes
BuildRequires : SQLAlchemy
BuildRequires : Sphinx
BuildRequires : Tempita
BuildRequires : WebOb
BuildRequires : aioeventlet
BuildRequires : alembic
BuildRequires : amqp
BuildRequires : anyjson
BuildRequires : automaton
BuildRequires : cffi
BuildRequires : cliff
BuildRequires : cmd2
BuildRequires : coverage
BuildRequires : cryptography
BuildRequires : ddt
BuildRequires : decorator
BuildRequires : discover
BuildRequires : docutils
BuildRequires : ecdsa
BuildRequires : enum34
BuildRequires : eventlet
BuildRequires : extras
BuildRequires : fixtures
BuildRequires : flake8
BuildRequires : funcsigs
BuildRequires : futures
BuildRequires : greenlet
BuildRequires : hacking
BuildRequires : httplib2
BuildRequires : iso8601
BuildRequires : jsonpatch
BuildRequires : jsonpointer
BuildRequires : jsonschema
BuildRequires : keystonemiddleware
BuildRequires : kombu
BuildRequires : linecache2
BuildRequires : lxml
BuildRequires : mccabe
BuildRequires : mox
BuildRequires : mox3
BuildRequires : msgpack-python
BuildRequires : netaddr
BuildRequires : netifaces
BuildRequires : networkx
BuildRequires : ordereddict
BuildRequires : os-brick
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.db
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.middleware
BuildRequires : oslo.policy
BuildRequires : oslo.reports
BuildRequires : oslo.rootwrap
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : oslo.versionedobjects
BuildRequires : oslo.vmware
BuildRequires : oslosphinx
BuildRequires : oslotest
BuildRequires : osprofiler
BuildRequires : paramiko
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : posix_ipc
BuildRequires : prettytable
BuildRequires : psycopg2
BuildRequires : py-python
BuildRequires : pyOpenSSL
BuildRequires : pyasn1
BuildRequires : pycadf
BuildRequires : pycparser
BuildRequires : pycrypto
BuildRequires : pyflakes
BuildRequires : pyparsing
BuildRequires : pytest
BuildRequires : python-barbicanclient
BuildRequires : python-dev
BuildRequires : python-glanceclient
BuildRequires : python-keystoneclient
BuildRequires : python-mimeparse
BuildRequires : python-mock
BuildRequires : python-novaclient
BuildRequires : python-subunit
BuildRequires : python-swiftclient
BuildRequires : pytz
BuildRequires : repoze.lru
BuildRequires : requests
BuildRequires : retrying
BuildRequires : rtslib-fb
BuildRequires : setuptools
BuildRequires : simplejson
BuildRequires : six
BuildRequires : sqlalchemy-migrate
BuildRequires : sqlparse
BuildRequires : stevedore
BuildRequires : suds-jurko
BuildRequires : taskflow
BuildRequires : tempest-lib
BuildRequires : testrepository
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : tox
BuildRequires : traceback2
BuildRequires : trollius
BuildRequires : unittest2
BuildRequires : urllib3
BuildRequires : virtualenv
BuildRequires : warlock
Patch1: 0001-default-config.patch
Patch2: 0002-cinder-sudoers-entry.patch
Patch3: 0003-Add-cinder-s-tgt-config.patch
Patch4: 0004-move-rootwrap-location.patch
Patch5: 0005-Use-oslo-to-find-config-files.patch
Patch6: 0006-Set-default-syslog.patch

%description
This is a database migration repository.
More information at
http://code.google.com/p/sqlalchemy-migrate/

%package bin
Summary: bin components for the cinder package.
Group: Binaries
Requires: cinder-data
Requires: cinder-config

%description bin
bin components for the cinder package.


%package config
Summary: config components for the cinder package.
Group: Default

%description config
config components for the cinder package.


%package data
Summary: data components for the cinder package.
Group: Data

%description data
data components for the cinder package.


%package python
Summary: python components for the cinder package.
Group: Default
Requires: keystonemiddleware
Requires: netaddr
Requires: oslo.config
Requires: stevedore

%description python
python components for the cinder package.


%prep
%setup -q -n cinder-7.0.1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/cinder.conf
## make_install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/cinder
install -p -D -m 644 etc/cinder/*.conf %{buildroot}/usr/share/defaults/cinder/
install -p -D -m 644 etc/cinder/*.ini %{buildroot}/usr/share/defaults/cinder/
install -p -D -m 644 etc/cinder/*.json %{buildroot}/usr/share/defaults/cinder/
install -p -D -m 644 etc/cinder/cinder.conf.sample %{buildroot}/usr/share/defaults/cinder/cinder.conf
install -d -m 755 %{buildroot}/usr/share/cinder/rootwrap.d
mv %{buildroot}/usr/share/defaults/cinder/rootwrap.conf %{buildroot}/usr/share/cinder/
install -p -D -m 640 etc/cinder/rootwrap.d/*.filters %{buildroot}/usr/share/cinder/rootwrap.d/
install -d -m 750 %{buildroot}/usr/share/defaults/sudo/sudoers.d
install -p -D -m 440 etc/sudoers.d/cinder.sudoers %{buildroot}/usr/share/defaults/sudo/sudoers.d/cinder
install -d -m 750 %{buildroot}/usr/share/defaults/tgt/conf.d/
install -p -D -m 640 cinder.tgt %{buildroot}/usr/share/defaults/tgt/conf.d/cinder.conf
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cinder-all
/usr/bin/cinder-api
/usr/bin/cinder-backup
/usr/bin/cinder-manage
/usr/bin/cinder-rootwrap
/usr/bin/cinder-rtstool
/usr/bin/cinder-scheduler
/usr/bin/cinder-volume
/usr/bin/cinder-volume-usage-audit

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/cinder.conf

%files data
%defattr(-,root,root,-)
/usr/share/cinder/rootwrap.conf
/usr/share/cinder/rootwrap.d/volume.filters
/usr/share/defaults/cinder/api-httpd.conf
/usr/share/defaults/cinder/api-paste.ini
/usr/share/defaults/cinder/cinder.conf
/usr/share/defaults/cinder/logging_sample.conf
/usr/share/defaults/cinder/policy.json
/usr/share/defaults/sudo/sudoers.d/cinder
/usr/share/defaults/tgt/conf.d/cinder.conf

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
