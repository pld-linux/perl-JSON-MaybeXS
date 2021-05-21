#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	JSON
%define		pnam	MaybeXS
Summary:	JSON::MaybeXS - Use Cpanel::JSON::XS with a fallback to JSON::XS and JSON::PP
Summary(pl.UTF-8):	JSON::MaybeXS - używanie Cpanel::JSON::XS, a w przypadku braku JSON::XS lub JSON::PP
Name:		perl-JSON-MaybeXS
Version:	1.004003
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/JSON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e46181e34588428d317932744597a7ab
URL:		https://metacpan.org/release/JSON-MaybeXS
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-JSON-PP >= 2.27300
BuildRequires:	perl-JSON-XS >= 3.0
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Needs >= 0.002006
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
# not packaged yet
#Suggests:	perl-Cpanel-JSON-XS >= 2.3310
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module first checks to see if either Cpanel::JSON::XS or JSON::XS
is already loaded, in which case it uses that module. Otherwise it
tries to load Cpanel::JSON::XS, then JSON::XS, then JSON::PP in order,
and either uses the first module it finds or throws an error.

%description -l pl.UTF-8
Ten moduł najpierw sprawdza, czy moduł Cpanel::JSON::XS lub JSON::XS
jest już załadowany, wtedy używa tego modułu. W przeciwnym wypadku
próbuje załadować po kolei Cpanel::JSON::XS, JSON::XS oraz JSON::PP i
używa pierwszego znalezionego modułu lub rzuca błąd.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/JSON/MaybeXS.pm
%{_mandir}/man3/JSON::MaybeXS.3pm*
