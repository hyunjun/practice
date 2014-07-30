# IPython

## usage
```
$ ipython notebook --ip=[x.y.z.w] --port=[port num] --pylab=inline --notebook-dir=[dir]
```

## installation
* CentOS6.3
```
# pip install numpy scipy matplotlib pandas sympy nose pyzmq jinja2 ipython
```
  * prerequisite for scipy
  ```
  # wget http://mirror.centos.org/centos/6/os/x86_64/Packages/atlas-devel-3.8.4-2.el6.x86_64.rpm
  # wget http://mirror.centos.org/centos/6/os/x86_64/Packages/blas-devel-3.2.1-4.el6.x86_64.rpm
  # wget http://mirror.centos.org/centos/6/os/x86_64/Packages/lapack-devel-3.2.1-4.el6.x86_64.rpm
  # rpm -ivh atlas-devel-3.8.4-2.el6.x86_64.rpm
  # yum install blas
  # rpm -ivh blas-devel-3.2.1-4.el6.x86_64.rpm
  # yum install lapack
  # rpm -ivh lapack-devel-3.2.1-4.el6.x86_64.rpm
  ```
  * enthought; failed
    * https://www.enthought.com/products/epd/free/

