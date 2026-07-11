%global tl_name covington
%global tl_revision 77216

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.16
Release:	%{tl_revision}.1
Summary:	LaTeX macros for Linguistics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/covington
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/covington.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/covington.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Numerous minor LaTeX enhancements for linguistics, including multiple
accents on the same letter, interline glosses (word-by-word
translations), Discourse Representation Structures, and example
numbering.

