%ifnarch x86_64
%define skip_mem_check 1
%endif

Name:           libstoragemgmt
Version:        1.6.1
Release:        2%{?dist}
Summary:        Storage array management library
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://github.com/libstorage/libstoragemgmt
Source0:        https://github.com/libstorage/libstoragemgmt/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch1:         BZ_1524490_fix_megaraid_cache.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       %{name}-python
BuildRequires:  autoconf automake libtool yajl-devel libxml2-devel check-devel perl
BuildRequires:  openssl-devel
BuildRequires:  python-argparse
BuildRequires:  glib2-devel
BuildRequires:  systemd
BuildRequires:  bash-completion
BuildRequires:  libconfig-devel
BuildRequires:  systemd-devel
BuildRequires:  python-devel
BuildRequires:  procps
BuildRequires:  chrpath
BuildRequires:  python-six
BuildRequires:  sqlite-devel
%if 0%{?skip_mem_check} == 0
BuildRequires:  valgrind
%endif
BuildRequires:  python-pyudev
Requires: initscripts
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The libStorageMgmt library will provide a vendor agnostic open source storage
application programming interface (API) that will allow management of storage
arrays.  The library includes a command line interface for interactive use and
scripting (command lsmcli).  The library also has a daemon that is used for
executing plug-ins in a separate process (lsmd).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        python
Summary:        Python client libraries and plug-in support for %{name}
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-python-clibs
Requires:       python-six
BuildArch:      noarch

%description    python
The %{name}-python package contains python client libraries as
well as python framework support and open source plug-ins written in python.

%package        python-clibs
Summary:        Python C extension module for %{name}
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description    python-clibs
The %{name}-python-clibs package contains python client C extension
libraries.

%package        smis-plugin
Summary:        Files for SMI-S generic array support for %{name}
Group:          System Environment/Libraries
BuildRequires:  pywbem
Requires:       pywbem
Requires:       %{name}-python = %{version}-%{release}
Requires(post): %{name}-python = %{version}-%{release}
Requires(postun): %{name}-python = %{version}-%{release}
BuildArch:      noarch

%description    smis-plugin
The %{name}-smis-plugin package contains plug-in for generic SMI-S array
support.


%package        netapp-plugin
Summary:        Files for NetApp array support for %{name}
Group:          System Environment/Libraries
BuildRequires:  m2crypto
Requires:       m2crypto
Requires:       %{name}-python = %{version}-%{release}
Requires(post): %{name}-python = %{version}-%{release}
Requires(postun): %{name}-python = %{version}-%{release}
BuildArch:      noarch

%description    netapp-plugin
The %{name}-netapp-plugin package contains plug-in for NetApp array
support.


%package        targetd-plugin
Summary:        Files for targetd array support for %{name}
Group:          System Environment/Libraries
Requires:       %{name}-python = %{version}-%{release}
Requires(post): %{name}-python = %{version}-%{release}
Requires(postun): %{name}-python = %{version}-%{release}
BuildArch:      noarch

%description    targetd-plugin
The %{name}-targetd-plugin package contains plug-in for targetd array
support.


%package        nstor-plugin
Summary:        Files for NexentaStor array support for %{name}
Group:          System Environment/Libraries
Requires:       %{name}-python = %{version}-%{release}
Requires(post): %{name}-python = %{version}-%{release}
Requires(postun): %{name}-python = %{version}-%{release}
BuildArch:      noarch

%description    nstor-plugin
The %{name}-nstor-plugin package contains plug-in for NexentaStor array
support.

%package        megaraid-plugin
Summary:        Files for LSI MegaRAID support for %{name}
Group:          System Environment/Libraries
Requires:       %{name}-python = %{version}-%{release}
Requires(post): %{name}-python = %{version}-%{release}
Requires(postun): %{name}-python = %{version}-%{release}
BuildArch:      noarch

%description    megaraid-plugin
The %{name}-megaraid-plugin package contains the plugin for LSI
MegaRAID storage management via storcli.

