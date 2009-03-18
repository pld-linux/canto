Summary:	Canto is an Atom/RSS feed reader for the console
Summary(hu.UTF-8):	Canto egy Atom/RSS hírolvasó konzolra
Name:		canto
Version:	0.6.7
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://codezen.org/static/%{name}-%{version}.tar.gz
# Source0-md5:	fc8e6d9c788270363814534baa193e55
URL:		http://www.codezen.org/canto
BuildRequires:	ncurses-devel
BuildRequires:	python-devel >= 2.4.0
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-chardet
Requires:	python-feedparser
Obsoletes:	nrss
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Canto is an Atom/RSS feed reader for the console that is meant to be
quick, concise, and colorful. It's meant to allow you to crank through
feeds like you've never cranked before by providing a minimal, yet
information packed interface. No navigating menus. No dense blocks of
unreadable white text. An interface with almost infinite customization
and extensibility using the excellent Python programming language.

%description -l hu.UTF-8
Canto egy Atom/RSS olvasó konzolra, azaz gyors, tömör és színes.
Egy nagyon egyszerű felüleletet biztosít. Nincsenek menük,
nincsenek sűrű képernyőrészek olvashatatlan fehér szöveggel.
Egy interfész, amely majdnem a végtelenségig beállítható és
bővíthető a Python programozási nyelv segítségével.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--prefix=%{_prefix} \
	--root=$RPM_BUILD_ROOT

# Hack to set correctly VERSION_TUPLE
rm -f $RPM_BUILD_ROOT%{py_sitedir}/canto/*.py{c,o}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}/canto
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/canto

%py_postclean

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}-fetch
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-fetch.1*
%{py_sitedir}/Canto-*.egg-info
%dir %{py_sitedir}/canto
%attr(755,root,root) %{py_sitedir}/canto/widecurse.so
%{py_sitedir}/canto/*.py[co]
