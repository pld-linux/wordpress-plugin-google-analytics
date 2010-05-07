%define		plugin	google-analytics-for-wordpress
Summary:	Google Analytics plugin for WordPress
Name:		wordpress-plugin-google-analytics
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/Publishing
URL:		http://wordpress.org/extend/plugins/google-analytics-for-wordpress/
# Use DF or something. On each download it has new md5.
# Source0:	http://downloads.wordpress.org/plugin/%{plugin}.zip
Source0:	http://execve.pl/PLD/%{plugin}.zip
# Source0-md5:	9c9abd877fc326d489a80eed40537847
BuildRequires:	js
BuildRequires:	unzip
BuildRequires:	yuicompressor
Requires:	wordpress >= 2.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wordpressdir	%{_datadir}/wordpress
%define		pluginssubdir	wp-content/plugins
%define		pluginsdir		%{wordpressdir}/%{pluginssubdir}
%define		plugindir		%{pluginsdir}/%{plugin}

%description
Google analytics plugin easily adds your Google Analytics tracking
code to all pages within your blog. That's it's main functionality, it
adds a few "extra's" though:
  - Tagging outgoing links
  - Tracking downloads
  - Tracking AdSense clicks
  - Tracking image search keywords
  - Tracking original searches for Yahoo!'s Search Assistant
  - Adding extra search engines
  - Urchin

%prep
%setup -q -n %{plugin}

mkdir build

%build
yuicompressor yst_plugin_tools.css > build/yst_plugin_tools.css
yuicompressor custom_se_async.js > build/custom_se_async.js
js -C -f build/custom_se_async.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a *.php *.png $RPM_BUILD_ROOT%{plugindir}
cp -a images $RPM_BUILD_ROOT%{plugindir}
cp -a build/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{plugindir}
