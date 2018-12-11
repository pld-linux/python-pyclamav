# TODO
# - R: clamav? library requiring daemon???
Summary:	A Python interface to libclamav
Summary(pl.UTF-8):	Interfejs Pythona do libclamav
Name:		python-pyclamav
Version:	0.4.1
Release:	15
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://norman.free.fr/norman/python/pyclamav/pyclamav-%{version}.tar.gz
# Source0-md5:	9e1f29ea118bac87223ff4df3c077556
Patch0:		%{name}-new-api.patch
URL:		http://xael.org/norman/python/pyclamav/index.html
BuildRequires:	clamav-devel >= 0.95
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.4
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-modules >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	clamav >= 0.95
Requires:	python
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python interface to libclamav.

%description -l pl.UTF-8
Interfejs Pythona do libclamav.

%prep
%setup -q -n pyclamav-%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags} $(pkg-config --cflags libclamav)"
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

cp -a example.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGELOG
%attr(755,root,root) %{py_sitedir}/pyclamav.so
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/example.py
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pyclamav-%{version}-py*.egg-info
%endif
