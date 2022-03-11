#Algo-Search-and-Find

Pulled from: https://www.unix-ninja.com/p/A_cheat-sheet_for_password_crackers

Extract md5 hashes
`# egrep -oE '(^|[^a-fA-F0-9])[a-fA-F0-9]{32}([^a-fA-F0-9]|$)' *.txt | egrep -o '[a-fA-F0-9]{32}' > md5-hashes.txt`

An alternative could be with sed
`# sed -rn 's/.*[^a-fA-F0-9]([a-fA-F0-9]{32})[^a-fA-F0-9].*/1/p' *.txt > md5-hashes `

Note: The above regexes can be used for SHA1, SHA256 and other unsalted hashes represented in hex. The only thing you have to do is change the '{32}' to the corresponding length for your desired hash-type.

Extract valid MySQL-Old hashes
`# grep -e "[0-7][0-9a-f]{7}[0-7][0-9a-f]{7}" *.txt > mysql-old-hashes.txt `

Extract blowfish hashes
`# grep -e "$2a\$\08\$(.){75}" *.txt > blowfish-hashes.txt`

Extract Joomla hashes
`# egrep -o "([0-9a-zA-Z]{32}):(w{16,32})" *.txt > joomla.txt`

Extract VBulletin hashes
`# egrep -o "([0-9a-zA-Z]{32}):(S{3,32})" *.txt > vbulletin.txt`

Extraxt phpBB3-MD5
`# egrep -o '$H$S{31}' *.txt > phpBB3-md5.txt`

Extract Wordpress-MD5
`# egrep -o '$P$S{31}' *.txt > wordpress-md5.txt`

Extract Drupal 7
`# egrep -o '$S$S{52}' *.txt > drupal-7.txt`

Extract old Unix-md5
`egrep -o '$1$w{8}S{22}' *.txt > md5-unix-old.txt`

Extract md5-apr1
`egrep -o '$apr1$w{8}S{22}' *.txt > md5-apr1.txt`

Extract sha512crypt, SHA512(Unix)
`egrep -o '$6$w{8}S{86}' *.txt > sha512crypt.txt`

Extract e-mails from text files
`grep -E -o "\b[a-zA-Z0-9.#?$*_-]+@[a-zA-Z0-9.#?$*_-]+.[a-zA-Z0-9.-]+\b" *.txt > e-mails.txt`

Extract HTTP URLs from text files
`grep http | grep -shoP 'http.*?[" >]' *.txt > http-urls.txt`

For extracting HTTPS, FTP and other URL format use 
`grep -E '(((https|ftp|gopher)|mailto)[.:][^ >"	]*|www.[-a-z0-9.]+)[^ .,;	>">):]' *.txt > urls.txt`

Note: if grep returns "Binary file (standard input) matches" use the following approaches 
`tr '[\000-\011\013-\037177-377]' '.' < *.log | grep -E "Your_Regex"`
`cat -v *.log | egrep -o "Your_Regex"`

Extract Floating point numbers
`# grep -E -o "^[-+]?[0-9]*.?[0-9]+([eE][-+]?[0-9]+)?$" *.txt > floats.txt`

Extract credit card data
`Visa # grep -E -o "4[0-9]{3}[ -]?[0-9]{4}[ -]?[0-9]{4}[ -]?[0-9]{4}" *.txt > visa.txt`

MasterCard 
`# grep -E -o "5[0-9]{3}[ -]?[0-9]{4}[ -]?[0-9]{4}[ -]?[0-9]{4}" *.txt > mastercard.txt`

American Express 
`# grep -E -o "\b3[47][0-9]{13}\b" *.txt > american-express.txt`

Diners Club 
`# grep -E -o "\b3(?:0[0-5]|[68][0-9])[0-9]{11}\b" *.txt > diners.txt`

Discover 
`# grep -E -o "6011[ -]?[0-9]{4}[ -]?[0-9]{4}[ -]?[0-9]{4}" *.txt > discover.txt`

JCB 
`# grep -E -o "\b(?:2131|1800|35d{3})d{11}\b" *.txt > jcb.txt`

AMEX 
`# grep -E -o "3[47][0-9]{2}[ -]?[0-9]{6}[ -]?[0-9]{5}" *.txt > amex.txt`

Extract Social Security Number (SSN)
`# grep -E -o "[0-9]{3}[ -]?[0-9]{2}[ -]?[0-9]{4}" *.txt > ssn.txt`

Extract Indiana Driver License Number
`# grep -E -o "[0-9]{4}[ -]?[0-9]{2}[ -]?[0-9]{4}" *.txt > indiana-dln.txt`

Extract US Passport Cards
`# grep -E -o "C0[0-9]{7}" *.txt > us-pass-card.txt`

Extract US Passport Number
`# grep -E -o "[23][0-9]{8}" *.txt > us-pass-num.txt`

Extract US Phone Numberss
`# grep -Po 'd{3}[s-_]?d{3}[s-_]?d{4}' *.txt > us-phones.txt`

Extract ISBN Numbers
`# egrep -a -o "\bISBN(?:-1[03])?:? (?=[0-9X]{10}$|(?=(?:[0-9]+[- ]){3})[- 0-9X]{13}$|97[89][0-9]{10}$|(?=(?:[0-9]+[- ]){4})[- 0-9]{17}$)(?:97[89][- ]?)?[0-9]{1,5}[- ]?[0-9]+[- ]?[0-9]+[- ]?[0-9X]\b" *.txt > isbn.txt`