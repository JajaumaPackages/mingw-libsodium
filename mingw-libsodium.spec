%?mingw_package_header

Name:           mingw-libsodium
Version:        1.0.12
Release:        1%{?dist}
Summary:        MinGW port of libsodium

License:        ISC license
URL:            http://doc.libsodium.org/
Source0:        http://download.libsodium.org/libsodium/releases/libsodium-%{version}.tar.gz

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc

BuildArch:      noarch

%description
MinGW Windows port of libsodium.

# Win32
%package -n mingw32-libsodium
Summary:        32-bit version of libsodium for Windows

%description -n mingw32-libsodium
%mingw32_description

# Win64
%package -n mingw64-libsodium
Summary:        64-bit version of libsodium for Windows

%description -n mingw64-libsodium
%mingw64_description

%?mingw_debug_package

%prep
%setup -qn libsodium-%{version}

%build
%mingw_configure --disable-silent-rules
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{mingw32_bindir}/*.def
rm -f %{buildroot}%{mingw32_libdir}/*.la
rm -f %{buildroot}%{mingw64_bindir}/*.def
rm -f %{buildroot}%{mingw64_libdir}/*.la


# Win32
%files -n mingw32-libsodium
%{mingw32_bindir}/libsodium-18.dll
%{mingw32_includedir}/sodium.h
%{mingw32_includedir}/sodium/
%{mingw32_libdir}/libsodium.a
%{mingw32_libdir}/libsodium.dll.a
%{mingw32_libdir}/pkgconfig/libsodium.pc

# Win64
%files -n mingw64-libsodium
%{mingw64_bindir}/libsodium-18.dll
%{mingw64_includedir}/sodium.h
%{mingw64_includedir}/sodium/
%{mingw64_libdir}/libsodium.a
%{mingw64_libdir}/libsodium.dll.a
%{mingw64_libdir}/pkgconfig/libsodium.pc

%changelog
* Sun Apr 09 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.0.12-1
- Initial release
