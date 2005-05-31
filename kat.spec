Summary:	Desktop Search Engine for Linux
Summary(pl):	Silnik wyszukiwania dla Linuksa
Name:		kat
Version:	0.5.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kat/%{name}-%{version}.tar.gz
# Source0-md5:	f5785ac5126032a8f673640135b820e7
URL:		http://kat.sourceforge.net/
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	poppler-qt-devel >= 0.3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kat is an application for KDE designed to index files. Meta
information, fulltext and thumbnails are extracted from documents,
images, mp3 and other media allowing quick and accurate information
retrieval. Similar to the Windows application WhereIsIt, but also
similar to Google Desktop Search, Kat is completely written in C++,
using Qt3, KDE and KIO libraries. The application is based on the
extensible kfile plugin architecture of KDE in order to facilitate the
creation of new media managers for emerging file formats. Kat is the
first KDE application using the new fulltext kfile plugins.

%description -l pl
Kat to aplikacja dla KDE przeznaczona do indeksowania plik�w. Wydobywa
metainformacje, pe�ny tekst oraz miniaturki z dokument�w, obrazk�w,
mp3 i innych medi�w umo�liwiaj�c szybkie i dok�adne odtwarzanie
informacji. Podobnie do windowsowej aplikacji WhereIsIt, a tak�e
podobnie do Google Desktop Search, Kat jest napisany ca�kowicie w C++
przy u�yciu bibliotek Qt3, KDE i KIO. Aplikacja jest oparta na
rozszerzalnej architekturze wtyczek kfile z KDE, aby u�atwi� tworzenie
nowych zarz�dc�w medi�w dla pojawiaj�cych si� format�w plik�w. Kat to
pierwsza aplikacja KDE u�ywaj�ca nowych pe�notekstowych wtyczek kfile.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* admin
%configure \
	--disable-rpath \
	--enable-final \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{name} --with-kde

rm -rf $RPM_BUILD_ROOT%{_datadir}/apps/katepart

%clean
rm -fr $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_desktopdir}/kde/*.desktop
%{_datadir}/apps/kat
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/services/*.*
%{_datadir}/servicetypes/*.*
%{_iconsdir}/*/*/apps/*.png