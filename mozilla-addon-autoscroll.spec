Summary:	Automatic scrolling functionality
Summary(pl):	Automatyczne przewijanie
%define		_realname	autoscroll
Name:		mozilla-addon-%{_realname}
Version:	1.0
Release:	3
License:	MPL 1.1/GPL 2.0/LGPL 2.1
Group:		X11/Applications/Networking
Source0:	http://home.jesus.ox.ac.uk/~ecatmur/projects/mozilla/%{_realname}.xpi
# Source0-md5:	ab274fec67e8697d6f5f7bd1676be82f
Source1:	http://lednerg.home.comcast.net/%{_realname}_icons.zip
# Source1-md5:	359b61e2fadb43e560634da8cfe34ba8
Source2:	%{_realname}-installed-chrome.txt
URL:		http://home.jesus.ox.ac.uk/~ecatmur/projects/mozilla/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
AutoScroll is an addon for Mozilla and Phoenix and possibly other
browsers which support XPI packages that emulates the autoscrolling
functionality of Internet Explorer. For those unfamiliar with this,
when you middle click on a page (typically by clicking a mouse wheel
button) you can then move the mouse up and down to have the page
scroll by you without further mouse movements.

%description -l pl
AutoScroll jest dodatkiem do Mozilli i Phoeniksa oraz prawdopodobnie
innych przegl±darek obs³uguj±cych pakiety XPI, który emuluje
funkcjonalno¶æ autoprzewijania znan± z Internet Explorera. Klikniêcie
¶rodkowym przyciskiem myszy na stronie (zazwyczaj przez naci¶niêcie
rolki) i ruch myszy w którym¶ kierunku powoduje przewijanie strony bez
konieczno¶ci wykonywania kolejnych ruchów mysz±.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
unzip -o %{SOURCE1} -d $RPM_BUILD_ROOT%{_chromedir}/%{_realname}/content
install %{SOURCE2} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}
%{_chromedir}/%{_realname}-installed-chrome.txt
