#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Quantum
%define	pnam	Entanglement
Summary:	Quantum::Entanglement - QM entanglement of variables in Perl
Summary(pl):	Quantum::Entanglement - zawik�anie zmiennych mechaniki kwantowej w Perlu
Name:		perl-Quantum-Entanglement
Version:	0.32
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl(Math::Complex)
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Essentially, this allows you to put variables into a superposition of
states, have them interact with each other (so that all states
interact) and then observe them (testing to see if they satisfy some
comparison operator, printing them) which will collapse the entire
system so that it is consistent with your knowledge.

%description -l pl
Zasadniczo ten modu� pozwala na umieszczanie zmiennych w superpozycji
stan�w, pozwalanie im na oddzia�ywanie na siebie (tak, �e wszystkie
stany oddzia�ywuj� ze sob�) i obserwowanie ich (sprawdzanie, czy s�
zgodne z pewnym operatorem por�wnania, wypisywanie ich), kt�ra za�amie
ca�y system, kt�ry jest sp�jny wedle naszej wiedzy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
