# Corvette

Corvette is a static site generator that creates a directory listing similar to an autoindex.

EXAMPLE IMAGE HERE (before and after)

To see Corvette in action on a live site, check out [https://philipkiely.com/assets/](https://philipkiely.com/assets/).


NOTE

Implementation detail/design decisions: clickable breadcrumbs but NO back/.. listed in the directory, a little more friendly for non-terminal users

```html
Index of <a href="/">https://philipkiely.com</a>/<a href="/assets">assets</a>/<a href="/assets/img">img</a>
```


## Installation

Corvette is written in Python and is installable with pip. It is strongly recommended that you use Corvette (and any other Python packages) in a virtual environment. To install, run:

```
pip install corvette
```

Alternately, you can clone this repository and build the package locally.

## Configuration

Create and edit a corvetteconf.py 

Stuff worth configuring:

```
# Display Information
ROOT_NAME = Assets
ROOT_LINK = https://example.com/assets

# Build Information
OUTPUT_DIR = 
ICONS = 
TEMPLATE = 
```

## Usage

**Important:**

1. Always run Corvette in your build script after your assets folder is generated for distribution to ensure complete, correct paths.
2. Corvette assumes it is run in the project's root directory. Configure paths appropriately.

## Themes

Out of the box, Corvette uses the default theme Bootstrap Basic to build pages. The source code for that theme is distributed along within the library and can be viewed in this repository at `/theme/templates`. It is written to be easy to read and adapt into your own theme and uses 100% of the available data passed by Jinja's `render()` method.

Corvette is designed to integrate with your existing (Python-based) static site generator, but can stand alone. As such, it is easier to add a single file, named `corvette.html` to avoid file name conflicts, to your existing Jinja-based template than to maintain a separate theme, but the latter is possible.

### Adding Corvette to an Existing Theme



Assumes you have your own base.html


### Creating a New Theme for Corvette

Use a JSON file to bring your own icons (name: \[extensions\])

page.html is theme "Bootstrap Basic"

Maybe it should be named corvette.html to make it easier to use existing themes!

## Development

Use a virtual environment with requirements.txt (only dependency is Jinja and its dependencies)

Helpful command: `rm */index.html` to get rid of generated indexes.

### Setting Up


### Distribution


### Tests

The tests run off of a set of sample assets, listed below. All contents of all files are open source, public domain, or royalty-free to use.


* Hamlet (Folger Shakespeare).pdf
* Kayak_Lake_Unsplash.png
* Mountain_Cabin_Unsplash.jpg
* Neffex - Fight Back (Clip).mp3
* Neffex - Fight Back (Clip).mp4
* Romeo & Juliet (Folger Shakespeare).docx
* Romeo & Juliet (Folger Shakespeare).epub
* Titanic_Data.csv
* Titanic_Data.xlsx
* **bootstrap-5.0.0-beta2-dist/**
  * **css/**
    * bootstrap-grid.css
    * bootstrap-grid.css.map
    * *...(30 more)*
  * **js/**
    * bootstrap.bundle.js
    * bootstrap.esm.js
    * *...(10 more)*
* bootstrap-5.0.0-beta2-dist.zip
* **empty/**
* sonnet_vi.md
* sonnet_xxii.txt

To run the tests, implement tests.

## About

Corvette is created by [Philip Kiely](https://philipkiely.com) and open source under the MIT License. Corvette is sponsored by [PK&C](https://pkandc.com).