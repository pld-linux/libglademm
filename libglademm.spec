Summary:	C++ wrappers for libglade
Summary(pl):	Interfejsy C++ dla libglade
Name:		libglademm
Version:	2.3.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
# Source0-md5:	2f23868e9f203ca6c4058ebd23ca07e6
URL:		http://www.gnome.org/
BuildRequires:	gtkmm-devel >= 2.3.1
BuildRequires:	libglade2-devel >= 2.3.0
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
Requires:	gtkmm-devel >= 2.3.1

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
%attr(755,root,root) %{_libdir}/libglademm*.so
%{_libdir}/libglademm*.la
%{_includedir}/%{name}-2.4
%{_libdir}/%{name}-2.0
%{_libdir}/%{name}-2.4
%{_pkgconfigdir}/%{name}-2.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libglademm*.a
