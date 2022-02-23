# hello adventurer!

# there are some things wrong with this script that is used to decrypt
# a file containing the magic passphrase!
# use what you've learned to figure out what's wrong and correct it
# the comments and console output should give you enough clues to
# figure it out

# you'll definitely need the lolcat package to run this, so make sure
# that it's installed (sudo apt install lolcat)

# make aliases work within the bash script
shopt -s expand_aliases

# find the difference between two files and isolate the right side
alias findrightdiff='diff --changed-group-format="%>" --unchanged-group-format=""'

# apply the diff alias above and remove excess quotations from the output
# using sed, then write the output to a new file
finddiff files/words1.txt files/words2.txt | sed 's/"//g' > key.txt

# decrypt the magic phrase using the previously created file as
# the decryption key
ccdecrypt magicpassphrase.txt.cpt -K key.txt

# print the magic passphrase to console!
lolcat magicpassphrase.txt

# comment out these next two commands if you want to keep the key
# and leave the passphrase readable

# re-encrypt the passphrase with the same key used to decrypt it
ccencrypt magicpassphrase.txt -k key.txt

# delete the key file
rm key.txt
