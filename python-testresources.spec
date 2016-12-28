#
# Conditional build:
%bcond_without	tests	# make check [note: testBasicSortTests sometimes fails, non-deterministically]
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Testresources - pyunit extension for managing expensive test resources
Summary(pl.UTF-8):	Testresources - rozszerzenie pyunit do zarządzania kosztownymi zasobami dla testów
Name:		python-testresources
Version:	1.0.0
Release:	2
License:	Apache v2.0 or BSD
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/testresources/
Source0:	https://pypi.python.org/packages/source/t/testresources/testresources-%{version}.tar.gz
# Source0-md5:	32baee3f93d237192addc061646057b9
Patch0:		%{name}-tests.patch
URL:		https://launchpad.net/testresources
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-docutils
BuildRequires:	python-fixtures
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-pbr >= 1.3
BuildRequires:	python-setuptools
BuildRequires:	python-testtools
%endif
%if %{with python3}
BuildRequires:	python3-docutils
BuildRequires:	python3-fixtures
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-pbr >= 1.3
BuildRequires:	python3-setuptools
BuildRequires:	python3-testtools
%endif
Requires:	python-fixtures
Requires:	python-modules >= 1:2.5
Requires:	python-testtools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
testresources extends unittest with a clean and simple API to provide
test optimisation where expensive common resources are needed for test
cases - for example sample working trees for VCS systems, reference
databases for enterprise applications, or web servers.

%description -l pl.UTF-8
Moduł testresources rozszerza moduł unittest o czyste i proste API
pozwalające na optymalizację testów w przypadku, kiedy przypadki
testowe wymagają kosztownych wspólnych zasobów - np. przykładowych
drzew roboczych dla systemów kontroli wersji, wzorcowe bazy danych dla
aplikacji biznesowych albo serwerów WWW.

%package -n python3-testresources
Summary:	Testresources - pyunit extension for managing expensive test resources
Summary(pl.UTF-8):	Testresources - rozszerzenie pyunit do zarządzania kosztownymi zasobami dla testów
Group:		Libraries/Python
Requires:	python3-fixtures
Requires:	python3-modules >= 1:3.2
Requires:	python3-testtools

%description -n python3-testresources
testresources extends unittest with a clean and simple API to provide
test optimisation where expensive common resources are needed for test
cases - for example sample working trees for VCS systems, reference
databases for enterprise applications, or web servers.

%description -n python3-testresources -l pl.UTF-8
Moduł testresources rozszerza moduł unittest o czyste i proste API
pozwalające na optymalizację testów w przypadku, kiedy przypadki
testowe wymagają kosztownych wspólnych zasobów - np. przykładowych
drzew roboczych dla systemów kontroli wersji, wzorcowe bazy danych dla
aplikacji biznesowych albo serwerów WWW.

%prep
%setup -q -n testresources-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%{?with_tests:%{__make} check PYTHON=%{__python}}
%endif

%if %{with python3}
%py3_build

%{?with_tests:%{__make} check PYTHON=%{__python3}}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/testresources/tests
%endif

%if %{with python3}
%py3_install
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/testresources/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING ChangeLog GOALS NEWS README TODO
%{py_sitescriptdir}/testresources
%{py_sitescriptdir}/testresources-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-testresources
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING ChangeLog GOALS NEWS README TODO
%{py3_sitescriptdir}/testresources
%{py3_sitescriptdir}/testresources-%{version}-py*.egg-info
%endif
