# basic-rpm-create
Example of a basic rpm creation 

In this example, you need work from your $HOME directory.


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

