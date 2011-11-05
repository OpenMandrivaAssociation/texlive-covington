# revision 17750
# category Package
# catalog-ctan /macros/latex/contrib/covington
# catalog-date 2010-04-05 22:57:39 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-covington
Version:	20100405
Release:	1
Summary:	Linguistic support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/covington
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/covington.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/covington.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Numerous minor LaTeX enhancements for linguistics, including
multiple accents on the same letter, interline glosses (word-
by-word translations), Discourse Representation Structures, and
example numbering.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/covington/covington.sty
%doc %{_texmfdistdir}/doc/latex/covington/covington.pdf
%doc %{_texmfdistdir}/doc/latex/covington/covington.tex
%doc %{_texmfdistdir}/doc/latex/covington/covingtonGerm.pdf
%doc %{_texmfdistdir}/doc/latex/covington/covingtonGerm.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
