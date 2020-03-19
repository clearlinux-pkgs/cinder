#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC43F0EE211DFED8 (infra-root@openstack.org)
#
Name     : cinder
Version  : 14.0.2
Release  : 54
URL      : http://tarballs.openstack.org/cinder/cinder-14.0.2.tar.gz
Source0  : http://tarballs.openstack.org/cinder/cinder-14.0.2.tar.gz
Source1  : cinder.tmpfiles
Source2  : http://tarballs.openstack.org/cinder/cinder-14.0.2.tar.gz.asc
Summary  : OpenStack Block Storage
Group    : Development/Tools
License  : Apache-2.0
Requires: cinder-bin = %{version}-%{release}
Requires: cinder-config = %{version}-%{release}
Requires: cinder-data = %{version}-%{release}
Requires: cinder-license = %{version}-%{release}
Requires: cinder-python = %{version}-%{release}
Requires: cinder-python3 = %{version}-%{release}
Requires: Paste
Requires: PasteDeploy
Requires: Routes
Requires: SQLAlchemy
Requires: WebOb
Requires: castellan
Requires: cryptography
Requires: cursive
Requires: decorator
Requires: defusedxml
Requires: eventlet
Requires: google-api-python-client
Requires: greenlet
Requires: httplib2
Requires: ipaddress
Requires: iso8601
Requires: jsonschema
Requires: keystoneauth1
Requires: keystonemiddleware
Requires: lxml
Requires: oauth2client
Requires: os-brick
Requires: os-win
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.context
Requires: oslo.db
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.middleware
Requires: oslo.policy
Requires: oslo.privsep
Requires: oslo.reports
Requires: oslo.rootwrap
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.upgradecheck
Requires: oslo.utils
Requires: oslo.versionedobjects
Requires: oslo.vmware
Requires: osprofiler
Requires: paramiko
Requires: pbr
Requires: psutil
Requires: pyparsing
Requires: python-barbicanclient
Requires: python-glanceclient
Requires: python-keystoneclient
Requires: python-novaclient
Requires: python-swiftclient
Requires: pytz
Requires: requests
Requires: retrying
Requires: rtslib-fb
Requires: six
Requires: sphinx-feature-classification
Requires: sqlalchemy-migrate
Requires: stevedore
Requires: suds-jurko
Requires: taskflow
Requires: tooz
BuildRequires : Paste
BuildRequires : PasteDeploy
BuildRequires : Routes
BuildRequires : SQLAlchemy
BuildRequires : WebOb
BuildRequires : buildreq-distutils3
BuildRequires : castellan
BuildRequires : cryptography
BuildRequires : cursive
BuildRequires : decorator
BuildRequires : defusedxml
BuildRequires : eventlet
BuildRequires : google-api-python-client
BuildRequires : greenlet
BuildRequires : httplib2
BuildRequires : ipaddress
BuildRequires : iso8601
BuildRequires : jsonschema
BuildRequires : keystoneauth1
BuildRequires : keystonemiddleware
BuildRequires : lxml
BuildRequires : oauth2client
BuildRequires : os-brick
BuildRequires : os-win
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.db
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.middleware
BuildRequires : oslo.policy
BuildRequires : oslo.privsep
BuildRequires : oslo.reports
BuildRequires : oslo.rootwrap
BuildRequires : oslo.serialization
BuildRequires : oslo.service
BuildRequires : oslo.upgradecheck
BuildRequires : oslo.utils
BuildRequires : oslo.versionedobjects
BuildRequires : oslo.vmware
BuildRequires : osprofiler
BuildRequires : paramiko
BuildRequires : pbr
BuildRequires : psutil
BuildRequires : pyparsing
BuildRequires : python-barbicanclient
BuildRequires : python-glanceclient
BuildRequires : python-keystoneclient
BuildRequires : python-novaclient
BuildRequires : python-swiftclient
BuildRequires : pytz
BuildRequires : requests
BuildRequires : retrying
BuildRequires : rtslib-fb
BuildRequires : six
BuildRequires : sphinx-feature-classification
BuildRequires : sqlalchemy-migrate
BuildRequires : stevedore
BuildRequires : suds-jurko
BuildRequires : taskflow
BuildRequires : tooz
Patch1: 0001-default-config.patch
Patch2: 0002-cinder-sudoers-entry.patch
Patch3: 0003-Add-cinder-s-tgt-config.patch
Patch4: 0004-move-rootwrap-location.patch
Patch5: 0005-Set-default-syslog-disable-logging-to-var-log.patch
Patch6: 0006-Unfreeze-jsonschema.patch

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the cinder package.
Group: Binaries
Requires: cinder-data = %{version}-%{release}
Requires: cinder-config = %{version}-%{release}
Requires: cinder-license = %{version}-%{release}

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


