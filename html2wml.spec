Summary:	Html2Wml - a Perl program that converts HTML documents to WML
Summary(pl):	Html2Wml - program w Perlu konwertuj�cy dokumenty HTML do WML-a
Name:		html2wml
Version:	0.4.10
Release:	1
License:	GPL
Group:		Applications/Networking
Buildarch:	noarch
Source0:	http://maddingue.free.fr/softwares/download/Html2Wml/%{name}-%{version}.tar.gz
# Source0-md5:	855947a5e4287fe9d4fd87abfee7f760
URL:		http://html2wml.org
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Text::Template)
Requires:	perl(XML::Parser)
Requires:	perl(Text::Template)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Html2Wml is a Perl program that converts HTML documents to WML decks,
i.e. documents that are viewable on a Wap device. 

%description -l pl
Html2Wml to program w Perlu konwertuj�cy dokumenty HTML do dokument�w
WML, kt�re mo�na ogl�da� na urz�dzeniach WAP.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/man/* $RPM_BUILD_ROOT%{_mandir}
rm $RPM_BUILD_ROOT/man -r
mv $RPM_BUILD_ROOT/bin/* $RPM_BUILD_ROOT%{_bindir}
rm $RPM_BUILD_ROOT/bin -r

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/*
%attr(755,root,root) %{_bindir}/*
