Name:		texlive-lshort-russian
Version:	20061228
Release:	1
Summary:	Russian introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/russian
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-russian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-russian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Russian version of A Short Introduction to LaTeX2e.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-russian/lshortru.pdf
%doc %{_texmfdistdir}/doc/latex/lshort-russian/lshortru.zip

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
