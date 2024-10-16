#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
# autospec version: v20
# autospec commit: 4d029647d79e
#
Name     : ndpi
Version  : 4.0
Release  : 19
URL      : https://github.com/ntop/nDPI/archive/4.0/nDPI-4.0.tar.gz
Source0  : https://github.com/ntop/nDPI/archive/4.0/nDPI-4.0.tar.gz
Summary  : deep packet inspection library
Group    : Development/Tools
License  : GPL-2.0 LGPL-3.0
Requires: ndpi-bin = %{version}-%{release}
Requires: ndpi-data = %{version}-%{release}
Requires: ndpi-lib = %{version}-%{release}
Requires: ndpi-license = %{version}-%{release}
BuildRequires : file
BuildRequires : libgcrypt-dev
BuildRequires : libpcap-dev
BuildRequires : numactl-dev
BuildRequires : pkgconfig(json-c)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-library-install-location.patch

%description
=== HOMEBREW PACKAGE ===
NB: Work in progress
- SUBMIT FORMULA
cp ndpi.rb /usr/local/Library/Formula/

%package bin
Summary: bin components for the ndpi package.
Group: Binaries
Requires: ndpi-data = %{version}-%{release}
Requires: ndpi-license = %{version}-%{release}

%description bin
bin components for the ndpi package.


%package data
Summary: data components for the ndpi package.
Group: Data

%description data
data components for the ndpi package.


%package dev
Summary: dev components for the ndpi package.
Group: Development
Requires: ndpi-lib = %{version}-%{release}
Requires: ndpi-bin = %{version}-%{release}
Requires: ndpi-data = %{version}-%{release}
Provides: ndpi-devel = %{version}-%{release}
Requires: ndpi = %{version}-%{release}

%description dev
dev components for the ndpi package.


%package lib
Summary: lib components for the ndpi package.
Group: Libraries
Requires: ndpi-data = %{version}-%{release}
Requires: ndpi-license = %{version}-%{release}

%description lib
lib components for the ndpi package.


%package license
Summary: license components for the ndpi package.
Group: Default

%description license
license components for the ndpi package.


%prep
%setup -q -n nDPI-4.0
cd %{_builddir}/nDPI-4.0
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728610824
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%autogen --disable-static
make  %{?_smp_mflags}

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728610824
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ndpi
cp %{_builddir}/nDPI-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ndpi/e203d4ef09d404fa5c03cf6590e44231665be689 || :
cp %{_builddir}/nDPI-%{version}/packages/ubuntu/debian/COPYRIGHT %{buildroot}/usr/share/package-licenses/ndpi/dfac199a7539a404407098a2541b9482279f690d || :
export GOAMD64=v2
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/bin/ndpi/ndpiCustomCategory.txt
rm -f %{buildroot}*/usr/bin/ndpi/ndpiProtos.txt

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ndpiReader

%files data
%defattr(-,root,root,-)
/usr/share/ndpi/ndpiCustomCategory.txt
/usr/share/ndpi/ndpiProtos.txt

%files dev
%defattr(-,root,root,-)
/usr/include/ndpi/ndpi_api.h
/usr/include/ndpi/ndpi_classify.h
/usr/include/ndpi/ndpi_config.h
/usr/include/ndpi/ndpi_define.h
/usr/include/ndpi/ndpi_encryption.h
/usr/include/ndpi/ndpi_includes.h
/usr/include/ndpi/ndpi_includes_OpenBSD.h
/usr/include/ndpi/ndpi_main.h
/usr/include/ndpi/ndpi_patricia_typedefs.h
/usr/include/ndpi/ndpi_protocol_ids.h
/usr/include/ndpi/ndpi_protocols.h
/usr/include/ndpi/ndpi_typedefs.h
/usr/include/ndpi/ndpi_unix.h
/usr/include/ndpi/ndpi_utils.h
/usr/include/ndpi/ndpi_win32.h
/usr/lib64/libndpi.so
/usr/lib64/pkgconfig/libndpi.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libndpi.so.4
/usr/lib64/libndpi.so.4.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ndpi/dfac199a7539a404407098a2541b9482279f690d
/usr/share/package-licenses/ndpi/e203d4ef09d404fa5c03cf6590e44231665be689
