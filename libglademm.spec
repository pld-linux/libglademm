# TODO:
# - examples subpackage
#
Summary:	C++ wrappers for libglade
Summary(pl.UTF-8):	Interfejsy C++ dla libglade
Name:		libglademm
Version:	2.6.7
Release:	9
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libglademm/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	f9ca5b67f6c551ea98790ab5f21c19d0
Patch0:		no-get_defs-in-gcc5.patch
URL:		https://www.gtkmm.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibmm-devel >= 2.4
BuildRequires:	gtkmm-devel >= 2.12.1
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:1.5
BuildRequires:	m4
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libglade2 >= 1:2.6.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libglade.

%description -l pl.UTF-8
Interfejsy C++ dla libglade.

%package devel
Summary:	Devel files for libglademm
Summary(pl.UTF-8):	Pliki nagłówkowe dla libglademm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkmm-devel >= 2.12.1
Requires:	libglade2-devel >= 1:2.6.2

%description devel
Devel files for libglademm.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libglademm.

%package static
Summary:	libglademm static library
Summary(pl.UTF-8):	Biblioteka statyczna libglademm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libglademm static library.

%description static -l pl.UTF-8
Biblioteka statyczna libglademm.

%package doc
Summary:	Documentation for libglademm
Summary(pl.UTF-8):	Dokumentacja dla libglademm
Group:		Documentation
Requires:	devhelp

%description doc
Documentation for libglademm.

%description doc -l pl.UTF-8
Dokumentacja dla libglademm.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcxxflags} -std=c++11"
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_docdir}/gnomemm-2.6/libglademm-2.4 $RPM_BUILD_ROOT%{_docdir}/libglademm-2.4
%{__sed} -i -e 's,doc/gnomemm-2\.6/libglademm-2\.4,doc/libglademm-2.4,g' $RPM_BUILD_ROOT%{_datadir}/devhelp/books/libglademm-2.4/libglademm-2.4.devhelp

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libglademm-2.4.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libglademm-2.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglademm-2.4.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglademm-2.4.so
%{_includedir}/libglademm-2.4
%{_libdir}/libglademm-2.4
%{_pkgconfigdir}/libglademm-2.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libglademm-2.4.a

%files doc
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/libglademm-2.4
%{_docdir}/libglademm-2.4
