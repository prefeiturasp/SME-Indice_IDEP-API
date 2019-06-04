#!/usr/bin/env bash
if [ "$TRAVIS_BRANCH" != "dev" ]; then
    exit 0;
fi

export GIT_COMMITTER_EMAIL="giusepper11@gmail.com"
export GIT_COMMITTER_NAME="Giuseppe Rosa"

git remote update
git fetch
git checkout --track origin/homolog || exit
git merge "$TRAVIS_COMMIT" || exit
git push