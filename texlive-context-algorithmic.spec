# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-algorithmic
# catalog-date 2009-11-09 14:30:19 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-algorithmic
Version:	20091109
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3

%description
Support for typesetting algorithms.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_mtxrun_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
	%_texmf_mtxrun_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/algorithmic/t-algorithmic.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
