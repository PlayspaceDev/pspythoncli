# Python CLI

## Create a new python tool

Create a new repo and marge this repo in as a remote

```sh
git remote add template git@gitlab.playspace.com:tools/pspythoncli.git
git remote update template
git merge template/master --allow-unrelated-histories # or any other object
git remote set-url --push template no-pushing
```

Now you can apply your changes at will.

## Upgrade your tool

To pickup the latest changes from the template just merge them in using

```sh
git remote update template
git merge template/master --allow-unrelated-histories # or any other object
```