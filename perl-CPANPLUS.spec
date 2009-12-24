%define	upstream_name	 CPANPLUS
%define upstream_version 0.9001

%define _requires_exceptions perl(Your::Module::Here)

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	API & CLI access to the CPAN mirrors
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CPANPLUS/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildArch:	noarch
BuildRequires:	perl(Archive::Extract) >=  0.16
BuildRequires: perl(Crypt::OpenPGP)
BuildRequires: perl(File::Fetch) >= 0.16
BuildRequires: perl(IPC::Cmd) >= 0.42
BuildRequires: perl(Locale::Maketext::Simple) >= 0.01
BuildRequires: perl(Log::Message) >= 0.01
BuildRequires: perl(Module::CoreList) >= 2.09
BuildRequires: perl(Module::Load) >= 0.10
BuildRequires: perl(Module::Load::Conditional) >= 0.28
BuildRequires: perl(Module::Loaded) >= 0.01
BuildRequires: perl(Object::Accessor) >= 0.34
BuildRequires: perl(Package::Constants) >= 0.01
BuildRequires: perl(Params::Check) >= 0.22
BuildRequires: perl(Parse::CPAN::Meta) >= 0.02
BuildRequires: perl(Term::UI) >= 0.05
BuildRequires: perl(Test::Harness) >= 2.62
BuildRequires: perl-version >= 0.70
BuildRequires: perl(Archive::Tar)
BuildRequires: perl(IO::Zlib)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Log::Message::Simple)
Buildroot:%{_tmppath}/%{name}-%{version}-%{release}

# (misc) not detected automatically, needed by CPANPLUS/Module.pm line 450
# fixing bug https://qa.mandriva.com/show_bug.cgi?id=35018
Requires: perl(Module::CoreList)
Requires: perl(Module::Pluggable)
Requires: perl(Module::Signature)
Requires: perl(version)

%description
The CPANPLUS library is an API to the CPAN mirrors and a collection of
interactive shells, commandline programs, etc, that use this API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
%doc README ChangeLog
%{_bindir}/cpan2dist
%{_bindir}/cpanp
%{_bindir}/cpanp-run-perl
%{perl_vendorlib}/CPANPLUS*
%{_mandir}/*/*
