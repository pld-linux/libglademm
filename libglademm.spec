Summary:	C++ wrappers for libglade
Summary(pl):	Interfejsy C++ dla libglade
Name:		libglademm
Version:	2.1.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
# Source0-md5:	e907e10c01dca51044a93af68e12aa53
URL:		http://www.gnome.org/
BuildRequires:	gtkmm-devel >= 2.2.8
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libglade.

%description -l pl
Interfejsy C++ dla libglade.

%package devel
Summary:	Devel files for libglademm
Summary(pl):	Pliki nag³ówkowe dla libglademm
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtkmm-devel >= 2.2.8
Requires:	libglade2-devel >= 2.0.1

%description devel
Devel files for libglademm.

%description devel -l pl
Pliki nag³ówkowe dla libglademm.

%package static
Summary:	libglademm static library
Summary(pl):	Biblioteka statyczna libglademm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libglademm static library.

%description static -l pl
Biblioteka statyczna libglademm.

%prep
%setup -q

%build
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libglademm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-2.0
%{_libdir}/libglademm*.la
%{_libdir}/libglademm*.so
%{_libdir}/%{name}-2.0
%{_pkgconfigdir}/%{name}-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libglademm*.a
