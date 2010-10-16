%define upstream_name    File-Path-Tiny
%define upstream_version 0.1

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Recursive versions of mkdir() and rmdir() without as much overhead as File::Path
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


