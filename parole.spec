%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A modern media player based on the GStreamer framework
Name:		parole
Version:	0.3.0.3
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
Obsoletes:	xfmedia
Obsoletes:	%{name}-browser-plugin < 0.2.0.5

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
