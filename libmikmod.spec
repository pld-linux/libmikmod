Summary:	libmikmod - a portable sound library for Unix
Summary(fr):	Bibliothèque sonore libmikmod
Summary(pl):	libmikmod - biblioteka do obs³ugi d¼wiêku dla ró¿nych Unixów
Name:		libmikmod
Version:	3.1.9
Release:	2
License:	LGPL
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://mikmod.darkorb.net/libmikmod/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
URL:		http://mikmod.darkorb.net/
BuildRequires:	gettext-devel >= 0.10.35-9
BuildRequires:	esound-devel
BuildRequires:	audiofile-devel
%ifnarch sparc sparc64
BuildRequires:	alsa-devel
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libmikmod is a portable sound library, capable of playing samples as
well as module files, originally written by Jean-Paul Mikkers (MikMak)
for DOS. It has subsequently been hacked by many hands and now runs on
many Unix flavours.

It uses the OSS /dev/dsp driver including in all recent kernels for
output, as well as ALSA and EsounD, and will also write wav files.

Supported file formats include mod, stm, s3m, mtm, xm, and it. Full
source included, use of this library for music/sound effects in your
own programs is encouraged !

%description -l fr
Une bibliothèque sonore portable pour Unix et d'autres systèmes,
capable de jouer aussi bien des effets sonores que des modules, sur un
grand choix de périphériques sonores.

%description -l pl
Biblioteka d¼wiêku dla Unixa i innych systemów, umo¿liwiaj±ca
odtwarzanie sampli i modu³ów d¼wiêkowych na wielu rodzajach urz±dzeñ
d¼wiêkowych.

%package devel
Summary:	Libraries and include files to develop libmikmod applications
Summary(fr):	Bibliothèques et includes pour programmer pour libmikmod
Summary(pl):	Biblioteki i pliki nag³ówkowe dla libmikmod
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Libraries and include files to develop libmikmod applications.

%description devel -l fr
Bibliothèques et includes pour programmer pour libmikmod.

%description devel -l pl
Biblioteki i pliki nag³ówkowe do tworzenia aplikacji dla libmikmod.

%package static
Summary:	Static libmikmod libraries
Summary(fr):	Bibliothèques statiques libmikmod
Summary(pl):	Biblioteki statyczne libmikmod
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libmikmod libraries.

%description static -l fr
Bibliothèques statiques libmikmod.

%description static -l pl
Biblioteki statyczne libmikmod.

%prep
%setup -q 
%patch -p0

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-alsa \
	--enable-esd \
	--enable-oss
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT{%{_infodir},%{_mandir}/man1}/* \
	AUTHORS NEWS PROBLEMS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,PROBLEMS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/libmikmod-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/*.la

%{_mandir}/man1/libmikmod-config.1*
%{_infodir}/mikmod*
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
