# Git

## Usage
* clone
  * usage
  ```
  git clone git@github.com:[id]/[repository].git
  git clone https://[id]@github.com:[id]/[repository].git
  ```
  * 공용 서버 계정과 각자 git 계정을 가지고 공동 개발을 하는 경우 https://gist.github.com/hyunjun/54fd1254451409c53db4
* remove untracked files
```
git clean -f
```
* svn revert
```
git checkout -- [src]
```
* transfer repository
  * git to git
    * create repository to move
    ```
    $ cd old_repo
    $ git remote -v
    origin  git@old.url:id/old_repo.git (fetch)
    origin  git@old.url:id/old_repo.git (push)
    $ git remote set-url origin git@new.url:id/new_repo.git
    $ git remote -v
    origin  git@new.url:id/new_repo.git (fetch)
    origin  git@new.url:id/new_repo.git (push)
    $ git push -u origin --all
    Counting objects: 74, done.
    Delta compression using up to 16 threads.
    Compressing objects: 100% (67/67), done.
    Writing objects: 100% (74/74), 163.78 KiB, done.
    Total 74 (delta 13), reused 0 (delta 0)
    To git@new.url:id/new_repo.git
     * [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
    $
    ```

## Error

## links
