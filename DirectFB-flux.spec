# NOTE: original package name is flux, but flux.spec is already occupied by fluxlib.org
Summary:	flux - interface description language used by DirectFB
Summary(pl.UTF-8):	flux - język opisu interfejsów używany przez DirectFB
Name:		DirectFB-flux
Version:	1.4.4
Release:	5
License:	MIT
Group:		Development/Tools
Source0:	http://www.directfb.net/downloads/Core/flux/flux-%{version}.tar.gz
# Source0-md5:	49e8c11ea1b7894edfa18dd00cfe419c
URL:		http://www.directfb.net/
BuildRequires:	DirectFB-devel >= 1:1.6.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
Requires:	DirectFB >= 1:1.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
flux is an interface description language used by DirectFB.

fluxcomp compiles .flux files to .cpp or .c files.

%description -l pl.UTF-8
flux to język opisu interfejsów używany przez DirectFB.

fluxcomp kompiluje pliki .flux do plików .cpp lub .c.

%prep
%setup -q -n flux-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/fluxcomp
