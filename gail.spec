Summary:	Accessibility implementation for GTK+ and GNOME libraries
Name:		gail
Version:	0.13
Release:	0.1
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://developer.gnome.org/projects/gap
License:	LGPL
Group:		X11/Libraries
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gtk+2-devel
BuildRequires:	libgnomecanvas-devel

%define         _prefix         /usr/X11R6

%description
GAIL implements the abstract interfaces found in ATK for GTK+ and
GNOME libraries, enabling accessibility technologies such as at-spi to
access those GUIs.

%package devel
Summary:	Header files to compile applications that use GAIL
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
gail-devel contains the feader files required to compile applications 
against the GAIL libraries.

%package static
Summary:	Static libraries to compile applications that use GAIL
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
gail-devel contains the static libraries required to compile applications 
against the GAIL libraries.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc=no \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
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
