%global mod_name Flask-SQLAlchemy
%if 0%{?fedora}
# there's no python3 in el*, disabling the python3 build
%global with_python3 1
%endif

Name:           python-flask-sqlalchemy
Version:        2.1
Release:        5%{?dist}
Summary:        Adds SQLAlchemy support to Flask application

Group:          Development/Libraries
License:        BSD
URL:            http://github.com/mitsuhiko/flask-sqlalchemy
Source0:        http://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-flask
Requires:       python-sqlalchemy

%description
Flask-SQLAlchemy is an extension for Flask that adds support for
SQLAlchemy to your application. It aims to simplify using SQLAlchemy with
Flask by providing useful defaults and extra helpers that make it easier
to accomplish common tasks.

%package -n python2-flask-sqlalchemy
Summary:        Adds SQLAlchemy support to Flask application
%{?python_provide:%python_provide python2-%{mod_name}}
%{?python_provide:%python_provide python2-flask-sqlalchemy}
BuildRequires:  python2-devel
%if 0%{?fedora}
BuildRequires:  python2-setuptools
%else
BuildRequires:  python-setuptools
%endif
BuildRequires:  python-flask
BuildRequires:  python-sqlalchemy
Requires:       python-flask
Requires:       python-sqlalchemy

%description -n python2-flask-sqlalchemy
Flask-SQLAlchemy is an extension for Flask that adds support for
SQLAlchemy to your application. It aims to simplify using SQLAlchemy with
Flask by providing useful defaults and extra helpers that make it easier
to accomplish common tasks.

Python 2 version.

%if 0%{?with_python3}
%package -n python3-flask-sqlalchemy
Summary:        Adds SQLAlchemy support to Flask application
%{?python_provide:%python_provide python3-%{mod_name}}
%{?python_provide:%python_provide python3-flask-sqlalchemy}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-flask
BuildRequires:  python3-sqlalchemy
Requires:       python3-flask
Requires:       python3-sqlalchemy

%description -n python3-flask-sqlalchemy
Flask-SQLAlchemy is an extension for Flask that adds support for
SQLAlchemy to your application. It aims to simplify using SQLAlchemy with
Flask by providing useful defaults and extra helpers that make it easier
to accomplish common tasks.

Python 3 version.
%endif # with_python3

%prep
%setup -q -n %{mod_name}-%{version}
rm -f docs/_static/.DS_Store
rm -f docs/.DS_Store
rm -f docs/_themes/.gitignore
chmod -x docs/_static/flask-sqlalchemy-small.png

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%check
%{__python2} setup.py test

%if 0%{?with_python3}
%{__python3} setup.py test
%endif
 
%files -n python2-flask-sqlalchemy
%license LICENSE
%doc docs/ README CHANGES PKG-INFO
%{python2_sitelib}/*.egg-info/
%{python2_sitelib}/flask_sqlalchemy/

%if 0%{?with_python3}
%files -n python3-flask-sqlalchemy
%license LICENSE
%doc docs/ README CHANGES PKG-INFO
%{python3_sitelib}/*.egg-info/
%{python3_sitelib}/flask_sqlalchemy/
%endif # with_python3

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1-1
- Update to 2.1
- Follow new packaging guidelines
- Run tests

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 10 2014 Tim Flink <tflink@fedoraproject.org> - 2.0-1
- enable python3 builds only for fedora - there's no python3 in el*

* Wed Dec 10 2014 Tim Flink <tflink@fedoraproject.org> - 2.0-1
- Upgraded to upstream 2.0
- Enhanced internal signal control, made more customizable and less global to play nice with non-flask-sqlalchemy sessions

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 21 2014 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0-2
- Fixed #1055251

* Wed Aug 07 2013 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 1.0-1
- Upgraded to upstream 1.0 and added python3 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Tim Flink <tflink@fedoraproject.ort> - 0.16-1
- Upgraded to upstream 0.16

* Tue Aug 21 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.14-4
- Added python-sqlalchemy as requires

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.14-1
- Initial RPM release
