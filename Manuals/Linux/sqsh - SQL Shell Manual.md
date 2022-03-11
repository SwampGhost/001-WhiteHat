#sqsh #mysq #sql-cmd-exploitl 
####################################**COMMON USES:**####################################
connect to db:
`# sqsh -S {host ip} -U {username} -P {.sqshrc file}`

Load Query once connected: 
`1> SELECT * FROM dbname.dbo.table WHERE {conditionals}`

action query: 
`2> go`

Use any normal query syntax to execute SQL commands and extract data. 
Query will output to terminal screen unless you for output to a different location
####################################**EXPLOIT POTENTIAL:**####################################
`3>xp_cmdshell {cmd}`
ex. 
`3>xp_cmdshell whoami`

Any cmdlet for the given OS should work is this function is enabled. 
cmd ex. 
```* dir
* type
* etc...
```
**CONSIDERATION**
There is potential to use this capability to create a vector of shell access to the given system. The capability will need to be validated through injections to the DB. The method to inject must not prevent shell escape chars or chained commands. If a shell to the system is secured, it will be at the permissions assigned to the account running SQL unless other execution methods are utilized.

MANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTARTMANUALSTART
####################################**TITLE:**#################################### 
sqsh - SQL Shell - Interactive database shell
####################################**Sources:**#################################### 
pbone.net - MAN sqsh - 03.12.2014 - http://rpm.pbone.net/manpage_idpl_26038000_numer_1_nazwa_sqsh.html
uchicago.edu - user commands - no date - http://people.cs.uchicago.edu/~sco/sqsh.pdf
 
####################################**Description:**####################################
Sqsh (pronounced skwish) is short for SQshelL (pronounced s-q-shell), and is intended as a replacement for the venerable 'isql' program supplied by Sybase. It came about due to years of frustration of trying to do real work with a program that was never meant to perform real work.

