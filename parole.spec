%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A modern media player based on the GStreamer framework
Name:		parole
Version:	0.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/parole
Source0:	http://archive.xfce.org/src/apps/parole/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	gstreamer0.10-devel
BuildRequires:	libgstreamer0.10-plugins-base-devel
BuildRequires:	libxfce4ui-devel >= 4.9.0
BuildRequires:	libnotify-devel
BuildRequires:	taglib-devel
BuildRequires:	dbus-glib-devel

%description
New media player for Xfce desktop environment.

%package %{name}-devel
Summary:	Development files for %{name}
Group:		Development/C

%description %{name}-devel
Development files and headers for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TODO THANKS
%{_bindir}/%{name}
%{_libdir}/parole-0/*.so
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/%{name}

%files %{name}-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h


%changelog
* Tue Aug 21 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0.2-1
+ Revision: 815559
- disable static libraries
- update to new version 0.3.0.2
- drop old patch0
- package devel files
- spec file clean

* Mon Apr 09 2012 Crispin Boylan <crisb@mandriva.org> 0.2.0.6-2
+ Revision: 790104
- Fix gold linker build

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild
    - drop old stuff from spec file

* Sun Apr 17 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0.6-1
+ Revision: 654238
- update to new version 0.2.0.6

* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0.5-1
+ Revision: 653308
- add missing buildrequire on dbus-glib-devel
- update to new version 0.2.0.5
- drop browser-plugin subpackage, because upstread did drop the plugin

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0.2-4
+ Revision: 633058
- rebuild for new Xfce 4.8.0

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0.2-3mdv2011.0
+ Revision: 579666
- rebuild for new xfce 4.7.0

* Sun Apr 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0.2-2mdv2010.1
+ Revision: 536073
- rebuild for new xulrunner

* Mon Jan 25 2010 Funda Wang <fwang@mandriva.org> 0.2.0.2-1mdv2010.1
+ Revision: 496190
- new verison 0.2.0.2

* Fri Jan 15 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.2.0.1-1mdv2010.1
+ Revision: 491924
- update to new version 0.2.0.1

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 0.2.0-1mdv2010.1
+ Revision: 486871
- update to new version 0.2.0

* Tue Dec 01 2009 Funda Wang <fwang@mandriva.org> 0.1.99-1mdv2010.1
+ Revision: 472298
- new version 0.1.99

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to version 0.1.98

* Wed Nov 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.96-1mdv2010.1
+ Revision: 470069
- Update to 0.1.96

* Wed Nov 25 2009 Funda Wang <fwang@mandriva.org> 0.1.95-1mdv2010.1
+ Revision: 470035
- fix linkage
- add plugin sub package
- new version 0.1.95

* Sat Nov 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.91-1mdv2010.1
+ Revision: 462243
- update to new version 0.1.91

* Sun Oct 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.1.90-1mdv2010.0
+ Revision: 456674
- add spec and source files
- Created package structure for parole.

