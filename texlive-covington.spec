Name:		texlive-covington
Version:	67472
Release:	1
Summary:	Linguistic support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/covington
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/covington.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/covington.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/covington
%doc %{_texmfdistdir}/doc/latex/covington

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