Sqsh is much more than a nice prompt, it is intended to provide much of the functionality provided by a good shell, such as variables, aliasing, redirection, pipes, back-grounding, job control, history, command substitution, and dynamic configuration. Also, as a by-product of the design, it is remarkably easy to extend and add functionality. 
####################################**OPTIONS-Brief:**####################################
```bash
sqsh [[options]] [[args......]] [-a count] [-A packet_size] [-b] [-B] [-c [cmdend]] [-C sql ] [-d severity] [-D database] [-e] [-E editor] [-f severity] [-G tds_version] [-h] [-H hostname] [-i filename] [-I interfaces] [-J charset] [-k keywords] [-K keytab] [-l debug_flags] [-L var=value] [-m style] [-n on|off] [-N appname] [-o filename] [-p] [-P [password]] [-Q query_timeout] [-r [sqshrc]] [-R server principal] [-s colsep] [-S server] [-t [filter]] [-T login_timeout] [-U username] [-v] [-V [bcdimoqru]] [-w width] [ -X ] [-y directory] [-z language] [-Z [secmech|default|none]]
```
####################################**OPTIONS-Expanded:**####################################
```bash
The following options may be used to adjust some of the behavior of sqsh, however a large portion of the
configuration options are available only through environment variables which may be set at runtime or via a
.sqshrc file.
Options may also be supplied in the SQSH environment variable. This variable is parsed prior to parsing
the command line, so in most cases the command line will override the contents of the variable. Be aware
Version 2.0 Last change: 04 Sep 1999 1

**NOTE!!: User Commands SQSH ( 1 )**
that for options which are allowed to supplied multiple times, such as -c, supplying them both in a variable
and on the command line will be the same as supplying them multiple times on the command line.
-a count Sets the maximum count of failures (as determined by the $thresh_fail variable) that
may occur before sqsh will abort. Setting this to 0 indicates that sqsh should not exit on
errors. This value defaults to 0 and may also be set using the $thresh_exit variable. See
section EXIT STATUS for details.

sqsh [options] [args...]
 - [−a count]
 
 - [−A packet_size] |Specifies the size of the network TDS packets used to communicate with the SQL server. This value must be between 512 and 2048, and be a multiple of 512. Check your SQL Server configuration to determine supported packet sizes. This value may also be specified at run-time using the $packet_size variable.
 
 - [−b ] |Suppress the banner message upon startup. This is unnecessary in cases where stdout has been redirected to a file. This option may also be set via the $banner variable.
 
 - [−B ] |Turns off all buffering of stdin, stdout, and stderr. This feature allows sqsh to be run from an interactive control script such as chat and expect.
 
 - [-c [cmdend]]  |Internally sqsh provides the command \go to send a batch of SQL to the database andprovides a single alias, go for this command. Each time cmdend is supplied a new alias for \go is established.
 
 - [-C sql ] |Causes the sql command to issued by sqsh, similar to the same behavior exhibited by the -i flag. This sql statment may not contain double quotes (this limitation will be lifted in future releases of sqsh).
 
 - [-d severity] |Sets the minimum SQL Server error severity that will be displayed to the user. The default is 0, and valid ranges are from 0 to 22. This may also be set using the $thresh_display variable. See section EXIT STATUS.
 
 - [-D database] |Causes sqsh to attempt to start with your database context set to database rather than your default database (usually master). This may also be set using the $database variable.
 
 - [-e] |Includes each command issued to sqsh to be included in the output. This option may also be set via the $echo variable (which is unrelated to the \echo command).
 
 - [-E editor] |editor Set the default editor to editor. This may also be set using the UNIX environment variable $EDITOR to the name of the editor desired.
 
 - [-f severity] |Sets the minimum severity level considered a failure by sqsh. This is the same as setting the $thresh_fail variable. See section EXIT STATUS for details.
 
 - [-h] |Turns off column headers and trailing "(# rows affected)" from batch output.
 
 - [-i filename] |Read all input from filename rather than from stdin.
 
 - [-H hostname] |Sets the client hostname as reported in sysprocesses. This may also be set via the $hostname variable.
 
 - [-I interfaces] |When a connection is established to the database, the interfaces file is used to turn the value of $DSQUERY into the hostname and port to which the connection will be made, by default this is located in $SYBASE/interfaces. This flag allows this default to be overridden.
 
 - [-J charset] |Specifies the character set to be used on the client side to communicate with SQL Server. This may also be set using the $charset environment variable.
 
 - [-k keywords] |Specifies a file containing a list of keywords to be used for keyword tab completion, if readline support has been compiled into sqsh. This file may also be set via the $keyword_file variable, which defaults to $HOME/.sqsh_words.
 
 - [-l debug_flags] |If sqsh has been compiled with -DDEBUG, this option may be used to turn on and off Version 2.0 Last change: 04 Sep 1999 2 User Commands SQSH ( 1 ) debugging options. See the $debug variable, below.
 
 - [-L var=value] | Sets the value of $var to value. This may be used to set the value of any sqsh variable even if an explicit command line variable is supplied for setting the variable. The -L flag may be used to set the value of non-configuration variables as well.
 
 - [-m style] |Changes the current display style to style. Currently supported styles are horiz, vert, bcp, html, meta, pretty and none. The current display style may also be set using the $style variable or via the -m flag to the \go command. 
 
 - [-o filename] |Redirects all output to filename rather than stdout.
 
 - [-p ] |Display performance statistics upon completion of every SQL batch. This option may also be turned on via the $statistics variable, or by supplying the -p flag to the \go command.
 
 - [-P [password]] |The Sybase password for username required to connect to server (default, NULL). The	password may also be set via $password. Supplying a password of ‘-’ causes the pass word to be read from the first line of stdin.	It should be noted that supplying your password on the command line is somewhat of a security hole, as any other user may be able to discover your password using ps(1). It is recommended that your default password be stored in a .sqshrc file which is not readable by anyone other than yourself.
 
 - [-r [sqshrc[:sqshrc ...]]] |Specifies an alternate .sqshrc file to be processed, rather than the default. If no sqshrc is supplied following **-r**, then no initialization files are processed. This flag must be the first argument supplied on the command line, all other instances will be ignored. 
 		* Kerberos support: Specifies a server principal to use for network (Kerberos)authentication, if the server name in the interfaces file differs from the realserver name.
		* See the Kerberos Support section below for details.
 
 - [-s colsep] |Causes the string colsep to be used to delimit SQL column output columns, this defaults to " ".
 
 - [-S server] |The name of the Sybase server to connect, the default of this is the external environment variable $DSQUERY. This value may also be set via the internal variable $DSQUERY. The servername must exist in the interfaces orsql.ini file. As an alternative it is also possible to specify the targetserver as host:port[:filter] where host may also be an IP address. Notethat filter may be defined in $SYBASE/$SYBASE_OCS/config/libtcl[64].cfg. Forexample: [FILTERS]    ssl=libsybfssl.so    ssl64=libsybfssl64.so
 
 - [-t [filter]] |Enables filtering of command batches through an external program, filter, prior to being sent to the SQL Server. If filter is not supplied, then $filter_prog is used (default is ‘m4 -’). This value may also be set via the $filter and $filter_prog variables.
 
 - [-T value] |Specifies the login timeout (similar to isql -l flag). If set specifies thenumber of seconds sqsh will wait before timing out a login request. Maps tothe $login_timeout variable.
 
 - [-U username] |The Sybase username to connect to the database as, this defaults to the username of the user running sqsh. The username may also be set via the $username variable.
 
 - [-v] |Displays the version number, $version, and exits.
 
 - [-V [bcdimoqru]] |Kerberos support: Specify the security options to use. See the Kerberos Support section below for details.
 
 - [-w width] |The maximum output width of a displayed result set, this defaults to 80 (the maximum for this value is 256).
 
 - [-X] |Initiates the login connection to the server with client-side password encryption (if supported). If either SQL Server does not recognize this option, or if the version of DB-Lib used to compile sqsh does not support this option, then it will be ignored. This option may also be set using the $encryption environment variable.
 
 - [-y directory] |Specifies a SYBASE directory to use other than the value of $SYBASE in order to find the interfaces file.
 
 - [-z language] |Specifies an alternate language to display sqsh prompts and messages. Without the -z flag, the server’s default language will be used. This may also be set using with the $language variable. 
 
 - [-Z [secmech|default|none]] |Kerberos support: Specify the security mechanism to use. See the Kerberos Support section below for details.
 
 args...
    If sqsh is run with the -i flag specifying an input file to be processed(rather than initiating an interactive session), arguments may be supplied onthe command line to be passed to the input file. These arguments may be accessedusing the variables ${0}, ${1}, ... (see the Variables section, below, formore information).

 ```
#################################### ADDITIONALL INFORMATION ####################################
	**Initialization**
Upon startup, sqsh initializes all internal environment variables, commands, and aliases to their default values, it then looks in the system-wide configuration file (usually /usr/local/etc/sqshrc), followed by a local configuration file$HOME/.sqshrc (this may be overridden via the SQSHRC external environment variable). If this file is found it is executed just like a script would be using the -i flag.

The .sqshrc file may contain anything that could normally be typed at the prompt, however it should be noted that at the time this file is read sqsh hasyet to establish a connection to the database, however most commands that perform database activity, such as \go will attempt to establish a database connection when executed (it may also prompt you for a password if necessary).Also, if database activity is required within this startup file, the \connect command (see COMMANDS, below) may be executed.

After the .sqshrc file has been executed, sqsh then parses any command line options (thus any variables set in your .sqshrc file may be overridden by command line options). Following that, if sqsh is run in interactive mode(i.e. without -i and if stdin is attached to a tty), it then looks for the file provided by the $history variable and loads the contents of that file into the history buffers. (see BUFFERS, below).

