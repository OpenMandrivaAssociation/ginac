%define api_version 1.4
%define major 0

%define libname              %mklibname ginac %{api_version} %{major}
%define libname_devel        %mklibname ginac %{api_version} -d
%define libname_static_devel %mklibname ginac %{api_version} -d -s

Name:           ginac
Version:        1.4.1
Release:        %mkrel 1
Summary:        C++ class library for symbolic calculations
License:        GPL
Group:          Sciences/Mathematics
Source0:        ftp://ftpthep.physik.uni-mainz.de/pub/GiNaC/ginac-%{version}.tar.bz2
URL:            http://www.ginac.de/
Requires(post): info-install
Requires(preun): info-install
BuildRequires:  chrpath
BuildRequires:  cln-devel
BuildRequires:  doxygen
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  tetex
BuildRequires:  tetex-dvips
BuildRequires:  tetex-latex
BuildRequires:  transfig
Obsoletes:      GiNaC < %{version}-%{release}
Provides:       GiNaC = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

%package -n     %{libname}
Summary:        C++ class library for symbolic calculations
Group:          Sciences/Mathematics

%description -n %{libname}
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This package provides the core GiNaC libraries.

%package -n %{libname_devel}
Summary:        Libraries, includes and more for developing GiNaC applications
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides:       ginac-devel = %{version}-%{release}
Provides:       ginac%{api_version}-devel = %{version}-%{release}

%description -n        %{libname_devel}
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This is the libraries, include files and other resources you can use
for developing GiNaC applications.

%package -n     %{libname_static_devel}
Summary:        Static libraries for developing GiNaC applications
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides:       ginac-static-devel = %{version}-%{release}
Provides:       ginac%{api_version}-static-devel = %{version}-%{release}

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
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%{_bindir}/chrpath -d %{buildroot}%{_libdir}/libginac-%{api_version}.so.%{major}.*.*
%{_bindir}/chrpath -d %{buildroot}%{_bindir}/{ginsh,viewgar}

%check
%{make} check

%clean
%{__rm} -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libname_devel}
%_install_info ginac.info

%preun -n %{libname_devel}
%_remove_install_info ginac.info

%files
%defattr(-,root,root,0755)
%{_bindir}/ginsh
%{_bindir}/viewgar
%{_mandir}/man1/ginsh.1*
%{_mandir}/man1/viewgar.1*

%files -n %{libname}
%defattr(-,root,root,0755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files -n %{libname_devel}
%defattr(-,root,root,0755)
%doc ChangeLog
%{_bindir}/ginac-excompiler
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_infodir}/*.info*

%files -n %{libname_static_devel}
%defattr(-,root,root,0755)
%{_libdir}/*.a
