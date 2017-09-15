# Prettify JSON

This script allows you to prettify json data from text file.

# Quickstart

Place pprint_json.py somewhere. Then run command line, go to folder in which you moved script and execute it with one parameter containing path to text file.

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>

```

Output data example:
```json

{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
