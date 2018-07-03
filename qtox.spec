Name:       qtox
Version:    1.16.0
Release:    1%{?dist}
Summary:    Feature-rich Tox client

# Main program: GPLv3+
# src/widget/flowlayout.*: BSD
# Smileys/Universe Smileys/emojione: CC-BY
# Smileys/Classic: CC-BY-SA
License:    GPLv3+ and BSD and CC-BY and CC-BY-SA
URL:        https://github.com/qTox/qTox/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Remove project_group tag from appdata.xml
Patch0:     qtox-1.16.0-remove_project_group.patch
# Remove -Werror from compile flags
Patch1:     qtox-1.12.1-disable_Werror.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  qtsingleapplication
BuildRequires:  pkgconfig(toxcore)
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
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.qtox.qTox.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/io.github.qtox.qTox.appdata.xml


%files
%license LICENSE smileys/Universe/LICENSE-GRAPHICS
%doc README.md CHANGELOG.md
%{_bindir}/qtox
%{_datadir}/metainfo/io.github.qtox.qTox.appdata.xml
%{_datadir}/applications/io.github.qtox.qTox.desktop
%{_datadir}/icons/hicolor/*/apps/qtox.*


%changelog
* Tue Jul 03 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.16.0-1
- Upstream release 1.16.0

* Tue Jun 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-3
- Rebuilt for toxcore soname bump

* Thu May 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-2
- Rebuild with new Toxcore

* Thu Apr 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.15.0-1
- Upstream release 1.15.0

* Thu Apr 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.14.1-1
- Upstream release 1.14.1

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

