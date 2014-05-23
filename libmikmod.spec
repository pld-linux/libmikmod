#
# Conditional build:
%bcond_without	alsa		# ALSA support
%bcond_with	esd		# EsounD support
%bcond_with	nas		# NAS support
%bcond_with	openal		# OpenAL support
%bcond_without	pulseaudio	# PulseAudio support
%bcond_with	sdl		# SDL support

Summary:	libmikmod - a portable sound library for Unix
Summary(es.UTF-8):	Biblioteca de sonidos libmikmod
Summary(fr.UTF-8):	Bibliothèque sonore libmikmod
Summary(pl.UTF-8):	libmikmod - biblioteka do obsługi dźwięku dla różnych Uniksów
Summary(pt_BR.UTF-8):	Biblioteca de som libmikmod
Summary(ru.UTF-8):	Звуковая библиотека libmikmod
Summary(uk.UTF-8):	Звукова бібліотека libmikmod
Name:		libmikmod
Version:	3.3.6
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/mikmod/%{name}-%{version}.tar.gz
# Source0-md5:	9dd9bed30c6f7607a55480234606071b
Patch0:		%{name}-info.patch
URL:		http://mikmod.raphnet.net/
%{?with_openal:BuildRequires:	OpenAL-devel}
%{?with_sdl:BuildRequires:	SDL2-devel >= 2.0.0}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
%{?with_esd:BuildRequires:	esound-devel >= 0.2.18}
BuildRequires:	gettext-devel >= 0.10.35-9
BuildRequires:	libtool
%{?with_nas:BuildRequires:	nas-devel}
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel}
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

%description -l es.UTF-8
Biblioteca de sonidos libmikmod.

%description -l fr.UTF-8
Une bibliothèque sonore portable pour Unix et d'autres systèmes,
capable de jouer aussi bien des effets sonores que des modules, sur un
grand choix de périphériques sonores.

%description -l pl.UTF-8
Biblioteka dźwięku dla Uniksa i innych systemów, umożliwiająca
odtwarzanie sampli i modułów dźwiękowych na wielu rodzajach urządzeń
dźwiękowych.

Wspierane formaty plików to między innymi mod, stm, s3m, mtm, xm i it.

%description -l pt_BR.UTF-8
Uma biblioteca de som portátil para o Unix e outros sistemas
operacionais, capaz de tocar samples agem de arquivos .mod, em uma
grande variedade de dispositivos de som.

%description -l ru.UTF-8
Мобильная звуковая библиотека для *nix, умеющая проигрывать сэмплы и
MOD'ы на большом количестве звуковых устройств.

%description -l uk.UTF-8
Переносима звукова бібліотека для *nix, здатна програвати семпли та
"модулі" на великій кількості звукових пристроїв.

%package devel
Summary:	Include files to develop libmikmod applications
Summary(es.UTF-8):	Archivos de inclusión para desarrollar aplicaciones libmikmod
Summary(fr.UTF-8):	Includes pour programmer pour libmikmod
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmikmod
Summary(pt_BR.UTF-8):	Arquivos de inclusão para desenvolver aplicações libmikmod
Summary(ru.UTF-8):	.h-файлы для разработки libmikmod-приложений
Summary(uk.UTF-8):	.h-файли для розробки програм, що користуються libmikmod
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libmikmod2-devel

%description devel
Include files to develop libmikmod applications.

%description devel -l es.UTF-8
Archivos de inclusión para desarrollar aplicaciones libmikmod.

%description devel -l fr.UTF-8
Includes pour programmer pour libmikmod.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji wykorzystujących bibliotekę
libmikmod.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para desenvolver aplicações libmikmod.

%description devel -l ru.UTF-8
.h-файлы для разработки libmikmod-приложений.

%description devel -l uk.UTF-8
.h-файли для розробки програм, що користуються libmikmod.

%package static
Summary:	Static libmikmod library
Summary(fr.UTF-8):	Bibliothèques statiques libmikmod
Summary(pl.UTF-8):	Biblioteka statyczna libmikmod
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libmikmod
Summary(ru.UTF-8):	Статические библиотеки для разработки libmikmod-приложений
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм, що користуються libmikmod
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmikmod library.

%description static -l fr.UTF-8
Bibliothèques statiques libmikmod.

%description static -l pl.UTF-8
Biblioteka statyczna libmikmod.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libmikmod.

%description static -l ru.UTF-8
Статические библиотеки для разработки libmikmod-приложений.

%description static -l uk.UTF-8
Статичні бібліотеки для розробки програм, що користуються libmikmod.

%prep
%setup -q
%patch0 -p0

%if %{without esd}
echo 'AC_DEFUN([AM_PATH_ESD],[$3])' >> acinclude.m4
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
# note: audiofile (af) driver is for DEC AudioFile server (libAF), not libaudiofile library;
# libgus was an ancient (Linux < 2.2) GUS support library ("ultra" package)
%configure \
	%{!?with_alsa:--disable-alsa} \
	%{!?with_esound:--disable-esd} \
	%{?with_nas:--enable-nas} \
	%{?with_openal:--enable-openal} \
	--enable-oss \
	%{!?with_pulseaudio:--disable-pulseaudio} \
	%{?with_sdl:--enable-sdl}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/libmikmod.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmikmod.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libmikmod-config
%attr(755,root,root) %{_libdir}/libmikmod.so
%{_libdir}/libmikmod.la
%{_includedir}/mikmod.h
%{_pkgconfigdir}/libmikmod.pc
%{_aclocaldir}/libmikmod.m4
%{_mandir}/man1/libmikmod-config.1*
%{_infodir}/mikmod.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libmikmod.a
