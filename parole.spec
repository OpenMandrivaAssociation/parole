%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A modern media player based on the GStreamer framework
Name:		parole
Version:	0.7.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/parole
Source0:	http://archive.xfce.org/src/apps/parole/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(gstreamer-1.0)
#BuildRequires:	pkgconfig(gstreamer-video-0.10)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.11
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(dbus-glib-1)
#Requires:	gstreamer0.10-plugins-base
#Requires:	gstreamer0.10-plugins-good
#Requires:	gstreamer0.10-plugins-bad
#Requires:	gstreamer0.10-plugins-ugly
#Requires:	gstreamer0.10-ffmpeg
#Requires:	gstreamer0.10-a52dec

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
