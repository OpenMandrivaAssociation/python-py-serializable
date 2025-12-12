Name:		python-py-serializable
Version:	2.1.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/py-serializable/py_serializable-%{version}.tar.gz
Summary:	Library for serializing and deserializing Python Objects to and from JSON and XML.
URL:		https://pypi.org/project/py-serializable/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python%{pyver}dist(poetry-core)
BuildSystem:	python
BuildArch:	noarch

%description
Library for serializing and deserializing Python Objects to and from JSON and XML.

%files
%{py_sitedir}/py_serializable
%{py_sitedir}/py_serializable-*.*-info
