#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spatstat.data
Version  : 2.1.0
Release  : 37
URL      : https://cran.r-project.org/src/contrib/spatstat.data_2.1-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spatstat.data_2.1-0.tar.gz
Summary  : Datasets for 'spatstat' Family
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-spatstat.utils
BuildRequires : R-spatstat.utils
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n spatstat.data
cd %{_builddir}/spatstat.data

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616432214

%install
export SOURCE_DATE_EPOCH=1616432214
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.data
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.data
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spatstat.data
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc spatstat.data || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spatstat.data/DESCRIPTION
/usr/lib64/R/library/spatstat.data/INDEX
/usr/lib64/R/library/spatstat.data/Meta/Rd.rds
/usr/lib64/R/library/spatstat.data/Meta/data.rds
/usr/lib64/R/library/spatstat.data/Meta/features.rds
/usr/lib64/R/library/spatstat.data/Meta/hsearch.rds
/usr/lib64/R/library/spatstat.data/Meta/links.rds
/usr/lib64/R/library/spatstat.data/Meta/nsInfo.rds
/usr/lib64/R/library/spatstat.data/Meta/package.rds
/usr/lib64/R/library/spatstat.data/NAMESPACE
/usr/lib64/R/library/spatstat.data/R/spatstat.data
/usr/lib64/R/library/spatstat.data/R/spatstat.data.rdb
/usr/lib64/R/library/spatstat.data/R/spatstat.data.rdx
/usr/lib64/R/library/spatstat.data/data/Rdata.rdb
/usr/lib64/R/library/spatstat.data/data/Rdata.rds
/usr/lib64/R/library/spatstat.data/data/Rdata.rdx
/usr/lib64/R/library/spatstat.data/doc/packagesizes.txt
/usr/lib64/R/library/spatstat.data/help/AnIndex
/usr/lib64/R/library/spatstat.data/help/aliases.rds
/usr/lib64/R/library/spatstat.data/help/macros/defns.Rd
/usr/lib64/R/library/spatstat.data/help/paths.rds
/usr/lib64/R/library/spatstat.data/help/spatstat.data.rdb
/usr/lib64/R/library/spatstat.data/help/spatstat.data.rdx
/usr/lib64/R/library/spatstat.data/html/00Index.html
/usr/lib64/R/library/spatstat.data/html/R.css
/usr/lib64/R/library/spatstat.data/rawdata/amacrine/amacrine.txt
/usr/lib64/R/library/spatstat.data/rawdata/finpines/finpines.txt
/usr/lib64/R/library/spatstat.data/rawdata/gorillas/vegetation.asc
/usr/lib64/R/library/spatstat.data/rawdata/osteo/osteo36.txt
/usr/lib64/R/library/spatstat.data/rawdata/sandholes/sandholes.jpg
/usr/lib64/R/library/spatstat.data/rawdata/vesicles/activezone.txt
/usr/lib64/R/library/spatstat.data/rawdata/vesicles/mitochondria.txt
/usr/lib64/R/library/spatstat.data/rawdata/vesicles/presynapse.txt
/usr/lib64/R/library/spatstat.data/rawdata/vesicles/vesicles.csv
/usr/lib64/R/library/spatstat.data/rawdata/vesicles/vesicles.txt
/usr/lib64/R/library/spatstat.data/rawdata/vesicles/vesiclesimage.tif
/usr/lib64/R/library/spatstat.data/rawdata/vesicles/vesiclesmask.tif
/usr/lib64/R/library/spatstat.data/rawdata/vesicles/vesicleswindow.csv
/usr/lib64/R/library/spatstat.data/rawdata/vesicles/vesicleswindow.txt
