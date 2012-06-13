%define major 2

%define libname              %mklibname ginac %{major}
%define libname_devel        %mklibname ginac -d
%define libname_static_devel %mklibname ginac -d -s

Name:		ginac
Version:	1.6.2
Release:	1
Summary:	C++ class library for symbolic calculations
License:	GPLv2+
Group:		Sciences/Mathematics
URL:		http://www.ginac.de/
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/GiNaC/ginac-%{version}.tar.bz2
BuildRequires:	chrpath
BuildRequires:	cln-devel
BuildRequires:	doxygen
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	tetex
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	transfig
BuildRequires:	bison
BuildRequires:	flex
Obsoletes:	GiNaC < %{version}-%{release}
Provides:	GiNaC = %{version}-%{release}

%description
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

%package -n %{libname}
Summary:	C++ class library for symbolic calculations
Group:		Sciences/Mathematics

%description -n %{libname}
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This package provides the core GiNaC libraries.

%package -n %{libname_devel}
Summary:	Libraries, includes and more for developing GiNaC applications
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	ginac-devel = %{version}-%{release}
Obsoletes:	%{_lib}ginac1.5-devel

%description -n %{libname_devel}
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This is the libraries, include files and other resources you can use
for developing GiNaC applications.

%package -n %{libname_static_devel}
Summary:	Static libraries for developing GiNaC applications
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	ginac-static-devel = %{version}-%{release}
Obsoletes:	%{_lib}ginac1.5-static-devel

%description -n %{libname_static_devel}
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This is the static libraries which you can use
for developing GiNaC applications.

%prep
%setup -q

%build
%configure2_5x --disable-rpath
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%check
%make check

%files
%doc AUTHORS NEWS README
%{_bindir}/ginsh
%{_bindir}/viewgar
%{_mandir}/man1/ginsh.1*
%{_mandir}/man1/viewgar.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{libname_devel}
%doc ChangeLog
%{_bindir}/ginac-excompiler
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*.info*

%files -n %{libname_static_devel}
%{_libdir}/*.a
