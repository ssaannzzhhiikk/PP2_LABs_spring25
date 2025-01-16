Link GitHowTo: https://githowto.com/ru
1)Install git


Give the name and E-mail to User
```
git config --global user.name "Your Name"
git config --global user.email "your_email@whatever.com"
```

2

```
mkdir work    (Creates the file called "work", "make directory")
cd work       (chooses the file "work")
touch hello.html   (creates empty file in "work", !works only with Mac/Unix)
for Win ( echo > hello.html )
```

```
git init      (creates repository)

git add file_name    (adds the file to "idexation", and makes it ready to be added to fixation)

git reset     (in order to cancel)

 git commit -m "Initial Commit"   (saves the changes, "-m" means message)

```

3
```
git status   (checks the state of repository)

code file_name    (to change file)
```

8
```
git add .   (uploads all the changes to current directroy and subdirectory)
```

9
```git log```  -  gives you history of changes
```git log --pretty=oneline```  - all in one line
- `--pretty="..."` — определяет формат вывода.
- `%h` — укороченный хеш коммита.
- `%ad` — дата коммита.
- `|` — просто визуальный разделитель.
- `%s` — комментарий.
- `%d` — дополнения коммита («головы» веток или теги).
- `%an` — имя автора.
- `--date=short` — сохраняет формат даты коротким и симпатичным.

10

```git checkout <hash>``` swithches to specific commit with this hash
```cat hello.html``` outputs the file

11
``` git tag v1```  creates the tag  (can see them with "checkout")

14
``` git revert``` cancels last commit (saves the history)






