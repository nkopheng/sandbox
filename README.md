# sandbox
GIT Hub Playground

# To clone the REPO:
git clone https://github.com/nkopheng/sandbox.git

# To get the update from the GITHUB:
git pull

# To create a branch:

# To switch to a branch:
git checkout -b testA

git push --set-upstream origion testA

# To a new file:
- create a file newfile.sh
- git add newfile.sh
- git commit -m "Added newfile.sh"

# To merge integration to testA
- Need to be at testA branch
- git merge origin/integration 

# To compare branch
- git diff master testA

# To replace local copy or bring fresh file back:
- git checkout -- hello.sh

