Name:       qtscenegraph-adaptation
Summary:    Scenegraph adaptation from playground
Version:    git
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        https://qt.gitorious.org/qtplayground/scenegraph
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qmake
BuildRequires:  pkgconfig(android-headers)
BuildRequires:  pkgconfig(libhardware)
BuildRequires:  fdupes

%description
This package contains system specific changes for the
Qt Quick Scene Graph.

#### Build section

%prep
%setup -q -n %{name}-%{version}

%build
export QTDIR=/usr/share/qt5
%qmake5 -config "animationdriver programbinary eglgralloctexture" "INCLUDEPATH+=/usr/lib/droid-devel/droid-headers/"

%install
rm -rf %{buildroot}
%qmake5_install

#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig




#### File section
%files
%defattr(-,root,root,-)
%{_libdir}/qt5/plugins/scenegraph/libcustomcontext.so


#### No changelog section, separate $pkg.changelog contains the history
