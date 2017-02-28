Name:		hello-world
Version:	1
Release:	2%{?dist}
Summary:	RPM HELLO WORLD TEST
Group:		TEST
License:	GPL+ or Artistic

#This hello script is placed in ~/rpmbuild/SOURCES/
Source0:	hello

%define _topdir %(echo $PWD)/

%description
SShow how easy creating an rpm can be for a simple script.

%install
install -D -m755 %{SOURCE0} %{buildroot}/usr/bin/hello

%files
%defattr(-,patchtool,patchtool)
/usr/bin/hello

%changelog
* Sun Apr 17 2016 michael.chanslor@gmail.com - 1-2
- Initial Creation of the spec file.


