%define name gtypist
%define version 2.7
%define release  %mkrel 3

Summary:	Gtypist is a universal typing tutor
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Text tools
License:	GPL
URL: 		http://www.gnu.org/software/gtypist/gtypist.html
Source: 	ftp://ftp.gnu.org/gnu/gtypist//%{name}-%{version}.tar.bz2
Buildrequires:	byacc bison libncurses-devel binutils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:  typist
Provides:   typist

%description

GNU Typist (also called gtypist) is a universal typing  tutor.  You  can
learn correct typing and improve your skills by practicing its exercises
on a regular basis.


%prep

%setup -q


%build

%configure
%make


%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%find_lang %{name}


%post
%_install_info %{name}.info


%preun
%_remove_install_info %{name}.info


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,755)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%_bindir/*
%_mandir/man1/*
%_datadir/%name/
%_infodir/%name.info*
%_datadir/emacs/site-lisp/*


