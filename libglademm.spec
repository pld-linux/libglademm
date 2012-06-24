Summary:	C++ wrappers for libglade
Summary(pl):	Interfejsy C++ dla libglade
Name:		libglademm
Version:	2.6.2
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libglademm/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	431a7d04514cabe26fcaedd7767b6a93
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtkmm-devel >= 2.9.8
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libglade.

%description -l pl
Interfejsy C++ dla libglade.

%package devel
Summary:	Devel files for libglademm
Summary(pl):	Pliki nag��wkowe dla libglademm
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm-devel >= 2.9.8
Requires:	libglade2-devel >= 1:2.6.0

%description devel
Devel files for libglademm.

%description devel -l pl
Pliki nag��wkowe dla libglademm.

%package static
Summary:	libglademm static library
Summary(pl):	Biblioteka statyczna libglademm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libglademm static library.

%description static -l pl
Biblioteka statyczna libglademm.

%package doc
Summary:	Documentation for libglademm
Summary(pl):	Dokumentacja dla libglademm
Group:		Documentation
Requires:	devhelp

%description doc
Documentation for libglademm.

%description devel -l pl
Dokumentacja dla libglademm.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
LDFLAGS="%{rpmldflags} -Wl,--as-needed"
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_docdir}/gnomemm-2.6/%{name}-2.4/docs installed-docs

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
%{_libdir}/%{name}-2.4
%{_pkgconfigdir}/%{name}-2.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libglademm*.a

%files doc
%defattr(644,root,root,755)
%doc installed-docs/*
%doc %{_datadir}/devhelp/books/%{name}-2.4