Immediately prior to establishing a connection to the database (either during startup, or by an explicit \connect or \reconnect command), the file$HOME/.sqsh_session is executed. The name of this file may be overridden using the $session variable. 

	**COMMAND LINE**
When a line is first read by sqsh, the first word is separated from the line.This word is then expanded of all variables (see Variable Substitution,below), followed by command expansion (see Command Substitution, below). The first word of the resulting string is then analyzed to see if it is either a valid sqsh command or alias.

The sqsh command line follows many of the same rules as Bourne shell,allowing file redirection, pipelining, command substitution, and back-grounding via the same syntax. 

	**COMMENTS**
Any line beginning with a # followed by a non-alphanumeric character (any character other than 0-9, a-z, A-Z, and _) causes the entire line to be ignored.Because of the possible collision with T-SQL session specific temp-table names,the line will not be ignored if the first character following the #, isalphanumeric. 

	**QUOTING**
Quoting is used to prevent the interpretation of special keywords or characters to sqsh, such as white-space, variable expansion, or command substitution. There are three types of quoting, escape, single-quotes, and double-quotes.

Enclosing characters in single quotes preserves the literal interpretation ofeach character contained within the quotes. A single quote may not appear within single quotes, even when preceded by an escape. For example:
```bash
    1> \echo I can not expand '$username'
```
outputs
```bash
    I can not expand $username
```
The characters \\ are used to escape the meaning (and thus prevent theinterpretation) of the character immediately following them. The \ characteritself may be escaped. For example:
```bash
    1> \echo I can\\'t expand '$username'
```
outputs
```bash
    I can't expand $username
```
The escape character may also be used to escape a new-line in order to perform aline continuation, in this case the new-line is discarded and the continued lineis automatically appended to the previous line, for example:
```bash
    1> \echo Hello \\    --> World!    Hello World!
```
Enclosing characters in double quotes preserves the literal meaning of allcharacters within them with the exception of $, ', and \\. A doublequote may be contained within double quotes by escaping it.
```bash
    1> \echo "\\"I can't deny it, I like $username\\", she said"
```
prints out
```bash
    "I can't deny it, I like gray", she said
```

	**EXPANSION**
After a line of input has been read, sqsh attempts to expand the line of any aliases (see Aliasing, below), following that it attempts to determine if the line begins with a command keyword. Once a line has been determined to contain a command name it has three types of expansion performed to it: variable substitution, followed by command substitution respectively. Finally, if a tilde was provided on the command line, then tilde expansion will be performed and the ~ will be substituted with the corresponding HOME directory name.
```bash
    1> \echo ~sybase/err.log
```
may result in /home/sybase/err.log for example.
```bash 
    1> exec sp_helpdb    2> go > ~/db.log
```
may result in a file /export/home/dba/db.log for example, depending on the Unix login and the exact OS you are using. Following this expansion the command line is separated into words and the command is executed. 

	**VARIABLE SUBSTITUTION**
