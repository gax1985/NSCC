


```
Panic Soft
#NoFreeOnExit TRUE

define ROOT     C:\Program Files\nxlog
define CERTDIR  %ROOT%\cert
define CONFDIR  %ROOT%\conf\nxlog.d
define LOGDIR   %ROOT%\data

include %CONFDIR%\\*.conf
define LOGFILE  %LOGDIR%\nxlog.log
LogFile %LOGFILE%

Moduledir %ROOT%\modules
CacheDir  %ROOT%\data
Pidfile   %ROOT%\data\nxlog.pid
SpoolDir  %ROOT%\data

<Extension _syslog>
    Module      xm_syslog
</Extension>

<Extension _charconv>
    Module      xm_charconv
    AutodetectCharsets iso8859-2, utf-8, utf-16, utf-32
</Extension>

<Extension _exec>
    Module      xm_exec
</Extension>

<Extension _fileop>
    Module      xm_fileop

    # Check the size of our log file hourly, rotate if larger than 5MB
    <Schedule>
        Every   1 hour
        Exec    if (file_exists('%LOGFILE%') and \
                   (file_size('%LOGFILE%') >= 5M)) \
                    file_cycle('%LOGFILE%', 8);
    </Schedule>

    # Rotate our log file every week on Sunday at midnight
    <Schedule>
        When    @weekly
        Exec    if file_exists('%LOGFILE%') file_cycle('%LOGFILE%', 8);
    </Schedule>
</Extension>

# Snare compatible example configuration
# Collecting event log
# <Input in>
#     Module      im_msvistalog
# </Input>
# 
# Converting events to Snare format and sending them out over TCP syslog
# <Output out>
#     Module      om_tcp
#     Host        192.168.1.1
#     Port        514
#     Exec        to_syslog_snare();
# </Output>
# 
# Connect input 'in' to output 'out'
# <Route 1>
#     Path        in => out
# </Route>


## Extension Additions :
###############


<Extension _xm_json>
	Module xm_json
</Extension>

<Extension _xm_syslog>
	Module xm_syslog
</Extension>


## Inputs :
############
<Input security_in>
	Module 		im_msvistalog
	<QueryXML>
		<QueryList>
			<Query Id=0>
				<Select Path="Security">*</Select>
			</Query>
		</QueryList>
	</QueryXML>
</Input

## Outputs :
############
<Output external_file>
	Module om_file
	File "C:\\Users\\W0400411\\Desktop\\security_events.json"
	Exec to_json();
</Output>


## The Route: 
#############

<Route>
	Path security_in => external_file
</Route>


```


## Sources 


Here are the direct links to the official online documentation for every module we used. I have mapped them specifically to the parts of your assignment so you can verify the syntax yourself.

---

### Part 1: Extensions (`xm_json` & `xm_syslog`)

You asked why we need these blocks. The documentation confirms these modules provide the "dictionaries" (functions) like `to_json()` or `parse_syslog()`.

- **Module:** `xm_json` (JSON Extension)
    
    - **Documentation Link:** [NXLog xm_json Documentation](https://docs.nxlog.co/agent/current/xm/json.html)
        
    - **Verification:** Look for the **`to_json()`** function on this page. It confirms that this function _"converts the fields to JSON"_.
        
- **Module:** `xm_syslog` (Syslog Extension)
    
    - **Documentation Link:** [NXLog xm_syslog Documentation](https://docs.nxlog.co/agent/current/xm/syslog.html)
        
    - **Verification:** This page confirms that loading this module allows you to use `parse_syslog()` and `to_syslog_bsd()`.
        

### Part 2: Input (`im_msvistalog`)

This was the tricky part where we chose `<QueryXML>` over the simpler `Channel` directive.

- **Module:** `im_msvistalog` (Windows Event Log for Vista/2008+)
    
    - **Documentation Link:** [NXLog im_msvistalog Documentation](https://docs.nxlog.co/agent/current/im/msvistalog.html)
        
    - **Verification:** Scroll down to the **Configuration** section. You will see the `<QueryXML>` block structure there. It confirms this module is used for collecting local Windows Event Logs.
        

### Part 3: Output (`om_file`)

This is where we defined the destination file on your C: drive.

- **Module:** `om_file` (File Output)
    
    - **Documentation Link:** [NXLog om_file Documentation](https://docs.nxlog.co/agent/current/om/file.html)
        
    - **Verification:** Check the **`File`** directive on this page. It confirms that this is mandatory and specifies the output filename. You can also see examples of using `Exec` inside the output block here.
        

### Part 4: Route (`Path`)

This connects your Input to your Output.

- **Concept:** Routes & Paths
    
    - **Documentation Link:** [NXLog Route Settings Documentation](https://docs.nxlog.co/agent/current/config/route-settings.html)
        
    - **Verification:** This page explains the syntax `Path Input_Name => Output_Name` and confirms that without this, the data flow is disconnected.
        

### A Note on "Example 53"

The specific **"Example 53"** referenced in our conversation comes from the **PDF Reference Manual (v3.0.14)** you uploaded . The online documentation is constantly updated (currently v6.x or "Agent Current"), so the example numbers will not match the PDF. However, the _syntax_ for the QueryXML block in the link above is identical to the PDF version you are using.****