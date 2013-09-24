%global packname  flexclust
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3.4
Release:          1
Summary:          Flexible Cluster Algorithms
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/flexclust_1.3-4.tar.gz
Requires:         R-graphics R-grid R-lattice R-modeltools R-methods
Requires:         R-stats R-stats4 
Requires:         R-ellipse R-clue R-cluster R-seriation R-multicore R-snow
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-graphics
BuildRequires:    R-grid R-lattice R-modeltools R-methods R-stats R-stats4
BuildRequires:    R-ellipse R-clue R-cluster R-seriation R-multicore R-snow

%description
The main function kcca implements a general framework for k-centroids
cluster analysis supporting arbitrary distance measures and centroid
computation. Further cluster methods include hard competitive learning,
neural gas, and QT clustering. There are numerous visualization methods
for cluster results (neighborhood graphs, convex cluster hulls, barcharts
of centroids, ...), and bootstrap methods for the analysis of cluster

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

