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

* Output Directories (array)
* Theme
* icons.json

## Usage

<temp>

There are three directories that matter

* The folder corvette's code is installed in
* The folder corvette's code is run in
* The folder the output is generated in

</temp>

**Note:** Always run Corvette in your build script after your assets folder is generated for distribution to ensure complete, correct paths.

## Themes

Assumes you have your own base.html

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