Name:           perl-CryptX
Version:        0.063
Release:        1%{?dist}
Summary:        Cryptographic toolkit (self-contained, no external libraries needed)
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CryptX/
Source0:        http://www.cpan.org/authors/id/M/MI/MIK/CryptX-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Cryptography in CryptX is based on https://github.com/libtom/libtomcrypt

%prep
%setup -q -n CryptX-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE META.json README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/CryptX*
%{perl_vendorarch}/Crypt/*
%{perl_vendorarch}/Math/*
%{_mandir}/man3/*

%changelog
* Tue Mar 19 2019 Johannes Grumboeck <johannes.grumboeck@porscheinformatik.at> 0.063-1
- Specfile autogenerated by cpanspec 1.78.
