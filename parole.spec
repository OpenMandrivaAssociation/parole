%define url_ver %(echo %{version} | cut -d. -f 1,2)
%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1

Summary:	A modern media player based on the GStreamer framework
Name:		parole
Version:	4.20.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/applications/parole
Source0:	https://archive.xfce.org/src/apps/parole/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	meson
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-video-1.0)
BuildRequires:	pkgconfig(libxfce4ui-2) >= 4.12
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(dbus-glib-1)
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-libav
Requires:	gstreamer1.0-a52dec

%description
New media player for Xfce desktop environment.

%package %{name}-devel
Summary:	Development files for %{name}
Group:		Development/C

%description %{name}-devel
Development files and headers for %{name}.

%prep
%autosetup -p1

%build
%meson \
	-Dx11=enabled \
 	-Dwayland=enabled

%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO THANKS
%{_bindir}/%{name}
%{_libdir}/parole-0/*.so
%{_datadir}/applications/org.xfce.Parole.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/%{name}
%{_datadir}/metainfo/parole.appdata.xml

%files %{name}-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
