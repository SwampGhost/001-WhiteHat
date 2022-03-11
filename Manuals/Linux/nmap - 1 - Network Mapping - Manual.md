#nmap #discovery #recon 
#####################################**MOST USED CLI**#####################################
```bash
## Will not include bash prompt. The prompt is causing formatting conflicts (visually). Comments out weigh bash prompt in current scenario.
## Always ping host previous to scan 
ping {ipofhost} OR {hostname} OR {dnsName}
- ping 10.10.10.14
- ping thatHostsName
- ping thatHostsName.com

## PASSIVE DICOVERY - TCP: If host responds to general ping, fast scan host to ID potential open / listening ports with SYN SCAN
## SYN Scan does partial TCP connect and must be initiated with SUDU priviledges
## Will scan  all 65535 ports via TCP and produce list of open / listening based on ports response / NO RST response
## If no port range is specified it will scan the first 1000 ports by default
nmap -sS -p- {hostIP} OR {hostName} OR {dnsName}
#examples
- nmap -sS -p- 10.10.10.14
- nmap -sS -p- thatHostsName
- nmap -sS -p- thatHostsName.com

## PASSIVE DISCOVERY - TCP - ALTERNATIVE: Some host may explicitly responsd with RST upon anon ICMP leading 
## scanners to think all ports are closed. If you are confident the system is, in fact, online
## use this scan to force a SYN TCP Scan of all ports
nmap -sS -Pn -p- {hostIP} OR {hostName} OR {dnsName}
#examples
- nmap -sS -Pn -p- 10.10.10.14
- nmap -sS -Pn -p- thatHostsName
- nmap -sS -Pn -p- thatHostsName.com

## PASSIVE DISCOVERY - UDP: Some targets may have services available on UDP. I typically don't scan UDP unless
## a TCP scan comes up short, has an unussual lost number of advertised ports, or all leads on TCP are a dead end. 
## Default and previos scans do not discover UDP. UDP scans take much longer. Average UDP against all ports 
## can take longer than 20 minutes. The design of UDP results in no validation of ports during passive 
## discovery (No Connect FCC Req). Reported results based on non-RST response from host. Reported as 
## Open/Listening. Must be validated by active / interactive scan. 
nmap -sU -p- {hostIP} OR {hostName} OR {dnsName}
#examples
- nmap -sU -p- 10.10.10.14
- nmap -sU -p- thatHostsName
- nmap -sU -p- thatHostsName.com

## ACTIVE SCAN - KNOWN PORTS: This will likely leave evidence of your systems interaction with the target
## on the remote system. If you are concnerned about tracing, you will need to obfuscated your IP and 
## MAC through various open source tools avaialble on the web. Identify the timing limit for each port
## scanned to reduce time spent scanning. If information is more valuable than speed, do not use 
## the -T parameter. If you value verbose, use the -v{vv}. The move "v" the more verbose up to 3 max. 
nmap -sV -T{1-5} -v -p p1,p2,p3 {hostIP} OR {hostName} OR {dnsName}
#examples
- nmap -sV -T{1-5} -v -p 22,80,443,1433 10.10.10.14
- nmap -sV -T{1-5} -v -p 22,80,443,1433 thatHostsName
- nmap -sV -T{1-5} -v -p 22,80,443,1433 thatHostsName.com

## ROUTE THROUGH PROXY - PARAMETER: If you are using burpe suite, ZAP, or similar proxy software, you may want to push 
## all information through it. To do that you need to use the proxy switch unless your terminal 
## your environment configurations. If you only have HTTPS / SOCKS4/5 setup, CLI will not be captured. I do not use the
## localhost as a proxy address. I seem to have a lot of problems that way. I have better results using 127.0.0.1
--proxies {proxyIP} OR {proxyDNSName} 
#examples
- --proxies 127.0.0.1
- --proxies localhost
- --proxies 10.10.10.2

## CHECK FOR VULNERABILITIES: Once services are identified, there may be value in running scripts against the services. 
## there are some options available, but select them carefully. Some script may negatively effect the hosts or 
## causng event notification to a moniitoring/reporting system that may ilicite unwanted attention or automated
## incident response systems. In a short hand, big issues for you. Optiions are noted after CLI examples. 
nmap -scripts={script1,script2,script3} OR {scriptGroup} OR {levelOfInteraction} OR {technologyGroup} {hostIP} OR {hostName} OR {dnsName}
#examples
- nmap -scripts=http  {hostIP} OR {hostName} OR {dnsName}
- nmap -scripts=vuln  {hostIP} OR {hostName} OR {dnsName}
- nmap -scripts=discovery  {hostIP} OR {hostName} OR {dnsName}

## Locally stored scripts: /usr/share/nmap/scripts
## Script Options: 
- safe			Wont affect the target (passive)
- intrusive		Aggresive, potential to DoS host or others negative effects
- vuln			Scan for vulnerabilities
- exploit		Attempt to exploit a vulnerability
- auth			Attempt to bypass authentication for running services (e.g. Log into an FTP server anonymously)
- brute			Attempt to brute force credentials for running services
- discovery		Attempt to query running services for further information about the network (e.g. query an SNMP server).

## RUNTIME INTERACTION: During run time you are able to change minor configurations without 
## aborting the scan all together and starting over. The options that can be changed are: 
- v / V			Increase / Decrease the verbosity level
- d / D			Increase / Decrease the debugging level 
- p / P 		Turn on / off packet tracing 
- ? 			Print a runtime interaction help screen 
- anything else	Print out a status message
```

