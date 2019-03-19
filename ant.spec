Name:             internal-ant
Version:          1.9.13
Release:          1%{?dist}
Summary:          Apache Ant is a Java library and command-line tool whose mission is to drive processes described in build files as targets and extension points dependent upon each other.
License:          Apache License v2
URL:              https://ant.apache.org/
Source0:          http://mirror.ibcp.fr/pub/apache/ant/binaries/apache-ant-%{version}-bin.tar.gz
BuildArch:        noarch
BuildRoot:        %{_tmppath}/%{name}-%{version}-buildroot
Requires:         internal-oracle-jdk >= 1.8.131
Requires(post):   /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

# sysroot's configuration
#------------------------
%define _prefix         /opt/internal/root/opt
%define _exec_prefix    %{_prefix}
%define _antdir         %{_prefix}/ant
%define _sysconfdir     %{_antdir}/etc
%define _bindir         %{_antdir}/bin
%define _libdir         %{_antdir}/lib
%define _profiledir     /etc/profile.d
#------------------------

%description
Apache Ant is a Java library and command-line tool whose mission is to drive
processes described in build files as targets and extension points dependent
upon each other. The main known usage of Ant is the build of Java applications.
Ant supplies a number of built-in tasks allowing to compile, assemble, test
and run Java applications. Ant can also be used effectively to build non Java
applications, for instance C or C++ applications. More generally, Ant can be
used to pilot any type of process which can be described in terms of targets
and tasks.

%prep
%setup -qn apache-ant-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_antdir}
# Clean the source archive
rm patch.xml get-m2.xml fetch.xml contributors.xml
rm WHATSNEW
rm README
rm NOTICE
rm LICENSE
rm KEYS
rm INSTALL
rm CONTRIBUTORS
rm -r manual
# Copy the files in the targeted prefix
cp -R . $RPM_BUILD_ROOT/%{_antdir}
# Create the application profile for environment configuration
mkdir -p $RPM_BUILD_ROOT/%{_profiledir}
cat <<EOF > $RPM_BUILD_ROOT/%{_profiledir}/%{name}.sh
export ANT_HOME=%{_antdir}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/update-alternatives --install /usr/bin/ant ant %{_bindir}/ant 0

%postun
if [ $1 -eq 0 ] ; then
  /usr/sbin/update-alternatives --remove ant %{_bindir}/ant
fi

%files
%defattr (-,root,root)

# Files to include
%{_profiledir}/%{name}.sh
%{_bindir}/ant
%{_bindir}/ant.bat
%{_bindir}/ant.cmd
%{_bindir}/antRun
%{_bindir}/antRun.bat
%{_bindir}/antRun.pl
%{_bindir}/antenv.cmd
%{_bindir}/complete-ant-cmd.pl
%{_bindir}/envset.cmd
%{_bindir}/lcp.bat
%{_bindir}/runant.pl
%{_bindir}/runant.py
%{_bindir}/runrc.cmd
%{_sysconfdir}/ant-bootstrap.jar
%{_sysconfdir}/changelog.xsl
%{_sysconfdir}/checkstyle/checkstyle-frames-sortby-check.xsl
%{_sysconfdir}/checkstyle/checkstyle-frames.xsl
%{_sysconfdir}/checkstyle/checkstyle-text.xsl
%{_sysconfdir}/checkstyle/checkstyle-xdoc.xsl
%{_sysconfdir}/coverage-frames.xsl
%{_sysconfdir}/jdepend-frames.xsl
%{_sysconfdir}/jdepend.xsl
%{_sysconfdir}/junit-frames-xalan1.xsl
%{_sysconfdir}/junit-frames.xsl
%{_sysconfdir}/junit-noframes.xsl
%{_sysconfdir}/log.xsl
%{_sysconfdir}/maudit-frames.xsl
%{_sysconfdir}/mmetrics-frames.xsl
%{_sysconfdir}/tagdiff.xsl
%{_libdir}/ant-antlr.jar
%{_libdir}/ant-antlr.pom
%{_libdir}/ant-apache-bcel.jar
%{_libdir}/ant-apache-bcel.pom
%{_libdir}/ant-apache-bsf.jar
%{_libdir}/ant-apache-bsf.pom
%{_libdir}/ant-apache-log4j.jar
%{_libdir}/ant-apache-log4j.pom
%{_libdir}/ant-apache-oro.jar
%{_libdir}/ant-apache-oro.pom
%{_libdir}/ant-apache-regexp.jar
%{_libdir}/ant-apache-regexp.pom
%{_libdir}/ant-apache-resolver.jar
%{_libdir}/ant-apache-resolver.pom
%{_libdir}/ant-apache-xalan2.jar
%{_libdir}/ant-apache-xalan2.pom
%{_libdir}/ant-commons-logging.jar
%{_libdir}/ant-commons-logging.pom
%{_libdir}/ant-commons-net.jar
%{_libdir}/ant-commons-net.pom
%{_libdir}/ant-jai.jar
%{_libdir}/ant-jai.pom
%{_libdir}/ant-javamail.jar
%{_libdir}/ant-javamail.pom
%{_libdir}/ant-jdepend.jar
%{_libdir}/ant-jdepend.pom
%{_libdir}/ant-jmf.jar
%{_libdir}/ant-jmf.pom
%{_libdir}/ant-jsch.jar
%{_libdir}/ant-jsch.pom
%{_libdir}/ant-junit.jar
%{_libdir}/ant-junit.pom
%{_libdir}/ant-junit4.jar
%{_libdir}/ant-junit4.pom
%{_libdir}/ant-launcher.jar
%{_libdir}/ant-launcher.pom
%{_libdir}/ant-netrexx.jar
%{_libdir}/ant-netrexx.pom
%{_libdir}/ant-parent.pom
%{_libdir}/ant-swing.jar
%{_libdir}/ant-swing.pom
%{_libdir}/ant-testutil.jar
%{_libdir}/ant-testutil.pom
%{_libdir}/ant.jar
%{_libdir}/ant.pom
%{_libdir}/libraries.properties

# Files to exclude
%exclude %{_libdir}/README

# Directories owned by this RPM
%dir %{_antdir}
%dir %{_sysconfdir}
%dir %{_sysconfdir}/checkstyle
%dir %{_bindir}
%dir %{_libdir}

%changelog
* Thu Jan 17 2019 Antoine Allard <antoine.allard@internal.com>
- Create the RPM

