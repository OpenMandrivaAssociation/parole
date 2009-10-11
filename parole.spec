%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A modern media player based on the GStreamer framework
Name:		parole
Version:	0.1.90
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/parole
Source0:	http://archive.xfce.org/src/apps/parole/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	gstreamer0.10-devel
BuildRequires:	libgstreamer0.10-plugins-base-devel
BuildRequires:	libxfcegui4-devel >= 4.6.0
BuildRequires:	libnotify-devel
BuildRequires:	taglib-devel
Obsoletes:	xfmedia
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
New media player for Xfce desktop environment.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# (tpg) not needed for now
find %{buildroot} -name *.la -type f -exec rm -rf {} \;
rm -rf %{buildroot}%{_includedir}/%{name}

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO THANKS
%{_bindir}/%{name}
%{_libdir}/parole-0/*.so
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/%{name}/pixmaps/*.png
