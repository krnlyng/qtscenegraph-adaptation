Name:       qtscenegraph-adaptation
Summary:    Scenegraph adaptation from playground
Version:    git
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qmake
BuildRequires:  droid-system-sbj-devel
BuildRequires:  fdupes
BuildRequires:  libhybris-sbj-libhardware-devel

%description
This package contains system specific changes for the
Qt Quick Scene Graph.

#### Build section

%prep
%setup -q -n %{name}-%{version}

%build
export QTDIR=/usr/share/qt5
%qmake5 -config "animationdriver programbinary eglgralloctexture" "INCLUDEPATH+=/usr/include/droid-sbj /usr/include/droid-sbj/android"

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
