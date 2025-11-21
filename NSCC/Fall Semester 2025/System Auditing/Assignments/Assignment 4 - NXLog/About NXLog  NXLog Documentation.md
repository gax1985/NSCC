---
title: "About NXLog | NXLog Documentation"
source: "https://docs.nxlog.co/userguide/intro/about-nxlog.html"
author:
published:
created: 2025-11-19
description: "This section introduces the features and log collection technologies available in NXLog that builds up a comprehensive, multi-platform, high-performance logging solution."
tags:
  - "clippings"
---
## About NXLog

Modern IT infrastructure produces large volumes of event logging data. In a single organization, hundreds or thousands of different devices, applications, and appliances generate event log messages. These messages require many log processing tasks, including filtration, classification, correlation, forwarding, and storage. In most organizations these requirements are met with a collection of scripts and programs, each with its custom format and configuration. NXLog provides a single, high-performance, multi-platform product for solving all of these tasks and achieving consistent results.

At NXLog’s inception, there were various logging solutions available, but none with the required features. Most were single-threaded and Syslog-oriented, without native support for Windows. Work on NXLog began with the goal of building a modern logger with a multi-threaded design, a clear configuration syntax, multi-platform support, and clean source code. NXLog was born in 2009 as a closed source product heavily used in several production deployments. The source code of NXLog Community Edition was released in November 2011.

NXLog can process event logs from thousands of different sources with volumes over 100,000 events per second. It can accept event logs over TCP, TLS/SSL, and UDP; from files and databases; and in Syslog, Windows Event Log, and JSON formats. NXLog can also perform advanced processing on log messages, such as rewriting, correlating, alerting, pattern matching, scheduling, and log file rotation. It supports prioritized processing of certain log messages, and can buffer messages on disk or in memory to work around problems with input latency or network congestion. After processing, NXLog can store or forward event logs in any of many supported formats. Inputs, outputs, log formats, and complex processing are implemented with a modular architecture and a powerful configuration language.

## NXLog features

This section gives an overview of some of the key advantages of NXLog over alternative systems.

#### Multi-platform deployment

Installer packages are provided for multiple platforms, including Linux and Windows. You can use NXLog across your entire infrastructure, without resorting to different tools for different platforms.

#### Client or server operation

Depending on the configuration, NXLog will run as a server, a client, or a combination of both. You have the freedom to choose the deployment architecture that best meets your needs. For example, NXLog can collect local log data and forward it, relay data without storing it locally, or save incoming log data to disk.

#### Many input and output types and formats

NXLog can accept data from many different sources, convert the data internally, and output it to other destinations. You can use NXLog as a single tool to process all of the different types of logs in your organization. For example, logs can be collected from files, databases, Unix domain sockets, network connections, and other sources. BSD Syslog, IETF Syslog, the Snare Agent format, Windows Event Log, JSON, and other formats are supported. NXLog can likely be configured to read or write logs in your custom application format, using the NXLog language and provided extension modules.

#### High performance, scalable architecture

With an event-based architecture for processing tasks in parallel, non-blocking input and output where possible, and a worker thread pool for incoming log messages, NXLog is designed for high performance on modern multi-core and multi-processor systems. The input/output readiness notifications provided by most operating systems are used to efficiently handle large numbers of open files and network connections.

#### Security

NXLog provides features throughout the application to maintain the security of your log data and systems. The core can be configured to run as an unprivileged user, and special privileges (such as binding to ports below 1024) are accessed through Linux capabilities rather than requiring the application to run as root. TLS/SSL is supported for encrypted, authenticated communications and to prevent data interception or alteration during transmission.

#### Modular architecture

NXLog has a lightweight, modular architecture, providing a reduced memory footprint and increased flexibility for different uses. The core handles files, events, and sockets, and provides the configuration language; modules provide the input, output, and processing capabilities. Because modules use a common API, you can write new modules to extend the features of NXLog.

#### Message buffering

Log messages can be buffered in memory or on disk. This increases reliability by holding messages in a temporary cache when a network connectivity issue or dropout occurs. Conditional buffering can be configured by using the NXLog language to define relevant conditions. For example, UDP messages may arrive faster than they can be processed, and NXLog can buffer the messages to disk for processing when the system is under less load. Conditional buffering can be used to explicitly buffer log messages during certain hours of the day or when the system load is high.

#### Prioritized processing

NXLog can be configured to separate high-priority log processing from low-priority log processing, ensuring that it processes the most important data first. When the system is experiencing high load, NXLog will avoid dropping important incoming messages. For example, incoming UDP messages can be prioritized to prevent dropped logs if a high volume of TCP messages overloads the system.

#### Message durability

Built-in flow control ensures that a blocked output does not cause dropped log messages when buffers are full. In combination with the previously mentioned parallel processing, buffering, and prioritization, the possibility of message loss is greatly reduced.

#### Familiar and powerful configuration syntax

NXLog uses an Apache-style configuration syntax that is easy to read and can be parsed or generated with scripts. The NXLog language supports advanced scripting and processing capabilities that are usually only found in full-fledged scripting languages. The syntax is similar to Perl, so users familiar with that language can learn it easily. It supports polymorphic functions and procedures and regular expressions with captured sub-strings. Modules can register additional functions and procedures to further extend the capabilities of the language.

#### Scheduled tasks and log rotation

NXLog includes a scheduler service. A task can be scheduled from any module without requiring an external tool such as Cron. Log files can be rotated automatically, on a time-based schedule or according to file size. The file reader and writer modules in NXLog can detect when an input or output file moves or changes its name, and re-open the file automatically.

#### Advanced message processing

NXLog can perform advanced processing actions on log messages, in addition to the core features already mentioned. By using additional modules, NXLog can solve many related tasks such as message classification, event correlation, pattern matching, message filtering, message rewriting, and conditional alerting. You can use a single tool for all log processing functionality.

#### Offline processing

Sometimes log messages need to be processed in batches for conversion, filtering, or analysis. NXLog provides an offline mode in which it processes all input and then exits. Because NXLog does not assume that the event time and processing time are identical, time-based correlation features can be used even during offline log processing.

#### International character and encoding support

NXLog supports explicit character set conversion and automatic character set detection. Log messages received in different character sets can be automatically normalized to a common standard, allowing messages to be compared across different sources.

## NXLog Enterprise Edition features

While the NXLog Community Edition provides all the flexibility and performance of the NXLog engine, the NXLog Enterprise Edition provides additional enhancements, including modules and core features, as well as regular hot-fixes and updates which are crucial in a professional environment. The Enterprise Edition provides the following enhancements.

#### Additional platform support

In addition to Linux and Windows, installer packages are provided for the BSDs and the major variants of Unix (AIX, Solaris, and macOS) operating systems.

#### Signed installer packages

Installer packages are digitally signed to ensure that the binaries are not corrupted or compromised. In many cases, this is a compliance mandate.

#### On-the-wire compression