%package license
Summary: license components for the cinder package.
Group: Default

%description license
license components for the cinder package.


%package python
Summary: python components for the cinder package.
Group: Default
Requires: cinder-python3 = %{version}-%{release}

%description python
python components for the cinder package.


%package python3
Summary: python3 components for the cinder package.
Group: Default
Requires: python3-core
Provides: pypi(cinder)
Requires: pypi(castellan)
Requires: pypi(cryptography)
Requires: pypi(cursive)
Requires: pypi(decorator)
Requires: pypi(defusedxml)
Requires: pypi(eventlet)
Requires: pypi(google_api_python_client)
Requires: pypi(greenlet)
Requires: pypi(httplib2)
Requires: pypi(iso8601)
Requires: pypi(jsonschema)
Requires: pypi(keystoneauth1)
Requires: pypi(keystonemiddleware)
Requires: pypi(lxml)
Requires: pypi(oauth2client)
Requires: pypi(os_brick)
Requires: pypi(os_win)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.config)
Requires: pypi(oslo.context)
Requires: pypi(oslo.db)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.log)
Requires: pypi(oslo.messaging)
Requires: pypi(oslo.middleware)
Requires: pypi(oslo.policy)
Requires: pypi(oslo.privsep)
Requires: pypi(oslo.reports)
Requires: pypi(oslo.rootwrap)
Requires: pypi(oslo.serialization)
Requires: pypi(oslo.service)
Requires: pypi(oslo.upgradecheck)
Requires: pypi(oslo.utils)
Requires: pypi(oslo.versionedobjects)
Requires: pypi(oslo.vmware)
Requires: pypi(osprofiler)
Requires: pypi(paramiko)
Requires: pypi(paste)
Requires: pypi(pastedeploy)
Requires: pypi(pbr)
Requires: pypi(prettytable)
Requires: pypi(psutil)
Requires: pypi(pyparsing)
Requires: pypi(python_barbicanclient)
Requires: pypi(python_glanceclient)
Requires: pypi(python_keystoneclient)
Requires: pypi(python_novaclient)
Requires: pypi(python_swiftclient)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(retrying)
Requires: pypi(routes)
Requires: pypi(rtslib_fb)
Requires: pypi(six)
Requires: pypi(sqlalchemy)
Requires: pypi(sqlalchemy_migrate)
Requires: pypi(stevedore)
Requires: pypi(suds_jurko)
Requires: pypi(taskflow)
Requires: pypi(tooz)
Requires: pypi(webob)

%description python3
python3 components for the cinder package.


%prep
%setup -q -n cinder-14.0.2
cd %{_builddir}/cinder-14.0.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584642777
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cinder
cp %{_builddir}/cinder-14.0.2/LICENSE %{buildroot}/usr/share/package-licenses/cinder/294b43b2cec9919063be1a3b49e8722648424779
cp %{_builddir}/cinder-14.0.2/contrib/block-box/LICENSE %{buildroot}/usr/share/package-licenses/cinder/92170cdc034b2ff819323ff670d3b7266c8bffcd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/cinder.conf
## install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/cinder
mv %{buildroot}/usr/etc/cinder  %{buildroot}/usr/share/defaults/cinder

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

## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cinder-api
/usr/bin/cinder-backup
/usr/bin/cinder-manage
/usr/bin/cinder-rootwrap
/usr/bin/cinder-rtstool
/usr/bin/cinder-scheduler
/usr/bin/cinder-status
/usr/bin/cinder-volume
/usr/bin/cinder-volume-usage-audit
/usr/bin/cinder-wsgi

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
/usr/share/defaults/cinder/cinder/api-paste.ini
/usr/share/defaults/cinder/cinder/resource_filters.json
/usr/share/defaults/cinder/cinder/rootwrap.conf
/usr/share/defaults/cinder/cinder/rootwrap.d/volume.filters
/usr/share/defaults/cinder/logging_sample.conf
/usr/share/defaults/cinder/resource_filters.json
/usr/share/defaults/sudo/sudoers.d/cinder
/usr/share/defaults/tgt/conf.d/cinder.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cinder/294b43b2cec9919063be1a3b49e8722648424779
/usr/share/package-licenses/cinder/92170cdc034b2ff819323ff670d3b7266c8bffcd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
