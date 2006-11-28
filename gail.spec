#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	Accessibility implementation for GTK+ and GNOME libraries
Summary(pl):	Implementacja ułatwiania pracy niepełnosprawnym dla GTK+ i GNOME
Name:		gail
Version:	1.9.3
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/gail/1.9/%{name}-%{version}.tar.bz2
# Source0-md5:	1e8825da60fd19833dfc6b2068f05ec9
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	atk-devel >= 1:1.12.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.5
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.7}
BuildRequires:	gtk-doc-automake
BuildRequires:	libgnomecanvas-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	libgnomecanvas >= 2.14.0
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
Requires:	atk-devel >= 1:1.12.3
%{?with_apidocs:Requires:	gtk-doc-common}
Requires:	gtk+2-devel >= 2:2.10.5
Requires:	libgnomecanvas-devel >= 2.14.0

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

%package apidocs
Summary:	API documentation 
Summary(pl):	Dokumentacja API 
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
 API documentation.

%description apidocs -l pl
Dokumentacja API.

%prep
%setup -q

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_apidocs:--enable-gtk-doc} \
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/lib*.so
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gail-1.0
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/*
%endif
