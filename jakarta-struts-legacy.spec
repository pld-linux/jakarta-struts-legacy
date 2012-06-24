Summary:	struts-legacy - classes removed from the core Struts distribution
Summary(pl):	struts-legacy - klasy usuni�te z g��wnej dystrybucji Struts
Name:		jakarta-struts-legacy
Version:	1.0
Release:	0.1
License:	Apache License
Source0:	http://www.apache.org/dist/jakarta/struts/struts-legacy/struts-legacy-%{version}-src.tar.gz
# Source0-md5:	805b7f3e787c1469f57fed9f5eebc3a1
Group:		Development/Languages/Java
URL:		http://jakarta.apache.org/struts/
BuildRequires:	jakarta-ant >= 1.6
BuildRequires:	servlet
BuildRequires:	jdbc-stdext >= 2.0-2
BuildRequires:	jakarta-commons-beanutils
BuildRequires:	jakarta-commons-collections
Requires:	servlet
Requires:	jdbc-stdext >= 2.0
Requires:	jakarta-commons-beanutils
Requires:	jakarta-commons-collections
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The struts-legacy distribution contains classes which have been
removed from the core Struts distribution but may still be of
interest. These classes are considered "stable" but are *not* actively
maintained (hence, the name "legacy").

%description -l pl
Pakiet struts-legacy zawiera klasy, kt�re zosta�y usuni�te z g��wnej
dystrybucji Struts, ale mog� nadal by� interesuj�ce. Klasy te s�
uznane za "stabilne", ale *nie* s� aktywnie utrzymywane (st�d nazwa
"legacy").

%prep
%setup -q -n struts-legacy-%{version}-src

%build
ant -Dcommons-logging.jar=/usr/share/java/commons-logging.jar \
    -Djdk.version=1.4 \
    -Djdbc20ext.jar=/usr/share/java/jdbc-stdext.jar \
    dist

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp dist/*.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dist/docs/api dist/LICENSE.txt
%{_javadir}/*.jar
