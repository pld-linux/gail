Summary:	Accessibility implementation for GTK+ and GNOME libraries
Summary(pl):	Implementacja ułatwiania pracy niepełnosprawnym dla GTK+ i GNOME
Name:		gail
Version:	1.3.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	765071d58561c3773df69264aa8f8987
Patch0:		%{name}-am.patch
URL:		http://developer.gnome.org/projects/gap
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	gtk-doc
BuildRequires:	libgnomecanvas-devel >= 2.3.0
BuildRequires:	atk-devel >= 1.3.3
BuildRequires:	libtool
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
Requires:	%{name} = %{version}

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
Requires:	%{name}-devel = %{version}

%description static
gail-static contains the static GAIL libraries.

%description static -l pl
Pakiet gail-static zawiera statyczne biblioteki GAIL.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/lib*.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/gail-1.0
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
