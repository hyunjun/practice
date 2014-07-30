# Git

## Usage
* svn revert
```
git checkout -- [src]
```
* 저장소 이전
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
