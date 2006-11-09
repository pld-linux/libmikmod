#
# Conditional build:
%bcond_with	alsa	# with ALSA; warning: SIGSEGV while using oss
#
%define		_ver	3.1.11
Summary:	libmikmod - a portable sound library for Unix
Summary(es):	Biblioteca de sonidos libmikmod
Summary(fr):	BibliothХque sonore libmikmod
Summary(pl):	libmikmod - biblioteka do obsЁugi d╪wiЙku dla rС©nych UniksСw
Summary(pt_BR):	Biblioteca de som libmikmod
Summary(ru):	Звуковая библиотека libmikmod
Summary(uk):	Звукова б╕бл╕отека libmikmod
Name:		libmikmod
Version:	%{_ver}a
Release:	3
License:	LGPL
Group:		Libraries
#Source0Download: http://mikmod.raphnet.net/
Source0:	http://mikmod.raphnet.net/files/%{name}-%{_ver}.tar.gz
# Source0-md5:	705106da305e8de191549f1e7393185c
Source1:	http://mikmod.raphnet.net/files/%{name}-3.1.11-a.diff
# Source1-md5:	5e56be5a32eecf3cfa195379a5ecb0ef
Patch0:		%{name}-info.patch
Patch1:		%{name}-AC_LIBOBJ.patch
URL:		http://mikmod.raphnet.net/
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	audiofile-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-devel >= 0.10.35-9
BuildRequires:	libtool
BuildRequires:	texinfo
Obsoletes:	libmikmod2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libmikmod is a portable sound library, capable of playing samples as
well as module files, originally written by Jean-Paul Mikkers (MikMak)
for DOS. It has subsequently been hacked by many hands and now runs on
many Unix flavours.

It uses the OSS /dev/dsp driver including in all recent kernels for
output, as well as ALSA and EsounD, and will also write WAV files.

Supported file formats include mod, stm, s3m, mtm, xm, and it. Full
source included, use of this library for music/sound effects in your
own programs is encouraged !

%description -l es
Biblioteca de sonidos libmikmod.

%description -l fr
Une bibliothХque sonore portable pour Unix et d'autres systХmes,
capable de jouer aussi bien des effets sonores que des modules, sur un
grand choix de pИriphИriques sonores.

%description -l pl
Biblioteka d╪wiЙku dla Uniksa i innych systemСw, umo©liwiaj╠ca
odtwarzanie sampli i moduЁСw d╪wiЙkowych na wielu rodzajach urz╠dzeЯ
d╪wiЙkowych.

Wspierane formaty plikСw to miЙdzy innymi mod, stm, s3m, mtm, xm i it.

%description -l pt_BR
Uma biblioteca de som portАtil para o Unix e outros sistemas
operacionais, capaz de tocar samples agem de arquivos .mod, em uma
grande variedade de dispositivos de som.

%description -l ru
Мобильная звуковая библиотека для *nix, умеющая проигрывать сэмплы и
MOD'ы на большом количестве звуковых устройств.

%description -l uk
Переносима звукова б╕бл╕отека для *nix, здатна програвати семпли та
"модул╕" на велик╕й к╕лькост╕ звукових пристро╖в.

%package devel
Summary:	Libraries and include files to develop libmikmod applications
Summary(es):	Archivos de inclusiСn y bibliotecas para desarrollar aplicaciones libmikmod
Summary(fr):	BibliothХques et includes pour programmer pour libmikmod
Summary(pl):	Biblioteki i pliki nagЁСwkowe dla libmikmod
Summary(pt_BR):	Arquivos de inclusЦo e bibliotecas para desenvolver aplicaГУes libmikmod
Summary(ru):	.h-файлы для разработки libmikmod-приложений
Summary(uk):	.h-файли для розробки програм, що користуються libmikmod
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libmikmod2-devel

%description devel
Libraries and include files to develop libmikmod applications.

%description devel -l es
Archivos de inclusiСn y bibliotecas para desarrollar aplicaciones
libmikmod.

%description devel -l fr
BibliothХques et includes pour programmer pour libmikmod.

%description devel -l pl
Biblioteki i pliki nagЁСwkowe do tworzenia aplikacji dla libmikmod.

%description devel -l pt_BR
Arquivos de inclusЦo e bibliotecas para desenvolver aplicaГУes
libmikmod.

%description devel -l ru
.h-файлы для разработки libmikmod-приложений.

%description devel -l uk
.h-файли для розробки програм, що користуються libmikmod.

%package static
Summary:	Static libmikmod libraries
Summary(fr):	BibliothХques statiques libmikmod
Summary(pl):	Biblioteki statyczne libmikmod
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com libmikmod
Summary(ru):	Статические библиотеки для разработки libmikmod-приложений
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки програм, що користуються libmikmod
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmikmod libraries.

%description static -l fr
BibliothХques statiques libmikmod.

%description static -l pl
Biblioteki statyczne libmikmod.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com libmikmod.

%description static -l ru
Статические библиотеки для разработки libmikmod-приложений.

%description static -l uk
Статичн╕ б╕бл╕отеки для розробки програм, що користуються libmikmod.

%prep
%setup -q -n %{name}-%{_ver}
%{__patch} -p1 < %{SOURCE1}
%patch0 -p0
%patch1 -p1

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
