%define _empty_manifest_terminate_build 0

Name:       nwg-panel
Version:    0.10.11
Release:    1
Summary:    GTK3-based panel for sway window manager and Hyprland Wayland compositors
Group:      System/X11/Utilities/NWG 
License:    MIT
URL:        https://github.com/nwg-piotr/nwg-panel
Source0:     https://github.com/nwg-piotr/nwg-panel/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

 
BuildRequires: pkgconfig(python)
BuildRequires: python3dist(setuptools)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildArch:  noarch
 
Requires:   typelib(GtkLayerShell)
Requires:   gtk+3.0
Requires:   python-gobject3
Requires:   python-gi
Requires:   python3dist(i3ipc)
Requires:   wlr-randr
# Missing in OMV
#Recommends: light
Requires: playerctl
#Recommends: pamixer
Recommends: python3dist(netifaces)
Recommends: python3dist(psutil)
Recommends: python3dist(pybluez)
 
 
%description
I have been using sway since 2019 and find it the most comfortable working
environment, but... Have you ever missed all the graphical bells and whistles
in your panel, we used to have in tint2? It happens to me. That's why I
decided to try to code a GTK-based panel, including best features from my two
favourites: Waybar and tint2. Many thanks to Developers and Contributors of
the both projects!
 
There are 8 modules available at the moment, and I don't plan on many more.
Basis system controls are available in the Controls module, and whatever else
you may need, there's an executor for that.
 
 
%prep
%autosetup -p1
 
#sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
#    nwg_panel/executors/arch_updates.py
 
 
%build
%py_build
 
%install
%py_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_bindir}/nwg-dwl-interface
%{_bindir}/nwg-processes
%{python_sitelib}/nwg_panel-*-py%{python_version}.egg-info/
%{python_sitelib}/nwg_panel/
