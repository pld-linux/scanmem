# TODO:	package GUI
Summary:	Interactive debugging utility
Name:		scanmem
Version:	0.13
Release:	2
License:	GPL v3
Group:		Development/Debuggers
# v0.15.2 at	https://github.com/scanmem/scanmem/archive/v%{version}.tar.gz
Source0:	http://scanmem.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	1c23eda15db242ff0aac96d94be11db1
URL:		http://taviso.decsystem.org/scanmem.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scanmem is a simple interactive debugging utility for linux, used to
locate the address of a variable in an executing process. This can be
used for the analysis or modification of a hostile process on a
compromised machine, reverse engineering, or as a "pokefinder" to
cheat at video games.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
chmod +x configure
%configure \
	--enable-gui
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