#####################################**NAME**#####################################
nmap — NETWORK MAPPING TOOL

#####################################**SOURCES**#####################################
The creators and sustainers of the nmap project. This is a highly developed and valuable tool for recon.
nmap.org - https://nmap.org/book/man.html & susequent pages on site

#####################################**DESCRIPTION**#####################################
Nmap (“Network Mapper”) is an open source tool for network exploration and security auditing. It was designed to rapidly scan large networks, although it works fine against single hosts. Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics. While Nmap is commonly used for security audits, many systems and network administrators find it useful for routine tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime.

The output from Nmap is a list of scanned targets, with supplemental information on each depending on the options used. Key among that information is the “interesting ports table”. That table lists the port number and protocol, service name, and state. The state is either open, filtered, closed, or unfiltered. Open means that an application on the target machine is listening for connections/packets on that port. Filtered means that a firewall, filter, or other network obstacle is blocking the port so that Nmap cannot tell whether it is open or closed. Closed ports have no application listening on them, though they could open up at any time. Ports are classified as unfiltered when they are responsive to Nmap's probes, but Nmap cannot determine whether they are open or closed. Nmap reports the state combinations open|filtered and closed|filtered when it cannot determine which of the two states describe a port. The port table may also include software version details when version detection has been requested. When an IP protocol scan is requested (-sO), Nmap provides information on supported IP protocols rather than listening ports.