%package        hpsa-plugin
Summary:        Files for HPE SmartArray support for %{name}
Group:          System Environment/Libraries
Requires:       python-pyudev
Requires:       %{name}-python = %{version}-%{release}
Requires(post): %{name}-python = %{version}-%{release}
Requires(postun): %{name}-python = %{version}-%{release}
BuildArch:      noarch

%description    hpsa-plugin
The %{name}-hpsa-plugin package contains the plugin for HPE
SmartArray storage management via hpssacli.

%package        udev
Summary:        Udev files for %{name}
Group:          System Environment/Base

%description    udev
The %{name}-udev package contains udev rules and helper utilities for
uevents generated by the kernel.

%package        arcconf-plugin
Summary:        Files for Microsemi Adaptec and Smart Family support for %{name}
Group:          System Environment/Libraries
Requires:       %{name}-python = %{version}-%{release}
Requires(post): %{name}-python = %{version}-%{release}
Requires(postun): %{name}-python = %{version}-%{release}
BuildArch:      noarch

%description    arcconf-plugin
The %{name}-arcconf-plugin package contains the plugin for Microsemi
Adaptec RAID and Smart Family Controller storage management.

%package        nfs-plugin
Summary:        Files for NFS local filesystem support for %{name}
Group:          System Environment/Libraries
Requires:       %{name}-python = %{version}-%{release}
Requires:       %{name}-nfs-plugin-clibs = %{version}-%{release}
Requires(post): %{name}-python = %{version}-%{release}
Requires(postun): %{name}-python = %{version}-%{release}
BuildArch:      noarch

%description    nfs-plugin
The nfs-plugin package contains plug-in for local NFS exports support.

%package        nfs-plugin-clibs
Summary:        Python C extension module for %{name} NFS plugin
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description    nfs-plugin-clibs
The %{name}-nfs-plugin-clibs package contains python C extension for %{name}
NFS plugin.

%package        local-plugin
Summary:        Files for local pseudo plugin of %{name}
Group:          System Environment/Libraries
Requires:       %{name}-python = %{version}-%{release}
Requires(post): %{name}-python = %{version}-%{release}
Requires(postun): %{name}-python = %{version}-%{release}
BuildArch:      noarch

%description    local-plugin
The nfs-plugin package contains plug-in for local NFS exports support.
LibstorageMgmt local plugin allows user to manage locally storage system
without caring which real plugin(s) should be used.

%prep
%setup -q
%patch1 -p1 -b .megaraid-cache

#Make sure you always have a build section, even when you don't
#need it, see: https://bugzilla.redhat.com/show_bug.cgi?id=192422
%build

#Tell the install program to preserve file date/timestamps
%configure --disable-static \
%if 0%{?skip_mem_check} == 1
    --without-mem-leak-test
%endif

V=1 make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

install -d -m 0755 %{buildroot}/%{_unitdir}
install -m 0644 packaging/daemon/libstoragemgmt.service \
    %{buildroot}/%{_unitdir}/libstoragemgmt.service

#tempfiles.d configuration for /var/run
mkdir -p %{buildroot}/%{_tmpfilesdir}
install -m 0644 packaging/daemon/lsm-tmpfiles.conf \
    %{buildroot}/%{_tmpfilesdir}/%{name}.conf

#Files for udev handling
mkdir -p %{buildroot}/%{_udevrulesdir}
install -m 0644 tools/udev/90-scsi-ua.rules \
    %{buildroot}/%{_udevrulesdir}/90-scsi-ua.rules
install -m 0755 tools/udev/scan-scsi-target \
    %{buildroot}/%{_udevrulesdir}/../scan-scsi-target

%clean
rm -rf %{buildroot}

%check
if ! make check
then
  cat ./test-suite.log || true
  exit 1
fi

%pre
getent group libstoragemgmt >/dev/null || groupadd -r libstoragemgmt
getent passwd libstoragemgmt >/dev/null || \
    useradd -r -g libstoragemgmt -d /var/run/lsm -s /sbin/nologin \
    -c "daemon account for libstoragemgmt" libstoragemgmt

%post
/sbin/ldconfig
# Create tmp socket folders.
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%systemd_post libstoragemgmt.service

