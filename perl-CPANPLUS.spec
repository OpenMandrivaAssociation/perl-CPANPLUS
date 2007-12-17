%define	module	CPANPLUS
%define name	perl-%{module}
%define	modprefix CPANPLUS

%define version 0.82

%define	rel	2
%define release %mkrel %{rel}
%define _requires_exceptions perl(Your::Module::Here)

Summary:	API & CLI access to the CPAN mirrors
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
Source1:    bash-completion
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildArch:	noarch
BuildRequires:	perl(Archive::Extract) >=  0.16
BuildRequires: perl(Crypt::OpenPGP)
BuildRequires: perl(File::Fetch) >= 0.08
BuildRequires: perl(IPC::Cmd) >= 0.36
BuildRequires: perl(Locale::Maketext::Simple) >= 0.01
BuildRequires: perl(Log::Message) >= 0.01
BuildRequires: perl(Module::CoreList) >= 2.09
BuildRequires: perl(Module::Load) >= 0.10
BuildRequires: perl(Module::Load::Conditional) >= 0.16
BuildRequires: perl(Module::Loaded) >= 0.01
BuildRequires: perl(Object::Accessor) >= 0.32
BuildRequires: perl(Package::Constants) >= 0.01
BuildRequires: perl(Params::Check) >= 0.22
BuildRequires: perl(Term::UI) >= 0.05
BuildRequires: perl(Test::Harness) >= 2.62
BuildRequires: perl-version >= 0.70
BuildRequires: perl(Archive::Tar)
BuildRequires: perl(IO::Zlib)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Log::Message::Simple)

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

# bash completion
install -m 755 -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/bash_completion.d/cpan2dist

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/bash_completion.d/cpan2dist
%{_bindir}/cpan2dist
%{_bindir}/cpanp
%{_bindir}/cpanp-run-perl
%doc README ChangeLog
%{perl_vendorlib}/%{modprefix}*
%{_mandir}/*/*
