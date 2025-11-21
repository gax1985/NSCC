---
title: "Collecting, parsing, and forwarding syslog logs | NXLog Documentation"
source: "https://docs.nxlog.co/integrate/syslog.html"
author:
published:
created: 2025-11-21
description: "Collecting, parsing, and forwarding syslog logs and explaining different syslog formats such as BSD syslog and IETF syslog.  It also discusses collecting, parsing, and filtering syslog log files."
tags:
  - "clippings"
---
## Collecting, parsing, and forwarding syslog logs

Syslog is a standard protocol that network devices, operating systems, and applications use to log various system events and messages. Like any other log type, you can send syslog formatted logs to a central log server for further analysis, troubleshooting, auditing, or storage purposes. Syslog messages typically include information about the message’s source, the event’s severity level, and a timestamp.

NXLog can collect, generate, and forward log entries in various syslog formats. NXLog has a dedicated extension module to provide functions for parsing syslog messages. With its plethora of syslog support, NXLog is well suited to consolidate any syslog events, whether syslog Windows events or Linux syslog. With all its capabilities, you can even look at NXLog as a fully featured syslog server. This section describes the different syslog protocols and discusses how to use them with NXLog.

## BSD syslog (RFC 3164)

The original syslog was written for the Sendmail open-source email server in the 1980s. It was later adopted by many other applications and implemented across many operating systems, and became the standard logging system for Unix-style systems. There was no authoritative publication about syslog until 2001 when the Internet Engineering Task Force (IETF) published informational RFC 3164, which described the "observed behavior" among implementations. Today, modern implementations follow RFC 3164, which attempts to accommodate the many older implementations. Still, many undocumented variations exist among the BSD syslog protocols implemented by various applications and devices.

BSD syslog example

```log
<30>Nov 21 11:40:27 myserver sshd[26459]: Accepted publickey for john from 192.168.1.1 port 41193 ssh2
```

log

BSD syslog defines both the log entry format and the transport. The message format is free-form, allowing the payload to be JSON or another structured data format.

### BSD syslog format

BSD syslog uses a simple format comprised of three parts.

|  | While this is the common and recommended format for a BSD syslog message, there are no set requirements, and a device may send a BSD syslog log message containing only a free-form message without PRI or HEADER parts. |
| --- | --- |

