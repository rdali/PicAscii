===============================================================================


PicAscii
Picasso in ASCII art; ASCII written by ASCII

===============================================================================

    
    ----------------------------------------------------------------------------------------------
                                                  HELP
    ----------------------------------------------------------------------------------------------


    PicASCII.py draws your ASCII string using ASCII characters to be added in text files!
    US-ASCII letters:
    !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~


    usage: PicASCII.py -s myString [options]

    -s myString: a string made of ASCII letters.
                 To code newlines use "\"
                             ~~~ Allowed letters: ~~~
                 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO
                 PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

    -t text:     a character used to fill in the text. Default = "@"
                             ~~~ Allowed letters: ~~~
                 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO
                 PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

    -f filler:   a character used to fill in spaces in the text. Default = " "
                             ~~~ Allowed letters: ~~~
                 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNO
                 PQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

    -m mode:     mode used to print characters. Default: "norm"
                                ~~~ options: ~~~
                avail: print out of available letters in the used text and filler
                norm: normal: letters printed with some spacing between letters
                stag: staggard: letters are staggared verically
                sq  : squish  : normal printing, less spaces between letters
                ss  : satggard & squished: letters are staggared and squished
    -i indent   indent = integer: is the stagger indentation.
                ONLY used if mode = stag or ss. Default = 2.
    -c case     mode used to print characters. Default: "norm"
                up: Upper Caps: prints all letters as capital letters
                lo: lower Caps: prints all letters as lower case letters
    -b begin    a character added to the beginning of a line, usually a comment
                character.

    -d decorate character to be used for frame


    

    ----------------------------------------------------------------------------------------------
                                     PicASCII is complete!
                            Rola Dali; 2018; https://github.com/rdali
                           OPEN SOURCE: use, test, modify, distribute!
    ----------------------------------------------------------------------------------------------



### Usage: 

```
python picascii.py -s "HELLO WORLD" -t "O" -d "&"
```


### License:

PicASCII is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation.

PicASCII is distributed in the hopes that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.
