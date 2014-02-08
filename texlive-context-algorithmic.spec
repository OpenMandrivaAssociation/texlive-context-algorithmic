# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-algorithmic
# catalog-date 2009-11-09 14:30:19 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-algorithmic
Version:	20091109
Release:	3
Summary:	Algorithm handling
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-algorithmic
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-algorithmic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
Support for typesetting algorithms.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/algorithmic/t-algorithmic.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091109-2
+ Revision: 750485
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091109-1
+ Revision: 718123
- texlive-context-algorithmic
- texlive-context-algorithmic
- texlive-context-algorithmic
- texlive-context-algorithmic

