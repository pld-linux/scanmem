Summary:	Interactive debugging utility
Name:		scanmem
Version:	0.07
Release:	1
License:	GPL v2
Group:		Development/Debuggers
Source0:	http://taviso.decsystem.org/files/scanmem/%{name}-%{version}.tar.gz
# Source0-md5:	a28baa2cf69b58b2773e379a49dae11c
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
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
