#################################**Service and Version Detection**#################################
Point Nmap at a remote machine and it might tell you that ports 25/tcp, 80/tcp, and 53/udp are open. Using its nmap-services database of about 2,200 well-known services, Nmap would report that those ports probably correspond to a mail server (SMTP), web server (HTTP), and name server (DNS) respectively. This lookup is usually accurate—the vast majority of daemons listening on TCP port 25 are, in fact, mail servers. However, you should not bet your security on this! People can and do run services on strange ports.

Even if Nmap is right, and the hypothetical server above is running SMTP, HTTP, and DNS servers, that is not a lot of information. When doing vulnerability assessments (or even simple network inventories) of your companies or clients, you really want to know which mail and DNS servers and versions are running. Having an accurate version number helps dramatically in determining which exploits a server is vulnerable to. Version detection helps you obtain this information.

After TCP and/or UDP ports are discovered using one of the other scan methods, version detection interrogates those ports to determine more about what is actually running. The nmap-service-probes database contains probes for querying various services and match expressions to recognize and parse responses. Nmap tries to determine the service protocol (e.g. FTP, SSH, Telnet, HTTP), the application name (e.g. ISC BIND, Apache httpd, Solaris telnetd), the version number, hostname, device type (e.g. printer, router), the OS family (e.g. Windows, Linux). When possible, Nmap also gets the Common Platform Enumeration (CPE) representation of this information. Sometimes miscellaneous details like whether an X server is open to connections, the SSH protocol version, or the KaZaA user name, are available. Of course, most services don't provide all of this information. If Nmap was compiled with OpenSSL support, it will connect to SSL servers to deduce the service listening behind that encryption layer. Some UDP ports are left in the open|filtered state after a UDP port scan is unable to determine whether the port is open or filtered. Version detection will try to elicit a response from these ports (just as it does with open ports), and change the state to open if it succeeds. open|filtered TCP ports are treated the same way. Note that the Nmap -A option enables version detection among other things. Version detection is described in detail in Chapter 7, Service and Application Version Detection.

When RPC services are discovered, the Nmap RPC grinder is automatically used to determine the RPC program and version numbers. It takes all the TCP/UDP ports detected as RPC and floods them with SunRPC program NULL commands in an attempt to determine whether they are RPC ports, and if so, what program and version number they serve up. Thus you can effectively obtain the same info as rpcinfo -p even if the target's portmapper is behind a firewall (or protected by TCP wrappers). Decoys do not currently work with RPC scan.

When Nmap receives responses from a service but cannot match them to its database, it prints out a special fingerprint and a URL for you to submit it to if you know for sure what is running on the port. Please take a couple minutes to make the submission so that your find can benefit everyone. Thanks to these submissions, Nmap has about 6,500 pattern matches for more than 650 protocols such as SMTP, FTP, HTTP, etc.

Version detection is enabled and controlled with the following options:

-sV (Version detection)
    Enables version detection, as discussed above. Alternatively, you can use -A, which enables version detection among other things. -sR is an alias for -sV. Prior to March 2011, it was used to active the RPC grinder separately from version detection, but now these options are always combined.

