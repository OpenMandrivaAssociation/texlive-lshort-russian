# revision 18906
# category Package
# catalog-ctan /info/lshort/russian
# catalog-date 2006-12-28 00:06:45 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-lshort-russian
Version:	20061228
Release:	10
Summary:	Russian introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/russian
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-russian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-russian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061228-2
+ Revision: 753480
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061228-1
+ Revision: 718900
- texlive-lshort-russian
- texlive-lshort-russian
- texlive-lshort-russian
- texlive-lshort-russian

