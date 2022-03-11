````
Reverse Image Search

md5sum and compare with OG

exiftool 
- Compare size with original
---- if size is different, adjust to bigger size
- see if there is extra data / fields
- run --info to see if it's pwd protected

strings | less - Look for anything obvious 
---- binary strings
---- anything out of place

eog {file}
- zoom in and look around a bit

stegsolve & then hit the letter 0 & select file
- works on JPG
- look at layers, see if anything pops

png Specific - zsteg

foremost

binwalk 
- see if there are other files within 
- extra and separate files
- run -dd="types:ext:cmd"  example: binwalk -dd=".*" {filename}