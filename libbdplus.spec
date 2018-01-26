%global commit0 795a9e43d904f948c096dbe34a8e647177b5bb2a
%global date 20170409
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           libbdplus
Version:        0.1.2
Release:        1%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:        Open implementation of BD+ protocol
License:        LGPLv2+
URL:            http://www.videolan.org/developers/%{name}.html

#Source0:        ftp://ftp.videolan.org/pub/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source0:        %{name}-%{shortcommit0}.tar.xz
Source1:        %{name}-snapshot.sh

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(libaacs) >= 0.7.0

%description
libbdplus is a research project to implement the BD+ System Specifications.
This research project provides, through an open-source library, a way to
understand how the BD+ protocol works.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -n %{name}

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete
mkdir -p %{buildroot}%{_sysconfdir}/xdg/bdplus

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog README.txt
%{_libdir}/*.so.*
%{_sysconfdir}/xdg/bdplus

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 25 2018 Simone Caronni <negativo17@gmail.com> - 0.1.2-2.20170409git795a9e4
- First build.