The PRI part, or "priority", is calculated from the facility and severity codes. The facility code indicates the type of program that generated the message, and the severity code indicates the message’s severity (see the [Syslog facilities](https://docs.nxlog.co/integrate/#facilities) and [Syslog severities](https://docs.nxlog.co/integrate/#severities) tables below). The priority code is calculated by multiplying the facility code by eight and then adding the severity code.

|  | The PRI part is not written to file by many syslog loggers. In that case, each log entry begins with the HEADER. |
| --- | --- |

The HEADER part contains two fields: TIMESTAMP and HOSTNAME. The TIMESTAMP provides the local time when the message was generated in `Mmm dd hh:mm:ss` format, with no year or time zone specified; the HOSTNAME is the host’s name where the message was generated.

The MSG part contains two fields: TAG and CONTENT. The TAG is the name of the program or process that generated the message and contains only alphanumeric characters. Any other character will represent the beginning of the CONTENT field. The CONTENT field often includes the process ID enclosed by brackets (`[]`), a colon (`:`), a space, and then the actual message. In the [log sample](https://docs.nxlog.co/integrate/#bsd-sample) above, the MSG part begins with `myserver sshd[26459]: Accepted publickey`; in this case, the TAG is `ssh`, and the CONTENT field starts with `[26459]`. The CONTENT field can contain only ASCII printable characters (32-126).

Commonly used fields in the BSD syslog format

```log
<PRI>TIMESTAMP HOSTNAME TAG[PID]: MESSAGE
```

log

| Facility Code | Description |
| --- | --- |
| 0 | kernel messages |
| 1 | user-level messages |
| 2 | mail system |
| 3 | system daemons |
| 4 | security/authorization messages |
| 5 | messages generated internally by syslogd |
| 6 | line printer subsystem |
| 7 | network news subsystem |
| 8 | UUCP subsystem |
| 9 | clock daemon |
| 10 | security/authorization messages |
| 11 | FTP daemon |
| 12 | NTP subsystem |
| 13 | log audit |
| 14 | log alert |
| 15 | scheduling daemon |
| 16 | local use 0 (local0) |
| 17 | local use 1 (local1) |
| 18 | local use 2 (local2) |
| 19 | local use 3 (local3) |
| 20 | local use 4 (local4) |
| 21 | local use 5 (local5) |
| 22 | local use 6 (local6) |
| 23 | local use 7 (local7) |

| Severity Code | Description |
| --- | --- |
| 0 | Emergency: system is unusable |
| 1 | Alert: action must be taken immediately |
| 2 | Critical: critical conditions |
| 3 | Error: error conditions |
| 4 | Warning: warning conditions |
| 5 | Notice: normal but significant condition |
| 6 | Informational:informational messages |
| 7 | Debug: debug-level messages |

### BSD syslog transport

According to RFC 3164, the BSD syslog protocol uses UDP as its transport layer. Each UDP packet carries a single log entry. BSD syslog implementations often also support plain TCP and TLS transports, though these are not covered by RFC 3164.

### Disadvantages of BSD syslog

There are several disadvantages associated with the BSD syslog protocol.

- The transport defined by RFC 3164 uses UDP and provides no mechanism to ensure reliable log delivery, integrity, or confidentiality of log messages.
- Many undocumented variations exist among implementations.
- The timestamp indicates neither the year nor the timezone and does not provide precision greater than the second.
- The PRI field (and, therefore, the facility and severity codes) are not retained by many syslog loggers when writing to log files.
- The entire length of the log entry is limited to 1024 bytes.
- Only ASCII characters 32-126 are allowed, with no Unicode or line breaks.

## IETF syslog (RFC 5424-5426)

In 2009, the IETF released RFC 5424, 5425, and 5426 as "Proposed Standards" intended to replace the "legacy" BSD syslog. RFC 5425 includes a timestamp with year, timezone, and fractional seconds; provides a "structured data" field for key-value pairs; and offers UTF-8 encoding. RFC 5425 defines the use of TLS transport and supports multi-line log messages. RFC 5426 describes the use of UDP transport.

IETF syslog example

```log
<165>1 2003-10-11T22:14:15.003Z mymachine.example.com evntslog - ID47 [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"] An application event log entry...
```

log

### IETF syslog format

IETF syslog uses a base format similar to that of BSD syslog.

- PRI: message priority (same as BSD syslog)
- VERSION: syslog format version (always "1" for RFC 5424 logs)
- TIMESTAMP: derived from RFC 3339 (`YYYY-MM-DDTHH:MM:SS.000000Z`, or with the time zone specified)
- HOSTNAME
- APP-NAME: device or application that generated the message
- PROCID: ID of the process that generated the message
- MSGID: message type (for example, "TCPIN" for incoming TCP traffic and "TCPOUT" for outgoing)

|  | The PRI field is not written to file by many syslog loggers. In that case, each log entry begins with the VERSION field. |
| --- | --- |

The STRUCTURED-DATA part is optional. If it is omitted, then a hyphen acts as a placeholder. Otherwise, it is surrounded by brackets. It contains an ID of the block and a list of space-separated "key=value" pairs.

The MSG part is optional and contains a free-form, single-line message. If the message is encoded in UTF-8, then it may be preceded by a Unicode byte order mark (BOM).

Fields in the IETF syslog format

```log
<PRI>VERSION TIMESTAMP HOSTNAME APP-NAME PROCID MSGID [SD-ID STRUCTURED-DATA] MESSAGE
```

log

### IETF syslog transport

IETF syslog can use UDP, plain TCP, or TLS transport. UDP transport is described by RFC 5426, and TLS transport by RFC 5425.

RFC 5425 also documents the octet-framing method used for TLS transport and provides support for multi-line messages. Octet-framing can also be used with plain TCP; TLS is not required. The message is prefixed with the length, as shown in the following example of the raw data sent over TCP/TLS.

Syslog example with octet-framing

```log
101 <13>1 2012-01-01T17:15:52.873750+01:00 myhost - - - [NXLOG@14506 TestField="test value"] test message
```

log

IETF syslog is commonly transferred without octet-framing over TCP or TLS. In this case, the newline (`\n`) character is used as the record separator, similar to how BSD syslog is transferred over TCP or TLS.

## Collecting and parsing syslog

NXLog can be configured to collect syslog logs by:

- Reading syslog files written by another local syslog agent.
- Collecting syslog via the local `/dev/log` Unix domain socket.
- Receiving syslog over the network (via UDP, TCP, or TLS).

### Reading syslog files

Configuring NXLog to read syslog from a file allows another local syslog agent to continue its logging operations as before. NXLog will likely not have access to the facility and severity codes because most syslog loggers do not write the PRI field to log files.

Ensure NXLog is permitted to read log files in `/var/log`. See [Reading Rsyslog log files](https://docs.nxlog.co/integrate/linux-logs.html#rsyslog-log-files) for more information.

Example 1. Reading syslog from file

This configuration reads log messages from files and parses them using the [parse\_syslog()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-parse-syslog) procedure.

nxlog.conf

```config
<Extension _syslog>
    Module    xm_syslog
</Extension>

<Input in>
    Module    im_file
    File      '/var/log/messages'
    Exec      parse_syslog();
</Input>
```

config

|  | The [parse\_syslog()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-parse-syslog) procedure parses the log entry as either BSD or IETF format (the [parse\_syslog\_bsd()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-parse-syslog-bsd) and [parse\_syslog\_ietf()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-parse-syslog-ietf) procedures can be used alternatively). |
| --- | --- |

### Collecting syslog via /dev/log

Many applications support logging by sending log messages to the `/dev/log` Unix domain socket. It is the responsibility of the system logger to accept these messages and then store them as configured. NXLog can receive logs sent to the `/dev/log` Unix domain socket instead of the stock syslog logger.

1. Configure NXLog (see the [example](https://docs.nxlog.co/integrate/#devlog-example) below).
2. Disable the stock syslog agent’s collection of `/dev/log` messages if necessary. See also [Replacing Rsyslog](https://docs.nxlog.co/integrate/linux-logs.html#replacing-rsyslog). Either
	- Disable the service entirely (for example, `systemctl --now disable rsyslogd`) or
	- Modify the configuration to disable reading from `/dev/log` (for example, remove `$ModLoad imuxsock` from `/etc/rsyslog.conf` and restart Rsyslog).
3. Restart NXLog.

Example 2. Collecting syslog from /dev/log

With this configuration, NXLog uses the [im\_uds](https://docs.nxlog.co/refman/current/im/uds.html) module to read messages from the `/dev/log` and the [parse\_syslog()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-parse-syslog) procedure to parse them.

|  | [FlowControl](https://docs.nxlog.co/refman/current/configuration.html#module-flowcontrol) should be disabled for collecting from `/dev/log`. Otherwise, the `syslog()` system call will block if the Output queue becomes full, resulting in an unresponsive system. |
| --- | --- |

nxlog.conf

```config
<Extension _syslog>
    Module         xm_syslog
</Extension>

<Input in>
    Module         im_uds
    UDS            /dev/log
    FlowControl    FALSE
    Exec           parse_syslog();
</Input>
```

config

### Collecting syslog via UDP, TCP, or TLS

NXLog can be configured to listen on a port and collect syslog over the network. A port can be used to receive messages with UDP, TCP, or TLS transport. The local syslog agent may already be configured to listen on port 514 for UDP log messages from local applications.

1. Configure NXLog with [im\_udp](https://docs.nxlog.co/refman/current/im/udp.html), [im\_tcp](https://docs.nxlog.co/refman/current/im/tcp.html), or [im\_ssl](https://docs.nxlog.co/refman/current/im/ssl.html). See the examples below.
2. For NXLog to listen for messages on port 514, the local syslog agent must not be listening on that port number. It may be necessary to do either of the following:
	- Disable the service entirely (for example, `systemctl disable rsyslogd`).
	- Modify the configuration to disable listening on port 514 (for example, remove `input(type="imudp" port="514")` from `/etc/rsyslog.conf` and restart Rsyslog).
3. Restart NXLog.

Example 3. Receiving syslog via UDP

This configuration accepts either BSD or IETF syslog from the local system only, via UDP.

|  | The UDP transport can lose log entries and is therefore not recommended for receiving logs over the network. |
| --- | --- |

nxlog.conf

```config
<Extension _syslog>
    Module        xm_syslog
</Extension>

<Input in>
    Module        im_udp
    ListenAddr    localhost:514
    Exec          parse_syslog();
</Input>
```

config

Example 4. Receiving syslog via TCP

This configuration accepts either BSD or IETF syslog via TCP without supporting octet-framing.

nxlog.conf

```config
<Extension _syslog>
    Module        xm_syslog
</Extension>

<Input in>
    Module        im_tcp
    ListenAddr    0.0.0.0:1514
    Exec          parse_syslog();
</Input>
```

config

Example 5. Receiving IETF syslog via TCP with octet-framing

This configuration accepts IETF syslog via TCP, with support for octet-framing.

|  | Though this is for plain TCP, the [Syslog\_TLS](https://docs.nxlog.co/refman/current/xm/syslog.html#outputtype-syslog-tls) directive is required because it refers to the octet-framing method described by RFC 5425. |
| --- | --- |

nxlog.conf

```config
<Extension _syslog>
    Module        xm_syslog
</Extension>

<Input in>
    Module        im_tcp
    ListenAddr    0.0.0.0:1514
    InputType     Syslog_TLS
    Exec          parse_syslog_ietf();
</Input>
```

config

Example 6. Receiving IETF syslog via TLS

This configuration accepts IETF syslog via TLS, with support for octet-framing.

nxlog.conf

```config
<Extension _syslog>
    Module         xm_syslog
</Extension>

<Input in>
    Module         im_ssl
    ListenAddr     0.0.0.0:6514
    CAFile         %CERTDIR%/ca.pem
    CertFile       %CERTDIR%/client-cert.pem
    CertKeyFile    %CERTDIR%/client-key.pem
    InputType      Syslog_TLS
    Exec           parse_syslog_ietf();
</Input>
```

config

## Filtering syslog

Filtering syslog messages means keeping or discarding messages based on their contents. Filtering can be carried out using [conditional statements](https://docs.nxlog.co/userguide/configure/language.html#if-else) and values from event record fields. For more details about fields, see the [Event records and fields](https://docs.nxlog.co/userguide/intro/event-records-and-fields.html) section.

Example 7. Filtering syslog messages by severity

The configuration below reads user-space messages from the `/dev/log` socket using the [im\_uds](https://docs.nxlog.co/refman/current/im/uds.html) module. In the [Exec](https://docs.nxlog.co/refman/current/configuration.html#module-exec) block, messages are parsed using the [parse\_syslog\_bsd()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-parse-syslog-bsd) procedure from the [xm\_syslog](https://docs.nxlog.co/refman/current/xm/syslog.html) module.

Using conditional statement values from the `$SyslogSeverityValue` field are checked, and messages with severity over `6` are discarded using the [drop()](https://docs.nxlog.co/refman/current/language-core-procedures.html#proc-drop) procedure.

The remaining messages are converted to JSON using [to\_json()](https://docs.nxlog.co/refman/current/xm/json.html#proc-to-json) procedure from the [xm\_json](https://docs.nxlog.co/refman/current/xm/json.html) module.

nxlog.conf

```config
<Extension json>
    Module    xm_json
</Extension>

<Input from_uds>
    Module    im_uds
    UDS       /dev/log
    <Exec>
        parse_syslog_bsd();
        if NOT ($SyslogSeverityValue < 6)
        {
            drop();
        }
        to_json();
    </Exec>
</Input>
```

config

Messages can also be filtered using the values of a group of fields.

Example 8. Filtering syslog by various values

The configuration below reads log messages from the `/dev/log` socket using the [im\_uds](https://docs.nxlog.co/refman/current/im/uds.html) module. In the [Exec](https://docs.nxlog.co/refman/current/configuration.html#module-exec) block, messages are parsed using the [parse\_syslog\_bsd()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-parse-syslog-bsd) procedure from the [xm\_syslog](https://docs.nxlog.co/refman/current/xm/syslog.html) module.

Using the conditional statement, complex filtering is carried out as per the following parameters:

- Severity, using the value from the `$SyslogSeverityValue` field.
- Facility, using the value from the `$SyslogFacility` field.
- Source name, using the value from the `$SourceName` field.

If a message does not meet at least one filtering condition, it is discarded using the [drop()](https://docs.nxlog.co/refman/current/language-core-procedures.html#proc-drop) procedure. Otherwise, it is converted to JSON using [to\_json()](https://docs.nxlog.co/refman/current/xm/json.html#proc-to-json) procedure from the [xm\_json](https://docs.nxlog.co/refman/current/xm/json.html) module.

nxlog.conf

```config
<Extension json>
    Module    xm_json
</Extension>

<Input from_uds>
    Module    im_uds
    UDS       /dev/log
    <Exec>
        parse_syslog_bsd();
        if NOT (
               ($SyslogSeverityValue < 6) OR
               ($SyslogFacility IN ('AUTHPRIV', 'AUTH', 'MAIL', 'CRON')) OR
               ($SourceName IN ('apt','nxlog','osqueryd'))
               )
        {
            drop();
        }
        to_json();
    </Exec>
</Input>
```

config

Syslog messages can be filtered by the `$Message` field values using [regular expressions](https://docs.nxlog.co/refman/current/language-expressions.html#regexp).

Using regular regular expressions, syslog messages can be filtered by the `$Message` field values.

Example 9. Filtering syslog by the message field

The configuration below reads log messages from the Linux kernel using the [im\_kernel](https://docs.nxlog.co/refman/current/im/kernel.html) module. In the [Exec](https://docs.nxlog.co/refman/current/configuration.html#module-exec) block, messages are parsed using the [parse\_syslog\_bsd()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-parse-syslog-bsd) procedure from the [xm\_syslog](https://docs.nxlog.co/refman/current/xm/syslog.html) module.

Using the conditional statement, messages without the **mount options** string in the `$Message` field are discarded using the [drop()](https://docs.nxlog.co/refman/current/language-core-procedures.html#proc-drop) procedure.

The remaining messages are converted to JSON using [to\_json()](https://docs.nxlog.co/refman/current/xm/json.html#proc-to-json) procedure from the [xm\_json](https://docs.nxlog.co/refman/current/xm/json.html) module.

nxlog.conf

```config
<Extension json>
    Module    xm_json
</Extension>

<Input from_kernel>
    Module    im_kernel
    <Exec>
        parse_syslog_bsd();
        if NOT ($Message =~ /mount options/)
        {
            drop();
        }
        to_json();
    </Exec>
</Input>
```

config

## Generating syslog messages

NXLog can be configured to generate BSD or IETF syslog and:

- Write it to file.
- Send messages to the local syslog daemon via the `/dev/log` Unix domain socket.
- Forward messages to another destination over the network (via UDP, TCP, or TLS).

In each case, the [to\_syslog\_bsd()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-to-syslog-bsd) and [to\_syslog\_ietf()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-to-syslog-ietf) procedures generate the `$raw_event` field from the corresponding [fields](https://docs.nxlog.co/refman/current/xm/syslog.html#fields) in the event record.

### Writing syslog to file

The [om\_file](https://docs.nxlog.co/refman/current/om/file.html) module is used to write logs to file.

Example 10. Writing BSD syslog to file

This configuration write logs to the specified file in the BSD syslog format.

nxlog.conf

```config
<Extension _syslog>
    Module    xm_syslog
</Extension>

<Output out>
    Module    om_file
    File      "/var/log/syslog"
    Exec      to_syslog_bsd();
</Output>
```

config

NXLog can be configured to write BSD syslog to a file without the PRI part, emulating traditional syslog implementations.

Example 11. Writing BSD syslog without the PRI

This configuration includes a regular expression for removing the PRI part from the `$raw_event` field after the [to\_syslog\_bsd()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-to-syslog-bsd) procedure generates it.

nxlog.conf

```config
<Extension _syslog>
    Module    xm_syslog
</Extension>

<Output out>
    Module    om_file
    File      "/var/log/syslog"
    Exec      to_syslog_bsd(); $raw_event =~ s/^\<\d+\>//;
</Output>
```

config

### Sending syslog to the local syslog daemon via /dev/log

The [om\_uds](https://docs.nxlog.co/refman/current/om/uds.html) module can be used for sending logs to a Unix domain socket.

Example 12. Sending syslog to /dev/log

This configuration sends BSD Syslog to the Syslog daemon via `/dev/log`.

nxlog.conf

```config
<Extension _syslog>
    Module    xm_syslog
</Extension>

<Output out>
    Module    om_uds
    UDS       /dev/log
    Exec      to_syslog_bsd();
</Output>
```

config

### Forwarding syslog to a remote logger via UDP, TCP, or TLS

The [om\_udp](https://docs.nxlog.co/refman/current/om/udp.html), [om\_tcp](https://docs.nxlog.co/refman/current/om/tcp.html), and [om\_ssl](https://docs.nxlog.co/refman/current/om/ssl.html) modules can be used for sending syslog over the network.

Example 13. Forwarding BSD syslog via UDP

This configuration sends logs in BSD syslog format to the specified host via UDP port 514.

nxlog.conf

```config
<Extension _syslog>
    Module    xm_syslog
</Extension>

<Output out>
    Module    om_udp
    Host      192.168.1.1:514
    Exec      to_syslog_bsd();
</Output>
```

config

Example 14. Forwarding BSD syslog via TCP

This configuration sends logs in BSD format to the specified host via TCP port 1514.

nxlog.conf

```config
<Extension _syslog>
    Module    xm_syslog
</Extension>

<Output out>
    Module    om_tcp
    Host      192.168.1.1:1514
    Exec      to_syslog_bsd();
</Output>
```

config

Example 15. Forwarding IETF syslog via TLS

With this configuration, NXLog sends logs in IETF format to the specified host via port 6514.

nxlog.conf

```config
<Extension _syslog>
    Module         xm_syslog
</Extension>

<Output out>
    Module         om_ssl
    Host           192.168.1.1:6514
    CAFile         %CERTDIR%/ca.pem
    CertFile       %CERTDIR%/client-cert.pem
    CertKeyFile    %CERTDIR%/client-key.pem
    OutputType     Syslog_TLS
    Exec           to_syslog_ietf();
</Output>
```

config

|  | The `OutputType [Syslog_TLS](https://docs.nxlog.co/refman/current/xm/syslog.html#outputtype-syslog-tls)` directive is necessary if octet-framing is required. The name was chosen to refer to the octet-framing method described by RFC 5425. |
| --- | --- |

## Extending syslog

BSD syslog uses a free-form message field, and does not provide a standard way to include key-value pairs in log messages. This section documents practices in implementing structured data using BSD syslog as transport.

### IETF syslog Structured-Data

As documented above, the Structured-Data part of the IETF syslog format provides a syntax for key-value pairs.

Syslog example

```log
<13>1 2016-10-13T14:23:11.000000-06:00 myserver - - - [NXLOG@14506 Purpose="test"] This is a test message.
```

log

NXLog can parse IETF Syslog with the [parse\_syslog()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-parse-syslog) procedure provided by the [xm\_syslog](https://docs.nxlog.co/refman/current/xm/syslog.html) extension module.

Example 16. Parsing IETF syslog with structured-data

With this configuration, NXLog parses the input IETF syslog format from a file, converts it to JSON, and outputs the result to a file.

nxlog.conf

```config
<Extension _json>
    Module    xm_json
</Extension>

<Extension _syslog>
    Module    xm_syslog
</Extension>

<Input in>
    Module    im_file
    File      '/var/log/messages'
    Exec      parse_syslog();
</Input>

<Output out>
    Module    om_file
    File      '/var/log/json'
    Exec      to_json();
</Output>

<Route r>
    Path      in => out
</Route>
```

config

Output sample

```json
{
  "EventReceivedTime": "2016-10-13 15:23:12",
  "SourceModuleName": "in",
  "SourceModuleType": "im_file",
  "SyslogFacilityValue": 1,
  "SyslogFacility": "USER",
  "SyslogSeverityValue": 5,
  "SyslogSeverity": "NOTICE",
  "SeverityValue": 2,
  "Severity": "INFO",
  "EventTime": "2016-10-13 15:23:11",
  "Hostname": "myserver",
  "Purpose": "test",
  "Message": "This is a test log message."
}
```

json

NXLog can also generate IETF syslog with a Structured-Data part using the [to\_syslog\_ietf()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-to-syslog-ietf) procedure provided by the *xm\_syslog* extension module.

Example 17. Generating IETF syslog with structured-data

With the following configuration, NXLog will parse the input JSON from a file, convert it to IETF syslog format and output the result to a file.

nxlog.conf

```config
<Extension _json>
    Module    xm_json
</Extension>

<Extension _syslog>
    Module    xm_syslog
</Extension>

<Input in>
    Module    im_file
    File      '/var/log/json'
    Exec      parse_json();
</Input>

<Output out>
    Module    om_file
    File      '/var/log/ietf'
    Exec      to_syslog_ietf();
</Output>

<Route r>
    Path      in => out  
</Route>
```

config

Input sample

```json
{
  "EventTime": "2016-09-13 11:23:11",
  "Hostname": "myserver",
  "Purpose": "test",
  "Message": "This is a test log message."
}
```

json

Output sample

```log
<13>1 2016-09-13T11:23:11.000000-05:00 myserver - - - [NXLOG@14506 EventReceivedTime="2016-09-13 11:23:12" SourceModuleName="in" SourceModuleType="im_file" Purpose="test] This is a test log message.
```

log

### JSON over syslog

JSON has recently become popular for transferring structured data. For compatibility with syslog devices, it is common practice to encapsulate JSON in syslog. NXLog can generate JSON with the [to\_json()](https://docs.nxlog.co/refman/current/xm/json.html#proc-to-json) procedure function provided by the [xm\_json](https://docs.nxlog.co/refman/current/xm/json.html) extension module.

With the following configuration, NXLog will read the Windows Event Log, convert it to JSON format, add a syslog header, and send the logs via UDP to a syslog agent. NXLog log messages are also included (via the [im\_internal](https://docs.nxlog.co/refman/current/im/internal.html) module).

nxlog.conf

```config
<Extension _json>
    Module    xm_json
</Extension>

<Extension _syslog>
    Module    xm_syslog
</Extension>

<Input internal>
    Module    im_internal
</Input>

<Input eventlog>
    Module    im_msvistalog
</Input>

<Output out>
    Module    om_udp
    Host      192.168.1.1:514
    Exec      $Message = to_json(); to_syslog_bsd();
</Output>

<Route r>
    Path      internal, eventlog => out  
</Route>
```

config

|  | If syslog compatibility is not a concern, JSON can be transported without the syslog header (omit the [to\_syslog\_bsd()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-to-syslog-bsd) procedure). |
| --- | --- |

### Other syslog extensions

See also these formats, which extend BSD syslog by using the free-form message field to contain key-value pairs.

Disclaimer

While we endeavor to keep the information in this topic up to date and correct, NXLog makes no representations or warranties of any kind, express or implied about the completeness, accuracy, reliability, suitability, or availability of the content represented here. We update our screenshots and instructions on a best-effort basis.

The accurateness of the content was tested and proved to be working in our lab environment at the time of the last revision with the following software versions:

NXLog version 5.7.7898  
Linux Mint 20.3 Una  
Ubuntu 20.04 Focal Fossa  

*Last revision: 8 March 2023*