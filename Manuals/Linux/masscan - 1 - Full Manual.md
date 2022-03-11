#####################################**NAME**##########################################
## 					masscan - Fast scan of the internet
#######################################**SYNOPSIS**########################################
	- masscan {ipAddress} OR {ipRange} -p {p1,p2,p3} OR {p1-65535}
	
#######################################**DESCRIPTION**########################################
##  masscan is an Internet-scale port scanner, useful for large scale surveys of the 
##  Internet, or of internal networks. While the default transmit rate is only  100  
##  packets/second,  it can  optional  go  as  fast  as  25  million packets/second, a 
##  rate sufficient to scan the Internet in 3 minutes for one port.

#######################################**SYNOPSIS**########################################
##
- <ip/range> ## anything on the command-line not prefixed with a ´-´ is assumed to  be  an IP address or range. There are three valid formats. The first is a single IPv4 address like "192.168.0.1". The second is a range like "10.0.0.1-10.0.0.100". The third  is  a CIDR  address,  like  "0.0.0.0/0".  At  least  one  target must be specified. Multiple	targets can be specified. This can be  specified  as  multiple  options  separated  by space,   or   can   be   separated   by   a   comma   as  a  single  option,  such  as 10.0.0.0/8,192.168.0.1.

--range <ip/range> ## the same as target range spec described above, except as  a  named parameter instead of an unnamed one.

-p  <ports, --ports <ports> ## specifies the port(s) to be scanned. A single port can be specified, like -p80. A range of ports can be specified, like  -p  20-25.  A  list  of 	ports/ranges  can be specified, like -p80,20-25. UDP ports can also be specified, like --ports U:161,U:1024-1100.
	
--banners ## specifies that banners should be grabbed, like HTTP server  versions,  HTML title fields, and so forth. Only a few protocols are supported.

--rate <packets-per-second>: ##	specifies the desired rate for transmitting packets. This can be very small numbers, like 0.1 for transmitting packets at rates of one every  10 seconds,  for  very  large  numbers  like  10000000,  which attempts to transmit at 10 million packets/second. In my experience, Windows and can do 250 thousand packets per second,  and  latest  versions  of  Linux  can  do 2.5 million packets per second. The PF_RING driver is needed to get to 25 million packets/second.

-c <filename>, --conf <filename> ## reads in a configuration file.  The  format  of  the configuration file is described below.

--resume  <filename> ## the same as --conf, except that a few options are automatically set, such as --append-output. The format of the configuration file is described below.

--echo ## don´t run, but instead dump the current configuration to a file. This file can then  be  used  with the -c option. The format of this output is described below under ´CONFIGURATION FILE´.

-e <ifname>, --adapter <ifname> ## use the named raw network interface, such  as  "eth0" or  "dna1". If not specified, the first network interface found with a default gateway will be used.

--adapter-ip <ip-address> ## send packets using this IP address. If not specified, then the  first IP address bound to the network interface will be used. Instead of a single IP address, a range may be specified. NOTE: The size of the  range  must  be  an  even power of 2, such as 1, 2, 4, 8, 16, 1024 etc. addresses.

