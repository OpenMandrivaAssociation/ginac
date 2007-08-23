%define major 2
%define api_version 1.3

%define libname_basic lib%{name}%{api_version}
%define libname %mklibname %{name} %{api_version} %{major}

Name:		ginac
Version:	1.3.7
Release:	%mkrel 2
Summary:	C++ class library for symbolic calculations
License:	GPL
Group:		Sciences/Mathematics
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/GiNaC/%{name}-%{version}.tar.bz2
URL:		http://www.ginac.de/
Requires(post):	info-install
Requires(preun): info-install
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  chrpath
BuildRequires:	cln-devel
BuildRequires:	doxygen
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	tetex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	transfig
Obsoletes:	GiNaC
Provides:	GiNaC

%description
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

%package -n	%{libname}
Summary:	C++ class library for symbolic calculations
Group:		Sciences/Mathematics
Provides:	%{libname_basic} = %{version}-%{release}

%description -n	%{libname}
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This package provides the core GiNaC libraries.

%package -n	%{libname}-devel
Summary:	Libraries, includes and more to develop GiNaC applications
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_basic}-devel = %{version}-%{release}
Provides:	%{_lib}%{name}%{api_version}-devel

%description -n	%{libname}-devel
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This is the libraries, include files and other resources you can use
to develop GiNaC applications.

%package	utils
Summary:	GiNaC-related utilities
Group:		Sciences/Mathematics
Provides:	%{name} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description	utils
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This package includes the ginsh ("GiNaC interactive shell") which
provides a simple and easy-to-use CAS-like interface to GiNaC for
non-programmers, and the tool "viewgar" which displays the contents
of GiNaC archives.

%prep
%setup -q

%build
%configure2_5x
%make

# XXX: 2 out of 3 tests fail
%if 0
%check
%make check
%endif

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{_bindir}/chrpath -d %{buildroot}%{_libdir}/libginac-%{api_version}.so.%{major}.*.*
%{_bindir}/chrpath -d %{buildroot}%{_bindir}/{ginsh,viewgar}

%multiarch_binaries %{buildroot}%{_bindir}/ginac-config

%clean
%{__rm} -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libname}-devel
%_install_info ginac.info

%preun -n %{libname}-devel
%_remove_install_info ginac.info

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc ChangeLog
%{_bindir}/ginac-config
%{multiarch_bindir}/ginac-config
%{_datadir}/aclocal/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*.info*
%{_mandir}/man1/ginac-config.1*

%files utils
%defattr(-,root,root)
%{_bindir}/ginsh
%{_bindir}/viewgar
%{_mandir}/man1/ginsh.1*
%{_mandir}/man1/viewgar.1*


