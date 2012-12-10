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


%changelog
* Wed Jun 13 2012 Andrey Bondrov <abondrov@mandriva.org> 1.6.2-1
+ Revision: 805435
- New version 1.6.2, drop some legacy junk

* Wed Jul 20 2011 Funda Wang <fwang@mandriva.org> 1.6.1-1
+ Revision: 690706
- new version 1.6.1

* Tue May 24 2011 Funda Wang <fwang@mandriva.org> 1.6.0-1
+ Revision: 678214
- SILENt; typo
- update file list
- new version 1.6.0

* Mon Jul 12 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.5.8-1mdv2011.0
+ Revision: 551174
- update to 1.5.8

* Thu Apr 22 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.5.7-1mdv2010.1
+ Revision: 538002
- update to 1.5.7

* Thu Jan 28 2010 Frederik Himpe <fhimpe@mandriva.org> 1.5.6-1mdv2010.1
+ Revision: 497679
- Update to new version 1.5.6

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 1.5.5-1mdv2010.1
+ Revision: 473926
- new version 1.5.5

* Wed Aug 05 2009 Funda Wang <fwang@mandriva.org> 1.5.3-5mdv2010.0
+ Revision: 410281
- fix build with latest gcc
- rebuild for new cln

  + Frederik Himpe <fhimpe@mandriva.org>
    - Update to new version 1.5.3
    - Remove patch integrated upstream

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.1-4mdv2010.0
+ Revision: 378431
- fix build
- rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild

  + David Walluck <walluck@mandriva.org>
    - add sources
    - 1.5.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Apr 20 2008 David Walluck <walluck@mandriva.org> 1.4.3-1mdv2009.0
+ Revision: 195976
- 1.4.3

* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.1-2mdv2008.1
+ Revision: 182203
- rebuild for new cln
- add missing buildrequires on bison and flex
- make use of %%major in file list
- do not package COPYING file
- new license policy

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 24 2007 David Walluck <walluck@mandriva.org> 1.4.1-1mdv2008.1
+ Revision: 111739
- 1.4.1

* Fri Oct 19 2007 David Walluck <walluck@mandriva.org> 1.4.0-2mdv2008.1
+ Revision: 100279
- rebuild

* Tue Sep 18 2007 David Walluck <walluck@mandriva.org> 1.4.0-1mdv2008.1
+ Revision: 89368
- 1.4.0

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.3.7-2mdv2008.0
+ Revision: 70249
- kill file require on info-install


* Fri Mar 23 2007 David Walluck <walluck@mandriva.org> 1.3.7-1mdv2007.1
+ Revision: 148697
- 1.3.7

* Sat Dec 16 2006 David Walluck <walluck@mandriva.org> 1.3.6-1mdv2007.1
+ Revision: 98069
- 1.3.6
- Import ginac

* Mon Sep 11 2006 David Walluck <walluck@mandriva.org> 1.3.5-1mdv2007.0
- 1.3.5
- major should be 2
- fix macro in changelog

* Wed Apr 19 2006 David Walluck <walluck@mandriva.org> 1.3.4-1mdk
- 1.3.4

* Sun Oct 30 2005 David Walluck <walluck@mandriva.org> 1.3.3-1mdk
- 1.3.3
- drop gcc4 patch (merged upstream)

* Sat Sep 03 2005 David Walluck <walluck@mandriva.org> 1.3.2-1mdk
- 1.3.2
- name is now ginac
- apply gcc4 patch from suse
- BuildRequires: doxygen, tetex, tetex-dvips, tetex-latex, transfig
- don't use PreReq

* Mon Apr 04 2005 Abel Cheung <deaddog@mandrake.org> 1.3.0-3mdk
- Rebuild & multiarch

* Tue Dec 28 2004 Abel Cheung <deaddog@mandrake.org> 1.3.0-2mdk
- Cleanup this beautified crap, at least make sure devel package
  is usable

* Tue Oct 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3.0-1mdk
- 1.3.0

* Thu Oct 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.4-1mdk
- 1.2.4

* Sun Aug 29 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2.3-2mdk 
- %%major in include path
- provide icons in the 2 sizes
- fix distlint DIRM
- fix menu capitalisation

* Sat Aug 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.3-1mdk
- 1.2.3

* Thu Aug 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-1mdk
- 1.2.2

* Wed Jun 16 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2.1-2mdk
- rebuild
- %%mklibname

* Tue Jun 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.1-1mdk
- 1.2.1

