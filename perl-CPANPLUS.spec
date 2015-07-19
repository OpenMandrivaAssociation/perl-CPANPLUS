%define	modname	CPANPLUS
%define modver 0.9152

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Your::Module::Here\\)'
%else
%define _requires_exceptions perl(Your::Module::Here)
%endif

Summary:	API & CLI access to the CPAN mirrors
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/%{modname}/%{modname}-%{modver}.tar.gz
BuildArch:	noarch

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Extract) >=  0.160.0
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(File::Fetch) >= 0.160.0
BuildRequires:	perl(IO::Zlib)
BuildRequires:	perl(IPC::Cmd) >= 0.420.0
BuildRequires:	perl(Locale::Maketext::Simple) >= 0.10.0
BuildRequires:	perl(Log::Message) >= 0.10.0
BuildRequires:	perl(Log::Message::Simple)
BuildRequires:	perl(Module::CoreList) >= 2.90.0
BuildRequires:	perl(Module::Load) >= 0.100.0
BuildRequires:	perl(Module::Load::Conditional) >= 0.280.0
BuildRequires:	perl(Module::Loaded) >= 0.10.0
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Object::Accessor) >= 0.340.0
BuildRequires:	perl(Package::Constants) >= 0.10.0
BuildRequires:	perl(Params::Check) >= 0.220.0
BuildRequires:	perl(Parse::CPAN::Meta) >= 0.20.0
BuildRequires:	perl(Term::UI) >= 0.50.0
BuildRequires:	perl(Test::Harness) >= 2.620.0
BuildRequires:	perl(version)
# (misc) not detected automatically, needed by CPANPLUS/Module.pm line 450
Requires:	perl(Module::CoreList)
Requires:	perl(Module::Pluggable)
Requires:	perl(Module::Signature)
Requires:	perl(version)

%description
The CPANPLUS library is an API to the CPAN mirrors and a collection of
interactive shells, commandline programs, etc, that use this API.

%prep
%setup -qn %{modname}-%{modver}
# wants to write to the root fs
rm -f t/20_CPANPLUS-Dist-MM.t

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

# MD 20121223 man file conflicts with perl 5.16
# it's easier to remove here atm than in perl
rm -f %{buildroot}%{_mandir}/man1/cpanp.1*

%files
%doc README ChangeLog
%{_bindir}/cpan2dist
%{_bindir}/cpanp
%{_bindir}/cpanp-run-perl
%{perl_vendorlib}/CPANPLUS*
%{_mandir}/man1/*
%{_mandir}/man3/*
