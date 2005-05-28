Summary:	Desktop Search Engine for Linux
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
BuildRequires:	sqlite3-devel
BuildRequires:	rpmbuild(macros) >= 1.129
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
%attr(755,root,root) %{_libdir}/lib*.so.*
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_libdir}/kde3/*.la
%{_desktopdir}/kde/*.desktop
%{_datadir}/apps/kat
%{_datadir}/mimelnk/application/*.desktop
%{_datadir}/services/*.*
%{_datadir}/servicetypes/*.*
%{_iconsdir}/*/*/apps/*.png