The character $ is used to indicate variable substitution or expansion within aword. These variables may be assigned values by the \set command like so:
```bash
    1> \set name=value
```
name may be a character or underscore followed by any combination of characters, digits, or underscore, and may not contain any special characters,such as (') and ("). The restriction on the first character being a digit is introduced because SQL allows the representation of money data types as $nn.nnwhere n is a digit.

*value* may contain anything, however if it is to include white-space, then it must be quoted (see Words & Quoting, above). Note that in order to prevent the expansion of a variable use either single quotes, or two \'s, like thus:
```bash
    1> \echo \\$name    $name
```
Variables may be referenced in one of two ways:
- *$variable* In this manner all characters, digits, and underscores are treated as the name of the variable until another type of character is reached (either a special character, or a white-space). 
- *${variable}* The braces are required only when variable is followed by a letter, digit, or underscore that is not to be interpreted as part of its name. Note that the same effect may be achieved using double quotes.

It should be noted that because the variables are expanded prior to breaking the command line into words, if the contents of the variable contain white spaces, they are treated as significant by the parser. In the following example:
```bash
    1> \set x="1 2 3"    1> \echo $x
```
the \echo command receives three arguments, "1", "2", and "3", although it looks as if only one argument was passed to it. This behavior is consistent with most shells (such as csh, bourne shell, etc.). 

	**COMMAND SUBSTITUTION**
Sqsh supports a second form of expansion called command substitution. This form of expansion substitutes a command on the command line with the output of the external UNIX command. This expansion may be achieved by placing the command line to be executed in back-quotes (`). For example:
```bash
    1> \set password=`/sybase/bin/getpwd $DSQUERY`    1> \echo $password    ilikepickles
```
This example, the external program /sybase/bin/getpwd is executed with the current contents of the $DSQUERY environment variable, the entire expression is then replaced with the output of getpwd (ilikepickles) prior to executing the\set command. By default, the output of the substituted command is first broken into words according to the contents of the $ifs variable prior to assembling together back into the command line. So, by overriding the contents of $ifs you may affect the behavior of the substitution process.

For example:
```bash
    1> \set ifs=":"    1> \echo `echo hello:how:are:you`    hello how are you
```
This mechanism is frequently useful for parsing input files, such as/etc/passwd into fields. 
	
	**INPUT/OUTPUT REDIRECTION**
As with standard Bourne shell (and most other shells, for that matter), acommand's input and output may be redirected using a special notation interpreted by the shell. The following may appear anywhere on the command line, but only redirection that is specified prior to a pipe (|) actually has any effect on the behavior of internal sqsh commands (refer to Pipes, below).
```BASH
<word
    Use the file word as the standard input for the command. Typically very fewsqsh commands actually read anything from stdin, so this will usually have noeffect (see the \loop command).
[n]>word
    Associate the output of file descriptor n (stdout, by default) with fileword. If this file does not exist it is created; otherwise it is truncated tozero length.
[n]>>word
    Append the output of file descriptor n (stdout, by default) to file word,creating it if it does not exist.
[m]>&n
```  
Redirect the output of file descriptor m (stdout by default), to same output as file descriptor n. The order in which redirections are specified on the command line is significant, as the redirections are evaluated left-to-right.For example:
```BASH
        1> select * from select /* syntax error */    2> \go >/tmp/output 2>&1
```
This statement first redirects the standard output of the \go command to thefile /tmp/output, then redirects the stderr to the same file. So, when the commands fails, the error output will be found in the file /tmp/output. However, by changing the order of redirection, you can completely change the meaning:
```BASH 
		1> select * from select    2> \go 2>&1 >/tmp/output    Msg 156, Level 15, State 1    Server 'SQSH_TEST', Line 1    Incorrect syntax near the keyword 'select'.
```
In this case, error output will be sent to stdout, while what would have gone to stdout is redirected to /tmp/output (in this case /tmp/output will be empty).

Please read the section on Background Jobs, below, for detailed info on the interaction between file redirection and background jobs. 

	**PIPES**
A pipeline is a sequence of one or more commands separated by a '|', each command using the stdout of the preceding program for its own stdin. However the first command in the pipeline must be a sqsh command, and all other commands must be external (or UNIX) programs. Any sqsh command may be run through a pipeline, although for many of them (such as the \set command) it doesn'treally make any sense to do this. The following is an example of a pipeline:
```BASH
    1> select * from syslogins    2> \go | more
```
This command causes the result set generated by the \go command to be sent to the more(1) program, which then sends it to your screen, pausing at each screen full of data (this is the primary reason that I wrote sqsh).

There are several peculiarities in the way in which sqsh deals with pipelines as opposed to the way in which standard Bourne shell treats them.

Everything following the first occurrence of a pipe (|) character is broken into white-space delimited words, including such special shell commands as '2>&1'and other occurrences of pipes. If there are any variables contained in these words they are expanded following the same quoting rules as described in Words & Quoting, above, with the one exception that all quotes are left in place. These words are then reassembled into a single string and shipped off to/bin/sh for processing.

In short, sqsh makes no attempt to interpret what follows the first pipe,instead it is shipped off to a "real" shell to do the work. The rationale behind this is that I was lazy and didn't feel like writing all of the same bizarre variable handling, &&'ing, ||'ing, grouping, and variable expansion rules that Bourne shell supports, and instead I let Bourne do the dirty work.

The advantage of this method is that you can do some very complex stuff after the pipeline, such as:
```BASH
    1> select * from syscolumns    2> \go | (cd /tmp; compress -c > sysolumns.Z)
```
Not that I can think of any real reason to do this...but you can if you want to. 
	
	**BACKGROUND**
Backgrounding provides a mechanism whereby you may run any sqsh command as abackground process and continue working while it runs. Sqsh offers two types of backgrounding:

- **Deferred:** In this mode sqsh redirects all output of the background job to a temporary file(located in the directory $tmp_dir) while the job is running, so that the output is not intermixed with what you are currently working on. When the job completes you are notified of the process completion and the output may be viewed using the \show command.

- **Non-Deferred:** This corresponds to the common idea of a background process under UNIX. In this mode the output of the job is not implicitly redirected for you, and thus may become intermingled with what you are currently working. The mode selection you choose is selectable via the $defer_bg variable (which defaults to '1', or'On'). Typically the only reason to not use deferred mode is to prevent large result sets from filling up your file system.

To specify that a job be run in the background, simply append a & to the end ofthe command line, as:
```BASH
    1> sp_long_arduous_proc 1, 30    2> \go &    Job #1 running [xxxx]    1>
```
When sqsh encounters the & on the end of the command line it spawns a childprocess (with a Unix process id of xxxx) then the child process calls the\go. \go command then establishes a new connection to the database (usingthe current values of the $DSQUERY, $username, $password variables)and executes the shown query. While the job is executing the commands \jobs,\wait and \kill may be used to monitor or alter a currently running job(see section COMMANDS, below). When any job completes sqsh will display anotification, such as:
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!EDITING STOPPED HERE
```BASH
1> select count(*) from <return>    Job #1 complete (output pending)    2>
```
When a job completes, if it had no output, it is immediately considered terminated and will not show up in the current list of running jobs. However if the complete job has pending output, it will continue to be displayed as a running job (with the \jobs command) until a \show is used to display the output of the job.When you exit your parent sqsh session and there are background jobs active thena message is shown: You have running jobs or pending job output.You have to process all the jobs first before being able to exit sqsh.

There is a known bug with job backgrounding when used in conjunction with pipes,please refer to the BUGS section at the end of the manual. 
Buffers
In normal isql only two buffers are maintained; the buffer into which you are currently typing, and a buffer that contains the last batch executed (this is kept around for when you run 'vi', or 'edit').

Sqsh maintains several distinct sets of buffers:

- Work Buffer: This buffer corresponds directly to the isql work buffer. Itis the buffer into which you enter the current batch prior to sending it to thedatabase.
- History Buffer: This is actually a chain of 0 or more buffers (configurableby the $histsize variable) of the last $histsize batches that have been run. This buffer is only maintained when sqsh is run in interactive mode; that is, batches executed using the -i flag, or executed via redirection from the UNIX prompt will not be maintained in history (after all, they are already in a file somewhere).

If the variable $histsave is True (see section SPECIAL VARIABLES) and sqsh is in interactive mode, then the current history buffer is written to $HOME/.sqsh_history when you exit. This file is then read back into sqsh the next time it is started in interactive mode.

Named Buffers: At any time during a session the Work Buffer, or any of the History Buffers may be copied into a named buffer using the \buf-copy command (see section COMMANDS, below). These buffers are lost when you exit(however you may use the \buf-save command to save named buffers to a file).

	**BUFFER SHORT-HAND**
Many commands allow all of these buffers to be referenced in a short-hand fashion, very similar to the way that csh(1) references its commands history.Any of these short hands may be used for any buffer parameter described in the COMMANDS section:

- !.			The current work buffer.
- !!			The last command executed (note, this is not available in non-interactive modeas it does not maintain a history).
- !+			The next available history entry. This is a write-only buffer, so typically onlyapplies to such commands as \buf-copy.
- !n			Refers to history #n. Each time an entry is written to history it is assigned anincreasing number from the last entry, with this short-hand you may reference any given history.
- !buf_name		Just for consistency this is supplied as a reference to named bufferbuf_name, however buf_name without the leading '!' is also considered	correct.
- buf_name	    Refers to the named buffer buf_name.

	**VARIABLES**	
Variables may also be contained within work buffers. Under these circumstances the variables remain unexpanded until the buffer is sent to the database (viathe \go command), during which time they are expanded and replaced within the buffer. This behavior may be altered via the $expand variable.(see Special Variables, below).

The following is an example of using variables within a buffer:
```BASH
    1> \set table_name=syscolumns    1> select count(*) from $table_name    2> \go
```
This is the equivalent of performing the query:
```BASH
    1> select count(*) from syscolumns    2> \go
```
directly. Typically this feature is useful for reusing large complex where clauses, or long column names.

Quoting rules apply the same in SQL buffers as they do in command lines. That is, any variables contained within double quotes (") are expanded and variables contained within single quotes (') are left untouched. Thus:
```BASH
    1> select "$username", '$username'    2> \go
```
yields the results
```BASH
    ---- ---------    gray $username
```
	
	**COMMAND SUBSTITUTION**
As with the command line, the output of UNIX commands may also be substituted within a SQL buffer upon execution (once again, only if the $expand variable is set to 1, or true). In this circumstance the command contained within back quotes (`) is replaced with its output prior to forwarding the buffer to SQLserver. For example:
```BASH
    1> select count(*) from `echo syscolumns`    2> \go
```
Causes the strings 'echo syscolumns' to be replaced by the word sys columns prior to executing the command. It should be noted that thecontents of the substituted command are only executed at the time of the \go command, not when the line of SQL is input. 
Flow-of-Control
New with version 2.0 of sqsh, is the ability to perform basic flow-of-control and functions using the \if, \while, \do, and \func commands.

	**BLOCKS & SQL BUFFERS**
All sqsh flow-of-control commands are block-based. That is, if the test expression of the command is met, then a block of sqsh-script will be executed.For example, the definition of the \if command is:
```BASH
    \if expression        block    \fi
```
This block may be any number of lines of sqsh commands, SQL, or flow-of-control statements to be executed if the expression evaluates to asuccess condition (0).

Each block has its own SQL buffer for the duration that the block is executed. That is, the following statements:
```BASH
    1> /*    2> ** IMPROPER USAGE OF IF BLOCK    3> */    4> select count(*) from    5> \if [ $x -gt 10 ]    6>     sysobjects    7> \else    8>     sysindexes    9> \fi    5> go
```
will yield:
```BASH 
    Msg 102, Level 15, State 1    Server 'bps_pro', Line 1    Incorrect syntax near 'from'
```
because the string 'sysobjects' or 'sysindexes' were inserted into their own SQL buffers. These buffers are discarded as soon as the end of the block was reached, and since a \go command was not contained within the block, no additional errors were generated.

Thus, the correct way to write the above expression would be:
```BASH
    1> /*    2> ** PROPER USAGE OF IF BLOCK    3> */    4>  \if [ $x -gt 10 ]    5>     select count(*) from sysobjects    6>     go    7> \else    8>     select count(*) from sysindexes    9>     go    10> \fi
```
or, even:
```BASH
    1> /*    2> ** PROPER USAGE OF IF BLOCK    3> */    4>  \if [ $x -gt 10 ]    5>     \set table_name=sysobjects    6> \else    7>     \set table_name=sysindexes    8> \fi    4> select * from $table_name    5> go
```
Also, note that the line number displayed in the sqsh prompt resets to thecurrent position in the outer SQL buffer after reaching the \fi terminator.

	**EXPRESSIONS**
All flow-of-control statements in sqsh take an expression to determine whichblock of code to execute. Just like UNIX's Bourne Shell, this expressionis simply an operating system program that is executed by sqsh. If the commandreturns a success status (calls exit(0)), then it is considered successful.

For example, with following statement:
```BASH
    \while test $x -lt 10        block    \done
```
will execute the contents of block while the current value of $x is less than10. Note that 'test' is a standard UNIX program to perform basic string or numeric comparisons (among other things). Also, unlike many shells, sqsh has no built-in version of 'test'.

Sqsh does, however, support the standard short form of 'test':
```BASH
    \while [ $x -lt 10 ]        block    \done
```
With this expression the open brace ('[') is replaced by the sqsh parser with 'test', and the close brace (']') is discarded.

	**UNSUPPORTED EXPRESSIONS**
Currently sqsh does not support the standard shell predicate operators '&&'and '||'. These can be performed like so:
```BASH 
	\if sh -c "cmd1 && cmd2"        block    \done

	\if statement
```
The \if command performs conditional execution of a sqsh block based upon the outcome of a supplied expression:
```BASH 
    \if expr1        block1    \elif expr2        block2    \else        block3    \fi
```
In this example, if expression expr1 evaluates to true, then the blockblock1 is evaluated. Otherwise, if the expression expr2 evaluates to true,then block block 2 is evaluated. Finally, if all other tests fail block3 is evaluated.

Note that, unlike Bourne Shell, every \if command must be accompanies by a trailing \fi statement. Also the sqsh parser is not terribly intelligent: The\else and \fi statements must be the only contents on the line in which they appear, and they may not be aliased to another name.
```BASH
	\while statement
````
The \while command executes a block of sqsh code for the while a supplied expression remains true.
```BASH
    \while expr        block    \done
```
In this example, while the expression expr evaluates to true, then the block block is evaluated.

The \break statement may be used to break out of the inner-most \while or\for loop (more on \for below).
```BASH
\for statement
```
The \for command executes a block of sqsh code for each word supplied:
```BASH
    \for var in word ...        block    \done
```
For each word supplied, the value of the variable $var is set to the word and the block of code is executed. Execution ends when there are no more words in the list.

As with \while the \break statement may be used to break out of the inner-most execution loop.
```BASH
	\do command
```
The \do command is kind of a cross between a statement and a command.

It is a form of \go (see below for details on the \go command) in which a block of sqsh code may be executed for each row of data returned from the query. When the block is executed, special sqsh variables #[0-9]+ (a hash followed by a number) may be used to reference the values in the returned query.For example the following command:
```BASH
    select dbid, name from master..sysdatabases    \do        \echo "Checkpointing database #2, dbid #1"        use #2        go        checkpoint        go    \done
```
would cause a CHECKPOINT command to be issued in each database on the server.

	**COMMAND LINE OPTIONS**
The \do command establishes a new connection to be used by the block of code when executed. By default, this connection is established to the current server (the current setting of $DSQUERY), using the current username ($username) and the current password ($password). This behavior may,however, be overridden using command line options:
```
-D database  	Establishes the connection to the database as the supplied database.
-U username		Establishes the connection to the server as the supplied username.
-P password		Establishes the connection to the server using the supplied password (whichis hopefully a valid password for the supplied username).
-S server | host:port[:filter]	Establishes the connection to the supplied server.
-n				 Do not create a connection for use by the \do loop. This flag is mutuallyexclusive with the above flags. With this flag enabled, attempts to performdatabase commands within the block will generate a flurry of CT-Libraryerrors.
```
	**COLUMN VARIABLES**
As mentioned above, the values of the columns in the current result set may be determined using the special #[0-9]+ variables. Thus, the variable #1 would contain the value of column number one of the current result set, and #122 could contain the value of the 122'nd column (column numbers begin at 1).

In the case of nested \do loops, values in previous nesting levels may be referred to by simply appending an addition '#' for each previous nesting level, like so:
```BASH
    select id, name from sysobjects    \do        select name, indid from sysindexes where id = #1        \do            \echo "Table ##2 (objid ##1) has index #1"        \done    \done
```
obviously, this isn't the way you would do this query in real life, but you get the idea.

When expanding columns with NULL values, the column variable will expand to an empty string (''). Also, references to non-existent columns, such as #0,will result in an empty string ('').

As with regular sqsh variables (those referenced with a '$'), column variables will not be expanded when contained within single quotes.

	**ABORTING**
If the \break or \return commands are issued during the processing of a\do loop, the current query will be canceled, the connection used by the loop will be closed (unless the -n flag was supplied) and the \do loop will abort.
```BASH 
\func command
```
The \func command is used to define a reusable block of sqsh code as a function. Functions are defined like so:
```BASH
    \func stats        \if [ $# -ne 1 ]            \echo "use: stats [on | off]"            \return 1        \fi        set statistics io ${1}        set statistics time ${1}        go    \done
```
In this example a new function is established called stats that expects a single argument, either ``on'' or ``off''. Using this argument, stats will enable or disable time-based and I/O-based statistics.

Once established, the function may be called like so:
```BASH
    \call stats on
```
Causing all instances of ${1} to be replaced with the first command line argument to stats.

	**COMMNAND LINE OPTIONS**
Currently only one command line argument is available to the \func command.
```BASH
-x	Causes the function to be exported as a sqsh command. That is, the functionmay be invoked directly without requiring the \call command. This behavior isoptional because command names can potentially conflict with T-SQL keywords.When using this flag it is recommended that you prepend a backslash (\) to yourfunction name.
```
	**FUNCTION VARIABLES**
As shown in the example above, several special variables are available for use within the body of the function. These are:
```BASH
$#	Expands to the number of arguments supplied to the function or script wheninvoked.
$*	Expands to the complete list of arguments supplied to the function or scriptwhen invoked.
${0}..${N}	Expands to positional arguments to the function. ${0} is the name of thefunction or the script file being invoked, ${1} is the first argument,${2} the second and so-on, up to argument N. Note that, unlike most shells,sqsh requires that function arguments be referred to using the special curlybrace syntax (${1}, rather than $1). The reason for this is that $1 is a validMONEY value and using the curly braces gets rid of this ambiguity.
$?	After the invocation of a function, this will contain its return value (seebelow).
```
	**RETURN VALUE**
A value may be returned from a function via the \return command.

Like so:
```BASH
    \return N
```
Where N is a positive value. This return value is available to the caller of the function via the $? variable. As convention, a return value of 0 is used to indicate a success.

If \return is not explicitly called, the default return value is the current value of the $? variable (which is set to 0 upon entry of the function).Thus, if any SQL statements are invoked within the function, the default return value of $? will be the last error code returned during the processing of the SQL statement. 

	**KERBEROS SUPPORT**
Starting with version 2.1.6, sqsh provides the same command line options as isql to handle Kerberos network authentication.

In version 2.1.5 experimental Kerberos support was added using the -K and -R options. -K was merely a switch to set Kerberos on. In sqsh 2.1.6 a more advanced implementation of network authentication is introduced, although still experimental.

By using the parameters -K, -R, -V, -Z you can make use of your defined network security settings (libtcl.cfg). The named options are identical to the ones defined for isql.
```BASH
-K keytab_file
    Keytab_file name for DCE.
-R server_principal
    Server principal name when servername specified in interfaces differs from thereal server name.
-V [bcdimoqru]
    Specify security options to use with the security mechanism. Each characterstands for a specific security service.
-Z [secmech|default|none]
    Request a security mechanism defined for Kerberos, DCE or PAM in yourlibtcl.cfg file. Use secmech to specify the name of a SECURITY entry ordefault for the first available entry in libtcl.cfg. None must bespecified to disable network authentication or reset possible existingvalues in variables $secmech or $secure_options.
```
For example, connecting to a server using Kerberos (which happens to bethe default, i.e. first entry in libtcl.cfg [SECURITY] tab in this example):
```BASH
    ~$ sqsh -SSYB1502 -Uuser1 -RFC6A1502 -Z    \connect: Network authenticated session expires at:            16 Feb 2010 15:28:39 (11764 secs)    SYB1502.user1.master.1> select @@servername,@@authmech,                                 show_sec_services();    ----------------  -----------  ----------------------------------    FC6A1502          kerberos     unifiedlogin delegation mutualauth                                 integrity confidentiality                                 detectreplay detectseq
```
Note that the real name of the server (@@servername) differs from the server name in the interfaces file, so we have to specify the principal name through the -R parameter.When you do not specify the -V parameter together with -Z, all available security options will be enabled. When -V is specified without any security service options, only option u for Network Authentication will be implicitly set and the default security mechanism will be used if -Z is not specified.
```BASH
    [user1AATTlinux-fc6a ~]$ sqsh -SFC6A1502 -Uuser1 -V    Open Client Message    Layer 7, Origin 9, Severity 5, Number 1    ct_connect(): security service layer: internal security control                layer error:                Security service provider internal error -1765328352                occurred.    [user1AATTlinux-fc6a ~]$ kinit    Password for user1AATTLOCALDOMAIN:    [user1AATTlinux-fc6a ~]$ sqsh -SFC6A1502 -Uuser1 -V    \connect: Network authenticated session expires at:            16 Feb 2010 15:28:39 (10964 secs)    FC6A1502.user1.master.1>
```
When the connection succeeds, sqsh will store the real name of the security mechanism in the variable $secmech. For example: ```\echo $secmech``` may showcsfkrb5. The parameter -V takes a list of characters from the possible values of bcdimoqru. The option u enables Network Authentication, is the default and will allways be set when using -V or -Z, specified or not.
```BASH
    b - chanbinding     : Channel binding    c - confidentiality : Data confidentiality service    d - delegation      : Allow delegated credentials    i - integrity       : Data integrity service    m - mutualauth      : Mutual authentication for connection                          establishment    o - dataorigin      : Data origin stamping service    q - detectseq       : Out-of-sequence detection    r - detectreplay    : Data replay detection    u - unifiedlogin    : Network Authentication
```
Please check master.dbo.syssecmechs for available services. Non-existing or not supported services supplied with -V are silently ignored. If you specify-V and/or -Z, sqsh assumes network authentication is tried and no password is required.

If you have a network authenticated connection and want to \reconnect using normal ASE authentication with username and password, you have to reset the network authentication variables by specifying -Z none

For example:
```BASH
    [user1AATTlinux-fc6a ~]$ sqsh -SFC6A1502 -Uuser1 -V    \connect: Network authenticated session expires at:            16 Feb 2010 15:28:39 (10764 secs)    FC6A1502.user1.master.1> \echo $secmech csfkrb5    FC6A1502.user1.master.1> \reconnect -SASE1502 -Usa -Psybase    Open Client Message    Layer 7, Origin 9, Severity 5, Number 8    ct_connect(): security service layer: internal security control                layer error:    Consistency checks performed on the credential failed    (minor status 0).    FC6A1502.user1.master.1> \reconnect -SASE1502 -Usa -Psybase -Znone    ASE1502.sa.master.1>
```
The first \reconnect fails because sqsh still wants to try network authentication. However, no user principal for 'sa' exists and no ticket is set and thus the connection fails. The second \reconnect succeeds as the -Z none option reset appropriate variables.If the Kerberos ticket is renewed with kinit or any other client tool, the sqsh session must perform a \reconnect to refresh the credentials and to prevent a premature session abort. With the command \snace you can request for the session expiration interval. Depending on the security services that areset, the database connection may be closed without warning as soon as the ticket expires.

See chapter 16 "External Authentication" from the Sybase System Administration Guide volume 1 for more information on Kerberos network authentication i, e.a. 
##################COMMANDS############################ 
	**READ-EVAL-PRINT**
The read-eval-print loop is the heart of the sqsh system and is responsible for prompting a user for input and determining what should be done with it.Typically this loop is for internal use only, however they are open to the userbecause there are some creative things that can be done with them.

\loop [-i] [-n] [-e sql] [file]
    The \loop command reads input either from a file, a supplied SQL statement,or from a user (see the options below), determining whether the current line is a portion of a T-SQL statement or a sqsh command, and performing the appropriate action. When run in an interactive mode \loop is also responsible for displaying the current prompt (see $prompt below).

    \loop completes when all input has been depleted (end-of-file is encountered)or when a command, such as \exit requests that \loop exit.

        -i	Normally, if file is supplied and does not exist, \loop will return withan error condition, usually causing sqsh to exit. By supplying the -i flag,control will be returned to the calling loop as if end-of-file had been reached(that is, with no error condition).
        -n	By default, \loop will automatically attempt to connect to the database if aconnection has not already been established via the \connect command. The-n flag disables this behavior allowing \loop to process commands that donot require database support.
        -e sql	Causes \loop to process the contents of sql as if the user had typed it atthe prompt and an implicit call to \go is automatically appended to thestatement. If multiple instances of -e are supplied, they are all sent as asingle batch to the SQL Server for processing. This option may not be used incombination with a file name as well.
        file	Specifies the name of a file to be used as input rather than reading inputfrom the user or from the -e flag.

###########################DATABASE MANIPULATION#########################################
Given the size and complexity of sqsh (just look at the length of this man page), it is amazing how few database manipulation commands that there actually are. The following are commands that affect or use the current database connection:
```BASH
\connect [-A packet size] [-c] [-D db] [-G tds version} [-S srv] [-U user] [-P pass] [-I ifile] [-J charset] [-K keytab] [-R server_principal] [-n] [-N appname] [-Q query_timeout] [-T login_timeout] [-V [bcdimoqru]] [-X] [-z language] [-Z [secmech|default|none]]
    This command is used primarily for internal use to establish a connection to adatabase. If a connection is already established it has no effect, however if aconnection has not been established and $password has not been supplied, thenthe password is requested and a connection is established. \connect acceptsthe following parameters:

        -A	|Specifies the size of the network TDS packets used to communicate with the SQLserver. This value must be between 512 and 8192, and be a multiple of 512. Checkyour SQL Server configuration to determine supported packet sizes. This valuemay also be specified at run-time using the $packet_size variable.
        -c	|By default, the \connect command uses the contents of $database todetermine the database context that should be used upon establishing theconnection (this is used by \reconnect to preserve the current databasecontext upon reconnection). The -c flag suppresses this behavior and thedefault database context of login is used instead.
        -D db |Causes \connect to attempt to automatically switch the database context todb after establishing the connection. Using this flag is identical to setting the $database variable prior toestablishing the connection.
        -G tds version |Set the TDS version to use. See the global startup parameter -G for moreinformation on TDS version.
        -S srv host:port[:filter] |The name or address of the Sybase server to connect, this defaults to$DSQUERY if not supplied.
        -U user |The Sybase user to connect to the database as, this defaults to $usernamevariable if not supplied.
        -P pass |The password for user required to connect to server. This defaults to$password if not supplied.
        -I ifile	|The full path of an alternate Sybase interfaces file to use.
        -J charset	|The name of the client character set to communicate with the server.
        -K keytab_file |Used for DCE user authentication.
        -R principal_name	|Use for Kerberos user authentication to specify the name of the serverprincipal when the name differs from the $DSQUERY value. See also the discussion on Kerberos support.
        -n	|Specifies that the connection must use ANSI compliant chained mode.
        -N appname |Specify the application name the server will use for program_name in thesysprocesses table.
        -Q query_timeout |Set a query timeout period in seconds.
        -T login_timeout |Specifies a maximum wait time for session setup.
        -V [bcdimoqru] |Security services used for Kerberos support and other security mechanisms.
        -X	|Initiates the login connection to the server with client-side passwordencryption (if supported). If either SQL Server does not recognize this option,or if the version of CT-Lib used to compile sqsh does not support thisoption, then it will be ignored. This option may also be set using the$encryption environment variable.
        -z language |Specifies an alternate language to display sqsh prompts and messages. Withoutthe -z flag, the serverS default language will be used. This may also be setusing the $language variable.
        -Z [secmech|default|none] |Specifies the security mechanism to use for user authentication. For examplecsfkrb5 for Kerberos support.

\reconnect [-A packet size] [-c] [-D db] [-G tds version} [-S srv] [-U user] [-P pass] [-I ifile] [-J charset] [-K keytab] [-R server_principal] [-n] [-N appname] [-Q query_timeout] [-T login_timeout] [-V [bcdimoqru]] [-X] [-z language] [-Z [secmech|default|none]]
    The \reconnect command may be used to force a reconnection to the databaseusing a new username, server name, or password (if desired). If this commandfails, the current connection remains (if there is any), however if it succeedsthen the current connection is closed and the new connection becomes the onlyactive one.

    All arguments that are accepted by \connect are also accepted by\reconnect (in fact \reconnect uses \connect to establish the newconnection).
\run
    This command will execute a script file like \loop but the \run commandwill allow optional script parameters. Furthermore the command accepts thefollowing parameters.

        -e |Run the script file with echo on.
        -f |Suppress footers.
        -h |Suppress headers.
        -l |Suppres separator lines with pretty output style.
        -n |Disable SQL buffer variable expansion.
        -p |Report runtime statistics.
        -m style |Specify output style {bcp|csv|horiz|html|meta|none|pretty|vert}.
        -i filename	Required parameter to specify a filename to be run by sqsh.

        For example: \run -p -i ~/tmp/runtst.sqsh 10 -m pretty

\lcd dirname
    Local Change Directory. 
```

##############################**Historical Usage and Information**##########################################
When logged into a MySQL terminal and type 'help' the following screen is presented. 
```bash
:r           \abort       \alias       \bcp         \break       \buf-append  \buf-copy    \buf-del   
\buf-edit    \buf-get     \buf-load    \buf-save    \buf-show    \call        \clear       \connect   
\do          \done        \echo        \exit        \for         \func        \go          \help      
\hist-load   \hist-save   \history     \if          \jobs        \kill        \lcd         \lock      
\loop        \ls          \pwd         \quit        \read        \reconnect   \redraw      \reset     
\return      \rpc         \run         \set         \shell       \show        \sleep       \snace     
\unalias     \wait        \warranty    \while       emacs        vi           
Use '\help [command]' for more details
```

The following screen is presented when you type a command wrong in sqsh
```bash
go id first last name
Use: \go [-d display] [-e] [-h] [-f] [-l] [-n] [-p] [-m mode] [-s sec]
          [-t [filter]] [-w width] [-x [xgeom]] [-T title] [xacts]
     -d display  When used with -x, send result to named display
     -e          Echo SQL buffer to output
     -h          Suppress headers
     -f          Suppress footers
     -l          Suppress line separators with pretty style output mode
     -n          Do not expand variables
     -p          Report runtime statistics
     -m mode     Switch display mode for result set
     -s sec      Sleep sec seconds between transactions
     -t [filter] Filter SQL through program
                 Optional filter value overrides default variable $filter_prog
     -w width    Override value of $width
     -x [xgeom]  Send result set to a XWin output window
                 Optional xgeom value overrides default variable $xgeom
     -T title    Used in conjunction with -x to set window title
     xacts       Repeat batch xacts times
```
