%include	/usr/lib/rpm/macros.perl
Summary:	Html2Wml - a Perl program that converts HTML documents to WML
Summary(pl):	Html2Wml - program w Perlu konwertuj±cy dokumenty HTML do WML-a
Name:		html2wml
Version:	0.4.10
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://maddingue.free.fr/softwares/download/Html2Wml/%{name}-%{version}.tar.gz
# Source0-md5:	855947a5e4287fe9d4fd87abfee7f760
URL:		http://html2wml.org
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-Text-Template
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
Requires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Html2Wml is a Perl program that converts HTML documents to WML decks,
i.e. documents that are viewable on a Wap device. 

%description -l pl
Html2Wml to program w Perlu konwertuj±cy dokumenty HTML do dokumentów
WML, które mo¿na ogl±daæ na urz±dzeniach WAP.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS NOTES README TODO doc/readme.html
%attr(755,root,root) %{_bindir}/*
