# Generated from mysql-2.8.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mysql
%if 0%{?rhel} <= 6 && 0%{?fedora} <= 16
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_cache %{gem_dir}/cache
%global gem_libdir %{gem_instdir}/lib
%global gem_extdir %{_libdir}/gems/exts/%{gem_name}-%{version}
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%global rubyabi 1.8
%else
%global rubyabi 1.9.1
%endif

Summary: This is the MySQL API module for Ruby
Name: rubygem-%{gem_name}
Version: 2.9.1
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://mysql-win.rubyforge.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby >= 1.8.6

BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: rubygems
BuildRequires: ruby >= 1.8.6
BuildRequires: ruby-devel
BuildRequires: mysql-devel
%if 0%{?rhel} >= 7 && 0%{?fedora} >= 16
BuildRequires: rubygems-devel
%endif

Provides: rubygem(%{gem_name}) = %{version}

%description
This is the MySQL API module for Ruby. It provides the same functions for Ruby
programs that the MySQL C API provides for C programs.
This is a conversion of tmtm's original extension into a proper RubyGems.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem install --local --install-dir .%{gem_dir} \
            -V \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir}/lib
# TODO: move the extensions
##mv %{buildroot}%{gem_instdir}/lib/shared_object.so %{buildroot}%{gem_extdir}/lib/



# Remove the binary extension sources and build leftovers.
rm -rf %{buildroot}%{geminstdir}/ext

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir}
%exclude %{gem_cache}
%{gem_spec}
%{_libdir}/ruby/gems/%{rubyabi}/gems/mysql-%{version}/
%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.txt

%changelog
* Fri Jun 07 2013 Sergey Mihailov <sergey.mihailov@gmail.com> - 2.9.1-2
- Update release

* Thu Jun 14 2012 jason - 2.8.1-1
- Initial package
