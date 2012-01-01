# NOTE: original package name is flux, but flux.spec is already occupied by fluxlib.org
Summary:	flux - interface description language used by DirectFB
Summary(pl.UTF-8):	flux - język opisu interfejsów używany przez DirectFB
Name:		DirectFB-flux
Version:	1.1.0
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://www.directfb.org/downloads/Core/flux/flux-%{version}.tar.gz
# Source0-md5:	25b3d11628d907019e1b7e7d1fb09ad7
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
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
