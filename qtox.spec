Name:       qtox
Version:    1.17.6
Release:    9%{?dist}
Summary:    Feature-rich Tox client

# Main program: GPLv3+
# src/widget/flowlayout.*: BSD
# Smileys/Universe Smileys/emojione: CC-BY
# Smileys/Classic: CC-BY-SA
License:    GPLv3+ and BSD and CC-BY and CC-BY-SA
URL:        https://github.com/qTox/qTox/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Remove project_group tag from appdata.xml
Patch0:     qTox-c0e9a3b-remove_project_group.patch
Patch1:     qTox-1.17.6-ffmpeg7.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  kf5-sonnet-devel
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  pkgconfig(toxcore) >= 0.2.10
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  pkgconfig(filteraudio)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  qt5-linguist
Requires:       hicolor-icon-theme
Requires:       toxcore >= 0.2.10
Requires:       ffmpeg-libs

%description
qTox is a powerful Tox client that follows the Tox design
guidelines while running on all major platforms.

%prep
%autosetup -p1 -n qTox-%{version}

%build
%cmake \
 -DSVGZ_ICON=OFF \
 -DUPDATE_CHECK=OFF \
 -DGIT_DESCRIBE=%{version}
%cmake_build

%install
%cmake_install

%check
cd %{_vpath_builddir}
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
* Wed Nov 06 2024 Sérgio Basto <sergio@serjux.com> - 1.17.6-9
- Rebuild for ffmpeg-7
- Add qTox-1.17.6-ffmpeg7.patch (Mamoru TASAKA) from rfbz #7096

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Leigh Scott <leigh123linux@gmail.com> - 1.17.6-5
- Rebuild for new ffmpeg

* Wed Feb 08 2023 Leigh Scott <leigh123linux@gmail.com> - 1.17.6-4
- rebuilt

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Tue May 17 2022 Leigh Scott <leigh123linux@gmail.com> - 1.17.6-2
- Fix crash (rfbz#6301)

* Thu Apr 07 2022 Leigh Scott <leigh123linux@gmail.com> - 1.17.6-1
- Update to 1.17.6

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.17.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 12 2021 Leigh Scott <leigh123linux@gmail.com> - 1.17.3-5
- Rebuilt for new ffmpeg snapshot

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.17.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.17.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 1.17.3-2
- Rebuilt for new ffmpeg snapshot

* Sat Dec 05 22:19:55 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.17.3-1
- Update to 1.17.3

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.16.3-5.20191018gita44cce6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.16.3-4.20191018gita44cce6
- Rebuild for ffmpeg-4.3 git

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.16.3-3.20191018gita44cce6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 18 17:59:35 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.16.3-2.20191018gita44cce6
- Pre-release a44cce65beb60c5f280b651e0c084fa9c2bdb0dc
- Update BuildRequires

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