--allports (Don't exclude any ports from version detection)
    By default, Nmap version detection skips TCP port 9100 because some printers simply print anything sent to that port, leading to dozens of pages of HTTP GET requests, binary SSL session requests, etc. This behavior can be changed by modifying or removing the Exclude directive in nmap-service-probes, or you can specify --allports to scan all ports regardless of any Exclude directive. 
	
--version-intensity <intensity> (Set version scan intensity)
    When performing a version scan (-sV), Nmap sends a series of probes, each of which is assigned a rarity value between one and nine. The lower-numbered probes are effective against a wide variety of common services, while the higher-numbered ones are rarely useful. The intensity level specifies which probes should be applied. The higher the number, the more likely it is the service will be correctly identified. However, high intensity scans take longer. The intensity must be between 0 and 9. The default is 7. When a probe is registered to the target port via the nmap-service-probes ports directive, that probe is tried regardless of intensity level. This ensures that the DNS probes will always be attempted against any open port 53, the SSL probe will be done against 443, etc.

--version-light (Enable light mode)
    This is a convenience alias for --version-intensity 2. This light mode makes version scanning much faster, but it is slightly less likely to identify services.

--version-all (Try every single probe)
    An alias for --version-intensity 9, ensuring that every single probe is attempted against each port.

--version-trace (Trace version scan activity)
    This causes Nmap to print out extensive debugging info about what version scanning is doing. It is a subset of what you get with --packet-trace.

#################################**CHAPTER 14 - OPERATING SYSTEM DETECTION**#################################
One of Nmap's best-known features is remote OS detection using TCP/IP stack fingerprinting. Nmap sends a series of TCP and UDP packets to the remote host and examines practically every bit in the responses. After performing dozens of tests such as TCP ISN sampling, TCP options support and ordering, IP ID sampling, and the initial window size check, Nmap compares the results to its nmap-os-db database of more than 2,600 known OS fingerprints and prints out the OS details if there is a match. Each fingerprint includes a freeform textual description of the OS, and a classification which provides the vendor name (e.g. Sun), underlying OS (e.g. Solaris), OS generation (e.g. 10), and device type (general purpose, router, switch, game console, etc). Most fingerprints also have a Common Platform Enumeration (CPE) representation, like cpe:/o:linux:linux_kernel:2.6.

If Nmap is unable to guess the OS of a machine, and conditions are good (e.g. at least one open port and one closed port were found), Nmap will provide a URL you can use to submit the fingerprint if you know (for sure) the OS running on the machine. By doing this you contribute to the pool of operating systems known to Nmap and thus it will be more accurate for everyone.

OS detection enables some other tests which make use of information that is gathered during the process anyway. One of these is TCP Sequence Predictability Classification. This measures approximately how hard it is to establish a forged TCP connection against the remote host. It is useful for exploiting source-IP based trust relationships (rlogin, firewall filters, etc) or for hiding the source of an attack. This sort of spoofing is rarely performed any more, but many machines are still vulnerable to it. The actual difficulty number is based on statistical sampling and may fluctuate. It is generally better to use the English classification such as “worthy challenge” or “trivial joke”. This is only reported in normal output in verbose (-v) mode. When verbose mode is enabled along with -O, IP ID sequence generation is also reported. Most machines are in the “incremental” class, which means that they increment the ID field in the IP header for each packet they send. This makes them vulnerable to several advanced information gathering and spoofing attacks.

Another bit of extra information enabled by OS detection is a guess at a target's uptime. This uses the TCP timestamp option (RFC 1323) to guess when a machine was last rebooted. The guess can be inaccurate due to the timestamp counter not being initialized to zero or the counter overflowing and wrapping around, so it is printed only in verbose mode.

OS detection is covered in Chapter 8, Remote OS Detection.

OS detection is enabled and controlled with the following options:

-O (Enable OS detection)
    Enables OS detection, as discussed above. Alternatively, you can use -A to enable OS detection along with other things.

--osscan-limit (Limit OS detection to promising targets)
    OS detection is far more effective if at least one open and one closed TCP port are found. Set this option and Nmap will not even try OS detection against hosts that do not meet this criteria. This can save substantial time, particularly on -Pn scans against many hosts. It only matters when OS detection is requested with -O or -A.

--osscan-guess; --fuzzy (Guess OS detection results)
    When Nmap is unable to detect a perfect OS match, it sometimes offers up near-matches as possibilities. The match has to be very close for Nmap to do this by default. Either of these (equivalent) options make Nmap guess more aggressively. Nmap will still tell you when an imperfect match is printed and display its confidence level (percentage) for each guess.

--max-os-tries (Set the maximum number of OS detection tries against a target)
    When Nmap performs OS detection against a target and fails to find a perfect match, it usually repeats the attempt. By default, Nmap tries five times if conditions are favorable for OS fingerprint submission, and twice when conditions aren't so good. Specifying a lower --max-os-tries value (such as 1) speeds Nmap up, though you miss out on retries which could potentially identify the OS. Alternatively, a high value may be set to allow even more retries when conditions are favorable. This is rarely done, except to generate better fingerprints for submission and integration into the Nmap OS database.

#################################**CHAPTER 15 - NMAP SCRIPTING ENGINE (NSE)**#################################
The Nmap Scripting Engine (NSE) is one of Nmap's most powerful and flexible features. It allows users to write (and share) simple scripts (using the Lua programming language ) to automate a wide variety of networking tasks. Those scripts are executed in parallel with the speed and efficiency you expect from Nmap. Users can rely on the growing and diverse set of scripts distributed with Nmap, or write their own to meet custom needs.

Tasks we had in mind when creating the system include network discovery, more sophisticated version detection, vulnerability detection. NSE can even be used for vulnerability exploitation.

To reflect those different uses and to simplify the choice of which scripts to run, each script contains a field associating it with one or more categories. Currently defined categories are auth, broadcast, default. discovery, dos, exploit, external, fuzzer, intrusive, malware, safe, version, and vuln. These are all described in the section called “Script Categories”.

Scripts are not run in a sandbox and thus could accidentally or maliciously damage your system or invade your privacy. Never run scripts from third parties unless you trust the authors or have carefully audited the scripts yourself.

The Nmap Scripting Engine is described in detail in Chapter 9, Nmap Scripting Engine and is controlled by the following options:

-sC
    Performs a script scan using the default set of scripts. It is equivalent to --script=default. Some of the scripts in this category are considered intrusive and should not be run against a target network without permission. 
	
--script <filename>|<category>|<directory>/|<expression>[,...]
    Runs a script scan using the comma-separated list of filenames, script categories, and directories. Each element in the list may also be a Boolean expression describing a more complex set of scripts. Each element is interpreted first as an expression, then as a category, and finally as a file or directory name.

There are two special features for advanced users only. One is to prefix script names and expressions with + to force them to run even if they normally wouldn't (e.g. the relevant service wasn't detected on the target port). The other is that the argument all may be used to specify every script in Nmap's database. Be cautious with this because NSE contains dangerous scripts such as exploits, brute force authentication crackers, and denial of service attacks.