###################################BASIC OPTIONS#########################################
```BASH
nmap -h ##switch requied to produce following menu
##formatted results for each of consumption - Autistic / Format Sensitive Friendly
##Nmap 7.92SVN ( https://nmap.org )
Usage: nmap [Scan Type(s)] [Options] {target specification}

TARGET SPECIFICATION:
  ##Can pass hostnames, IP addresses, networks, etc.
  ##Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename> #Input from list of hosts/networks
  -iR <num hosts> #Choose random targets
  --exclude <host1[,host2][,host3],...> #Exclude hosts/networks
  --excludefile <exclude_file> #Exclude list from file

HOST DISCOVERY:
  -sL ##List Scan - simply list targets to scan
  -sn ##Ping Scan - disable port scan
  -Pn ##Treat all hosts as online - skip host discovery
  -PS [portlist] ##TCP SYN - Discovery of given ports  ###ONLY IF SUDO!!###
  -PA [portlist] ##TCP ACK - Discovery of given ports
  -PU [portlist] ##UDP - Discovery of given ports
  -PY [portlist] ##SCTP  - Discovery of given ports TCP SYN/ACK
  -PE ##discovery probes - ICMP echo
  -PP ##discovery probes - timestamp
  -PM ##discovery probes - netmask request 
  -PO [protocol list] ##IP Protocol Ping
  -n ##Never do DNS resolution
  -R ##Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...> ##Specify custom DNS servers
  --system-dns ##Use OSs DNS resolver
  --traceroute ##Trace hop path to each host

SCAN TECHNIQUES:
  -sS #TCP SYN
  -sT #TCP Connect
  -sA #TCP ACK
  -sW #TCP Window
  -sM #TCP Maimon
  -sU #UDP Scan
  -sN #TCP Null
  -sF #TCP FIN 
  -sX #TCP Xmas
  --scanflags <flags> #Customize TCP scan flags
  -sI <zombie host[:probeport]> #Idle scan
  -sY #SCTP INIT/COOKIE
  -sZ #SCTP ECHO
  -sO #IP protocol scan
  -b <FTP relay host> #FTP bounce scan

PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges> ##Only scan specified ports Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  -p- ## scan all ports on protocol specified (Default = TCP)
  --exclude-ports <port ranges> ##Exclude the specified ports from scanning
  -F ##Fast mode - Scan fewer ports than the default scan
  -r ##Scan ports consecutively - dont randomize
  --top-ports <number> ##Scan <number> most common ports
  --port-ratio <ratio> ##Scan ports more common than <ratio>

SERVICE/VERSION DETECTION: (!!!!ACTIVE / SYSTEM INTERACTION / TRACE POSSIBLE!!!!)
  -sV ##Probe open ports to determine service/version info
  --version-intensity <level>: ##Set from 0 (light) to 9 (try all probes)
  --version-light ##Limit to most likely probes (intensity 2)
  --version-all ##Try every single probe (intensity 9)
  --version-trace ##Show detailed version scan activity (for debugging)

SCRIPT SCAN:
  -sC #Short hand for --script=default
  --script=<Lua scripts> ##<Lua scripts> is a comma separated list of directories, script-files or script-categories
  --script-args=<n1=v1,[n2=v2,...]> ##provide arguments to scripts
  --script-args-file=filename ##provide NSE script args in a file
  --script-trace ##Show all data sent and received
  --script-updatedb ##Update the script database.
  --script-help=<Lua scripts> ##Show help about scripts. <Lua scripts> is a comma-separated list of script-files or script-categories.

OS DETECTION:
  -O ##Enable OS detection
  --osscan-limit ##Limit OS detection to promising targets
  --osscan-guess ##Guess OS more aggressively

TIMING AND PERFORMANCE:
  ##Options which take <time> are in seconds, or append 'ms' (milliseconds), 's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
  -T<0-5> ##Set timing template (higher is faster)
  --min-hostgroup/max-hostgroup <size> ##Parallel host scan group sizes
  --min-parallelism/max-parallelism <numprobes> ##Probe parallelization
  --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time> ##Specifies probe round trip time
  --max-retries <tries> ##Caps number of port scan probe retransmissions.
  --host-timeout <time> ##Give up on target after this long
  --scan-delay/--max-scan-delay <time> ##Adjust delay between probes
  --min-rate <number> ##Send packets no slower than <number> per second
  --max-rate <number> ##Send packets no faster than <number> per second

FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu <val> ##fragment packets (optionally w/given MTU)
  -D <decoy1,decoy2[,ME],...> ##Cloak a scan with decoys
  -S <IP_Address> ##Spoof source address
  -e <iface> ##Use specified interface
  -g/--source-port <portnum> ##Use given port number
  --proxies <url1,[url2],...> ##Relay connections through HTTP/SOCKS4 proxies
  --data <hex string> ##Append a custom payload to sent packets
  --data-string <string> ##Append a custom ASCII string to sent packets
  --data-length <num> ##Append random data to sent packets
  --ip-options <options> ##Send packets with specified ip options
  --ttl <val> ##Set IP time-to-live field
  --spoof-mac <mac address/prefix/vendor name> ##Spoof your MAC address
  --badsum ##Send packets with a bogus TCP/UDP/SCTP checksum

OUTPUT:
  -oN <file> ## Normal Output
  -oX <file> ## XML Ouput
  -oS <file> ## s|<crIpt kIddi3 Output
  -oG <file> ## Grepable format output
  -oA <basename> ## Output in the three major formats at once
  -v ## Increase verbosity level (use -vv or more for greater effect)
  -d ## Increase debugging level (use -dd or more for greater effect)
  --reason ## Display the reason a port is in a particular state
  --open ## Only show open (or possibly open) ports
  --packet-trace ## Show all packets sent and received
  --iflist ## Print host interfaces and routes (for debugging)
  --append-output ## Append to rather than clobber specified output files
  --resume <filename> ## Resume an aborted scan
  --noninteractive ## Disable runtime interactions via keyboard
  --stylesheet <path/URL> ## XSL stylesheet to transform XML output to HTML
  --webxml ## Reference stylesheet from Nmap.Org for more portable XML
  --no-stylesheet ## Prevent associating of XSL stylesheet w/XML output

MISC:
  -6 ## Enable IPv6 scanning
  -A ## Enable OS detection, version detection, script scanning, and traceroute
  --datadir <dirname> ## Specify custom Nmap data file location
  --send-eth ## Send using raw ethernet frames
  --send-ip ## Send using IP packets
  --privileged ## Assume that the user is fully privileged
  --unprivileged ## Assume the user lacks raw socket privileges
  -V ## Print version number
  -h ## Print this help summary page.

EXAMPLES:
nmap -v -A scanme.nmap.org
nmap -v -sn 192.168.0.0/16 10.0.0.0/8
nmap -v -iR 10000 -Pn -p 80

SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
```
#####################################**PORT STATES RECOGNIZED BY NMAP**#####################################
```bash 
The six port states recognized by Nmap:
- open
	An application is actively accepting TCP connections, UDP datagrams or SCTP associations on this port. Finding these is often the primary goal of port scanning. Security minded people know that each open port is an avenue for attack. Attackers and pen-testers want to exploit the open ports, while administrators try to close or protect them with firewalls without thwarting legitimate users. Open ports are also interesting for non-security scans because they show services available for use on the network. 

- closed
	A closed port is accessible (it receives and responds to Nmap probe packets), but there is no application listening on it. They can be helpful in showing that a host is up on an IP address (host discovery, or ping scanning), and as part of OS detection. Because closed ports are reachable, it may be worth scanning later in case some open up. Administrators may want to consider blocking such ports with a firewall. Then they would appear in the filtered state, discussed next. 

- filtered
	Nmap cannot determine whether the port is open because packet filtering prevents its probes from reaching the port. The filtering could be from a dedicated firewall device, router rules, or host-based firewall software. These ports frustrate attackers because they provide so little information. Sometimes they respond with ICMP error messages such as type 3 code 13 (destination unreachable: communication administratively prohibited), but filters that simply drop probes without responding are far more common. This forces Nmap to retry several times just in case the probe was dropped due to network congestion rather than filtering. This slows down the scan dramatically.

- unfiltered
	The unfiltered state means that a port is accessible, but Nmap is unable to determine whether it is open or closed. Only the ACK scan, which is used to map firewall rulesets, classifies ports into this state. Scanning unfiltered ports with other scan types such as Window scan, SYN scan, or FIN scan, may help resolve whether the port is open. 

- open|filtered
	Nmap places ports in this state when it is unable to determine whether a port is open or filtered. This occurs for scan types in which open ports give no response. The lack of response could also mean that a packet filter dropped the probe or any response it elicited. So Nmap does not know for sure whether the port is open or being filtered. The UDP, IP protocol, FIN, NULL, and Xmas scans classify ports this way.

- closed|filtered
	This state is used when Nmap is unable to determine whether a port is closed or filtered. It is only used for the IP ID idle scan.
```