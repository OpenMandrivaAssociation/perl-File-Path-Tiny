%define upstream_name    File-Path-Tiny
%define upstream_version 0.7

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Recursive versions of mkdir() and rmdir() without File::Path overhead
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/File-Path-Tiny-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
The goal here is simply to provide recursive versions of the mkdir
manpage() and the rmdir manpage() with as little code and overhead as
possible.

This module is in no way meant to derogate the File::Path manpage and is in
no way an endorsement to go out and replace all use of the File::Path
manpage with the File::Path::Tiny manpage.

the File::Path manpage is very good at what it does but there's simply a
lot happening that we can do without much of the time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 654325
- rebuild for updated spec-helper

* Sat Oct 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 586064
- import perl-File-Path-Tiny


