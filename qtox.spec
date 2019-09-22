%global commit          af02542e05992bf94fcff37c365f638ad7b53d8d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20190922
# git describe
%global qtox_version    v1.16.3-652-gaf02542e

Name:       qtox
Version:    1.16.3
Release:    1.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:    Feature-rich Tox client

# Main program: GPLv3+
# src/widget/flowlayout.*: BSD
# Smileys/Universe Smileys/emojione: CC-BY
# Smileys/Classic: CC-BY-SA
License:    GPLv3+ and BSD and CC-BY and CC-BY-SA
URL:        https://github.com/qTox/qTox/
Source0:    %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

# Remove project_group tag from appdata.xml
Patch0:     qTox-af02542-remove_project_group.patch
# Remove -Werror from compile flags
Patch1:     qTox-af02542-disable_Werror.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  qtsingleapplication
BuildRequires:  pkgconfig(toxcore) >= 0.2.10
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
Requires:       toxcore >= 0.2.10

%description
qTox is a powerful Tox client that follows the Tox design
guidelines while running on all major platforms.

%prep
%autosetup -p1 -n qTox-%{commit}

%build
mkdir build && cd build
%cmake -DSVGZ_ICON=OFF \
       -DGIT_DESCRIBE=%{qtox_version} \
       -DGIT_VERSION=%{commit} \
       ..
%make_build

%install
cd build
%make_install

%check
cd build
ctest -V %{?_smp_mflags} ||:
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
* Sun Sep 22 19:59:25 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.16.3-1.20190922gitaf02542
- Pre-release af02542e05992bf94fcff37c365f638ad7b53d8d

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 1.16.2-4
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.16.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 17 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.16.2-1
- Upstream release 1.16.2

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
