%define	upstream_name	 CPANPLUS
%define upstream_version 0.9105

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Your::Module::Here\\)'
%else
%define _requires_exceptions perl(Your::Module::Here)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	API & CLI access to the CPAN mirrors
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CPANPLUS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Extract)          >=  0.160.0
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Crypt::OpenPGP)
BuildRequires:	perl(File::Fetch)               >= 0.160.0
BuildRequires:	perl(IO::Zlib)
BuildRequires:	perl(IPC::Cmd)                  >= 0.420.0
BuildRequires:	perl(Locale::Maketext::Simple)  >= 0.10.0
BuildRequires:	perl(Log::Message)              >= 0.10.0
BuildRequires:	perl(Log::Message::Simple)
BuildRequires:	perl(Module::CoreList)          >= 2.90.0
BuildRequires:	perl(Module::Load)              >= 0.100.0
BuildRequires:	perl(Module::Load::Conditional) >= 0.280.0
BuildRequires:	perl(Module::Loaded)            >= 0.10.0
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Object::Accessor)          >= 0.340.0
BuildRequires:	perl(Package::Constants)        >= 0.10.0
BuildRequires:	perl(Params::Check)             >= 0.220.0
BuildRequires:	perl(Parse::CPAN::Meta)         >= 0.20.0
BuildRequires:	perl(Term::UI)                  >= 0.50.0
BuildRequires:	perl(Test::Harness)             >= 2.620.0
BuildRequires:	perl(version)                   >= 1:0.700.0

BuildArch:	noarch

# (misc) not detected automatically, needed by CPANPLUS/Module.pm line 450
# fixing bug https://qa.mandriva.com/show_bug.cgi?id=35018
Requires:	perl(Module::CoreList)
Requires:	perl(Module::Pluggable)
Requires:	perl(Module::Signature)
Requires:	perl(version)

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
%makeinstall_std

%files
%doc README ChangeLog
%{_bindir}/cpan2dist
%{_bindir}/cpanp
%{_bindir}/cpanp-run-perl
%{perl_vendorlib}/CPANPLUS*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.910.500-4mdv2012.0
+ Revision: 765116
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.910.500-2
+ Revision: 763049
- rebuild

* Mon Jul 04 2011 Shlomi Fish <shlomif@mandriva.org> 0.910.500-1
+ Revision: 688679
- New version - CPANPLUS-0.9010

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.901.0-2
+ Revision: 667037
- mass rebuild

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.901.0-1mdv2011.0
+ Revision: 597212
- update to 0.9010

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.900.700-1mdv2011.0
+ Revision: 553064
- update to 0.9007

* Tue Mar 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.900.300-1mdv2010.1
+ Revision: 521607
- update to 0.9003

* Mon Mar 15 2010 Jérôme Quelin <jquelin@mandriva.org> 0.900.200-1mdv2010.1
+ Revision: 520141
- update to 0.9002
- update to 0.9001

* Thu Dec 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.900.100-1mdv2010.1
+ Revision: 482075
- update to 0.9001

* Mon Dec 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.900.0-1mdv2010.1
+ Revision: 480715
- update to 0.90

* Wed Jul 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.880.0-1mdv2010.0
+ Revision: 393636
- update to 0.88

* Tue Jul 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.860.100-1mdv2010.0
+ Revision: 393096
- bumping some buildrequires: versions
- bumping version of some buildrequires:
- update to 0.8601
- using %%perl_convert_version

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.84-6mdv2010.0
+ Revision: 392920
- fixing bug 35018

* Mon Mar 02 2009 Buchan Milne <bgmilne@mandriva.org> 0.84-5mdv2009.1
+ Revision: 347435
- More manual requires (bug #35018)

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - keep bash completion in its own package

* Wed Jan 28 2009 Michael Scherer <misc@mandriva.org> 0.84-3mdv2009.1
+ Revision: 334791
- add missing requires

* Thu Jun 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-2mdv2009.0
+ Revision: 218613
- bash completion enhancement

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-1mdv2008.1
+ Revision: 137995
- update to new version 0.84
- update to new version 0.84

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.82-2mdv2008.1
+ Revision: 109455
- bash completion

* Tue Aug 21 2007 Buchan Milne <bgmilne@mandriva.org> 0.82-1mdv2008.0
+ Revision: 68227
- New version 0.82

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.80-1mdv2008.0
+ Revision: 48174
- new version

* Tue Jun 26 2007 Buchan Milne <bgmilne@mandriva.org> 0.78-1mdv2008.0
+ Revision: 44565
- Import perl-CPANPLUS



* Thu Jun 21 2007 Buchan Milne <bgmilne@mandriva.org> 0.78-1mdv2007.1
- initial package
