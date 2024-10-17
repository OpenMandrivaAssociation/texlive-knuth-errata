Name:		texlive-knuth-errata
Version:	58682
Release:	2
Summary:	Knuth's published errata
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/knuth-errata
License:	knuth
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-errata.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-errata.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These files record details of problems reported in Knuth's
'Computers and Typesetting' series of books, for the Computer
Modern fonts, and for TeX, Metafont and related programs.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/generic/knuth-errata

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
