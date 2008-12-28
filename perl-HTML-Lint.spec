%define module	HTML-Lint
%define name	perl-%{module}
%define version 2.06
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Module to check for HTML errors
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This Perl module is used to check for HTML errors in strings or files.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/HTML
%{perl_vendorlib}/Test
%{_mandir}/*/*
%{_bindir}/*

