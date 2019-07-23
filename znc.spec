%define _disable_ld_no_undefined 1

Name:		znc
Version:	1.7.4
Release:	1
Summary:	An IRC bouncer with many advanced features
Group:		Networking/IRC
License:	GPLv2+
URL:		http://en.znc.in/wiki/ZNC
Source0:	http://znc.in/releases/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)

%files
%{_bindir}/%{name}
%{_libdir}/%{name}/*.so
%{_datadir}/%{name}/modules/*/tmpl/*tmpl
%{_datadir}/%{name}/modules/*/files
%{_datadir}/%{name}/webskins/*/tmpl/*tmpl
%{_datadir}/%{name}/webskins/*/pub/*
%{_mandir}/man1/%{name}.1.*

#-------------------------------------------------------------------------------
%package	devel
Summary:	Development Files for znc
Group:		Networking/IRC
Requires:	%{name} = %{version}
Requires:	pkgconfig(openssl)

%description	devel
Development Files for ZNC - An IRC bouncer with many advanced features

%files devel
%{_bindir}/%{name}-buildmod
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/%{name}-buildmod.1.*

#-------------------------------------------------------------------------------

%description
ZNC is an IRC bouncer with many advanced features such as a built-in web
interface, persistent connection (detaching), multiple users, per channel
playback buffer, SSL, IPv6, transparent DCC bouncing, and C++ module support,
to name a few.

%prep
%setup -q

%build
%configure2_5x --disable-perl
%make

%install
%makeinstall_std


