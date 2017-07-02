#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	JSON
%define		pnam	MaybeXS
%include	/usr/lib/rpm/macros.perl
Summary:	JSON::MaybeXS - Use Cpanel::JSON::XS with a fallback to JSON::XS and JSON::PP
Name:		perl-JSON-MaybeXS
Version:	1.003009
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/JSON/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3798c872e8988f6c903eca9f26c917d9
URL:		http://search.cpan.org/dist/JSON-MaybeXS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module first checks to see if either Cpanel::JSON::XS or JSON::XS
is already loaded, in which case it uses that module. Otherwise it
tries to load Cpanel::JSON::XS, then JSON::XS, then JSON::PP in order,
and either uses the first module it finds or throws an error.

It then exports the encode_json and decode_json functions from the
loaded module, along with a JSON constant that returns the class name
for calling new on.

If you're writing fresh code rather than replacing JSON.pm usage, you
might want to pass options as constructor args rather than calling
mutators, so we provide our own new method that supports that.

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
%{perl_vendorlib}/JSON/*.pm
%{_mandir}/man3/*
