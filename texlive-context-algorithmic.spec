Name:		texlive-context-algorithmic
Version:	47085
Release:	2
Summary:	Algorithm handling in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-algorithmic
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-algorithmic.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
Support for typesetting algorithms (a port of the LaTeX package
algorithmic, which was a predecessor of algorithmicx).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/algorithmic/t-algorithmic.mkii
%{_texmfdistdir}/tex/context/third/algorithmic/t-algorithmic.mkiv

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
