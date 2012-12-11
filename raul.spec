%define major 10
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		raul
Version:	0.8.0
Release:	2
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
./waf configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir}

./waf build

%install
rm -rf %{buildroot}
./waf install --destdir=%{buildroot}
chmod 0755 %{buildroot}%{_libdir}/libraul.so.%{major}*

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_libdir}/lib%{name}.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-2mdv2011.0
+ Revision: 614701
- the mass rebuild of 2010.1 packages

* Tue Jan 19 2010 Jérôme Brenier <incubusss@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 493777
- import raul


