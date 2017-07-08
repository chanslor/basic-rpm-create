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
```

:three:
```bash
rpmbuild --define "_topdir ${PWD}/" -bb SPECS/hello.spec
```

 Should have created rpm in  $HOME/basic-rpm-create/RPMS/

