# basic-rpm-create
Example of a basic rpm creation 



:one: 
```bash
#Clone this repo
git clone https://github.com/chanslor/basic-rpm-create.git
```

 :two:
```bash
cp .rpmmacros  $HOME
```

:three:
```bash
cd basic-rpm-create/SPECS
rpmbuild -bb hello.spec
```

 Should have created rpm in  $HOME/basic-rpm-create/RPMS/

