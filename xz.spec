Summary:	General-purpose data compression software
Name:		xz
Version:	5.2.0
Release:	1
Epoch:		1
License:	LGPL v2.1+, helper scripts on GPL v2+
Group:		Applications/Archiving
# git d05d6d65c41a4bc83f162fa3d67c5d84e8751634
Source0:	http://tukaani.org/xz/%{name}-%{version}.tar.gz
# Source0-md5:	be585bdf8672e4406632eda3d819e284
URL:		http://tukaani.org/xz/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-autopoint
BuildRequires:	libtool
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XZ Utils is free general-purpose data compression software with high
compression ratio. XZ Utils were written for POSIX-like systems, but
also work on some not-so-POSIX systems. XZ Utils are the successor to
LZMA Utils.

%package libs
Summary:	LZMA shared library
Group:		Libraries

%description libs
LZMA shared library.

%package devel
Summary:	Header file for LZMA library
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Header file for LZMA library.

%prep
%setup -q

%build
%{__autopoint}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/xz

%find_lang %{name}

%check
%{__make} check

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*lz*
%attr(755,root,root) %{_bindir}/*xz*
%{_mandir}/man1/lz*.1*
%{_mandir}/man1/unlzma.1*
%{_mandir}/man1/unxz.1*
%{_mandir}/man1/xz*.1*

%files libs
%defattr(644,root,root,755)
%doc AUTHORS COPYING README THANKS
%attr(755,root,root) %ghost %{_libdir}/liblzma.so.?
%attr(755,root,root) %{_libdir}/liblzma.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblzma.so
%{_includedir}/lzma.h
%{_includedir}/lzma
%{_pkgconfigdir}/liblzma.pc

