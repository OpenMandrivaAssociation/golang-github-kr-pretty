%global debug_package %{nil}

# Run tests in check section
%bcond_without check

# https://github.com/kr/pretty
%global goipath		github.com/kr/pretty
%global forgeurl	https://github.com/kr/pretty
Version:		0.3.1

%gometa

Summary:	Pretty printing for Go values
Name:		golang-github-kr-pretty

Release:	1
Source0:	https://github.com/kr/pretty/archive/v%{version}/pretty-%{version}.tar.gz
URL:		https://github.com/kr/pretty
License:	MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
BuildRequires:	golang(github.com/kr/text)
BuildRequires:	golang(github.com/rogpeppe/go-internal/fmtsort)
BuildArch:	noarch

%description
Pretty printing for Go values.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license License
%doc Readme

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n pretty-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

