# rpm-internal-ant

Build a RPM package for the **internal-ant** project.

## RPM build

```
$ docker run --rm -it --volume $(pwd):/specs --volume $(pwd):/output localhost:5000/aallrd/internal-build-rpm --build
[INFO] [14:32:47] RPM spec file: ant.spec
[...]
[SUCCESS] [10:25:08] Binary RPM file(s):
[SUCCESS] [10:25:08] * /root/rpmbuild/RPMS/noarch/internal-ant-1.9.13-1.el6.noarch.rpm
[SUCCESS] [10:25:08] Source RPM file(s):
[SUCCESS] [10:25:08] * /root/rpmbuild/SRPMS/internal-ant-1.9.13-1.el6.src.rpm
```

## RPM installation

### Using YUM

```
# Configure the vendor repo on the server
$ cat <<EOF >> /etc/yum.repos.d/vendors.repo

[vendor-internal]
name=internal
baseurl=http://localhost:4000/vendors/internal
enabled=1
gpgcheck=0
proxy=_none_
EOF

# Install the package using Yum
$ yum install -y --disablerepo=* --enablerepo=internal internal-ant
```

### Using RPM

```
$ wget http://localhost:4000/vendors/internal/internal-ant-1.9.13-1.el6.noarch.rpm
$ rpm -ivh internal-ant-1.9.13-1.el6.noarch.rpm
Preparing...    ########################################### [100%]
   1:internal-ant  ########################################### [100%]
```

## Usage

```
$ ant -version
Apache Ant(TM) version 1.9.13 compiled on July 10 2018
```

