Name:           filotimo-plymouth-theme
Version:        0.5
Release:        1%{?dist}
Summary:        Jimmac's spinner theme using the ACPI BGRT graphics as background - customised for Filotimo Linux

License:        GPL-2.0
URL:            https://github.com/filotimo-project/plymouth-theme
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       rsms-inter-fonts
Requires:       plymouth
Requires:       plymouth-scripts
Requires:       filotimo-branding

%description
Jimmac's spinner theme using the ACPI BGRT graphics as background - customised for Filotimo Linux.
Uses the Breeze cog as a spinner. Requires filotimo-branding for the watermark.

%define debug_package %{nil}

%prep
%setup -q

%build

%install
install -pm 0644 %{SOURCE0} LICENSE
cd src
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/filotimo
cp ./* %{buildroot}%{_datadir}/plymouth/themes/filotimo

%files
%license LICENSE
%dir %{_datadir}/plymouth/themes/filotimo
%{_datadir}/plymouth/themes/filotimo/*.png
%{_datadir}/plymouth/themes/filotimo/filotimo.plymouth

%post
plymouth-set-default-theme filotimo

%changelog
* Sat Feb 01 2025 Thomas Duckworth <tduck973564@gmail.com> 0.5-1
- fix loading icon (tduck973564@gmail.com)

* Thu Dec 19 2024 Thomas Duckworth <tduck973564@gmail.com> 0.4-3
- fix spec (tduck973564@gmail.com)

* Thu Dec 19 2024 Thomas Duckworth <tduck973564@gmail.com>
- fix spec (tduck973564@gmail.com)

* Thu Dec 19 2024 Thomas Duckworth <tduck973564@gmail.com>
- fix spec (tduck973564@gmail.com)

* Thu Dec 19 2024 Thomas Duckworth <tduck973564@gmail.com> 0.4-2
- new package built with tito

* Sat Jun 22 2024 Thomas Duckworth <tduck973564@gmail.com> 0.4-1
- update for branding release (tduck973564@gmail.com)

* Sat Jun 22 2024 Thomas Duckworth <tduck973564@gmail.com> 0.3-1
- Change fonts and size (tduck973564@gmail.com)

* Sat Jun 22 2024 Thomas Duckworth <tduck973564@gmail.com> 0.2-1
- Add post scriptlet for setting theme as default (tduck973564@gmail.com)

* Sat Jun 22 2024 Thomas Duckworth <tduck973564@gmail.com> 0.1-1
- new package built with tito
