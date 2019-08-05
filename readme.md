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

# add CC addon_common as submodule
git submodule add git@github.com:CGCookie/addon_common.git addon_common
```

## Creating a Blender 2.80 add-on using CookieCutter

Until CookieCutter is ready for Blender 2.79b and 2.80, development for Blender 2.80 is under the `b280` branch of CookieCutter.

```
# create new addon folder
mkdir newaddon
cd newaddon

# initialize as new git repo
git init .

# add CC addon_common as submodule
git submodule add git@github.com:CGCookie/addon_common.git addon_common
cd addon_common
git checkout b280
```

## Updating CookieCutter

```
# update CC addon_common
cd addon_common
git pull
```


## Notes

- rename addon-common to addon_common
