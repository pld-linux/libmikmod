%define		ver	3.1.7
%define		rel	d
Summary:	libmikmod sound library
Summary(fr):	Biblioth�que sonore libmikmod
Summary(pl):	Biblioteka d�wi�ku libmikmod
Name:		libmikmod
Version:	%{ver}%{rel}
Release:	5
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		http://www.multimania.com/miodrag/libmikmod/%{name}-%{ver}.tar.gz
Patch0:		libmikmod-%{ver}-a.patch
Patch1:		libmikmod-%{ver}-b.patch
Patch2:		libmikmod-%{ver}-c.patch
Patch3:		libmikmod-%{ver}-d.patch
Patch4:		libmikmod-info.patch
URL:		http://http://www.multimania.com/miodrag/mikmod/
BuildRequires:	gettext-devel >= 0.10.35-9
BuildRequires:	alsa-devel
BuildRequires:	esound-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
A portable sound library for Unix and other systems, capable of playing samples
as well as module files, on a wide range of sound devices.

%description -l fr
Une biblioth�que sonore portable pour Unix et d'autres syst�mes, capable de
jouer aussi bien des effets sonores que des modules, sur un grand choix de
p�riph�riques sonores.

%description -l pl
Biblioteka d�wi�ku dla Unixa i innych system�w, umo�liwiaj�ca odtwarzanie 
sampli i modu��w d�wi�kowych na wielu rodzajach urz�dze� d�wi�kowych.

%package devel
Summary:	Libraries and include files to develop libmikmod applications
Summary(fr):	Biblioth�ques et includes pour programmer pour libmikmod
Summary(pl):	Biblioteki i pliki nag��wkowe dla libmikmod
Group:		Development/Libraries
Group(pl):	Progamowanie/Biblioteki
Prereq:		/usr/sbin/fix-info-dir
Requires:	%{name} = %{version}

%description devel
Libraries and include files to develop libmikmod applications.

%description devel -l fr
Biblioth�ques et includes pour programmer pour libmikmod.

%description devel -l pl
Biblioteki i pliki nag��wkowe do tworzenia aplikacji dla libmikmod.

%package static
Summary:        Static libmikmod libraries
Summary(fr):	Biblioth�ques statiques libmikmod
Summary(pl):    Biblioteki statyczne libmikmod
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki
Requires:       %{name}-devel = %{version}

%description static
Static libmikmod libraries.

%description static -l fr
Biblioth�ques statiques libmikmod.

%description static -l pl
Biblioteki statyczne libmikmod.

%prep
%setup -q -n %{name}-%{ver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-alsa \
	--enable-esd \
	--enable-oss
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so.*.*

gzip -9nf $RPM_BUILD_ROOT{%{_infodir},%{_mandir}/man1}/* \
	AUTHORS NEWS PROBLEMS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun devel
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,PROBLEMS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/libmikmod-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/*.la

%{_mandir}/man1/libmikmod-config.1.gz
%{_infodir}/mikmod*
%{_includedir}/*
%{_datadir}/aclocal/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
