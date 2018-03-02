Name:       qtox
Version:    1.13.0
Release:    2%{?dist}
Summary:    Feature-rich Tox client

# Main program: GPLv3+
# src/widget/flowlayout.*: BSD
# Smileys/Universe Smileys/emojione: CC-BY
# Smileys/Classic: CC-BY-SA
License:    GPLv3+ and BSD and CC-BY and CC-BY-SA
URL:        https://github.com/qTox/qTox/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Remove project_group tag from appdata.xml
Patch0:     qtox-1.11.0-remove_project_group.patch
# Remove -Werror from compile flags
Patch1:     qtox-1.12.1-disable_Werror.patch
# https://github.com/qTox/qTox/issues/4958
Patch2:     0001-Move-Appdata-file-installation-to-usr-share-metainfo.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  qtsingleapplication
BuildRequires:  pkgconfig(libtoxcore)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(filteraudio)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  qt5-linguist
Requires:       hicolor-icon-theme


%description
qTox is a powerful Tox client that follows the Tox design 
guidelines while running on all major platforms. 


%prep
%autosetup -p1 -n qTox-%{version}


%build
mkdir build && cd build
%cmake ..
%make_build


%install
cd build
%make_install

# unzip qtox.svgz
gzip -dS z %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/qtox.svgz


%check
cd build
ctest -V %{?_smp_mflags}
desktop-file-validate %{buildroot}%{_datadir}/applications/qtox.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/qTox.appdata.xml


%files
%license LICENSE smileys/Universe/LICENSE-GRAPHICS
%doc README.md CHANGELOG.md
%{_bindir}/qtox
%{_datadir}/metainfo/qTox.appdata.xml
%{_datadir}/applications/qtox.desktop
%{_datadir}/icons/hicolor/*/apps/qtox.*


%changelog
* Fri Feb 16 2018 Robert-André Mauchin <zebob.m@gmail.com> 1.13.0-2
- Spec file refresh
- Move Appdata to metainfo

* Mon Nov 27 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.13.0-1
- New upstream release 1.13.0

* Thu Oct 12 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.12.1-1
- New upstream release 1.12.1

* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.11.0-2
- Fix typo

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> 1.11.0-1
- First RPM release

