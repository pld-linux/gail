Summary:	Accessibility implementation for GTK+ and GNOME libraries
Summary(pl):	Implementacja ułatwiania pracy niepełnosprawnym dla GTK+ i GNOME
Name:		gail
Version:	1.5.8
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.5/%{name}-%{version}.tar.bz2
# Source0-md5:	184227f0ec109ac5d3385e8dbe269f67
Patch0:		%{name}-locale-names.patch
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	atk-devel >= 1.6.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.3.6
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libgnomecanvas-devel >= 2.5.90
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.1-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GAIL implements the abstract interfaces found in ATK for GTK+ and
GNOME libraries, enabling accessibility technologies such as at-spi to
access those GUIs.

%description -l pl
GAIL jest implementacją abstrakcyjnych interfejsów z ATK dla bibliotek
GTK+ i GNOME, umożliwiającą korzystanie z technik takich jak at-spi,
aby ułatwić niepełnosprawnym korzystanie z tych GUI.

%package devel
Summary:	Header files to compile applications that use GAIL
Summary(pl):	Pliki nagłówkowe GAIL
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.3.6
Requires:	libgnomecanvas-devel >= 2.5.90

%description devel
gail-devel contains the header files required to compile applications
against the GAIL libraries.

%description devel -l pl
Pakiet gail-devel zawiera pliki nagłówkowe potrzebne do kompilowania
aplikacji używających bibliotek GAIL.

%package static
Summary:	Static GAIL libraries
Summary(pl):	Statyczne biblioteki GAIL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gail-static contains the static GAIL libraries.

%description static -l pl
Pakiet gail-static zawiera statyczne biblioteki GAIL.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no static modules and *.la for gtk modules - shut up check-files
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/lib*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/lib*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gail-1.0
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
