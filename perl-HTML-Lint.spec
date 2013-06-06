%define upstream_name	 HTML-Lint
%define upstream_version 2.20
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.20
Release:	1

Summary:	Module to check for HTML errors
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/HTML/HTML-Lint-2.20.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTML::Tagset)
BuildArch:	noarch

%description
This Perl module is used to check for HTML errors in strings or files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/HTML
%{perl_vendorlib}/Test
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.60.0-1mdv2010.0
+ Revision: 403256
- rebuild using %%perl_convert_version

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.06-1mdv2009.1
+ Revision: 320434
- update to new version 2.06

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.04-2mdv2009.0
+ Revision: 268521
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-1mdv2009.0
+ Revision: 214527
- update to new version 2.04

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-2mdv2008.0
+ Revision: 86471
- rebuild


* Mon Jun 19 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.02-1mdv2007.0
- First Mandriva release