--adapter-port  <port> ## send  packets  using  this  port number as the source. If not specified, a random port will be chosen in the range 40000 through  60000.  This  port should  be  filtered  by the host firewall (like iptables) to prevent the host network stack from interfering with arriving packets. Instead of a single port, a range can be specified,  like  40000-40003. NOTE: The size of the range must be an even power of 2, such as the example above that has a total of 4 addresses.

       ·   --adapter-mac <mac-address>: send packets using this as the source MAC address. If not
           specified, then the first MAC address bound to the network interface will be used.

       ·   --router-mac  <mac  address>:  send packets to this MAC address as the destination. If
           not specified, then the gateway address of the network interface will be ARPed.

       ·   --ping: indicates that the scan should include an  ICMP  echo  request.  This  may  be
           included with TCP and UDP scanning.

       ·   --exclude  <ip/range>:  blacklist  an  IP  address  or range, preventing it from being
           scanned. This overrides any target specification, guaranteeing that this address/range
           won´t be scanned. This has the same format as the normal target specification.

       ·   --excludefile <filename>: reads in a list of exclude ranges, in the same target format
           described above. These  ranges  override  any  targets,  preventing  them  from  being
           scanned.

       ·   --append-output: causes output to append to file, rather than overwriting the file.

       ·   --iflist: list the available network interfaces, and then exits.

       ·   --retries:  the number of retries to send, at 1 second intervals. Note that since this
           scanner is stateless, retries  are  sent  regardless  if  replies  have  already  been
           received.

       ·   --nmap: print help aobut nmap-compatibility alternatives for these options.

       ·   --pcap-payloads:  read  packets from a libpcap file containing packets and extract the
           UDP payloads, and associate those payloads with the destination port.  These  payloads
           will  then  be  used when sending UDP packets with the matching destination port. Only
           one payload will be remembered per port. Similar to --nmap-payloads.

       ·   --nmap-payloads <filename>: read in a file  in  the  same  format  as  the  nmap  file
           nmap-payloads.  This  contains  UDP  payload,  so  that we can send useful UDP packets
           instead of empty ones. Similar to --pcap-payloads.

       ·   --http-user-agent <user-agent>:  replaces  the  existing  user-agent  field  with  the
           indicated value when doing HTTP requests.

       ·   --open-only: report only open ports, not closed ports.

       ·   --pcap  <filename>:  saves  received  packets  (but  not  transmitted  packets) to the
           libpcap-format file.

       ·   --packet-trace: prints a summary of those packets sent and received. This is useful at
           low  rates,  like  a  few  packets per second, but will overwhelm the terminal at high
           rates.

       ·   --pfring: force the use of the PF_RING driver. The program will exit  if  PF_RING  DNA
           drvers are not available.

       ·   --resume-index: the point in the scan at when it was paused.

       ·   --resume-count:  the  maximum  number of probes to send before exiting. This is useful
           with the --resume-index to chop up a scan  and  split  it  among  multiple  instances,
           though the --shards option might be better.

       ·   --shards  <x>/<y>: splits the scan among instances. x is the id for this scan, while y
           is the total number of instances. For example, --shards 1/2 tells an instance to  send
           every  other  packet,  starting with index 0. Likewise, --shards 2/2 sends every other
           packet, but starting with index 1, so that it doesn´t overlap with the first example.

       ·   --rotate <time>: rotates the output file, renaming  it  with  the  current  timestamp,
           moving  it  to  a separate directory. The time is specified in number of seconds, like
           "3600" for an hour. Or, units of time can be specified, such as "hourly", or "6hours",
           or  "10min".  Times  are aligned on an even boundary, so if "daily" is specified, then
           the file will be rotated every day at midnight.

       ·   --rotate-offset <time>: an offset in the time. This is to accommodate timezones.

       ·   --rotate-dir <directory>: when rotating the file, this specifies  which  directory  to
           move the file to. A useful directory is /var/log/masscan.

       ·   --seed <integer>: an integer that seeds the random number generator. Using a different
           seed will cause packets to be sent in a different random order. Instead of an integer,
           the string time can be specified, which seeds using the local timestamp, automatically
           generating a differnet random order of scans.  If  no  seed  specified,  time  is  the
           default.

       ·   --regress: run a regression test, returns ´0´ on success and ´1´ on failure.

       ·   --ttl <num>: specifies the TTL of outgoing packets, defaults to 255.

       ·   --wait  <seconds>:  specifies the number of seconds after transmit is done to wait for
           receiving packets before exiting the program. The default is 10  seconds.  The  string
           forever can be specified to never terminate.

       ·   --offline:  don´t  actually  transmit  packets.  This  is  useful  with a low rate and
           --packet-trace to look at what packets might´ve been transmitted. Or, it´s useful with
           --rate  100000000  in  order  to  benchmark  how  fast transmit would work (assuming a
           zero-overhead driver). PF_RING is about 20% slower  than  the  benchmark  result  from
           offline mode.

       ·   -sL:  this  doesn´t do a scan, but instead creates a list of random addresses. This is
           useful for importing into  other  tools.  The  options  --shard,  --resume-index,  and
           --resume-count can be useful with this feature.

       ·   --interactive:  show  the results in realtime on the console. It has no effect if used
           with --output-format or --output-filename.

       ·   --output-format <fmt>: indicates the format of the output  file,  which  can  be  xml,
           binary, grepable, list, or JSON. The option --output-filename must be specified.

       ·   --output-filename  <filename>:  the  file  which  to save results to. If the parameter
           --output-format is not specified, then the default of xml will be used.

       ·   -oB <filename>: sets the output format to binary and saves the  output  in  the  given
           filename.  This  is  equivelent  to  using  the  --output-format and --output-filename
           parameters. The option --readscan can then be used to read  the  binary  file.  Binary
           files  are  mush  smaller  than  their XML equivelents, but require a separate step to
           convert back into XML or another readable format.

       ·   -oX <filename>: sets the output format to XML  and  saves  the  output  in  the  given
           filename.  This  is  equivelent to using the --output-format xml and --output-filename
           parameters.

       ·   -oG <filename>: sets the output format to grepable and saves the output in  the  given
           filename.   This   is   equivelent   to   using   the   --output-format  grepable  and
           --output-filename parameters.

       ·   -oJ <filename>: sets the output format to JSON and  saves  the  output  in  the  given
           filename.  This  is equivelent to using the --output-format json and --output-filename
           parameters.

       ·   -oL <filename>: sets the output format to a simple list format and saves the output in
           the  given  filename.  This  is  equivelent  to  using  the  --output-format  list and
           --output-filename parameters.

       ·   --readscan <binary-files>: reads the files created by the -oB option from a scan, then
           outputs  them  in  one  of the other formats, depending on command-line parameters. In
           other words, it can take the binary version of the output and convert it to an XML  or
           JSON format.
