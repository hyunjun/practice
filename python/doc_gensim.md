# gensim

## install
* proxy if necessary
```
# export http_proxy=http://xxx.yyy.zzz.www:pp; export https_proxy=https://xxx.yyy.zzz.www:pp
```
* prerequisite: atlas, blas, lapack
  * centos6 rpms; http://mirror.centos.org/centos/6/os/x86_64/Packages/
  ```
  # wget http://mirror.centos.org/centos/6/os/x86_64/Packages/atlas-devel-3.8.4-2.el6.x86_64.rpm
  # wget http://mirror.centos.org/centos/6/os/x86_64/Packages/blas-devel-3.2.1-4.el6.x86_64.rpm
  # wget http://mirror.centos.org/centos/6/os/x86_64/Packages/lapack-devel-3.2.1-4.el6.x86_64.rpm
  # rpm -ivh atlas-devel-3.8.4-2.el6.x86_64.rpm
  # rpm -ivh blas-devel-3.2.1-4.el6.x86_64.rpm
  # rpm -ivh lapack-devel-3.2.1-4.el6.x86_64.rpm
  ```
  * error message without these; ...libraries mkl,vml,guide not found...
* install gensim using pip
```
# pip install gensim
```
* etc
  * https://github.com/luispedro/BuildingMachineLearningSystemsWithPython
  * http://stackoverflow.com/questions/11863775/python-scipy-install-on-ubuntu
  * https://groups.google.com/forum/#!topic/theano-users/zQAE51j59hk
  * http://stackoverflow.com/questions/11863775/python-scipy-install-on-ubuntu
