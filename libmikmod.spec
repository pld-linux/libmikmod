#
# Conditional build:
%bcond_with	alsa	# with ALSA; warning: SIGSEGV while using oss
#
Summary:	libmikmod - a portable sound library for Unix
Summary(es):	Biblioteca de sonidos libmikmod
Summary(fr):	Bibliothèque sonore libmikmod
Summary(pl):	libmikmod - biblioteka do obs³ugi d¼wiêku dla ró¿nych Unixów
Summary(pt_BR):	Biblioteca de som libmikmod
Summary(ru):	ú×ÕËÏ×ÁÑ ÂÉÂÌÉÏÔÅËÁ libmikmod
Summary(uk):	ú×ÕËÏ×Á Â¦ÂÌ¦ÏÔÅËÁ libmikmod
Name:		libmikmod
Version:	3.1.10
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://www.mikmod.org/files/libmikmod/%{name}-%{version}.tar.gz
# Source0-md5: 14bf3f18cf0187f5dab46e42a3ddda84
Patch0:		%{name}-info.patch
Patch1:		%{name}-AC_LIBOBJ.patch
Patch2:		%{name}-am18.patch
URL:		http://www.mikmod.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel >= 0.10.35-9
BuildRequires:	esound-devel
BuildRequires:	audiofile-devel
BuildRequires:	texinfo
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libmikmod2

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

%description -l es
Biblioteca de sonidos libmikmod.

%description -l fr
Une bibliothèque sonore portable pour Unix et d'autres systèmes,
capable de jouer aussi bien des effets sonores que des modules, sur un
grand choix de périphériques sonores.

%description -l pl
Biblioteka d¼wiêku dla Unixa i innych systemów, umo¿liwiaj±ca
odtwarzanie sampli i modu³ów d¼wiêkowych na wielu rodzajach urz±dzeñ
d¼wiêkowych.

Wspierane formaty plików to miêdzy innymi mod, stm, s3m, mtm, xm i it.

%description -l pt_BR
Uma biblioteca de som portátil para o Unix e outros sistemas
operacionais, capaz de tocar samples agem de arquivos .mod, em uma
grande variedade de dispositivos de som.

%description -l ru
íÏÂÉÌØÎÁÑ Ú×ÕËÏ×ÁÑ ÂÉÂÌÉÏÔÅËÁ ÄÌÑ *nix, ÕÍÅÀÝÁÑ ÐÒÏÉÇÒÙ×ÁÔØ ÓÜÍÐÌÙ É
MOD'Ù ÎÁ ÂÏÌØÛÏÍ ËÏÌÉÞÅÓÔ×Å Ú×ÕËÏ×ÙÈ ÕÓÔÒÏÊÓÔ×.

%description -l uk
ðÅÒÅÎÏÓÉÍÁ Ú×ÕËÏ×Á Â¦ÂÌ¦ÏÔÅËÁ ÄÌÑ *nix, ÚÄÁÔÎÁ ÐÒÏÇÒÁ×ÁÔÉ ÓÅÍÐÌÉ ÔÁ
"ÍÏÄÕÌ¦" ÎÁ ×ÅÌÉË¦Ê Ë¦ÌØËÏÓÔ¦ Ú×ÕËÏ×ÉÈ ÐÒÉÓÔÒÏ§×.

%package devel
Summary:	Libraries and include files to develop libmikmod applications
Summary(es):	Archivos de inclusión y bibliotecas para desarrollar aplicaciones libmikmod
Summary(fr):	Bibliothèques et includes pour programmer pour libmikmod
Summary(pl):	Biblioteki i pliki nag³ówkowe dla libmikmod
Summary(pt_BR):	Arquivos de inclusão e bibliotecas para desenvolver aplicações libmikmod
Summary(ru):	.h-ÆÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ libmikmod-ÐÒÉÌÏÖÅÎÉÊ
Summary(uk):	.h-ÆÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ËÏÒÉÓÔÕÀÔØÓÑ libmikmod
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libmikmod2-devel

%description devel
Libraries and include files to develop libmikmod applications.

%description devel -l es
Archivos de inclusión y bibliotecas para desarrollar aplicaciones
libmikmod.

%description devel -l fr
Bibliothèques et includes pour programmer pour libmikmod.

%description devel -l pl
Biblioteki i pliki nag³ówkowe do tworzenia aplikacji dla libmikmod.

%description devel -l pt_BR
Arquivos de inclusão e bibliotecas para desenvolver aplicações
libmikmod.

%description devel -l ru
.h-ÆÁÊÌÙ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ libmikmod-ÐÒÉÌÏÖÅÎÉÊ.

%description devel -l uk
.h-ÆÁÊÌÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ËÏÒÉÓÔÕÀÔØÓÑ libmikmod.

%package static
Summary:	Static libmikmod libraries
Summary(fr):	Bibliothèques statiques libmikmod
Summary(pl):	Biblioteki statyczne libmikmod
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com libmikmod
Summary(ru):	óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ libmikmod-ÐÒÉÌÏÖÅÎÉÊ
Summary(uk):	óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ËÏÒÉÓÔÕÀÔØÓÑ libmikmod
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libmikmod libraries.

%description static -l fr
Bibliothèques statiques libmikmod.

%description static -l pl
Biblioteki statyczne libmikmod.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com libmikmod.

%description static -l ru
óÔÁÔÉÞÅÓËÉÅ ÂÉÂÌÉÏÔÅËÉ ÄÌÑ ÒÁÚÒÁÂÏÔËÉ libmikmod-ÐÒÉÌÏÖÅÎÉÊ.

%description static -l uk
óÔÁÔÉÞÎ¦ Â¦ÂÌ¦ÏÔÅËÉ ÄÌÑ ÒÏÚÒÏÂËÉ ÐÒÏÇÒÁÍ, ÝÏ ËÏÒÉÓÔÕÀÔØÓÑ libmikmod.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/{config.*,missing} .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	%{!?with_alsa:--disable-alsa}%{?with_alsa:--enable-alsa} \
	--enable-esd \
	--enable-oss
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libmikmod-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%{_mandir}/man1/libmikmod-config.1*
%{_infodir}/mikmod*
%{_includedir}/*
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