Log data can be transferred in compressed batches with the [im\_batchcompress](https://docs.nxlog.co/refman/current/im/batchcompress.html) and [om\_batchcompress](https://docs.nxlog.co/refman/current/om/batchcompress.html) input/output modules. This can help in limited bandwidth scenarios.

#### Better control over SSL and TLS

Due to vulnerabilities discovered in the SSL protocols, some protocols may need to be disabled. The various SSL/TLS networking modules in NXLog Enterprise Edition can be configured to allow only specific protocols via the SSLProtocol directive. On Windows, NXLog Enterprise Edition can utilize TLSv1.2 while NXLog Community Edition supports TLSv1.0 only.

#### ODBC input and output

The ODBC input and output modules, [im\_odbc](https://docs.nxlog.co/refman/current/im/odbc.html) and [om\_odbc](https://docs.nxlog.co/refman/current/om/odbc.html), allow log data to be read from or inserted into any ODBC-compliant database. The primary purpose of the *im\_odbc* module is native Windows MSSQL support to enable log collection from Windows applications that write logs to MSSQL. The *om\_odbc* output module can be used to insert data into an ODBC database. These modules are available on Windows and Linux too.

#### Remote management

The dedicated [xm\_admin](https://docs.nxlog.co/refman/current/xm/admin.html) extension module enables NXLog agents to be managed remotely over a secure SOAP/JSON SSL connection or to be integrated with existing monitoring and management tools. The configurations, correlation rules, patterns, and certificates can all be updated remotely from the NXLog Manager web interface or from scripts. In addition, the NXLog agents and the individual modules can be stopped/started and log collection statistics can be queried for real-time statistics.

Crash recovery

Additional functionality is provided to guarantee a clean recovery in the case of a system crash, ensuring that no messages are lost or duplicated.

Event correlation

The [pm\_evcorr](https://docs.nxlog.co/refman/current/pm/evcorr.html) processor module can efficiently solve complex event correlation tasks, with capabilities similar to what the open-source SEC tool provides.

HTTP/HTTPS support

The [im\_http](https://docs.nxlog.co/refman/current/im/http.html) and [om\_http](https://docs.nxlog.co/refman/current/om/http.html) input and output modules make it possible to send or receive log message data over HTTP or HTTPS.

TCP and UDP support

Accepting and initiating TCP and UDP connections to a remote server can be achieved using the dedicated protocol-specific [im\_tcp](https://docs.nxlog.co/refman/current/im/tcp.html) and [om\_tcp](https://docs.nxlog.co/refman/current/om/tcp.html) modules, as well as the [im\_udp](https://docs.nxlog.co/refman/current/im/udp.html) and [om\_udp](https://docs.nxlog.co/refman/current/om/udp.html) modules respectively.

UDP source IP address spoofing

Some SIEM and log collection systems use the IP address of the UDP Syslog packet sent by the client. As a server or relay, the [om\_udpspoof](https://docs.nxlog.co/refman/current/om/udpspoof.html) output module can be configured to retain the original IP address of the sender.

File integrity monitoring

Several compliance standards mandate file integrity monitoring. With the [im\_fim](https://docs.nxlog.co/refman/current/im/fim.html) input module, NXLog Enterprise Edition can be used to detect modifications to files or directories. This module is available on Windows as well as Linux.

Registry monitoring

The [im\_regmon](https://docs.nxlog.co/refman/current/im/regmon.html) module facilitates the monitoring of the Windows Registry and generates event records in case of changes in the monitored registry entries.

Network monitoring

The passive monitoring of network traffic can be implemented via utilizing the [im\_pcap](https://docs.nxlog.co/refman/current/im/pcap.html) module.

XML support

The [xm\_xml](https://docs.nxlog.co/refman/current/xm/xml.html) extension module can parse nested XML and data stored in XML attributes.

JSON support

Parsing of nested JSON is implemented in the [xm\_json](https://docs.nxlog.co/refman/current/xm/json.html) module. UTF-8 character encoding validation can be enforced to avoid parser failures caused by invalid UTF-8 encoding from other tools.

Support of key-value pairs

Parsing and generation of key-value formatted data can be accomplished by using the [xm\_kvp](https://docs.nxlog.co/refman/current/xm/kvp.html) module.

Parsing with patterns

- The [xm\_grok](https://docs.nxlog.co/refman/current/xm/grok.html) module can parse data using Grok patterns.
- The database of patterns in XML format can be applied using the [xm\_pattern](https://docs.nxlog.co/refman/current/xm/pattern.html) module.

Parsing multi-line logs

Messages which span multiple lines can be processed with the [xm\_multiline](https://docs.nxlog.co/refman/current/xm/multiline.html) module. The flexible configuration of the module is reached through the specification of the header line, the footer line, and the number of lines in a message.

Native W3C parser

The W3C format is widely used in various Microsoft products and perhaps IIS is the most well-known producer. Parsing of W3C is possible with the [xm\_csv](https://docs.nxlog.co/refman/current/xm/csv.html) extension module, but that requires defining the fields in the configuration and adjustment when the IIS configuration is changed. The [xm\_w3c](https://docs.nxlog.co/refman/current/xm/w3c.html) extension module can automatically parse the logs using the field information stored in the headers. It also supports automatic parsing of the data format produced by BRO.

More support for SIEM products

The [xm\_cef](https://docs.nxlog.co/refman/current/xm/cef.html) and [xm\_leef](https://docs.nxlog.co/refman/current/xm/leef.html) modules provide parsing and generation of CEF and LEEF formatted data. CEF (Common Event Format) was introduced by HP ArcSight and LEEF (Log Event Extended Format) is used by IBM Security QRadar.

Simplified data processing configuration

Two extension modules help simplify data processing. The [xm\_rewrite](https://docs.nxlog.co/refman/current/xm/rewrite.html) module allows fields to be renamed, kept (whitelisted), or deleted (blacklisted). It also supports the Exec directive so log processing logic can be localized to avoid duplicated statements. The [xm\_filelist](https://docs.nxlog.co/refman/current/xm/filelist.html) module provides two functions, [contains()](https://docs.nxlog.co/refman/current/xm/filelist.html#func-contains) and [matches()](https://docs.nxlog.co/refman/current/xm/filelist.html#func-matches), which can be invoked to check whether a string is present in a text file. This can be a username or an IP address for example. The files are cached in memory and any changes are automatically picked up without the need to reload NXLog.

Custom input, output, and extension modules

The Enterprise Edition of NXLog supports custom modules which can be developed in the following programming languages:

- Golang via the [im\_go](https://docs.nxlog.co/refman/current/im/go.html), [om\_go](https://docs.nxlog.co/refman/current/om/go.html), and [xm\_go](https://docs.nxlog.co/refman/current/xm/go.html) modules
- Java via the [im\_java](https://docs.nxlog.co/refman/current/im/java.html), [om\_java](https://docs.nxlog.co/refman/current/om/java.html), and [xm\_java](https://docs.nxlog.co/refman/current/xm/java.html) modules
- Perl via the [im\_perl](https://docs.nxlog.co/refman/current/im/perl.html), [om\_perl](https://docs.nxlog.co/refman/current/om/perl.html), and [xm\_perl](https://docs.nxlog.co/refman/current/xm/perl.html) modules
- Python via the [im\_python](https://docs.nxlog.co/refman/current/im/python.html), [om\_python](https://docs.nxlog.co/refman/current/om/python.html), and [xm\_python](https://docs.nxlog.co/refman/current/xm/python.html) modules
- Ruby via the [im\_ruby](https://docs.nxlog.co/refman/current/im/ruby.html), [om\_ruby](https://docs.nxlog.co/refman/current/om/ruby.html), and [xm\_ruby](https://docs.nxlog.co/refman/current/xm/ruby.html) modules

Name resolution

The [xm\_resolver](https://docs.nxlog.co/refman/current/xm/resolver.html) extension module provides cached DNS lookup functions for translating between IP addresses and host names. User and group names can also be mapped to/from user and group ids.

Elasticsearch integration

The [om\_elasticsearch](https://docs.nxlog.co/refman/current/om/elasticsearch.html) output module allows log data to be loaded directly into an Elasticsearch server without requiring Logstash.

Check Point LEA input

The [im\_checkpoint](https://docs.nxlog.co/refman/current/im/checkpoint.html) input module enables the remote collection of Check Point firewall logs over the OPSEC/LEA protocol. This feature is only available in the Linux version.

Redis Support

Redis is often used as an intermediate queue for log data. Two native modules, [im\_redis](https://docs.nxlog.co/refman/current/im/redis.html) and [om\_redis](https://docs.nxlog.co/refman/current/om/redis.html), are available to push and pull data to and from Redis servers.

SNMP input

The [xm\_snmp](https://docs.nxlog.co/refman/current/xm/snmp.html) extension module can be used to parse SNMP traps. The traps can then be handled like regular log messages: converted to Syslog, stored, forwarded, etc.

Multi-platform support for Windows Event Forwarding

The [im\_wseventing](https://docs.nxlog.co/refman/current/im/wseventing.html) input module can be used to collect forwarded events from Windows hosts. The Windows clients can be configured from Group Policy to send Windows Event Log using Windows Event Forwarding. While NXLog Enterprise Edition can collect Windows Event Log remotely over WMI and MSRPC, this module provides improved security for collecting from Windows machines in agentless mode, with support for both Kerberos and HTTPS data transfer. The *im\_wseventing* module is platform independent and available on Linux as well as Windows.

HDFS output

The [om\_webhdfs](https://docs.nxlog.co/refman/current/om/webhdfs.html) output module is available to support the Hadoop ecosystem.

Windows Performance Counters

The [im\_winperfcount](https://docs.nxlog.co/refman/current/im/winperfcount.html) input module can collect metrics from Windows Performance Counters such as CPU, disk, and memory statistics.

Reading Windows Event Log files directly

The [im\_msvistalog](https://docs.nxlog.co/refman/current/im/msvistalog.html) module can read `.evt`, `.evtx`, and `.etl` event log files directly; this is particularly useful for forensics purposes.

Additional Windows Event Log data

The [im\_msvistalog](https://docs.nxlog.co/refman/current/im/msvistalog.html) module retrieves the *EventData* and *UserData* parts which can contain important data in some log sources. In addition, SID values in the Windows Event Log *record* can be resolved to account names to produce the same output that Windows Event Viewer gives.

Event Tracing for Windows

The [im\_etw](https://docs.nxlog.co/refman/current/im/etw.html) module provides direct reading of event tracing data of both kernel and user-mode applications.

Netflow support

The [xm\_netflow](https://docs.nxlog.co/refman/current/xm/netflow.html) extension module can parse Netflow packets received over UDP. It supports Netflow v1, v5, v7, v9, and IPFIX.

ZeroMQ support

ZeroMQ is a popular high performance messaging library. The [im\_zmq](https://docs.nxlog.co/refman/current/im/zmq.html) and [om\_zmq](https://docs.nxlog.co/refman/current/om/zmq.html) modules provide input and output support for the ZeroMQ protocol.

Named pipes and domain sockets

The Enterprise Edition supports communicating logs via:

Testing facilities

Simple test events can be generated using the [im\_testgen](https://docs.nxlog.co/refman/current/im/testgen.html) module according to the specified counter. The [im\_null](https://docs.nxlog.co/refman/current/im/null.html) and [om\_null](https://docs.nxlog.co/refman/current/om/null.html) module can be used for testing purposes as well.

The [om\_blocker](https://docs.nxlog.co/refman/current/om/blocker.html) module can be used for blocking messages to simulate a blocked route.

Mark messages

Via the [im\_mark](https://docs.nxlog.co/refman/current/im/mark.html) module, NXLog can send mark messages confirming its correct operation.

Data transformation

NXLog Enterprise Edition supports conversion of message strings between various character sets. This may be useful when the encoding of accepted messages differs from UTF-8.  
Compression and encryption operations with logs are available via the [xm\_zlib](https://docs.nxlog.co/refman/current/xm/zlib.html) and [xm\_crypto](https://docs.nxlog.co/refman/current/xm/crypto.html) modules.

Manipulation with files

NXLog Enterprise Edition provides retention and rotation policies which can be applied to files, such as log retention based on the file size and age, and cyclic rotation and retention of files. All these features are available via the [xm\_fileop](https://docs.nxlog.co/refman/current/xm/fileop.html) module.

Execution of external scripts

External scripts can be run on startup at the input, output, and extension levels using the [im\_exec](https://docs.nxlog.co/refman/current/im/exec.html),[om\_exec](https://docs.nxlog.co/refman/current/om/exec.html), and [xm\_exec](https://docs.nxlog.co/refman/current/xm/exec.html) modules respectively.

Support of various log sources

NXLog Enterprise Edition supports a wider variety of log sources and provides additional functionalities to the modules which exist in both the Enterprise and Community versions of NXLog.

Buffering of messages

Using the [pm\_buffer](https://docs.nxlog.co/refman/current/pm/buffer.html) prevents from losing messages which arrive over UDP.

Regular hot fixes

Unlike NXLog Community Edition which is a volunteer effort, NXLog Enterprise Edition receives regular hot fixes and enhancements.

World class support

For NXLog Enterprise Edition, a dedicated professionally trained support team is available and ready to act at request. They can be available 24/7 with a world-class, 4-hour SLA.

Extensive documentation

Our constantly updated, ever-growing documentation, already well above 1500 pages, is a stand-alone product in itself. It is complete with configuration samples, real-world examples, and integration guides offering much more than a generic manual.

## Comparison of features

This section compares the features of the NXLog Community Edition and the NXLog Enterprise Edition as well as highlights the differences between them.

There are three possible scenarios in how the features overlap and differentiate between the two editions:

- The feature is present only in NXLog Enterprise Edition.
- The feature is present in both editions of NXLog with the exact same functionality.
- The feature is present in both editions of NXLog, but NXLog Enterprise Edition provides additional or enhanced functionality. In such cases, a link to a more detailed description of these differences is provided in the first column of the matrix table.

For easier interpretation, all NXLog features are grouped into the following logical subsections:

An NXLog Community Edition installation can be upgraded to NXLog Enterprise Edition. See the [Deployment](https://docs.nxlog.co/userguide/deploy/index.html) guide for your platform for more information.

### Supported formats

One of the most important aspects of logs is the format. It is crucial for log files that need to be read by other applications. Above all, it is best if logs are stored as structured data, rather than unstructured text. The format affects availability, readability, manageability, and size.

This subsection compares the data formats NXLog supports. In addition to these formats, NXLog can read and process log data using pattern matching to transform unstructured data into normalized, structured data.

<table><caption>Table 1. Supported formats and patterns</caption> <colgroup><col> <col> <col> <col></colgroup><thead><tr><th>Format and Pattern Name</th><th>NXLog Community Edition</th><th>NXLog Enterprise Edition</th><th>Feature advantage</th></tr></thead><tbody><tr><td colspan="4"><p><strong>The existing log formats</strong></p></td></tr><tr><td><p>AIX Audit Format (<a href="https://docs.nxlog.co/refman/current/xm/aixaudit.html">xm_aixaudit</a>)</p></td><td></td><td></td><td><p>In combination with the <a href="https://docs.nxlog.co/refman/current/im/file.html">im_file</a> module, this module can collect and parse AIX Audit events.</p></td></tr><tr><td><p>Apple System Log (<a href="https://docs.nxlog.co/refman/current/xm/asl.html">xm_asl</a>)</p></td><td></td><td></td><td><p>Apple system logs stored as ASL files and can be read and parsed using this module.</p></td></tr><tr><td><p>Solaris OS Basic Security Module (BSM) Auditing API (<a href="https://docs.nxlog.co/refman/current/im/bsm.html">im_bsm</a>, <a href="https://docs.nxlog.co/refman/current/xm/bsm.html">xm_bsm</a>)</p></td><td></td><td></td><td><p>Reads and processes BSM audit events either from file (<em>xm_bsm</em>) or directly from the kernel (<em>im_bsm</em>).</p></td></tr><tr><td><p>ArcSight Common Event Format (<a href="https://docs.nxlog.co/refman/current/xm/cef.html">xm_cef</a>)</p></td><td></td><td></td><td><p>Using this feature, the ArcSight CEF-formatted events can be both generated and read.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/userguide/intro/#supported-formats-csv">CSV</a> (<a href="https://docs.nxlog.co/refman/current/xm/csv.html">xm_csv</a>)</p></td><td></td><td></td><td><p>Generation and parsing of delimiter-separated data is an essential feature of the <em>xm_csv</em> module.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/userguide/intro/#supported-formats-gelf">Graylog Extended Log Format</a> (<a href="https://docs.nxlog.co/refman/current/xm/gelf.html">xm_gelf</a>)</p></td><td></td><td></td><td><p>This module enables receiving data in GELF format over the network as well as formatting data to GELF while forwarding it over the network.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/userguide/intro/#supported-formats-json">JSON</a> (<a href="https://docs.nxlog.co/refman/current/xm/json.html">xm_json</a>)</p></td><td></td><td></td><td><p>Converts raw events to JSON format as well as parses events from received JSON logs.</p></td></tr><tr><td><p>Key-Value Pairs (<a href="https://docs.nxlog.co/refman/current/xm/kvp.html">xm_kvp</a>)</p></td><td></td><td></td><td><p>Convenient method for distilling data formatted as key-value pairs (KVPs).</p></td></tr><tr><td><p>Log Event Extended Format (<a href="https://docs.nxlog.co/refman/current/xm/leef.html">xm_leef</a>)</p></td><td></td><td></td><td><p>Generates and reads the Log Event Extended Format (LEEF) commonly used by IBM Security QRadar products.</p></td></tr><tr><td><p>DNS Server Logs (<a href="https://docs.nxlog.co/refman/current/xm/msdns.html">xm_msdns</a>)</p></td><td></td><td></td><td><p>Reads Windows DNS Server logs and parses over 20 fields commonly used with these events.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/userguide/intro/#supported-formats-multiline-log-messages">Multiline Log Messages</a> (<a href="https://docs.nxlog.co/refman/current/xm/multiline.html">xm_multiline</a>)</p></td><td></td><td></td><td><p>A complete solution for processing multiline log events. Supports any combination of header lines, footer lines, and fixed line counts.</p></td></tr><tr><td><p>NetFlow Payload (<a href="https://docs.nxlog.co/refman/current/xm/netflow.html">xm_netflow</a>)</p></td><td></td><td></td><td><p>In combination with the <em>im_udp</em> module, this feature provides convenient parsing of Netflow protocol versions v1, v5, v7, v9, and IPFIX.</p></td></tr><tr><td><p>Radius NPS (<a href="https://docs.nxlog.co/refman/current/xm/nps.html">xm_nps</a>)</p></td><td></td><td></td><td><p>Allows for parsing file-based data in NPS Database format across all implementations, i.e. both IAS and NPS formatted data.</p></td></tr><tr><td><p>SNMP Trap Messages (<a href="https://docs.nxlog.co/refman/current/xm/snmp.html">xm_snmp</a>)</p></td><td></td><td></td><td><p>Provides capabilities for reading SNMP v1, v2c, and v3 trap messages.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/userguide/intro/#supported-formats-syslog">Syslog</a> (<a href="https://docs.nxlog.co/refman/current/xm/syslog.html">xm_syslog</a>)</p></td><td></td><td></td><td><p>Support for reading and writing all Syslog formats: BSD, IETF, and Snare.</p></td></tr><tr><td><p>W3C Extended Log File Format (<a href="https://docs.nxlog.co/refman/current/xm/w3c.html">xm_w3c</a>)</p></td><td></td><td></td><td><p>Supports parsing of data in the W3C Extended Log File Format, Zeek format, and Microsoft Exchange Message Tracking logs.</p></td></tr><tr><td><p>Binary WTMP Files (<a href="https://docs.nxlog.co/refman/current/xm/wtmp.html">xm_wtmp</a>)</p></td><td></td><td></td><td><p>Enables processing of binary <code>wtmp</code> files when used in conjunction with the <em>im_file</em> module.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/userguide/intro/#supported-formats-xml">XML</a> (<a href="https://docs.nxlog.co/refman/current/xm/xml.html">xm_xml</a>)</p></td><td></td><td></td><td><p>Enables parsing and writing XML-formatted data.</p></td></tr><tr><td colspan="4"><p><strong>Parsing with patterns</strong></p></td></tr><tr><td><p>Parsing with Grok Patterns (<a href="https://docs.nxlog.co/refman/current/xm/grok.html">xm_grok</a>)</p></td><td></td><td></td><td><p>Functionality for reading any kind of text log messages using Grok patterns.</p></td></tr><tr><td><p>Parsing with the Pattern Database (<a href="https://docs.nxlog.co/refman/current/xm/pattern.html">xm_pattern</a>)</p></td><td></td><td></td><td><p>Efficient, non-linear pattern matching using a pattern database in XML format. Each pattern definition can contain multiple field definitions thus allowing multi-dimensional pattern matching.</p></td></tr></tbody></table>

The following features are available in both editions of NXLog, but NXLog Enterprise Edition provides additional or enhanced functionality.

#### CSV

Although both versions of NXLog support processing CSV data, only NXLog Enterprise Edition provides **Field Count Enforcement** with its [StrictMode](https://docs.nxlog.co/refman/current/xm/csv.html#config-strictmode) directive that accepts a boolean value. When set to `TRUE`, the parser will ignore any CSV line not having the same number of fields as those listed in the [Fields](https://docs.nxlog.co/refman/current/xm/csv.html#config-fields) directive.

#### Graylog Extended Log Format (GELF)

NXLog Enterprise Edition enables these additional options for processing data in the Graylog Extended Log Format:

TCP input

When set to `GELF_TCP` and used in conjunction with the [TCP (im\_tcp)](https://docs.nxlog.co/refman/current/im/tcp.html) input module, the [InputType](https://docs.nxlog.co/refman/current/xm/gelf.html#inputtype-gelf-tcp) directive allows GELF data to be received over TCP.

Hidden fields

The [IncludeHiddenFields](https://docs.nxlog.co/refman/current/xm/gelf.html#config-includehiddenfields) directive, with a default boolean value of `TRUE`, supports inclusion of fields with names having a leading dot (`.`) or underscore (`_`) which would otherwise be discarded.

Event enrichment

GELF events are enriched with some [additional fields](https://docs.nxlog.co/refman/current/xm/gelf.html#fields):`$EventTime`, `$FullMessage`, `$Hostname`, `$SeverityValue`, `$ShortMessage`,`$SourceLine`, `$SyslogFacility`, and `$version`.

#### JSON

The [xm\_json](https://docs.nxlog.co/refman/current/xm/json.html) module of NXLog Enterprise Edition has several directives for customizing how JSON data is parsed and prepared for output:

Custom datetime formats

The *xm\_json* [DateFormat](https://docs.nxlog.co/refman/current/xm/json.html#config-dateformat) overrides the global [DateFormat](https://docs.nxlog.co/refman/current/configuration.html#global-dateformat).

Nested structure detection

By default,[DetectNestedJSON](https://docs.nxlog.co/refman/current/xm/json.html#config-detectnestedjson) is set to `TRUE` and preserves nested structures. `FALSE` will turn detection off and convert any values containing a JSON key-value pair to a flat string, e.g.`{"key":{"subkey":42}}` would be converted to `{"key":"{\"subkey\":42}"}`.

Flatten nested structures

The [Flatten](https://docs.nxlog.co/refman/current/xm/json.html#config-flatten) directive takes nested JSON fields and creates field names with dot notation to flatten the structure. For example, the following JSON structure:

```json
{"event":{"time":"2015-01-01T00:00:00.000Z","severity":"ERROR"}}
```

json

will be converted to

```json
{"event.time":"2015-01-01T00:00:00.000Z","event.severity":"ERROR"}
```

json

[ForceUTF8](https://docs.nxlog.co/refman/current/xm/json.html#config-forceutf8)

Converts the output to validated UTF-8 encoding regardless of the input encoding.

[IncludeHiddenFields](https://docs.nxlog.co/refman/current/xm/json.html#config-includehiddenfields)

Preserves hidden fields, i.e. those having names with a leading dot (`.`) or underscore (`_`).

[ParseDate](https://docs.nxlog.co/refman/current/xm/json.html#config-parsedate)

Enables automatic parsing of strings beginning with a 4-digit year as timestamps.

[PrettyPrint](https://docs.nxlog.co/refman/current/xm/json.html#config-prettyprint)

Takes single-line JSON records, puts each key-value pair on a new line, and indents elements based on the depth of nesting for creating a more human-readable data record.

[UnFlatten](https://docs.nxlog.co/refman/current/xm/json.html#config-unflatten)

Is the inverse of the [Flatten](https://docs.nxlog.co/refman/current/xm/json.html#config-flatten) process when using [to\_json()](https://docs.nxlog.co/refman/current/xm/json.html#proc-to-json) to recreate nested structures on output.

#### Multiline log messages

The [xm\_multiline](https://docs.nxlog.co/refman/current/xm/multiline.html) module of NXLog Enterprise Edition supports the [AutoFlush](https://docs.nxlog.co/refman/current/xm/multiline.html#config-autoflush) directive to automatically flush its read buffer once the [PollInterval](https://docs.nxlog.co/refman/current/im/file.html#config-pollinterval) time has elapsed. This enables a more timely processing of the last event while it waits for new events to be read.

#### Syslog

NXLog Enterprise Edition can improve readability of Syslog data by replacing line breaks inside messages with other characters using the [ReplaceLineBreaks](https://docs.nxlog.co/refman/current/xm/syslog.html#config-replacelinebreaks) directive. This option can be used with the [to\_syslog\_bsd()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-to-syslog-bsd),[to\_syslog\_ietf()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-to-syslog-ietf), and [to\_syslog\_snare()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-to-syslog-snare) procedures. The [to\_syslog\_ietf()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-to-syslog-ietf) procedure’s local time information can be replaced with UTC/GMT timestamps using the [UTCTimestamp](https://docs.nxlog.co/refman/current/xm/syslog.html#config-utctimestamp) directive.

#### XML

NXLog Enterprise Edition additionally provides features for working with XML, such as:

[IgnoreRootTag](https://docs.nxlog.co/refman/current/xm/xml.html#config-ignoreroottag)

Results in fields being "flattened" by not having the XML [root tag](https://docs.nxlog.co/refman/current/xm/xml.html#config-roottag) `Event` prefixed to them with dot notation. For example, `$Event.timestamp` will be simply `$timestamp`.

[IncludeHiddenFields](https://docs.nxlog.co/refman/current/xm/xml.html#config-includehiddenfields)

Preserves hidden fields, i.e. those having names with a leading dot (`.`) or underscore (`_`).

[ParseAttributes](https://docs.nxlog.co/refman/current/xm/xml.html#config-parseattributes)

Provides the ability to parse an XML field’s attributes in addition to its value. Given this XML sample

```xml
<Msg time='2014-06-27T00:27:38' type='ERROR'>foo</Msg>
```

xml

will be parsed as `$Msg.time`, `$Msg.type`, and `$Msg` fields. Otherwise, only `$Msg` with its string value `foo` would be added to event record.

[PrefixWinEvent](https://docs.nxlog.co/refman/current/xm/xml.html#config-prefixwinevent)

In the context of XML-formatted Windows events, this is the inverse process of [IgnoreRootTag](https://docs.nxlog.co/refman/current/xm/xml.html#config-ignoreroottag), in which events gleaned from [parse\_windows\_eventlog\_xml()](https://docs.nxlog.co/refman/current/xm/xml.html#proc-parse-windows-eventlog-xml) will have their fields prefixed with either `EventData` or `UserData` using dot notation depending on which XML section they belong to.

### Programming languages support

Supporting programming languages means that events can be read, processed, and forwarded using methods and procedures written in any of the supported languages. Being able to choose from a list of popular programming languages for developing custom modules offers a great deal of flexibility.

NXLog Enterprise Edition supports programming languages via the following types of modules:

- Input modules to replace the existing NXLog input modules
- Extension modules to process data coming from the input modules
- Output modules to replace the existing NXLog output modules

The table below lists supported programming languages.

| Supported Language | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| Go ( [im\_go](https://docs.nxlog.co/refman/current/im/go.html), [om\_go](https://docs.nxlog.co/refman/current/om/go.html), [xm\_go](https://docs.nxlog.co/refman/current/xm/go.html)) |  |  | Enables developing log processing modules using the Go or Golang programming language |
| Java ([im\_java](https://docs.nxlog.co/refman/current/im/java.html), [om\_java](https://docs.nxlog.co/refman/current/om/java.html), [xm\_java](https://docs.nxlog.co/refman/current/xm/java.html)) |  |  | Facilitates developing custom Java applications that can easily integrate with the NXLog infrastructure |
| Perl ([im\_perl](https://docs.nxlog.co/refman/current/im/perl.html), [om\_perl](https://docs.nxlog.co/refman/current/om/perl.html), [xm\_perl](https://docs.nxlog.co/refman/current/xm/perl.html)) |  |  | Perl, with its native regular expression capabilities, allows rapid development of terse scripts for high performance, complex parsing of logs. |
| Python ([im\_python](https://docs.nxlog.co/refman/current/im/python.html), [om\_python](https://docs.nxlog.co/refman/current/om/python.html), [xm\_python](https://docs.nxlog.co/refman/current/xm/python.html)) |  |  | Python scripts can be developed to customize how logs are read, processed, and output. |
| Ruby ([im\_ruby](https://docs.nxlog.co/refman/current/im/ruby.html), [om\_ruby](https://docs.nxlog.co/refman/current/om/ruby.html), [xm\_ruby](https://docs.nxlog.co/refman/current/xm/ruby.html)) |  |  | Ruby, with its native support for structured data formats like XML and JSON, can be used to develop applications for custom log processing. |

### Data transformation

The ability to transform captured log data is an essential feature of any log collection strategy.

The following table shows the features that can be used to transform data according to each edition of NXLog.

| Supported Feature | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| [Converting via Character Sets](https://docs.nxlog.co/userguide/intro/#data-transformation-character-sets) ([xm\_charconv](https://docs.nxlog.co/refman/current/xm/charconv.html)) |  |  | Log data can be converted between character sets (codepages) prior to parsing. |
| Blacklisting and Whitelisting of Log Entries ([xm\_filelist](https://docs.nxlog.co/refman/current/xm/filelist.html)) |  |  | Based on the contents of each file, files can be whitelisted or blacklisted using this feature. |
| [File Operations](https://docs.nxlog.co/userguide/intro/#data-transformation-file-hash) ([xm\_fileop](https://docs.nxlog.co/refman/current/xm/fileop.html)) |  |  | Provides convenient methods for implementing log rotation and retention policies for the specified log files. |
| Manipulating Fields ([xm\_rewrite](https://docs.nxlog.co/refman/current/xm/rewrite.html)) |  |  | Enables renaming and dropping of specific fields, as well as the enrichment of events with new fields defined in `Exec` statements. |
| Encryption and Decryption of Logs ([xm\_crypto](https://docs.nxlog.co/refman/current/xm/crypto.html)) |  |  | Enables log files to be encrypted and decrypted using AES symmetric encryption for secure storage and/or transport over a network. |
| Compression and Decompression of Logs ([xm\_zlib](https://docs.nxlog.co/refman/current/xm/zlib.html)) |  |  | Allows compressing log files using either `gzip` or `zlib` prior to transport. |
| Resolving IP addresses to Hostnames ([xm\_resolver](https://docs.nxlog.co/refman/current/xm/resolver.html)) |  |  | When log data needs to be human readable, enriching log events with the hostnames, user names, and groups names is preferable to IP addresses, user IDs, and group IDs. |

The following features are available in both editions of NXLog, but NXLog Enterprise Edition provides additional or enhanced functionality.

#### Converting via character sets

The following optional directives are only available with NXLog Enterprise Edition:

- [BigEndian](https://docs.nxlog.co/refman/current/xm/charconv.html#config-bigendian) to allow specifying the endianness
- [CharBytes](https://docs.nxlog.co/refman/current/xm/charconv.html#config-charbytes) to specify the byte-width of the encoding
- [LineReader](https://docs.nxlog.co/refman/current/xm/charconv.html#config-linereader) to set the input reader

#### File operations

NXLog Enterprise Edition has a [file\_hash()](https://docs.nxlog.co/refman/current/xm/fileop.html#func-file-hash) function to return the calculated hash of the specified file.

### Administration and monitoring

NXLog provides several administration and monitoring features, such as remote administration of agents as well as monitoring network traffic and file systems.

| Supported Feature | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| Secure Remote Administration ([xm\_admin](https://docs.nxlog.co/refman/current/xm/admin.html)) |  |  | Enables secure remote administration for NXLog agents and various monitoring tools using JSON or SOAP over HTTP/HTTPS. |
| [Execution of External Scripts](https://docs.nxlog.co/userguide/intro/#administration-and-monitoring-external-scripts) ([im\_exec](https://docs.nxlog.co/refman/current/im/exec.html), [om\_exec](https://docs.nxlog.co/refman/current/om/exec.html), [xm\_exec](https://docs.nxlog.co/refman/current/xm/exec.html)) |  |  | Supports the execution of an external program or script on startup. |
| Changes in Files and Directories ([im\_fim](https://docs.nxlog.co/refman/current/im/fim.html)) |  |  | This feature enables the monitoring of changes in specific files and directories for integrity monitoring. |
| Passive Monitoring of Network Traffic ([im\_pcap](https://docs.nxlog.co/refman/current/im/pcap.html)) |  |  | Enables NXLog to passively monitor and log network traffic for various protocols. |
| Windows Registry Monitoring ([im\_regmon](https://docs.nxlog.co/refman/current/im/regmon.html)) |  |  | Provides scanning of Windows registry and generates event records when changes are detected. |

The following features are available in both editions of NXLog, but NXLog Enterprise Edition provides additional or enhanced functionality.

#### Execution of external scripts

The [xm\_exec](https://docs.nxlog.co/refman/current/xm/exec.html) module of NXLog Enterprise Edition additionally supports execution of commands as a function.

The [Restart](https://docs.nxlog.co/refman/current/om/exec.html#config-restart) directive of NXLog Enterprise Edition can restart a process if it terminates unexpectedly.

### Log sources

NXLog supports log collection and processing from a wide variety of log sources. Practically any operating system found in enterprise computing environments is supported, as well as their native log sources. In most cases, the native modules that ship with NXLog for collecting logs suffice without any need for any additional software. The following table lists the modules designed for specific log sources.

| Source Name | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| Accounting Logs From a Linux or BSD Kernel ([im\_acct](https://docs.nxlog.co/refman/current/im/acct.html)) |  |  | Enables collecting and processing logs from a Linux or BSD kernel. |
| AIX Audit ([im\_aixaudit](https://docs.nxlog.co/refman/current/im/aixaudit.html)) |  |  | Along with the *xm\_aixaudit* module, AIX Audit logs can be read and parsed directly from the kernel. |
| macOS Endpoint Security ([im\_maces](https://docs.nxlog.co/refman/current/im/maces.html)) |  |  | Collects logs from Apple’s Endpoint Security auditing system. |
| Microsoft Azure Application Logs ([im\_azure](https://docs.nxlog.co/refman/current/im/azure.html)) |  |  | Parses logs from Microsoft Azure applications received over various TLS and SSL protocols. |
| Check Point Device Logs ([im\_checkpoint](https://docs.nxlog.co/refman/current/im/checkpoint.html)) |  |  | Remote collection of logs from Check Point devices using the OPSEC LEA protocol. |
| Database Logs via the [libdbi](http://libdbi.sourceforge.net/) library ([im\_dbi](https://docs.nxlog.co/refman/current/im/dbi.html#DBI%20\(im_dbi\)), [om\_dbi](https://docs.nxlog.co/refman/current/om/dbi.html)) |  |  | Convenient method for pulling and saving data to external databases using the [libdbi](http://libdbi.sourceforge.net/) database abstraction library. |
| Kernel Application Logs Using Event Tracing for Windows ([im\_etw](https://docs.nxlog.co/refman/current/im/etw.html)) |  |  | High-performance log collection using Event Tracing for Windows (ETW). |
| [Internal NXLog Logs](https://docs.nxlog.co/userguide/intro/#sources-collecting-logs-internal-logs) ([im\_internal](https://docs.nxlog.co/refman/current/im/internal.html)) |  |  | Enables reading internal NXLog logs. |
| Elasticsearch Server ([om\_elasticsearch](https://docs.nxlog.co/refman/current/om/elasticsearch.html)) |  |  | Enables forwarding logs to an Elasticsearch server. |
| Kafka Server Logs ([im\_kafka](https://docs.nxlog.co/refman/current/im/kafka.html), [om\_kafka](https://docs.nxlog.co/refman/current/om/kafka.html)) |  |  | Enables the collecting of event records from a Kafka topic as well as publishing event records to a Kafka topic. |
| [Logs From the Kernel Log Buffer](https://docs.nxlog.co/userguide/intro/#sources-collecting-logs-kernel-logs) ([im\_kernel](https://docs.nxlog.co/refman/current/im/kernel.html)) |  |  | Collects events from the kernel log buffer on Unix-like operating systems. |
| [Windows Event Log](https://docs.nxlog.co/userguide/intro/#sources-eventlog-messages) ([im\_mseventlog](https://docs.nxlog.co/refman/current/im/mseventlog.html), [im\_msvistalog](https://docs.nxlog.co/refman/current/im/msvistalog.html)) |  |  | Collects Windows Event Log messages using its native API. |
| Windows Event Collector ([im\_wseventing](https://docs.nxlog.co/refman/current/im/wseventing.html)) |  |  | Using the Windows Event Forwarding infrastructure, this feature enables collecting events from Windows Event Log. |
| Kernel Logs via Audit Rules ([im\_linuxaudit](https://docs.nxlog.co/refman/current/im/linuxaudit.html)) |  |  | Collects logs directly from the kernel using custom rules without the need for installing auditd or other userspace software. |
| Database Table Logs via ODBC ([im\_odbc](https://docs.nxlog.co/refman/current/im/odbc.html), [om\_odbc](https://docs.nxlog.co/refman/current/om/odbc.html)) |  |  | Uses ODBC for storing logs in ODBC-compliant databases. |
| Forwarding Logs to Raijin Server ( [om\_raijin](https://docs.nxlog.co/refman/current/om/raijin.html)) |  |  | Sends batched JSON records to Raijin Server for further analysis and archival. |
| Redis Server Log Tranfers ([im\_redis](https://docs.nxlog.co/refman/current/im/redis.html), [om\_redis](https://docs.nxlog.co/refman/current/om/redis.html)) |  |  | Enables the retrieval of data stored in a Redis server as well as populating a Redis server with log data. |
| Systemd Journal Logs ([im\_systemd](https://docs.nxlog.co/refman/current/im/systemd.html)) |  |  | Reads, parses, and processes events from the systemd journal. |
| Windows Performance Counters ([im\_winperfcount](https://docs.nxlog.co/refman/current/im/winperfcount.html)) |  |  | Enables the polling of various Windows Performance Counters to create event records. |

The following features are available in both editions of NXLog, but NXLog Enterprise Edition provides additional or enhanced functionality.

#### Internal NXLog logs

[LogqueueSize](https://docs.nxlog.co/refman/current/im/internal.html#config-logqueuesize)

Sets the number messages which are queued if delivery is delayed or blocked.

Event log enrichment

Additional fields which contain the module name and type.

#### Logs from the kernel log buffer

NXLog Enterprise Edition supports collecting kernel logs from various Linux, BSD, and macOS systems. However, NXLog Community Edition supports only Linux systems.

NXLog Enterprise Edition also provides the following directives:

[DeviceFile](https://docs.nxlog.co/refman/current/im/kernel.html#config-devicefile)

For accessing the device file to read events on non-Linux systems.

[PollInterval](https://docs.nxlog.co/refman/current/im/kernel.html#config-pollinterval)

Sets the interval to check for new events.

#### Windows Event Log

The Enterprise Edition’s [im\_msvistalog](https://docs.nxlog.co/refman/current/im/msvistalog.html) module supports the following optional directives not found in NXLog Community Edition:

[AddPrefix](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-addprefix)

Adds the `EventData` prefix to fields which are parsed from the `EventData` section of the event.

[ReadBatchSize](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-readbatchsize)

Specifies the number of event records the Windows Event Log API will pass to NXLog for further processing.

[CaptureEventXML](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-captureeventxml)

Enables the `$EventXML` field to store the raw XML-formatted event data.

[File](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-file)

Enables NXLog to read directly from the `.evt`, `.evtx`, or `.etl` log files.

[Language](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-language)

Sets the locale to use for rendering language/region-specific event fields such as date/time, currency, etc.

[RemoteAuthMethod](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-remoteauthmethod)

Sets the authentication method.

[RemoteDomain](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-remotedomain)

Specifies the authentication domain of the remote server for collecting event logs.

[RemotePassword](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-remotepassword)

Accepts the user password of the remote server for collecting event logs.

[RemoteServer](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-remoteserver)

Sets the name of the remote server from which event logs will be captured.

[RemoteUser](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-remoteuser)

Sets the user name on the remote server for collecting event logs.

[ResolveGUID](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-resolveguid)

Enables GUID to resolve values of the object names in the `$Message` field.

[ResolveSID](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-resolvesid)

Enables SID to resolve values of the object names in the `$Message` field.

[TolerateQueryErrors](https://docs.nxlog.co/refman/current/im/msvistalog.html#config-toleratequeryerrors)

Will prevent the module from starting if any source is invalid when set to `FALSE` (the default value).

### Protocols

Both editions of NXLog provide support for various protocols for working with logs, see the table below.

| Protocol Name | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| Batched Compression ([im\_batchcompress](https://docs.nxlog.co/refman/current/im/batchcompress.html), [om\_batchcompress](https://docs.nxlog.co/refman/current/om/batchcompress.html)) |  |  | Enables sending/receiving batches of log messages that are compressed and optionally encrypted to/from a remote NXLog agent. |
| [Files](https://docs.nxlog.co/userguide/intro/#protocols-files) ([im\_file](https://docs.nxlog.co/refman/current/im/file.html), [om\_file](https://docs.nxlog.co/refman/current/om/file.html)) |  |  | Facilities reading log messages from files and writing processed data to them. |
| WebHDFS ([om\_webhdfs](https://docs.nxlog.co/refman/current/om/webhdfs.html)) |  |  | Using the WebHDFS protocol, this feature can be used to store logs in Hadoop HDFS. |
| [HTTP](https://docs.nxlog.co/userguide/intro/#protocols-http) ([im\_http](https://docs.nxlog.co/refman/current/im/http.html), [om\_http](https://docs.nxlog.co/refman/current/om/http.html)) |  |  | Convenient log message communication using over the HTTP protocol, both inbound and outbound. |
| [Named pipes](https://docs.nxlog.co/userguide/intro/#protocols-named-pipes) ([im\_pipe](https://docs.nxlog.co/refman/current/im/pipe.html), [om\_pipe](https://docs.nxlog.co/refman/current/om/pipe.html)) |  |  | With this feature, named pipes of Unix-like operating systems can be utilized to send and receive log messages. |
| [TLS/SSL](https://docs.nxlog.co/userguide/intro/#protocols-tls) ( [im\_ssl](https://docs.nxlog.co/refman/current/im/ssl.html), [om\_ssl](https://docs.nxlog.co/refman/current/om/ssl.html)) |  |  | Provides TLS/SSL transportation capabilities for secure forwarding and retrieval of logs. |
| [TCP](https://docs.nxlog.co/userguide/intro/#protocols-tcp) ([im\_tcp](https://docs.nxlog.co/refman/current/im/tcp.html), [om\_tcp](https://docs.nxlog.co/refman/current/om/tcp.html)) |  |  | Accepts TCP connections for receiving event data and can send events to remote hosts over TCP. |
| [UDP](https://docs.nxlog.co/userguide/intro/#protocols-udp) ([im\_udp](https://docs.nxlog.co/refman/current/im/udp.html), [om\_udp](https://docs.nxlog.co/refman/current/om/udp.html)) |  |  | Enables log data to be sent and received as datagrams using the UDP protocol. |
| UDP With Spoofing ([om\_udpspoof](https://docs.nxlog.co/refman/current/om/udpspoof.html)) |  |  | With spoofing enabled, UDP packets will contain the IP address of the originating client that produced the message instead of the forwarding server. |
| Unix Domain Sockets ([im\_uds](https://docs.nxlog.co/refman/current/im/uds.html), [om\_uds](https://docs.nxlog.co/refman/current/om/uds.html)) |  |  | Enables log data to be sent or received over a Unix domain socket. |
| ZeroMQ ([im\_zmq](https://docs.nxlog.co/refman/current/im/zmq.html), [om\_zmq](https://docs.nxlog.co/refman/current/om/zmq.html)) |  |  | Supports message transport over ZeroMQ, a scalable high-throughput messaging library. |

The following features are available in both editions of NXLog, but NXLog Enterprise Edition provides additional or enhanced functionality.

#### Files

The [im\_file](https://docs.nxlog.co/refman/current/im/file.html) module of NXLog Enterprise Edition additionally provides the following optional directives:

[Exclude](https://docs.nxlog.co/refman/current/im/file.html#config-exclude)

Specifies a file or a set of files to be excluded.

[InputType](https://docs.nxlog.co/refman/current/im/file.html#config-inputtype)

Sets the input reader function.

[NoEscape](https://docs.nxlog.co/refman/current/im/file.html#config-noescape)

Specifies whether the backslash (\`\`) in file paths should be disabled as an escape sequence.

[OnEOF](https://docs.nxlog.co/refman/current/im/file.html#config-oneof)

A group of statements to be executed after a file has been completely read (on end-of-file).

The [om\_file](https://docs.nxlog.co/refman/current/om/file.html) module provides the optional [CacheSize](https://docs.nxlog.co/refman/current/om/file.html#config-cachesize) directive to keep files open and reduce the overhead caused by open/close operations.

#### HTTP

NXLog Community Edition provides only the output HTTP capabilities via the [om\_http](https://docs.nxlog.co/refman/current/om/http.html) module. NXLog Enterprise Edition supports the input and output capabilities via the [im\_http](https://docs.nxlog.co/refman/current/im/http.html) and [om\_http](https://docs.nxlog.co/refman/current/om/http.html) modules.

The Enterprise Edition’s [om\_udp](https://docs.nxlog.co/refman/current/om/udp.html) module supports multiple definitions of the [Host](https://docs.nxlog.co/refman/current/om/udp.html#config-host) directive which can be used to configure failover.

The [URL](https://docs.nxlog.co/refman/current/om/http.html#config-url) directive of NXLog Enterprise Edition can be specified multiple times for configuring failover. Its [HTTPSCADir](https://docs.nxlog.co/refman/current/om/http.html#config-httpscadir) and [HTTPSCAFile](https://docs.nxlog.co/refman/current/om/http.html#config-httpscafile) directives provide additional support for self-signed certificates.

NXLog Enterprise Edition supports the following optional directives not found in NXLog Community Edition:

[AddHeader](https://docs.nxlog.co/refman/current/om/http.html#config-addheader)

An additional header to be added to each HTTP request.

[BatchMode](https://docs.nxlog.co/refman/current/om/http.html#config-batchmode)

Toggles whether the data is sent as single event or a batch of events.

[ContentType](https://docs.nxlog.co/refman/current/om/http.html#config-contenttype)

Specifies the *Content-Type* HTTP header which can be used in conjunction with the [BatchMode](https://docs.nxlog.co/refman/current/om/http.html#config-batchmode) directive.

[FlushInterval](https://docs.nxlog.co/refman/current/om/http.html#config-flushinterval)

Sets the period of time after which accumulated data will be sent in batch mode.

[FlushLimit](https://docs.nxlog.co/refman/current/om/http.html#config-flushlimit)

The number of events to be batched together in a single POST request.

[HTTPSCAThumbprint](https://docs.nxlog.co/refman/current/om/http.html#config-httpscathumbprint)

The certificate thumbprint of the certificate authority (CA) which can be used to look up the CA certificate from the Windows certificate store.

[HTTPSCertThumbprint](https://docs.nxlog.co/refman/current/om/http.html#config-httpscertthumbprint)

The certificate thumbprint to be used for the SSL handshake.

[HTTPSCRLDir](https://docs.nxlog.co/refman/current/om/http.html#config-httpscrldir)

The path to the certificate revocation list. This list is used for verifying the certificate of the remote HTTPS server.

[HTTPSSSLCipher](https://docs.nxlog.co/refman/current/om/http.html#config-httpssslcipher)

Can be used to set the permitted SSL cipher list, overriding the default.

[HTTPSSSLCiphersuites](https://docs.nxlog.co/refman/current/om/http.html#config-httpssslciphersuites)

Can be used to define the permitted SSL cipher list in case the `HTTPSSSLProtocol` directive is set to `TLSv1.3`.

[HTTPSSSLProtocol](https://docs.nxlog.co/refman/current/om/http.html#config-httpssslprotocol)

Can be used to set the allowed TLS/SSL protocol(s).

[HTTPSSSLCompression](https://docs.nxlog.co/refman/current/om/http.html#config-httpssslcompression)

Enables data compression when sending over the network.

[ProxyAddress](https://docs.nxlog.co/refman/current/om/http.html#config-proxyaddress)

The IP address of the proxy server.

[ProxyPort](https://docs.nxlog.co/refman/current/om/http.html#config-proxyport)

The port number of the proxy server.

[SNI](https://docs.nxlog.co/refman/current/om/http.html#config-sni)

The host name for Server Name Indication (SNI) in HTTPS mode.

#### Named pipes

NXLog Community Edition only supports the named pipes input module, whereas NXLog Enterprise Edition allows logs to be sent to named pipes on UNIX-like operating systems with the [om\_pipe](https://docs.nxlog.co/refman/current/om/pipe.html) output module.

#### TLS/SSL

The [im\_ssl](https://docs.nxlog.co/refman/current/im/ssl.html) module of NXLog Enterprise Edition supports self-signed certificates and the following optional directives:

[CAThumbprint](https://docs.nxlog.co/refman/current/im/ssl.html#config-cathumbprint)

The certificate thumbprint of the certificate authority (CA) which can be used to look up the CA certificate from the Windows certificate store.

[CertThumbprint](https://docs.nxlog.co/refman/current/im/ssl.html#config-certthumbprint)

The certificate thumbprint to be used for the SSL handshake.

[SSLCipher](https://docs.nxlog.co/refman/current/im/ssl.html#config-sslcipher)

Can be used to set the permitted SSL cipher list, overriding the default.

[SSLCiphersuites](https://docs.nxlog.co/refman/current/im/ssl.html#config-sslciphersuites)

Can be used to define the permitted SSL cipher list in case the `HSSLProtocol` directive is set to `TLSv1.3`.

[SSLCompression](https://docs.nxlog.co/refman/current/im/ssl.html#config-sslcompression)

Enables data compression when sending over the network.

[SSLProtocol](https://docs.nxlog.co/refman/current/im/ssl.html#config-sslprotocol)

Sets the allowed TLS/SSL protocol(s).

The [om\_ssl](https://docs.nxlog.co/refman/current/om/ssl.html) module of NXLog Enterprise Edition provides additional functionalities to the following directives:

[Host](https://docs.nxlog.co/refman/current/om/ssl.html#config-host)

Can be specified multiple times to work in a failover configuration.

[CADir](https://docs.nxlog.co/refman/current/om/ssl.html#config-cadir) and [CAFile](https://docs.nxlog.co/refman/current/om/ssl.html#config-cafile)

Support self-signed certificates.

It also supports the following optional directives:

[CAThumbprint](https://docs.nxlog.co/refman/current/om/ssl.html#config-cathumbprint)

The certificate thumbprint of the certificate authority (CA) which can be used to look up the CA certificate from the Windows certificate store.

[CertThumbprint](https://docs.nxlog.co/refman/current/om/ssl.html#config-certthumbprint)

The certificate thumbprint to be used for the SSL handshake.

[LocalPort](https://docs.nxlog.co/refman/current/om/ssl.html#config-localport)

The local port number of the connection.

[SNI](https://docs.nxlog.co/refman/current/om/ssl.html#config-sni)

The host name for Server Name Indication (SNI).

[SSLCipher](https://docs.nxlog.co/refman/current/om/ssl.html#config-sslcipher)

Can be used to set the permitted SSL cipher list, overriding the default.

[SSLCiphersuites](https://docs.nxlog.co/refman/current/om/ssl.html#config-sslciphersuites)

Can be used to define the permitted SSL cipher list in case the `SSLProtocol` directive is set to `TLSv1.3`.

[SSLCompression](https://docs.nxlog.co/refman/current/om/ssl.html#config-sslcompression)

Enables data compression when sending over the network.

[SSLProtocol](https://docs.nxlog.co/refman/current/om/ssl.html#config-sslprotocol)

Sets the allowed TLS/SSL protocol(s).

[TCPNoDelay](https://docs.nxlog.co/refman/current/om/ssl.html#config-tcpnodelay)

Can be used to turn off the network optimization performed by Nagle’s algorithm.

#### TCP

The [im\_tcp](https://docs.nxlog.co/refman/current/im/tcp.html) module of NXLog Enterprise Edition supports the [ReusePort](https://docs.nxlog.co/refman/current/im/tcp.html#config-reuseport) directive to enable synchronous listening on the same port by multiple module instances.

The [Host](https://docs.nxlog.co/refman/current/om/tcp.html#config-host) directive of the [om\_tcp](https://docs.nxlog.co/refman/current/om/tcp.html) module can be defined several times to work in a failover configuration.

The [om\_tcp](https://docs.nxlog.co/refman/current/om/tcp.html) module also supports the following optional directives:

[LocalPort](https://docs.nxlog.co/refman/current/om/tcp.html#config-localport)

The local port number of the connection.

[Reconnect](https://docs.nxlog.co/refman/current/om/tcp.html#config-reconnect)

Sets the reconnect interval in seconds.

[TCPNoDelay](https://docs.nxlog.co/refman/current/om/tcp.html#config-tcpnodelay)

Turns off network optimization performed by Nagle’s algorithm.

#### UDP

The [im\_udp](https://docs.nxlog.co/refman/current/im/udp.html) module of NXLog Enterprise Edition provides the following directives:

[ReusePort](https://docs.nxlog.co/refman/current/im/udp.html#config-reuseport)

Enables synchronous listening on the same port by multiple module instances.

[UseRecvmmsg](https://docs.nxlog.co/refman/current/im/udp.html#config-recvmmsg)

Specifies that the `recvmmsg()` system call should be used whenever possible. This improves performance by enabling the reception of multiple messages per call.

The Enterprise Edition’s [om\_udp](https://docs.nxlog.co/refman/current/om/udp.html) module supports multiple definitions of the [Host](https://docs.nxlog.co/refman/current/om/udp.html#config-host) directive which can be used to configure failover.

The [om\_udp](https://docs.nxlog.co/refman/current/om/udp.html) module of NXLog Enterprise Edition also supports the following directives:

[LocalPort](https://docs.nxlog.co/refman/current/om/udp.html#config-localport)

The local port number of the connection.

[OutputType](https://docs.nxlog.co/refman/current/om/udp.html#config-outputtype)

Sets the output writer function for UDP datagrams.

[Reconnect](https://docs.nxlog.co/refman/current/om/udp.html#config-reconnect)

Sets the reconnect interval in seconds.

### Miscellaneous modules

| Operation Name | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| Collecting Mark ([im\_mark](https://docs.nxlog.co/refman/current/im/mark.html)) |  |  | For indicating periodic activity to ensure the logger is running when there are no log messages being received in from other sources. |
| Testing NXLog Configuration ([im\_null](https://docs.nxlog.co/refman/current/im/null.html), [om\_null](https://docs.nxlog.co/refman/current/om/null.html)) |  |  | Provides testing capabilities and allows creating dummy routes. |
| Generating Test Events ([im\_testgen](https://docs.nxlog.co/refman/current/im/testgen.html)) |  |  | For generating simple events which can be read and processed before running the system in production. |
| Simulation of Output Messages Blocking ([om\_blocker](https://docs.nxlog.co/refman/current/om/blocker.html)) |  |  | Additional testing capability which can block messages to simulate a blocked route. |
| [Buffering of Log Messages](https://docs.nxlog.co/userguide/intro/#miscellaneous-buffering-log-messages) ([pm\_buffer](https://docs.nxlog.co/refman/current/pm/buffer.html)) |  |  | Eliminates loss of log data by configuring log message buffers. |
| [Event Correlation](https://docs.nxlog.co/userguide/intro/#miscellaneous-event-correlation) ([pm\_evcorr](https://docs.nxlog.co/refman/current/pm/evcorr.html)) |  |  | Provides event correlation functionality in addition to available NXLog features, such as variables and statistical counters. |
| ASLR (address space layout randomization) |  |  | Binaries built using ASLR are more resistant to memory allocation exploits. (Windows only). |

The following features are available in both editions of NXLog, but NXLog Enterprise Edition provides additional or enhanced functionality.

#### Buffering of log messages

NXLog Enterprise Edition supports the [CreateDir](https://docs.nxlog.co/refman/current/pm/buffer.html#config-createdir) directive to create an output directory before opening the output file for writing.

#### Event correlation

NXLog Enterprise Edition supports the [Group](https://docs.nxlog.co/refman/current/pm/evcorr.html#config-group) rule to group messages based on the specified correlation context.

### Supported core functionalities

As opposed to module instance directives which do not extend beyond the scope of their respective instances, general and global directives can be applied to the entire NXLog configuration. Both of these directives are compared in this section:

- [General Directives](https://docs.nxlog.co/userguide/intro/#supported-core-functionalities-general-directives) can be used by all modules throughout the entire NXLog configuration.
- [Global Directives](https://docs.nxlog.co/userguide/intro/#supported-core-functionalities-global-directives) control the overall behavior of NXLog.

#### General directives

General directives provide configuration reusability. This reduces the amount of configuration needed, increases flexibility, and eliminates errors by using well-tested configuration components.

This subsection compares general directives which are supported by both editions of NXLog.

| Directive Name | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| [define](https://docs.nxlog.co/refman/current/configuration.html#general-define) |  |  | This feature allows you to define a constant or macro which can be used as directory name, code snippet, or regular expression. Once defined, you can insert it in a uniform manner within any of the module instances. |
| [envvar](https://docs.nxlog.co/refman/current/configuration.html#general-envvar) |  |  | Retrieves environment values to make them available for use with various NXLog components or in any module instance. |
| [include](https://docs.nxlog.co/refman/current/configuration.html#general-include) |  |  | Specifies a file or set of files which can extend the current NXLog configuration. After being included, the file configuration can be reused within the scope of the configuration. |
| [include\_stdout](https://docs.nxlog.co/refman/current/configuration.html#general-include-stdout) |  |  | Using this directive, the configuration content can be read through external commands. This may be useful when a configuration is generated dynamically and cannot be known beforehand. |

#### Global directives

Global directives control the overall behavior of NXLog and provide additional features which can improve its functionality.

##### Caching and batching

Caching adjusts the NXLog performance to specific needs. Batching log messages saves resources and optimizes the network performance by grouping messages together before forwarding them.

The following global directives can be used to fine-tune NXLog’s caching and batching settings.

<table><caption>Table 9. Caching and batching directives</caption> <colgroup><col> <col> <col> <col></colgroup><thead><tr><th>Directive Name</th><th>NXLog Community Edition</th><th>NXLog Enterprise Edition</th><th>Feature Advantage</th></tr></thead><tbody><tr><td colspan="4"><p><strong>Caching directives</strong></p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-cachedir">CacheDir</a></p></td><td></td><td></td><td><p>Specifies the directory where the cache file will be stored.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-cacheflushinterval">CacheFlushInterval</a></p></td><td></td><td></td><td><p>This option adjusts logging performance by specifying the interval for flushing the in-memory position cache to the cache file.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-cacheinvalidationtime">CacheInvalidationTime</a></p></td><td></td><td></td><td><p>Prevents the cache from growing indefinitely by discarding cache entries after their storage period exceeds this directive’s setting.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-cachesync">CacheSync</a></p></td><td></td><td></td><td><p>Guarantees crash-safe operation by delaying the in-memory cache flush to disk.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-nocache">NoCache</a></p></td><td></td><td></td><td><p>Globally disables NXLog’s caching mechanism.</p></td></tr><tr><td colspan="4"><p><strong>Batching directives</strong></p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-batchsize">BatchSize</a></p></td><td></td><td></td><td><p>Specifies the maximum number of records to collect in a batch before forwarding them to the next instance(s) in the route.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-batchflushinterval">BatchFlushInterval</a></p></td><td></td><td></td><td><p>Sets a timeout before forwarding each batch of messages to the next instance(s) in the route.</p></td></tr></tbody></table>

##### Preventing data loss

Persistent queuing provides the capability of temporarily writing the incoming log data to disk in case the in-memory queue overflows. Using flow control, NXLog operations can be suspended in case any module instance (input, processor, or output) becomes blocked or unable to process events. Both persistent queuing and flow control help prevent data loss.

The following general directives provide options for customizing NXLog’s persistent queuing and flow control features.

<table><caption>Table 10. Persistent queuing directives</caption> <colgroup><col> <col> <col> <col></colgroup><thead><tr><th>Directive Name</th><th>NXLog Community Edition</th><th>NXLog Enterprise Edition</th><th>Feature Advantage</th></tr></thead><tbody><tr><td colspan="4"><p><strong>Persistent queuing</strong></p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-logqueuedir">LogqueueDir</a></p></td><td></td><td></td><td><p>Specifies the directory where files of the persistent queue will be stored. Persistent storage prevents data loss and thus improves logging reliability.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-logqueuesize">LogqueueSize</a></p></td><td></td><td></td><td><p>In addition to the <code>LogqueueDir</code>, this directive offers flexibility in controlling the log queue size needed for persistent queuing.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-persistlogqueue">PersistLogqueue</a></p></td><td></td><td></td><td><p>This directive determines whether or not log queues should be saved to disk when necessary.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-synclogqueue">SyncLogqueue</a></p></td><td></td><td></td><td><p>To make the logging process more reliable and crash-safe, this option provides syncing capabilities for disk-based queues of processor and output module instances.</p></td></tr><tr><td colspan="4"><p><strong>Flow control</strong></p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-flowcontrol">FlowControl</a></p></td><td></td><td></td><td><p>This feature specifies whether the input-to-output flow should be controlled by NXLog to prevent data loss in case of failure at any stage.</p></td></tr><tr><td><p><a href="https://docs.nxlog.co/refman/current/configuration.html#global-flowcontrolfifo">FlowControlFIFO</a></p></td><td></td><td></td><td><p>A convenient way to enable FIFO mode for modules with disabled flow control functionality.</p></td></tr></tbody></table>

##### Processing dates

Customization of date formatting can be important when date/time information needs to be normalized and indexed for enabling it to used in time-based queries.

| Directive Name | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| [DateFormat](https://docs.nxlog.co/refman/current/configuration.html#global-dateformat) |  |  | Overrides the default date/time pattern which is used by the internal NXLog logging mechanism for converting `datetime` value to `string` value. |
| [GenerateDateInUTC](https://docs.nxlog.co/refman/current/configuration.html#global-generatedateinutc) |  |  | Allows using UTC instead of local time when generating dates in the `YYYY-MM-DD hh:mm:ss` format. |
| [ParseDateInUTC](https://docs.nxlog.co/refman/current/configuration.html#global-parsedateinutc) |  |  | Enables parsing the date in the `YYYY-MM-DD hh:mm:ss` format as UTC instead of processing it as local time. |

##### Memory and performance

These NXLog directives can be used to adjust performance and memory consumption.

| Directive Name | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| [StringLimit](https://docs.nxlog.co/refman/current/configuration.html#global-stringlimit) |  |  | To avoid memory exhaustion, each message string can be limited to a maximum size. This will guard NXLog against denial-of-service scenarios. |
| [SuppressRepeatingLogs](https://docs.nxlog.co/refman/current/configuration.html#global-suppressrepeatinglogs) |  |  | To avoid excessive consumption of disk space, this directive restricts the number of messages the internal logger can accept. |
| [Threads](https://docs.nxlog.co/refman/current/configuration.html#global-threads) |  |  | For fine-tuning NXLog’s performance, its number of threads can be explicitly set. If not specified, the number of threads is selected automatically. |

##### Debugging capabilities

The following directives are available for setting NXLog’s debugging options.

| Directive Name | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| [LogFile](https://docs.nxlog.co/refman/current/configuration.html#global-logfile) |  |  | Provides self-logging capabilities for convenient monitoring and debugging of NXLog-related problems. |
| [LogLevel](https://docs.nxlog.co/refman/current/configuration.html#global-loglevel) |  |  | Specifies the logging level for internal NXLog messages set by the `LogFile` directive. It features a granularity of five levels: either `CRITICAL`, `ERROR`, `WARNING`, `INFO`, or `DEBUG`. |
| [NoFreeOnExit](https://docs.nxlog.co/refman/current/configuration.html#global-nofreeonexit) |  |  | Additional debugging option which allows showing proper stack trace in module function calls. |

##### Other global directives

These remaining directives offer diverse features and options available with NXLog that do not fit exactly in any the previous categories covered in this section.

| Directive Name | NXLog Community Edition | NXLog Enterprise Edition | Feature Advantage |
| --- | --- | --- | --- |
| [Capabilities](https://docs.nxlog.co/refman/current/configuration.html#global-capabilities) |  |  | Allows specifying the required Linux capabilities to enable privileged kernel calls. |
| [EscapeGlobPatterns](https://docs.nxlog.co/refman/current/configuration.html#global-escapeglobpatterns) |  |  | Specifies the backslash (`\`) character to escape glob patterns or wildcarded entries; this measure provides convenience and unification with other company-wide approaches, standards, or other requirements. |
| [Group](https://docs.nxlog.co/refman/current/configuration.html#global-group) |  |  | Linux-only directive to specify the group ID that NXLog run as. |
| [IgnoreErrors](https://docs.nxlog.co/refman/current/configuration.html#global-ignoreerrors) |  |  | With this directive enabled, NXLog will continue to run even if it encounters configuration-related problems. If set to `FALSE`, NXLog will stop if errors are encountered. |
| [ModuleDir](https://docs.nxlog.co/refman/current/configuration.html#global-moduledir) |  |  | This option allows you to override the standard location where NXLog loadable modules are stored by default. |
| [Panic](https://docs.nxlog.co/refman/current/configuration.html#global-panic) |  |  | This directive provides a choice of three options, `HARD`, `SOFT`, or `OFF`, that will determine how NXLog should react when it finds itself in a *panic* condition (a critical state). |
| [PidFile](https://docs.nxlog.co/refman/current/configuration.html#global-pidfile) |  |  | To make configuration more convenient, this feature allows overriding the default PID file name which NXLog uses during its operation. |
| [ReadTimeout](https://docs.nxlog.co/refman/current/configuration.html#global-readtimeout) |  |  | Using this feature, the default exit condition timeout of the [nxlog-processor(8)](https://docs.nxlog.co/refman/current/man-pages.html#nxlog-processor-8) software can be overridden. |
| [RootDir](https://docs.nxlog.co/refman/current/configuration.html#global-rootdir) |  |  | As with the `SpoolDir` directive, this feature offers flexibility in setting a custom root directory location for NXLog. |
| [SpoolDir](https://docs.nxlog.co/refman/current/configuration.html#global-spooldir) |  |  | As with the `RootDir` directive, this feature offers flexibility in setting a custom working directory location for NXLog. |
| [User](https://docs.nxlog.co/refman/current/configuration.html#global-user) |  |  | For Unix-like operating systems this directive specifies the user NXLog will run as and consequently which permissions it will have. |

## What NXLog is not

NXLog provides a broad range of features for collecting, processing, forwarding, and storing log data. However, NXLog is *not* a SIEM product and does not provide:

- a graphical interface (or "dashboard") for searching logs and displaying reports,
- vulnerability detection or integration with external threat data,
- automatic analysis and correlation algorithms, or
- pre-configured compliance and retention policies.

NXLog *does* provide processing features that can be used to set up analysis, correlation, retention, and alerting; NXLog *can* be integrated with many other products to provide a complete solution for aggregation, analysis, and storage of log data.