File and directory names may be relative or absolute. Absolute names are used directly. Relative paths are looked for in the scripts of each of the following places until found:
	- (-datadir)
    - $NMAPDIR
    - ~/.nmap (not searched on Windows)
    - <APPDATA>\nmap (only on Windows)
    - the directory containing the nmap executable
    - the directory containing the nmap executable, followed by ../share/nmap (not searched on Windows)
    - NMAPDATADIR (not searched on Windows)
    - the current directory

When a directory name ending in / is given, Nmap loads every file in the directory whose name ends with .nse. All other files are ignored and directories are not searched recursively. When a filename is given, it does not have to have the .nse extension; it will be added automatically if necessary.

Nmap scripts are stored in a scripts subdirectory of the Nmap data directory by default (see Chapter 14, Understanding and Customizing Nmap Data Files). For efficiency, scripts are indexed in a database stored in scripts/script.db, which lists the category or categories in which each script belongs.

When referring to scripts from script.db by name, you can use a shell-style ‘*’ wildcard.

    nmap --script "http-*"

Loads all scripts whose name starts with http-, such as http-auth and http-open-proxy. The argument to --script had to be in quotes to protect the wildcard from the shell.

More complicated script selection can be done using the and, or, and not operators to build Boolean expressions. The operators have the same precedence as in Lua: not is the highest, followed by and and then or. You can alter precedence by using parentheses. Because expressions contain space characters it is necessary to quote them.

    nmap --script "not intrusive"
        Loads every script except for those in the intrusive category.

	nmap --script "default or safe"
        This is functionally equivalent to nmap --script "default,safe". It loads all scripts that are in the default category or the safe category or both.

	nmap --script "default and safe"
        Loads those scripts that are in both the default and safe categories.

	nmap --script "(default or safe or intrusive) and not http-*"
        Loads scripts in the default, safe, or intrusive categories, except for those whose names start with http-.

--script-args <n1>=<v1>,<n2>={<n3>=<v3>},<n4>={<v4>,<v5>}
	Lets you provide arguments to NSE scripts. Arguments are a comma-separated list of name=value pairs. Names and values may be strings not containing whitespace or the characters ‘{’, ‘}’, ‘=’, or ‘,’. To include one of these characters in a string, enclose the string in single or double quotes. Within a quoted string, ‘\’ escapes a quote. A backslash is only used to escape quotation marks in this special case; in all other cases a backslash is interpreted literally. Values may also be tables enclosed in {}, just as in Lua. A table may contain simple string values or more name-value pairs, including nested tables. Many scripts qualify their arguments with the script name, as in xmpp-info.server_name. You may use that full qualified version to affect just the specified script, or you may pass the unqualified version (server_name in this case) to affect all scripts using that argument name. A script will first check for its fully qualified argument name (the name specified in its documentation) before it accepts an unqualified argument name. A complex example of script arguments is --script-args 'user=foo,pass=",{}=bar",whois={whodb=nofollow+ripe},xmpp-info.server_name=localhost'. The online NSE Documentation Portal at https://nmap.org/nsedoc/ lists the arguments that each script accepts. 

--script-args-file <filename>
    Lets you load arguments to NSE scripts from a file. Any arguments on the command line supersede ones in the file. The file can be an absolute path, or a path relative to Nmap's usual search path (NMAPDIR, etc.) Arguments can be comma-separated or newline-separated, but otherwise follow the same rules as for --script-args, without requiring special quoting and escaping, since they are not parsed by the shell. 

--script-help <filename>|<category>|<directory>|<expression>|all[,...]
    Shows help about scripts. For each script matching the given specification, Nmap prints the script name, its categories, and its description. The specifications are the same as those accepted by --script; so for example if you want help about the ftp-anon script, you would run nmap --script-help ftp-anon. In addition to getting help for individual scripts, you can use this as a preview of what scripts will be run for a specification, for example with nmap --script-help default. 

--script-trace
    This option does what --packet-trace does, just one ISO layer higher. If this option is specified all incoming and outgoing communication performed by a script is printed. The displayed information includes the communication protocol, the source, the target and the transmitted data. If more than 5% of all transmitted data is not printable, then the trace output is in a hex dump format. Specifying --packet-trace enables script tracing too. 

--script-updatedb
    This option updates the script database found in scripts/script.db which is used by Nmap to determine the available default scripts and categories. It is only necessary to update the database if you have added or removed NSE scripts from the default scripts directory or if you have changed the categories of any script. This option is generally used by itself: nmap --script-updatedb.
	
