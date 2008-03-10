#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	Accessibility implementation for GTK+ and GNOME libraries
Summary(pl.UTF-8):	Implementacja ułatwiania pracy niepełnosprawnym dla GTK+ i GNOME
Name:		gail
Version:	1.22.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gail/1.22/%{name}-%{version}.tar.bz2
# Source0-md5:	ff500cc53d088bb7f13d35a4fcf81e80
URL:		http://developer.gnome.org/projects/gap/
BuildRequires:	atk-devel >= 1:1.22.0
BuildRequires:	autoconf
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.12.8
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	gtk-doc-automake >= 1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GAIL implements the abstract interfaces found in ATK for GTK+ and
GNOME libraries, enabling accessibility technologies such as AT-SPI to
access those GUIs.

%description -l pl.UTF-8
GAIL jest implementacją abstrakcyjnych interfejsów z ATK dla bibliotek
GTK+ i GNOME, umożliwiającą korzystanie z technik takich jak AT-SPI,
aby ułatwić niepełnosprawnym korzystanie z tych GUI.

%package devel
Summary:	Header files to compile applications that use GAIL
Summary(pl.UTF-8):	Pliki nagłówkowe GAIL
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	atk-devel >= 1:1.22.0
Requires:	gtk+2-devel >= 2:2.12.8

%description devel
gail-devel contains the header files required to compile applications
against the GAIL libraries.

%description devel -l pl.UTF-8
Pakiet gail-devel zawiera pliki nagłówkowe potrzebne do kompilowania
aplikacji używających bibliotek GAIL.

%package static
Summary:	Static GAIL libraries
Summary(pl.UTF-8):	Statyczne biblioteki GAIL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
gail-static contains the static GAIL libraries.

%description static -l pl.UTF-8
Pakiet gail-static zawiera statyczne biblioteki GAIL.

%package apidocs
Summary:	API documentation
Summary(pl.UTF-8):	Dokumentacja API
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation.

%description apidocs -l pl.UTF-8
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

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libferret.so
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libgail.so
%attr(755,root,root) %{_libdir}/libgailutil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgailutil.so.18

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgailutil.so
%{_libdir}/libgailutil.la
%{_includedir}/gail-1.0
%{_pkgconfigdir}/gail.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgailutil.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gail-libgail-util
%endif
