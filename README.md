# Python CLI

## Create a new python tool

Create a new repo and marge this repo in as a remote

```sh
git remote add template git@github.com:PlayspaceDev/pspythoncli.git
git remote update template
git merge template/master --allow-unrelated-histories # or any other object
git remote set-url --push template no-pushing
```

Now you can apply your changes at will.

### Upgrade

To pickup the latest changes from the template just merge them in using

```sh
git remote update template
git merge template/master --allow-unrelated-histories # or any other object
```

## Adding a new tool


## License

MIT License

Copyright (c) 2018 Playspace S.L.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
