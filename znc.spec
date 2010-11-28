%define _disable_ld_no_undefined 1
Name:       znc
Version:    0.096
Release:    %mkrel 1
License:    GPLv2+
Summary:    An IRC bounce with many advanced features
Group:      Networking/IRC
URL:        http://en.znc.in/wiki/ZNC
Source0:    http://sourceforge.net/projects/znc/files/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  openssl-devel

BuildRoot:      %_tmppath/%{name}-%{version}-%{release}-build
#-------------------------------------------------------------------------------
%package    devel
Summary:    Development Files for znc
Group:      Networking/IRC
Requires:   %{name} = %{version}

%description    devel
Development Files for ZNC - An IRC bounce with many advanced features

%files      devel
%defattr(-,root,root,-)
%_bindir/%{name}-buildmod
%_bindir/%{name}-config
%_includedir/%{name}/*.h
%_libdir/pkgconfig/%{name}.pc
%_mandir/man1/%{name}-buildmod.1.*
%_mandir/man1/%{name}-config.1.*
#-------------------------------------------------------------------------------

%description
ZNC is an IRC bounce with many advanced features such as a built-in web
interface, persistent connection (detaching), multiple users, per channel
playback buffer, SSL, IPv6, transparent DCC bouncing, and c++ module support,
to name a few.

%prep
%setup -q

%build
%configure2_5x --disable-perl
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%_bindir/%{name}
%_libdir/%{name}/*.so
%_datadir/%{name}/lastseen/*/*
%_datadir/%{name}/notes/*/*
%_datadir/%{name}/stickychan/*/*
%_datadir/%{name}/webadmin/*/*
%_datadir/%{name}/webskins/*/*/*
%_mandir/man1/%{name}.1.*
%_datadir/%{name}/blockuser/tmpl/blockuser_WebadminUser.tmpl
