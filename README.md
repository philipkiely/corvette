# Corvette

Corvette is a static site generator that creates a directory listing similar to an autoindex.

EXAMPLE IMAGE HERE (before and after)

To see Corvette in action on a live site, check out [https://philipkiely.com/assets/](https://philipkiely.com/assets/).

I wrote Corvette to use on my own websites. Packaging and distributing it as open source is an experiment in factoring something out of the (plate of spaghetti/big ball of mud) that is my build script. However, that means that there may be some weird behaviors or configuration steps if you're not using a similar overall setup.

## Installation

Corvette is written in Python and is installable with pip. It is strongly recommended that you use Corvette (and any other Python packages) in a virtual environment. To install, run:

```
pip install corvette
```

Alternately, you can clone this repository and build the package locally.

## Configuration

Create and edit a `corvetteconf.json`

Stuff worth configuring:

TODO: Fix

```
# Display Information
ROOT_NAME = "Assets" # Root Breadcrumb Text
ROOT_LINK = "/" # Root Breadcrumb Absolute URL

# Build Information
OUTPUT_DIR = "test/sample_assets" # Where the indexes will be created
TEMPLATE_DIR = "theme/templates" # Where the template lives
# ICONS = {} # If you want to override existing icon names
```

See the tests directory (link) or philipkiely.com (link) for examples.

## Usage

In your build script, include the line:

```
python -m corvette corvetteconf.json
```

The conf file is technically optional but you probably need it for any real-world use.

**Important:**

1. Always run Corvette in your build script after your assets folder is generated for distribution to ensure complete, correct paths.
2. Corvette assumes the underlying script is run in the project's root directory. Configure paths appropriately.
3. Corvette runs in place, as in it should be pointed directly at your `dist/` folder or equivalent.
4. Corvette does not come with its own live reload behavior, as it is intended to be used with your existing static site generator and development environment.

## Themes

Out of the box, Corvette uses the default theme "Bootstrap Basic" to build pages. The source code for that theme is distributed along within the library and can be viewed in this repository at `/theme/templates`. It is written to be easy to read and adapt into your own theme and uses 100% of the available data passed by Jinja's `render()` method.

Corvette is designed to integrate with your existing (Python-based) static site generator, but can stand alone. As such, it is easier to add a single file, named `corvette.html` by convention, to your existing Jinja-based template than to maintain a separate theme, but the latter is possible.

### Adding Corvette to an Existing Theme

If you already have a project in Pelican, MkDocs, Lektor, or any other static site generator that uses Jinja for templates, you only have to create a single file to use Corvette. Assuming you already have a `base.html` or similar, create `corvette.html` to extend that file and use this repository's example to write your own.

### Creating a New Jinja Theme for Corvette

If you want to create a new Jinja theme for Corvette (example use case: you're running just a file server) then create an appropriate template named `corvette.html` (no need for a `base.html` if the template is not designed to integrate with another template) and point `TEMPLATE_DIR` to it in `corvetteconf.py`.

If you're using Corvette with a project not written in Python, strongly consider porting the generator to your language for a simpler build process.

### Set Your Own Icons

If you're not using Bootstrap 5, you'll need to define your own icons (assuming you want icons in your theme). In `corvetteconf.py`, create a Python dictionary with the following format:

```
{
    "icon_classname_a": ["png", "jpg"],
    "icon_classname_a": ["pdf"]
}
```

You can do the same if you want to override the default icon configuration.

## Development

Use a virtual environment with requirements.txt (only dependency is Jinja and its dependencies): `pip install -r requirements.txt`.

Helpful command: `rm tests/**/index.html` to get rid of generated indexes.

### Contributing

If you have code changes, please make a pull request and I will review them!

### Distribution

Finished versions of Corvette are released on PyPi.

To get ready for distribution:

1. Increment the version number in `setup.py`
2. Run `python setup.py sdist`
3. Run `python -m twine upload dist/*` 

### Tests

The tests run off of a set of sample assets, listed below. All contents of all files are open source, public domain, or royalty-free to use.

* **bootstrap-5.0.0-beta2-dist/**
  * **css/**
    * bootstrap-grid.css
    * bootstrap-grid.css.map
    * *...(30 more)*
  * **js/**
    * bootstrap.bundle.js
    * bootstrap.esm.js
    * *...(10 more)*
* **empty/**
* Hamlet (Folger Shakespeare).pdf
* Kayak_Lake_Unsplash.png
* Mountain_Cabin_Unsplash.jpg
* Neffex - Fight Back (Clip).mp3
* Neffex - Fight Back (Clip).mp4
* Romeo & Juliet (Folger Shakespeare).docx
* Romeo & Juliet (Folger Shakespeare).epub
* Titanic_Data.csv
* Titanic_Data.xlsx
* bootstrap-5.0.0-beta2-dist.zip
* sonnet_vi.md
* sonnet_xxii.txt
* fizzbuzz.py

To run the tests, implement tests. Some stuff to write:

* A folder of correct files
* If files match, test passes
* If not, tests fail, print diff
* Test custom theme

At the moment, you just want to run `python -m corvette tests/corvetteconf.json` and visually confirm the output.

## About

Corvette is created by [Philip Kiely](https://philipkiely.com) and open source under the MIT License. Corvette is sponsored by [PK&C](https://pkandc.com).