# TODO
# - R: clamav? library requiring daemon???
Summary:	A Python interface to libclamav
Summary(pl.UTF-8):	Interfejs Pythona do libclamav
Name:		python-pyclamav
Version:	0.4.1
Release:	5
License:	GPL
Group:		Libraries/Python
Source0:	http://norman.free.fr/norman/python/pyclamav/pyclamav-%{version}.tar.gz
# Source0-md5:	9e1f29ea118bac87223ff4df3c077556
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

%description -l pl.UTF-8
Interfejs Pythona do libclamav.

%prep
%setup -q -n pyclamav-%{version}

%build
env CFLAGS="%{rpmcflags}" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__python} -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

cp -a example.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGELOG
%attr(755,root,root) %{py_sitedir}/*.so
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/example.py
%if "%{py_ver}" > "2.4"
%{py_sitedir}/*.egg-info
%endif
