# Git Commands — Complete Reference

A handy cheat sheet of the most useful Git commands, grouped by topic.

---

## 1. Setup & Configuration

```bash
git config --global user.name "Your Name"      # set your name
git config --global user.email "you@mail.com"  # set your email
git config --global core.editor "code --wait"  # set default editor
git config --list                              # view all settings
git --version                                  # check Git version
```

---

## 2. Starting a Repository

```bash
git init                       # create a new repo in current folder
git clone <url>                # copy a remote repo locally
git clone <url> <folder>       # clone into a specific folder
```

---

## 3. Basic Snapshotting (everyday workflow)

```bash
git status                     # show changed/staged files
git add <file>                 # stage one file
git add .                      # stage everything
git add -p                     # stage changes chunk by chunk
git reset <file>               # unstage a file (keep changes)
git commit -m "message"        # commit staged changes
git commit -am "message"       # stage tracked files + commit
git commit --amend             # edit the last commit
```

---

## 4. Viewing Changes & History

```bash
git diff                       # unstaged changes
git diff --staged              # staged changes
git log                        # full commit history
git log --oneline              # compact history
git log --oneline --graph --all  # visual branch graph
git show <commit>              # details of a commit
git blame <file>               # who changed each line
```

---

## 5. Branching

```bash
git branch                     # list branches
git branch <name>              # create a branch
git checkout <name>            # switch to a branch
git checkout -b <name>         # create + switch
git switch <name>              # switch (newer syntax)
git switch -c <name>           # create + switch (newer syntax)
git merge <name>               # merge branch into current
git branch -d <name>           # delete a branch
git branch -D <name>           # force-delete a branch
git branch -m <old> <new>      # rename a branch
```

---

## 6. Remote Repositories

```bash
git remote -v                  # list remotes
git remote add origin <url>    # link a remote
git push                       # push commits
git push -u origin main        # push + set upstream (first time)
git push origin <branch>       # push a specific branch
git pull                       # fetch + merge from remote
git fetch                      # download changes (no merge)
git remote remove origin       # remove a remote
```

---

## 7. Undoing Things

```bash
git restore <file>             # discard unstaged changes in a file
git restore --staged <file>    # unstage a file
git checkout -- <file>         # discard changes (older syntax)
git reset --soft HEAD~1        # undo last commit, keep changes staged
git reset --mixed HEAD~1       # undo last commit, keep changes unstaged
git reset --hard HEAD~1        # undo last commit, DISCARD changes
git revert <commit>            # make a new commit that undoes one
git clean -fd                  # delete untracked files & folders
```

---

## 8. Stashing (save work temporarily)

```bash
git stash                      # save uncommitted changes
git stash list                 # list stashes
git stash pop                  # restore + remove newest stash
git stash apply                # restore but keep the stash
git stash drop                 # delete newest stash
git stash clear                # delete all stashes
```

---

## 9. Tags (mark releases)

```bash
git tag                        # list tags
git tag v1.0                   # create a lightweight tag
git tag -a v1.0 -m "Release"   # create an annotated tag
git push origin v1.0           # push a tag
git push origin --tags         # push all tags
```

---

## 10. Inspecting & Comparing

```bash
git diff branchA..branchB      # compare two branches
git log branchA..branchB       # commits in B not in A
git shortlog -sn               # commit count per author
git reflog                     # history of HEAD (recover lost commits)
```

---

## 11. Handy Shortcuts

```bash
git log --oneline -5           # last 5 commits
git commit --amend --no-edit   # add to last commit, keep message
git checkout -                 # switch to previous branch
git rm <file>                  # remove + stage deletion
git mv <old> <new>             # rename + stage
```

---

### Quick everyday flow

```bash
git status
git add .
git commit -m "Describe what changed"
git push
```

> Tip: run `git status` often — it tells you exactly what state you're in
> and usually suggests the command you need next.
