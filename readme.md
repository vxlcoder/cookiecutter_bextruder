# BExtruder

This is an example add-on that demonstrates how to use CG Cookie CookieCutter to create add-ons for Blender 2.79b.

## To Clone...

```
git clone --recursive git@github.com:vxlcoder/cookiecutter_bextruder.git
```

## Creating a Blender 2.79b add-on using CookieCutter

```
# create new addon folder
mkdir newaddon
cd newaddon

# initialize as new git repo
git init .

# add CC addon-common as submodule
git submodule add git@github.com:CGCookie/addon-common.git addon-common
ln -s addon-common addon_common

# update CC addon-common
cd addon-common
git pull
```


## Notes

- rename addon-common to addon_common