Summary:	Html2Wml - a Perl program that converts HTML documents to WML
Summary(pl.UTF-8):	Html2Wml - program w Perlu konwertujący dokumenty HTML do WML-a
Name:		html2wml
Version:	0.4.11
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://maddingue.free.fr/softwares/download/Html2Wml/%{name}-%{version}.tar.gz
# Source0-md5:	a65c1d6bb9c5e0a12113bcee33762f12
URL:		http://html2wml.org/
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-Text-Template
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov
Requires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Html2Wml is a Perl program that converts HTML documents to WML decks,
i.e. documents that are viewable on a Wap device.

%description -l pl.UTF-8
Html2Wml to program w Perlu konwertujący dokumenty HTML do dokumentów
WML, które można oglądać na urządzeniach WAP.

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
