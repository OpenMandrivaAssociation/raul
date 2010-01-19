%define major 3
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		raul
Version:	0.6.0
Release:	%mkrel 1
Summary:	Realtime Audio Utility Library
License:	GPLv2+
Group:		System/Libraries
Url:		http://drobilla.net/software/raul/
Source0:	http://download.drobilla.net/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	waf
BuildRequires:	boost-devel
BuildRequires:	glib2-devel >= 2.2

%description
Raul (Realtime Audio Utility Library) is a C++ utility library 
primarily aimed at audio/musical applications.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}

Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Raul (Realtime Audio Utility Library) is a C++ utility library
primarily aimed at audio/musical applications.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++

Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{develname}
This package contains development files for %{name}.

%prep
%setup -q

%build
%setup_compile_flags
%__waf configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir}

%__waf build

%install
rm -rf %{buildroot}
%waf_install

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_libdir}/lib%{name}.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
