# basic-rpm-create
Example of a basic rpm creation 



:one: 
```bash
#Clone this repo
git clone https://github.com/chanslor/basic-rpm-create.git
```

 :two:
```bash

cd basic-rpm-create
mkdir -p ./rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
TOPDIR=$(pwd)/rpmbuild
```

:three:
```bash
cd SPECS
rpmbuild -bb hello.spec
```

 Should have created rpm in  $HOME/basic-rpm-create/RPMS/

