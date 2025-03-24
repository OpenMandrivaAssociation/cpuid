%define _empty_manifest_terminate_build 0

Summary:	Dumps CPUID information about the CPU(s)
Name:		cpuid
Version:	20250316
Release:	1
License:	BSD
Source0:	https://www.etallen.com/%{name}/%{name}-%{version}.src.tar.gz
Group:		System/Kernel and hardware
URL:		https://www.etallen.com

%description
Cpuid dumps detailed information about the CPU(s) gathered from the
CPUID instruction, and also determines the exact model of CPU(s). It
supports Intel, AMD, and VIA CPUs, as well as older Transmeta, Cyrix,
UMC, NexGen, and Rise CPUs.

%prep
%autosetup -p1

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
