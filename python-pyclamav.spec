Summary:	A Python interface to libclamav
Summary(pl):	Interfejs Pythona do libclamav
Name:		python-pyclamav
Version:	0.2.2
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://norman.free.fr/norman/python/pyclamav/pyclamav-%{version}.tar.gz
# Source0-md5:	0b274b73f71b8e4481c8fb30fd1c2bb2
URL:		http://xael.org/norman/python/pyclamav/index.html
BuildRequires:  clamav-devel >= 0:0.80
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.4
Requires:       clamav >= 0:0.80
Requires:	python
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python interface to libclamav.

%description -l pl
Interfejs Pythona do libclamav.

%prep
%setup -q -n pyclamav-%{version}

%build
env CFLAGS="%{rpmcflags}" %{_bindir}/python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{py_sitedir}/*.so
##%{py_sitedir}/*.py[co]
