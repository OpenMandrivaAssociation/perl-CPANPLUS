%define	module	CPANPLUS
%define name	perl-%{module}
%define	modprefix CPANPLUS

%define version 0.78

%define	rel	1
%define release %mkrel %{rel}
%define _requires_exceptions perl(Your::Module::Here)

Summary:	API & CLI access to the CPAN mirrors
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root
BuildRequires:	perl(Archive::Extract) >=  0.16 perl(Crypt::OpenPGP) perl(File::Fetch) >= 0.08 perl(IPC::Cmd) >= 0.36 perl(Locale::Maketext::Simple) >= 0.01 perl(Log::Message) >= 0.01 perl(Module::CoreList) >= 2.09 perl(Module::Load) >= 0.10 perl(Module::Load::Conditional) >= 0.16 perl(Module::Loaded) >= 0.01 perl(Object::Accessor) >= 0.32 perl(Package::Constants) >= 0.01 perl(Params::Check) >= 0.22 perl(Term::UI) >= 0.05 perl(Test::Harness) >= 2.62 perl-version >= 0.70

%description
The CPANPLUS library is an API to the CPAN mirrors and a collection of
interactive shells, commandline programs, etc, that use this API.

%prep
%setup -q -n %{module}-%{version}
# wants to write to the root fs
rm -f t/20_CPANPLUS-Dist-MM.t

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/cpan2dist
%{_bindir}/cpanp
%{_bindir}/cpanp-run-perl
%doc README ChangeLog
%{perl_vendorlib}/%{modprefix}*
%{_mandir}/*/*
