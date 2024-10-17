%define name gtypist
%define version 2.8.3
%define release   4

Summary:	Universal typing tutor
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Text tools
License:	GPLv3+
URL: 		https://www.gnu.org/software/gtypist/gtypist.html
Source0: 	ftp://ftp.gnu.org/gnu/gtypist/%{name}-%{version}.tar.bz2
Buildrequires:	byacc bison pkgconfig(ncurses) binutils emacs
Obsoletes:	typist
Provides:	typist

%description
GNU Typist (also called gtypist) is a universal typing  tutor.  You  can
learn correct typing and improve your skills by practicing its exercises
on a regular basis.


%prep
%setup -q


%build
%configure2_5x
%make


%install

%makeinstall_std
%find_lang %{name}






%files -f %{name}.lang
%defattr(-,root,root,755)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README THANKS TODO QUESTIONS
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%name/
%{_infodir}/%name.info*
%{_datadir}/emacs/site-lisp/*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.8.3-2mdv2011.0
+ Revision: 611032
- rebuild

* Sat Jan 09 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.8.3-1mdv2010.1
+ Revision: 488014
- update to 2.8.3

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.8.1-2mdv2010.0
+ Revision: 429346
- rebuild

* Sun Jul 20 2008 Funda Wang <fwang@mandriva.org> 2.8.1-1mdv2009.0
+ Revision: 238880
- update to new version 2.8.1

* Wed May 28 2008 Funda Wang <fwang@mandriva.org> 2.8-1mdv2009.0
+ Revision: 212198
- New version 2.8

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 2.7-4mdv2008.1
+ Revision: 170885
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix no-buildroot-tag
- fix spacing at top of description

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 2.7-3mdv2008.1
+ Revision: 132968
- BR emacs
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import gtypist


* Thu Jul 07 2005 Lenny Cartier <lenny@mandriva.com> 2.7-3mdk
- rebuild

* Wed May 19 2004 Michael Scherer <misc@mandrake.org> 2.7-2mdk
- add proper Obsoletes and Provides 
- rpmbuildupdate aware
- [DIRM]
- remove Prefix

* Wed Jan 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.7-1mdk
- 2.7

* Wed Apr 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.6.2-3mdk
- buildrequires

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.6.2-2mdk
- rebuild

* Thu Sep  5 2002 Han Boetes <han@linux-mandrake.com> 2.6.2-1mdk
- 2.6.2
- Minor spec cleanups

* Tue Apr 30 2002  Lenny Cartier <lenny@mandrakesoft.com> 2.6-1mdk
- 2.6

* Tue Jan 22 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.5-1mdk
- 2.5

* Thu Nov 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.4.1-1mdk
- 2.4.1

* Wed Oct 31 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.4-1mdk
- submitted by Han Boetes <han@mijncomputer.nl> :
	- Initial build (practise creates skill)
