%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A modern media player based on the GStreamer framework
Name:		parole
Version:	0.8.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/parole
Source0:	http://archive.xfce.org/src/apps/parole/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-video-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.12
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	automake1.4
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
%setup -q

%build
sed -i -e 's/libxfce4ui-2/libxfce4ui-1/g' configure*
aclocal
autoreconf -fiv
automake

%configure2_5x \
	--disable-static \
	--with-gstreamer=1.0

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
