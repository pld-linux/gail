Summary:	Accessibility implementation for GTK+ and GNOME libraries
Summary(pl):	Implementacja u³atwiania pracy niepe³nosprawnym dla GTK+ i GNOME
Name:		gail
Version:	0.16
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://developer.gnome.org/projects/gap
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.3
BuildRequires:	libgnomecanvas-devel >= 2.0.1
BuildRequires:	atk-devel >= 1.0.2
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
GAIL implements the abstract interfaces found in ATK for GTK+ and
GNOME libraries, enabling accessibility technologies such as at-spi to
access those GUIs.

%description -l pl
GAIL jest implementacj± abstrakcyjnych interfejsów z ATK dla bibliotek
GTK+ i GNOME, umo¿liwiaj±c± korzystanie z technik takich jak at-spi,
aby u³atwiæ niepe³nosprawnym korzystanie z tych GUI.

%package devel
Summary:	Header files to compile applications that use GAIL
Summary(pl):	Pliki nag³ówkowe GAIL
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
gail-devel contains the header files required to compile applications 
against the GAIL libraries.

%description devel -l pl
Pakiet gail-devel zawiera pliki nag³ówkowe potrzebne do kompilowania
aplikacji u¿ywaj±cych bibliotek GAIL.

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

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc=no \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/lib*.??

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.??
%{_includedir}/gail-1.0
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
