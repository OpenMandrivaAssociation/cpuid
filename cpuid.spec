%define _empty_manifest_terminate_build 0
%define snapshot 20200211

Summary:	Dumps CPUID information about the CPU(s)
Name:		cpuid
Version:	20221003
Release:	1
License:	BSD
Source0:	http://www.etallen.com/%{name}/%{name}-%{version}.src.tar.gz
Group:		System/Kernel and hardware
URL:		http://www.etallen.com

%description
Cpuid dumps detailed information about the CPU(s) gathered from the
CPUID instruction, and also determines the exact model of CPU(s). It
supports Intel, AMD, and VIA CPUs, as well as older Transmeta, Cyrix,
UMC, NexGen, and Rise CPUs.

%prep
%setup -q

%build
%make_build

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc ChangeLog FUTURE
%license LICENSE
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}

%changelog
* Fri Jul 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0-0.20120601.1mdv2012.0
+ Revision: 810393
- version update 20120601

* Sun Feb 26 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0-0.20120225.1
+ Revision: 780924
- update to 20120225

* Fri Mar 25 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0-0.20110305.1
+ Revision: 648418
- new version

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-0.20060917.3mdv2011.0
+ Revision: 617437
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.0-0.20060917.2mdv2010.0
+ Revision: 425243
- rebuild

* Mon Feb 18 2008 Olivier Blin <blino@mandriva.org> 1.0-0.20060917.1mdv2008.1
+ Revision: 171593
- update to 20060917 snapshot
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cpuid

