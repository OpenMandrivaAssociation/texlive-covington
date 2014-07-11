# revision 34064
# category Package
# catalog-ctan /macros/latex/contrib/covington
# catalog-date 2014-05-16 17:18:37 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-covington
Version:	20140516
Release:	2
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

%description
Numerous minor LaTeX enhancements for linguistics, including
multiple accents on the same letter, interline glosses (word-
by-word translations), Discourse Representation Structures, and
example numbering.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/covington/covington.sty
%doc %{_texmfdistdir}/doc/latex/covington/covington.pdf
%doc %{_texmfdistdir}/doc/latex/covington/covington.tex
%doc %{_texmfdistdir}/doc/latex/covington/covingtonGerm.pdf
%doc %{_texmfdistdir}/doc/latex/covington/covingtonGerm.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
