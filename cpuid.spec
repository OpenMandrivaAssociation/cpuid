%define snapshot 20120601

Summary:	Dumps CPUID information about the CPU(s)
Name:		cpuid
Version:	1.0
Release:	%mkrel 0.%{snapshot}.1
License:	BSD
Source0:	cpuid-%{snapshot}.src.tar.gz
Group:		System/Kernel and hardware
URL:		http://www.etallen.com

%description
Cpuid dumps detailed information about the CPU(s) gathered from the
CPUID instruction, and also determines the exact model of CPU(s). It
supports Intel, AMD, and VIA CPUs, as well as older Transmeta, Cyrix,
UMC, NexGen, and Rise CPUs.

%prep
%setup -q -n %{name}-%{snapshot}

%build
make

%install
mkdir -p %{buildroot}%{_bindir} \
	%{buildroot}%{_mandir}/man1

install -m 755 cpuid %{buildroot}%{_bindir}
install -m 644 cpuid.man %{buildroot}%{_mandir}/man1/cpuid.1

%files
%defattr(-,root,root)
%doc ChangeLog FUTURE LICENSE
%{_bindir}/cpuid
%{_mandir}/man1/cpuid.1*

