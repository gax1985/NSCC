---
title: "Reading and receiving logs | NXLog Documentation"
source: "https://docs.nxlog.co/userguide/configure/reading-logs.html"
author:
published:
created: 2025-11-21
description: "This topic explains the various sources NXLog can read, receive and process logs from."
tags:
  - "clippings"
---
## Reading and receiving logs

This chapter discusses log sources that you may need to use with NXLog, including:

## Receiving over the network

This section provides information and examples about receiving log messages from the network over various protocols.

UDP

The [im\_udp](https://docs.nxlog.co/refman/current/im/udp.html) module handles incoming messages over UDP.

Example 1. Using the im\_udp module

This input module instance shows the [im\_udp](https://docs.nxlog.co/refman/current/im/udp.html) module configured with the default options: localhost only and port 514.

nxlog.conf

```config
<Input udp>
    Module  im_udp
    Host    localhost
    Port    514
</Input>
```

config

|  | Though NXLog was designed to minimize message loss even in the case of UDP, adjusting the kernel buffers may reduce the likelihood of UDP message loss on a system under heavy load. The [Priority](https://docs.nxlog.co/refman/current/configuration.html#route-priority) directive in the *Route* block can also help. |
| --- | --- |

TCP

The [im\_tcp](https://docs.nxlog.co/refman/current/im/tcp.html) module handles incoming messages over TCP. For TLS/SSL, use the [im\_ssl](https://docs.nxlog.co/userguide/configure/#network-ssl) module.

Example 2. Using the im\_tcp module

This input module instance accepts TCP connections from any host on port 1514.

nxlog.conf

```config
<Input tcp>
    Module  im_tcp
    Host    0.0.0.0
    Port    1514
</Input>
```

config

SSL/TLS

The [im\_ssl](https://docs.nxlog.co/refman/current/im/ssl.html) module handles incoming messages over TCP with SSL/TLS security.

Example 3. Using the im\_ssl module

The following input module instance listens for SSL/TLS encrypted incoming logs on port 6514. The certificate file paths are specified relative to a previously [defined](https://docs.nxlog.co/userguide/configure/overview.html#define) `CERTDIR`.

nxlog.conf

```config
<Input in>
    Module      im_ssl
    Host        0.0.0.0
    Port        6514
    CAFile      %CERTDIR%/ca.pem
    CertFile    %CERTDIR%/client-cert.pem
    CertKeyFile %CERTDIR%/client-key.pem
</Input>
```

config

Syslog

To receive Syslog over the network, use one of the network modules above, coupled with [xm\_syslog](https://docs.nxlog.co/refman/current/xm/syslog.html). Syslog parsing is not required if you only need to forward or store the messages as they are. See also [Accepting Syslog via UDP, TCP, or TLS](https://docs.nxlog.co/integrate/syslog.html#accepting-syslog-network).

Example 4. Receiving syslog over TCP with octet-framing

With this example configuration, NXLog listens for messages on TCP port 1514. The [xm\_syslog](https://docs.nxlog.co/refman/current/xm/syslog.html) extension module provides the [Syslog\_TLS](https://docs.nxlog.co/refman/current/xm/syslog.html#inputtype-syslog-tls) InputType (for octet-framing) and the [parse\_syslog()](https://docs.nxlog.co/refman/current/xm/syslog.html#proc-parse-syslog) procedure for parsing Syslog messages.

nxlog.conf

```config
<Extension _syslog>
    Module  xm_syslog
</Extension>

<Output out>
    Module  om_tcp
    Host    192.168.1.1
    Port    1514
    Exec    to_syslog_ietf();
</Output>
```

config

## Reading from a database

With the [im\_dbi](https://docs.nxlog.co/refman/current/im/dbi.html#DBI%20\(im_dbi\)) and [im\_odbc](https://docs.nxlog.co/refman/current/im/odbc.html) modules it is possible to read logs directly from database servers. The *im\_dbi* module can be used on POSIX systems where libdbi is available. The *im\_odbc* module, available in NXLog Enterprise Edition, can be used with ODBC compatible databases on Windows, Linux, and Unix.

Example 5. Using the im\_dbi module

This example uses libdbi and the MySQL driver to read records from the `logdb` database.

nxlog.conf

```config
<Input in>
    Module  im_dbi
    Driver  mysql
    Option  host 127.0.0.1
    Option  username mysql
    Option  password mysql
    Option  dbname logdb
    SQL     SELECT id, facility, severity, hostname, timestamp, application, \
                   message FROM log
</Input>
```

config

Example 6. Using the im\_odbc module

[![ee badge](https://docs.nxlog.co/userguide/_images/ee-badge.png "NXLog Enterprise Edition exclusive feature")](https://nxlog.co/community-edition-vs-enterprise-edition) [**NXLog Enterprise Edition exclusive feature**](https://nxlog.co/community-edition-vs-enterprise-edition)

Here, the `mydb` database is accessed via ODBC.

nxlog.conf

```config
<Input in>
    Module              im_odbc
    ConnectionString    DSN=mssql;database=mydb;
    SQL                 SELECT RecordNumber as id, DateOccured as EventTime, \
                               data as Message from logtable WHERE RecordNumber > ?
</Input>
```

config

## Reading from files and sockets

Files

The [im\_file](https://docs.nxlog.co/refman/current/im/file.html) module can be used to read logs from files. See also [Reading Syslog Log Files](https://docs.nxlog.co/integrate/syslog.html#collecting-files).

Example 7. Using the im\_file module

This example reads from the specified file without performing any additional processing.

nxlog.conf

```config
<Input in>
    Module  im_file
    File    "/var/log/messages"
</Input>
```

config

Unix domain socket

Use the [im\_uds](https://docs.nxlog.co/refman/current/im/uds.html) module to read from a Unix domain socket. See also [Accepting Syslog via /dev/log](https://docs.nxlog.co/integrate/syslog.html#accepting-syslog-via-dev-log).

Example 8. Using the im\_uds module

With this configuration, NXLog will read messages from the `/dev/log` socket. NXLog’s flow control feature must be disabled in this case (see the [FlowControl](https://docs.nxlog.co/refman/current/configuration.html#module-flowcontrol) directive in the Reference Manual).

nxlog.conf

```config
<Input in>
    Module      im_uds
    UDS         /dev/log
    FlowControl FALSE
</Input>
```

config

## Receiving from an executable

The [im\_exec](https://docs.nxlog.co/refman/current/im/exec.html) module can be used to read logs from external programs and scripts over a pipe.

Example 9. Using the im\_exec module

This example uses the `tail` command to read messages from a file.

|  | The [im\_file](https://docs.nxlog.co/refman/current/im/file.html) module should be used to read log messages from files. This example only demonstrates the use of the [im\_exec](https://docs.nxlog.co/refman/current/im/exec.html) module. |
| --- | --- |

nxlog.conf

```config
<Input in>
    Module  im_exec
    Command /usr/bin/tail
    Arg     -f
    Arg     /var/log/messages
</Input>
```

config