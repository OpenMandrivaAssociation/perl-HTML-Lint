%define upstream_name	 HTML-Lint
%define upstream_version 2.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Module to check for HTML errors
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Tagset)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This Perl module is used to check for HTML errors in strings or files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