%preun
%systemd_preun libstoragemgmt.service

%postun
/sbin/ldconfig
%systemd_postun libstoragemgmt.service

# Need to restart lsmd if plugin is new installed or removed.
%post smis-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%postun smis-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%post netapp-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%postun netapp-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%post targetd-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%postun targetd-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%post nstor-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%postun nstor-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%post megaraid-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%postun megaraid-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%post hpsa-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%postun hpsa-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

# Need to restart lsmd if plugin is new installed or removed.
%post nfs-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart libstoragemgmt.service \
        >/dev/null 2>&1 || :
fi

%postun nfs-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart libstoragemgmt.service \
        >/dev/null 2>&1 || :
fi

# Need to restart lsmd if plugin is new installed or removed.
%post arcconf-plugin
if [ $1 -eq 1 ]; then
    # New install.
    /usr/bin/systemctl try-restart libstoragemgmt.service \
        >/dev/null 2>&1 || :
fi

%postun arcconf-plugin
if [ $1 -eq 0 ]; then
    # Remove
    /usr/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%doc README COPYING.LIB
%{_mandir}/man1/lsmcli.1*
%{_mandir}/man1/lsmd.1*
%{_mandir}/man5/lsmd.conf.5*
%{_libdir}/*.so.*
%{_bindir}/lsmcli
%{_datadir}/bash-completion/completions/lsmcli
%{_bindir}/lsmd
%{_bindir}/simc_lsmplugin
%dir %{_sysconfdir}/lsm
%dir %{_sysconfdir}/lsm/pluginconf.d
%config(noreplace) %{_sysconfdir}/lsm/lsmd.conf
%{_mandir}/man1/simc_lsmplugin.1*

%{_unitdir}/%{name}.service

%ghost %dir %attr(0755, -, -) /run/lsm/
%ghost %dir %attr(0755, -, -) /run/lsm/ipc

%attr(0644, root, root) %{_tmpfilesdir}/%{name}.conf

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/lsm_*
%{_mandir}/man3/libstoragemgmt*

%files python
%defattr(-,root,root,-)
#Python library files
%dir %{python_sitelib}/lsm
%{python_sitelib}/lsm/__init__.*
%dir %{python_sitelib}/lsm/external
%{python_sitelib}/lsm/external/*
%{python_sitelib}/lsm/_client.*
%{python_sitelib}/lsm/_common.*
%{python_sitelib}/lsm/_data.*
%{python_sitelib}/lsm/_iplugin.*
%{python_sitelib}/lsm/_pluginrunner.*
%{python_sitelib}/lsm/_transport.*
%{python_sitelib}/lsm/_local_disk.*
%{python_sitelib}/lsm/version.*
%dir %{python_sitelib}/lsm/plugin
%{python_sitelib}/lsm/plugin/__init__.*
%dir %{python_sitelib}/lsm/plugin/sim
%{python_sitelib}/lsm/plugin/sim/__init__.*
%{python_sitelib}/lsm/plugin/sim/simulator.*
%{python_sitelib}/lsm/plugin/sim/simarray.*
%dir %{python_sitelib}/lsm/lsmcli
%{python_sitelib}/lsm/lsmcli/__init__.*
%{python_sitelib}/lsm/lsmcli/data_display.*
%{python_sitelib}/lsm/lsmcli/cmdline.*
%{_bindir}/sim_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/sim.conf
%{_mandir}/man1/sim_lsmplugin.1*

# Compiled C files for python library
%files python-clibs
%{python_sitelib}/lsm/_clib.*

%files smis-plugin
%defattr(-,root,root,-)
%dir %{python_sitelib}/lsm/plugin/smispy
%{python_sitelib}/lsm/plugin/smispy/__init__.*
%{python_sitelib}/lsm/plugin/smispy/smis.*
%{python_sitelib}/lsm/plugin/smispy/dmtf.*
%{python_sitelib}/lsm/plugin/smispy/utils.*
%{python_sitelib}/lsm/plugin/smispy/smis_common.*
%{python_sitelib}/lsm/plugin/smispy/smis_cap.*
%{python_sitelib}/lsm/plugin/smispy/smis_sys.*
%{python_sitelib}/lsm/plugin/smispy/smis_pool.*
%{python_sitelib}/lsm/plugin/smispy/smis_disk.*
%{python_sitelib}/lsm/plugin/smispy/smis_vol.*
%{python_sitelib}/lsm/plugin/smispy/smis_ag.*
%{_bindir}/smispy_lsmplugin
%{_mandir}/man1/smispy_lsmplugin.1*

%files netapp-plugin
%defattr(-,root,root,-)
%dir %{python_sitelib}/lsm/plugin/ontap
%{python_sitelib}/lsm/plugin/ontap/__init__.*
%{python_sitelib}/lsm/plugin/ontap/na.*
%{python_sitelib}/lsm/plugin/ontap/ontap.*
%{_bindir}/ontap_lsmplugin
%{_mandir}/man1/ontap_lsmplugin.1*

%files targetd-plugin
%defattr(-,root,root,-)
%dir %{python_sitelib}/lsm/plugin/targetd
%{python_sitelib}/lsm/plugin/targetd/__init__.*
%{python_sitelib}/lsm/plugin/targetd/targetd.*
%{_bindir}/targetd_lsmplugin
%{_mandir}/man1/targetd_lsmplugin.1*

%files nstor-plugin
%defattr(-,root,root,-)
%dir %{python_sitelib}/lsm/plugin/nstor
%{python_sitelib}/lsm/plugin/nstor/__init__.*
%{python_sitelib}/lsm/plugin/nstor/nstor.*
%{_bindir}/nstor_lsmplugin
%{_mandir}/man1/nstor_lsmplugin.1*

%files udev
%defattr(-,root,root,-)
%{_udevrulesdir}/../scan-scsi-target
%{_udevrulesdir}/90-scsi-ua.rules

%files megaraid-plugin
%defattr(-,root,root,-)
%dir %{python_sitelib}/lsm/plugin/megaraid
%{python_sitelib}/lsm/plugin/megaraid/__init__.*
%{python_sitelib}/lsm/plugin/megaraid/megaraid.*
%{python_sitelib}/lsm/plugin/megaraid/utils.*
%{_bindir}/megaraid_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/megaraid.conf
%{_mandir}/man1/megaraid_lsmplugin.1*

%files hpsa-plugin
%defattr(-,root,root,-)
%dir %{python_sitelib}/lsm/plugin/hpsa
%{python_sitelib}/lsm/plugin/hpsa/__init__.*
%{python_sitelib}/lsm/plugin/hpsa/hpsa.*
%{python_sitelib}/lsm/plugin/hpsa/utils.*
%{_bindir}/hpsa_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/hpsa.conf
%{_mandir}/man1/hpsa_lsmplugin.1*

%files nfs-plugin
%defattr(-,root,root,-)
%dir %{python_sitelib}/lsm/plugin/nfs
%{python_sitelib}/lsm/plugin/nfs/__init__.*
%{python_sitelib}/lsm/plugin/nfs/nfs.*
%{_sysconfdir}/lsm/pluginconf.d/nfs.conf
%{_bindir}/nfs_lsmplugin
%{_mandir}/man1/nfs_lsmplugin.1*

%files nfs-plugin-clibs
%{python_sitelib}/lsm/plugin/nfs/nfs_clib.*

%files arcconf-plugin
%defattr(-,root,root,-)
%dir %{python_sitelib}/lsm/plugin/arcconf
%{python_sitelib}/lsm/plugin/arcconf/__init__.*
%{python_sitelib}/lsm/plugin/arcconf/arcconf.*
%{python_sitelib}/lsm/plugin/arcconf/utils.*
%{_bindir}/arcconf_lsmplugin
%config(noreplace) %{_sysconfdir}/lsm/pluginconf.d/arcconf.conf
%{_mandir}/man1/arcconf_lsmplugin.1*

%files local-plugin
%defattr(-,root,root,-)
%dir %{python_sitelib}/lsm/plugin/local
%{python_sitelib}/lsm/plugin/local/__init__.*
%{python_sitelib}/lsm/plugin/local/local.*
%{_sysconfdir}/lsm/pluginconf.d/local.conf
%{_bindir}/local_lsmplugin
%{_mandir}/man1/local_lsmplugin.1*

%changelog
* Tue Dec 12 2017 Gris Ge <fge@redhat.com> - 1.6.1-2
- Fix MegaRAID cache query and set. (RHBZ #1524490)

* Tue Oct 31 2017 Gris Ge <fge@redhat.com> - 1.6.1-1
- Upgrade to 1.6.1.

* Fri Oct 20 2017 Gris Ge <fge@redhat.com> - 1.6.0-2
- Fix missing pywbem import in SMI-S plugin

* Thu Oct 19 2017 Gris Ge <fge@redhat.com> - 1.6.0-1
- Upgrade to 1.6.0.

* Wed Oct 11 2017 Gris Ge <fge@redhat.com> - 1.5.0-2
- Fix multilib confliction of nfs-plugin by move binrary file to
  another subpackage libstoragemgmt-nfs-plugin-clibs

* Sat Sep 30 2017 Gris Ge <fge@redhat.com> - 1.5.0-1
- Upgraded to 1.5.0.

* Thu Mar 30 2017 Gris Ge <fge@redhat.com> 1.4.0-3
- Fix ONTAP SSL connection. # RHBZ 1437130

* Thu Feb 23 2017 Gris Ge <fge@redhat.com> 1.4.0-2
- Include a patch for incorrect use of sizeof in C library.

* Tue Feb 21 2017 Gris Ge <fge@redhat.com> 1.4.0-1
- Add Python3 support.
- New sub rpm package python3-libstoragemgmt.
- Add support of lmiwbem.
- Allow plugin test to be run concurrently.
- Bug fixes:
    * Fix megaraid plugin for dell PERC.
    * Fix local disk rotation speed query on NVMe disk.
    * Fix lsmcli incorrect try-expect on local disk query.
    * Fix all the gcc compile warnings.
    * Fix the obsolete usage of AC_OUTPUT in configure.ac.
- Library adds:
    * Query serial of local disk:
        lsm_local_disk_serial_num_get()/lsm.LocalDisk.serial_num_get()
    * Query LED status of local disk:
        lsm_local_disk_led_status_get()/lsm.LocalDisk.led_status_get()
    * Query link speed of local disk:
        lsm_local_disk_link_speed_get()/lsm.LocalDisk.link_speed_get()

* Wed Aug 03 2016 Gris Ge <fge@redhat.com> 1.3.4-1
- Upgrade to 1.3.4

* Wed Jul 13 2016 Gris Ge <fge@redhat.com> 1.3.2-7
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=1355637

* Wed Jun 22 2016 Gris Ge <fge@redhat.com> 1.3.2-6
- Apply the forgotten patch6.

* Wed Jun 22 2016 Gris Ge <fge@redhat.com> 1.3.2-5
- Fix compile warning by removing unused static function _sd_name_of().

* Tue Jun 21 2016 Gris Ge <fge@redhat.com> 1.3.2-4
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=1348394

* Tue Jun 21 2016 Gris Ge <fge@redhat.com> 1.3.2-3
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=1346898

* Fri Jun 17 2016 Gris Ge <fge@redhat.com> 1.3.2-2
- Fix https://bugzilla.redhat.com/show_bug.cgi?id=1346901

* Thu May 26 2016 Gris Ge <fge@redhat.com> 1.3.2-1
- New upstream release 1.3.2

* Tue Sep 8 2015 Tony Asleson <tasleson@redhat.com> 1.2.3-4
- Fix 'make check' when running as root
  https://bugzilla.redhat.com/show_bug.cgi?id=1260899

* Thu Jul 2 2015 Tony Asleson <tasleson@redhat.com> 1.2.3-3
- Megaraid fixes
  * https://bugzilla.redhat.com/show_bug.cgi?id=1238554
  * https://bugzilla.redhat.com/show_bug.cgi?id=1238582
  * https://bugzilla.redhat.com/show_bug.cgi?id=1238566
- Command line exit code fix:
  * https://bugzilla.redhat.com/show_bug.cgi?id=1238737

* Thu Jun 25 2015 Tony Asleson <tasleson@redhat.com> 1.2.3-2
- Be explicit in package version requirements
- Add build section back to get debug-infos

* Wed Jun 24 2015 Tony Asleson <tasleson@redhat.com> 1.2.3-1
- New upstream release
- New sub-pacakges:
    * libstoragemgmt-megaraid-plugin
    * libstoragemgmt-hpsa-plugin
- Add bash-completion script for lsmcli
- Replace the hardcoded udev path with %{_udevrulesdir}.
- Mark /run/lsm and /run/lsm/ipc as %ghost folder.
- Add 'Requires(post)' and 'Requires(postun)' to plugins in order
  to make sure plugin is installed after libstoragemgmt and removed before
  libstoragemgmt.

* Thu Dec 11 2014 Tony Asleson <tasleson@redhat.com> 1.1.0-2
- Remove PyYAML build dependency

* Thu Dec 4 2014 Tony Asleson <tasleson@redhat.com> 1.1.0-1
- New upstream release

* Mon Oct 6 2014 Tony Asleson  <tasleson@redhat.com> - 1.0.0-4
- Fix rpmdiff, error for path names
  https://bugzilla.redhat.com/show_bug.cgi?id=1149368
- Fix rpmdiff, multilib regressions
  https://bugzilla.redhat.com/show_bug.cgi?id=1149371

* Fri Oct 3 2014 Tony Asleson  <tasleson@redhat.com> - 1.0.0-3
- Use new systemd rpm macros
  https://bugzilla.redhat.com/show_bug.cgi?id=1149010
- Place config file in correct tmpfiles.d directory
  https://bugzilla.redhat.com/show_bug.cgi?id=1122087

* Mon Sep 8 2014 Tony Asleson  <tasleson@redhat.com> - 1.0.0-2
- Removed REST sub-package

* Sun Sep 7 2014 Tony Asleson <tasleson@redhat.com> - 1.0.0-1
- New upstream release

* Fri Feb 28 2014 Tony Asleson <tasleson@redhat.com> - 0.0.24-4
- https://bugzilla.redhat.com/show_bug.cgi?id=1071382

* Mon Feb 10 2014 Tony Asleson <tasleson@redhat.com> - 0.0.24-3
- Corrected coverity found bugs

* Thu Jan 30 2014 Tony Asleson <tasleson@redhat.com> - 0.0.24-2
- Missed patch to correct python paths

* Thu Jan 30 2014 Tony Asleson <tasleson@redhat.com> - 0.0.24-1
- New upstream release
- Patch nstor plugin for json instead of simple-json

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.0.22-10
- Mass rebuild 2014-01-24

* Fri Jan 3 2014 Ewan D. Milne <emilne@redhat.com> 0.0.22-9
- Fixed DEVPATH parsing in scan-scsi-target

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.0.22-7
- Mass rebuild 2013-12-27

* Mon Dec 2 2013 Tony Asleson <tasleson@redhat.com> 0.0.22-6
- https://bugzilla.redhat.com/show_bug.cgi?id=1019467

* Fri Nov 22 2013 Tony Asleson <tasleson@redhat.com> 0.0.22-5
- https://bugzilla.redhat.com/show_bug.cgi?id=1019320

* Mon Oct 14 2013 Tony Asleson <tasleson@redhat.com> 0.0.22-4
- https://bugzilla.redhat.com/show_bug.cgi?id=905465

* Fri Oct 4 2013 Tony Asleson <tasleson@redhat.com> 0.0.22-3
- https://bugzilla.redhat.com/show_bug.cgi?id=998898

* Tue Aug 13 2013 Tony Asleson <tasleson@redhat.com> 0.0.22-2
- BZ 987027
- BZ 990577
- BZ 968384
- New upstream release

* Tue Jul 16 2013 Tony Asleson <tasleson@redhat.com> 0.0.21-1
- New upstream release
- Put plug-ins in separate sub packages
- Don't include IBM plug-in on RHEL > 6, missing paramiko

* Tue May 28 2013 Tony Asleson <tasleson@redhat.com> - 0.0.20-1
- New upstream release
- Separate package for python libraries
- Make timestamps match on version.py in library
- Add python-paramiko requirement for IBM plug-in

* Mon Apr 22 2013 Tony Asleson <tasleson@redhat.com> 0.0.19-1
- New upstream release

* Fri Mar 8 2013 Tony Asleson <tasleson@redhat.com> 0.0.18-1
- New upstream release
- Corrected spec file for missing "fi" in postinstall

* Tue Jan 29 2013 Tony Asleson <tasleson@redhat.com> 0.0.16-1
- New upstream release

* Wed Oct 31 2012 Tony Asleson <tasleson@redhat.com> 0.0.14-1
- Initial RHEL Release
- Removed conditional checks for fedora as RHEL7 uses systemd

* Wed Oct 3 2012 Tony Asleson <tasleson@redhat.com> - 0.0.13-1
- New upstream release

* Tue Sep 18 2012 Tony Asleson <tasleson@redhat.com> - 0.0.12-1
- New upstream release

* Mon Aug 13 2012 Tony Asleson <tasleson@redhat.com> 0.0.11-1
- New upstream release

* Fri Jul 27 2012 Dan Horák <dan[at]danny.cz> - 0.0.9-3
- detect also non-x86 arches in Pegasus check

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Tony Asleson <tasleson@redhat.com> 0.0.9-1
- Initial checkin of lio plug-in
- System filtering via URI (smispy)
- Error code mapping (ontap)
- Fixed build so same build tarball is used for all binaries

* Mon Jun 4 2012 Tony Asleson <tasleson@redhat.com> 0.0.8-1
- Make building of SMI-S CPP plugin optional
- Add pkg-config file
- SMIS: Fix exception while retrieving Volumes
- SMIS: Fix exception while retrieving Volumes
- lsm: Add package imports
- Make Smis class available in lsm python package
- Add option to disable building C unit test
- Make simulator classes available in lsm python package
- Make ontap class available in lsm python package
- Changes to support building on Fedora 17 (v2)
- Spec. file updates from feedback from T. Callaway (spot)
- F17 linker symbol visibility correction
- Remove unneeded build dependencies and cleaned up some warnings
- C Updates, client C library feature parity with python

* Fri May 11 2012 Tony Asleson <tasleson@redhat.com> 0.0.7-1
- Bug fix for smi-s constants
- Display formatting improvements
- Added header option for lsmcli
- Improved version handling for builds
- Made terminology consistent
- Ability to list visibility for access groups and volumes
- Simulator plug-in fully supports all block operations
- Added support for multiple systems with a single plug-in instance

* Fri Apr 20 2012 Tony Asleson <tasleson@redhat.com> 0.0.6-1
- Documentation improvements (man & source code)
- Support for access groups
- Unified spec files Fedora/RHEL
- Package version auto generate
- Rpm target added to make
- Bug fix for missing optional property on volume retrieval (smispy plug-in)

* Fri Apr 6 2012 Tony Asleson <tasleson@redhat.com> 0.0.5-1
- Spec file clean-up improvements
- Async. operation added to lsmcli and ability to check on job status
- Sub volume replication support
- Ability to check for child dependencies on VOLUMES, FS and files
- SMI-S Bug fixes and improvements

* Mon Mar 26 2012 Tony Asleson <tasleson@redhat.com> 0.0.4-1
- Restore from snapshot
- Job identifiers string instead of integer
- Updated license address

* Wed Mar 14 2012 Tony Asleson <tasleson@redhat.com> 0.0.3-1
- Changes to installer, daemon uid, gid, /var/run/lsm/*
- NFS improvements and bug fixes
- Python library clean up (rpmlint errors)

* Sun Mar 11 2012 Tony Asleson <tasleson@redhat.com> 0.0.2-1
- Added NetApp native plugin

* Mon Feb 6 2012 Tony Asleson <tasleson@redhat.com>  0.0.1alpha-1
- Initial version of package
