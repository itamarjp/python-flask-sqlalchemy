%global mod_name Flask-SQLAlchemy

Name:           python-flask-sqlalchemy
Version:        0.14
Release:        1%{?dist}
Summary:        Adds SQLAlchemy support to Flask application

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/mitsuhiko/flask-sqlalchemy
Source0:        http://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-flask

%description
Flask-SQLAlchemy is an extension for Flask that adds support for
SQLAlchemy to your application. It aims to simplify using SQLAlchemy with 
Flask by providing useful defaults and extra helpers that make it easier 
to accomplish common tasks.

%prep
%setup -q -n %{mod_name}-%{version}
rm -f docs/_static/.DS_Store
rm -f docs/.DS_Store
rm -f docs/_themes/.gitignore
chmod -x docs/_static/flask-sqlalchemy-small.png

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc docs/ README CHANGES LICENSE PKG-INFO

%{python_sitelib}/*-nspkg.pth
%{python_sitelib}/*.egg-info/
%{python_sitelib}/flaskext/

%changelog
* Thu Jul 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.14-1
- Initial RPM release