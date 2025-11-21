---
title: "Event Log for Windows 2008/Vista/later (im_msvistalog) | NXLog Platform Documentation"
source: "https://docs.nxlog.co/agent/current/im/msvistalog.html"
author:
published:
created: 2025-11-21
description: "Documentation for NXLog Agent's Windows Event Log input module and how to collect events from Windows 2008, Vista, and later."
tags:
  - "clippings"
---
## Event Log for Windows 2008/Vista/later (im\_msvistalog)

This module can be used to collect Windows Event Log messages on Microsoft Windows platforms that support the newer Event Log API (also known as the Crimson Event Log subsystem), namely Windows 2008/Vista and later. See the official Microsoft documentation about [Event Logs](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc722404\(v=ws.11\)). The module supports reading all System, Application, and Custom events. It looks up the available channels and monitors events in each unless the [Query](https://docs.nxlog.co/agent/current/im/#config-query) and [Channel](https://docs.nxlog.co/agent/current/im/#config-channel) directives are explicitly defined. Event logs can be collected from remote servers over MSRPC.

|  | To examine the supported platforms, see the [list of installation packages](https://docs.nxlog.co/agent/current/install/modules-by-package.html). |
| --- | --- |

|  | For Windows 2003 and earlier, use the [im\_mseventlog](https://docs.nxlog.co/agent/current/im/mseventlog.html) module because the new Windows Event Log API is only available in Windows Vista, Windows 2008, and later. |
| --- | --- |

|  | Use the [im\_etw](https://docs.nxlog.co/agent/current/im/etw.html) module to collect Analytic and Debug logs as the Windows Event Log subsystem, which *im\_msvistalog* uses, does not support subscriptions to Debug or Analytic channels. |
| --- | --- |

|  | NXLog Agent can alter a field’s line ending according to [W3C recommendations](https://www.w3.org/TR/REC-xml/#sec-line-ends). Any CR LF and any CR that is not followed by an LF will be translated to a single LF. |
| --- | --- |

In addition to the standard set of [fields](https://docs.nxlog.co/agent/current/im/#fields) that are listed under the System section, event providers can define additional schema which enables logging additional data under the EventData section. The Security log makes use of this new feature and such additional fields can be seen in the following XML snippet:

```xml
<EventData>
  <Data Name="SubjectUserSid">S-1-5-18</Data>
  <Data Name="SubjectUserName">WIN-OUNNPISDHIG$</Data>
  <Data Name="SubjectDomainName">WORKGROUP</Data>
  <Data Name="SubjectLogonId">0x3e7</Data>
  <Data Name="TargetUserSid">S-1-5-18</Data>
  <Data Name="TargetUserName">SYSTEM</Data>
  <Data Name="TargetDomainName">NT AUTHORITY</Data>
  <Data Name="TargetLogonId">0x3e7</Data>
  <Data Name="LogonType">5</Data>
  <Data Name="LogonProcessName">Advapi</Data>
  <Data Name="AuthenticationPackageName">Negotiate</Data>
  <Data Name="WorkstationName" />
  <Data Name="LogonGuid">{00000000-0000-0000-0000-000000000000}</Data>
  <Data Name="TransmittedServices">-</Data>
  <Data Name="LmPackageName">-</Data>
  <Data Name="KeyLength">0</Data>
  <Data Name="ProcessId">0x1dc</Data>
  <Data Name="ProcessName">C:\Windows\System32\services.exe</Data>
  <Data Name="IpAddress">-</Data>
  <Data Name="IpPort">-</Data>
</EventData>
```

xml

NXLog Agent can extract this data when fields are logged using this schema. The values will be available in the fields of the internal NXLog Agent log structure. This is especially useful because there is no need to write pattern-matching rules to extract this data from the message. These fields can be used in filtering rules, be written into SQL tables, or be used to trigger actions. The [Exec](https://docs.nxlog.co/agent/current/config/common-settings.html#exec) directive can be used for filtering:

```config
<Input in>
    Module  im_msvistalog
    Exec    if ($TargetUserName == 'SYSTEM') OR \
               ($EventType == 'VERBOSE') drop();
</Input>
```

config

## Configuration

The *im\_msvistalog* module accepts the following directives in addition to the [common module directives](https://docs.nxlog.co/agent/current/config/common-settings.html).

### Optional directives

| `AddPrefix` | If this boolean directive is set to `TRUE`, names of fields parsed from the `<EventData>` portion of the event XML will be prefixed with `EventData.`. For example, `$EventData.SubjectUserName` will be added to the event record instead of `$SubjectUserName`. The same applies to `<UserData>`. This directive defaults to `FALSE`: field names will not be prefixed. |
| --- | --- |
| `CaptureEventXML` | This boolean directive defines whether the module should store raw XML-formatted event data. If set to `TRUE`, the module stores raw XML data in the [$EventXML](https://docs.nxlog.co/agent/current/im/#eventxml) field. By default, the value is set to `FALSE`, and the `$EventXML` field is not added to the record. |
| `CaptureMessage` | This boolean directive defines whether the module should create the [$Message](https://docs.nxlog.co/agent/current/im/#message) field. The default value is `TRUE`, and the value of the `$Message` field is created from the event’s `UserData` and `EventData` fields. If `$Message` is not essential, it is recommended to set it to `FALSE` to improve event processing speed. |
| `CaptureMessageFast` | This boolean directive defines whether the module should create the [$Message](https://docs.nxlog.co/agent/current/im/#message) field using the native Windows or custom NXLog Agent function. The default is `TRUE`; the module uses a custom NXLog Agent function that executes faster but may produce a slightly different value. When set to `FALSE`, the module uses the native Windows function to set the `$Message` field to the same value as Windows Event Viewer. This directive is automatically set to `FALSE` when [ParseEventXML](https://docs.nxlog.co/agent/current/im/#config-parseeventxml) is `TRUE`. |
| `ParseEventXML` | This boolean directive defines whether the module should use the older parsing method using the event XML. When set to `TRUE`, the module produces the same output as version 5. The default is `FALSE`; the module uses a custom NXLog Agent function optimized to execute faster but may produce a slightly different result. See [Backward-compatibility](https://docs.nxlog.co/agent/current/im/#backward-compatibility) below for more information. |
| `Channel` | The name of the Channel to query. If not specified, the module will read from all sources defined in the registry. See the MSDN documentation about [Event Selection](https://learn.microsoft.com/en-us/previous-versions//aa385231\(v=vs.85\)). |
| `File` | This optional directive can be used to specify a full path to a log file. Log file types that can be used have the `.evt` and `.evtx` extensions. If the **File** directive is specified, the [SavePos](https://docs.nxlog.co/agent/current/im/#config-savepos) directive will be overridden to `TRUE`.  \|  \| The **File** directive can also be used for reading `.etl` files with the limitation that the \_im\_msvistalog module can not seek in `.etl` files. It can only read these files from start to end. \| \| --- \| --- \|  The **File** directive can be specified multiple times to read from multiple files. This module finds files only when the module instance is started; any files added later will not be read until it is restarted. If the log file specified by this directive is updated with new event records while NXLog Agent is running (the file size or modification date attribute changes), the module detects the newly appended records on the fly without requiring the module instance to be restarted. Reading a Windows Event Log file directly is mostly useful for forensics purposes. The *System* log would be read directly with the following:  ```xml File "C:\Windows\System32\winevt\Logs\System.evtx" ```  You can use wildcards to specify file names and directories. Wildcards are not regular expressions but are patterns commonly used by Unix shells to expand filenames (also known as "globbing").  ?  Matches any single character.  \*  Matches any string, including the empty string.  \\\*  Matches the asterisk (`*`) character.  \\?  Matches the question mark (`?`) character.  \[…\]  Matches one character specified within the brackets. The brackets should contain a single character (for example, `[a]`) or a range of characters (`[a-z]`). If the first character in the brackets is `^` or `!`, it reverses the wildcard matching logic (the wildcard matches any character *not* in the brackets). The backslash (`\`) characters are ignored and should be used to escape `]` and `-` characters as well as `^` and `!` at the beginning of the pathname. |
| `Language` | This optional directive specifies a language to use for rendering the events. The language should be given as a hyphen-separated language/region code (for example, `fr-FR` for French). Note that the required language support must be installed on the system. If this directive is not given, the system’s default locale is used. |
| `PollInterval` | This directive specifies how frequently the module will check for new events, in seconds. If this directive is not specified, the default is 1 second. Fractional seconds may be specified (`PollInterval 0.5` will check twice every second). |
| `Query` | This directive specifies the query for returning only specific Windows Event Log sources. See the MSDN documentation about [Event Selection](https://learn.microsoft.com/en-us/previous-versions//aa385231\(v=vs.85\)). Note that this directive requires a single-line parameter, so multi-line query XML should be specified using line continuation:  ```config Query <QueryList>         <Query Id='1'>          <Select Path='Security'>*[System/Level=4]</Select>         </Query>       </QueryList> ```  config  When the **Query** contains an XPath style expression, the [Channel](https://docs.nxlog.co/agent/current/im/#config-channel) must also be specified. Otherwise, if an XML Query is specified, the [Channel](https://docs.nxlog.co/agent/current/im/#config-channel) should not be used. |
| `QueryXML` | This directive is the same as the [Query](https://docs.nxlog.co/agent/current/im/#config-query) directive above, except it can be used as a block. Multi-line XML queries can be used without line continuation, and the XML Query can be copied directly from Event Viewer.  \|  \| Commenting with the `#` mark does not work within multi-line Query directives or QueryXML blocks. In this case, use XML-style comments `<!--   -->` as shown in the example above. Failure to follow this syntax for comments within queries will render the module instance useless. Since NXLog Agent does not parse the content of QueryXML blocks, this behavior is expected. \| \| --- \| --- \| |
| `ReadBatchSize` | This optional directive can be used to specify the number of events the Windows Event Log API will pass to the module for processing. Larger sizes may increase throughput. Note that there is a known issue in the Windows Event Log subsystem: when this value is higher than 31 it may fail to retrieve some events on busy systems, returning the error "EvtNext failed with error 1734: The array bounds are invalid." For this reason, increasing this value is not recommended. The default is `31`. |
| `ReadFromLast` | This optional boolean directive instructs the module on where to start reading events from the log source. Reading all events can result in a lot of messages and is usually not the expected behavior.  When `TRUE`, NXLog Agent will only read events logged after NXLog Agent started, unless **SavePos** is `TRUE` and a saved position for this log source is found in the cache file.   When `FALSE`, NXLog Agent will read all events in the log source from the start, unless **SavePos** is `TRUE` and a saved position for this log source is found in the cache file.   If the **ReadFromLast** directive is not specified, it defaults to `TRUE`.  The following matrix shows the outcome of this directive in conjunction with the **SavePos** directive:  \| ReadFromLast \| SavePos \| Saved position \| Outcome \| \| --- \| --- \| --- \| --- \| \| `TRUE` \| `TRUE` \| Yes \| Reads events from the saved position. \| \| `TRUE` \| `TRUE` \| No \| Reads events that are logged after NXLog Agent is started. \| \| `TRUE` \| `FALSE` \| Yes \| Reads events that are logged after NXLog Agent is started. \| \| `TRUE` \| `FALSE` \| No \| Reads events that are logged after NXLog Agent is started. \| \| `FALSE` \| `TRUE` \| Yes \| Reads events from the saved position. \| \| `FALSE` \| `TRUE` \| No \| Reads all events. \| \| `FALSE` \| `FALSE` \| Yes \| Reads all events. \| \| `FALSE` \| `FALSE` \| No \| Reads all events. \|  NOTE  The **SavePos** directive can be overridden by the global [NoCache](https://docs.nxlog.co/agent/current/config/global-settings.html#nocache) directive. If **NoCache** is `TRUE`, the **SavePos** directive is considered to be `FALSE`. |
| `RemoteAuthMethod` | This optional directive specifies the authentication method to use. Available values are `Default`, `Negotiate`, `Kerberos`, and `NTLM`. When the directive is not specified, `Default` is used, which is actually `Negotiate`. |
| `RemoteDomain` | Domain of the user used for authentication when logging on the remote server to collect event logs. |
| `RemotePassword` | Password of the user used for authentication when logging on to the remote server to collect event logs. |
| `RemoteServer` | This optional directive specifies the name of the remote server to collect event logs. If not specified, the module will collect locally. |
| `RemoteUser` | Name of the user used for authentication when logging on to the remote server to collect event logs. |
| `ResolveGUID` | This optional boolean directive defines whether the module resolves GUID values to their object names. The GUIDs that are resolved depend on the value of the [ResolvedIDOutput](https://docs.nxlog.co/agent/current/im/#config-resolvedidoutput) directive. The default setting is `FALSE`; the module will not resolve GUID values. Windows Event Viewer shows the Message with the GUID values resolved, and this must be enabled to get the same output with NXLog Agent. |
| `ResolveSID` | This optional boolean directive defines whether the module resolves SID values to user names. The SIDs that are resolved depend on the value of the [ResolvedIDOutput](https://docs.nxlog.co/agent/current/im/#config-resolvedidoutput) directive. The default setting is `FALSE`; the module will not resolve SID values. |
| `ResolvedIDOutput` | This optional directive specifies which SID or GUID values to resolve. It is only valid if **ResolveSID** or **ResolveGUID** are `TRUE`. The default value is `FIELDS`. The possible values are:  FIELDS  - If [ResolveGUID](https://docs.nxlog.co/agent/current/im/#config-resolveguid) is `TRUE`, the module resolves fields containing a GUID value and creates a new field with the result. The new field will have the same name but with the *DN* suffix. If a field with the same name already exists, the module will preserve it and will not add the new field. - If [ResolveSID](https://docs.nxlog.co/agent/current/im/#config-resolvesid) is `TRUE`, the module resolves fields containing an SID value and creates a new field with the result. The new field will have the same name but with the *Name* suffix. If a field with the same name already exists, the module will preserve it and will not add the new field.  BOTH  - If [ResolveGUID](https://docs.nxlog.co/agent/current/im/#config-resolveguid) is `TRUE`, the module resolves fields containing a GUID value and GUIDs in the `$Message` field. GUIDs must be visible in the message when you open the event in Windows Event Viewer for NXLog Agent to produce the same result. - If [ResolveSID](https://docs.nxlog.co/agent/current/im/#config-resolvesid) is `TRUE`, the module resolves fields containing an SID value and SIDs in the `$Message` field. SIDs must be visible in the message when you open the event in Windows Event Viewer for NXLog Agent to produce the same result. |
| `ResubscribeInterval` | Specifies the period in seconds after which the module will resubscribe to providers and channels in case of errors. The default value is 60 seconds. The minimum accepted value is 10 seconds, and the maximum is 4,294,967,295 (32-bit unsigned integer). The module uses this directive in combination with [TolerateQueryErrors](https://docs.nxlog.co/agent/current/im/#config-toleratequeryerrors) set to `TRUE` to periodically resubscribe to the list of providers defined in the configuration. In case a provider is unavailable, it is ignored until it becomes available. |
| `SavePos` | This optional boolean directive instructs the module whether to save the position of the last read event before NXLog Agent exits. On the next startup, NXLog Agent will try to read the saved position from the cache file. This directive in conjunction with the [ReadFromLast](https://docs.nxlog.co/agent/current/im/#config-readfromlast) directive allows for resuming reading events directly from the saved position.  When `TRUE`, the position of the last read event is saved and will be read from the cache file upon startup.   If this directive is not specified, it defaults to `TRUE`.  This directive can be overridden by the global [NoCache](https://docs.nxlog.co/agent/current/config/global-settings.html#nocache) directive. If **NoCache** is `TRUE`, the **SavePos** directive is considered to be `FALSE`. |
| `TolerateQueryErrors` | This boolean directive specifies that *im\_msvistalog* should ignore any invalid sources in the query. The default is `FALSE`: *im\_msvistalog* will fail to start if any source is invalid. |

## Backward-compatibility

NXLog Agent version 6 uses a faster algorithm to read Windows events. However, this may result in a slightly different output than previous versions. You can revert the change by setting the [ParseEventXML](https://docs.nxlog.co/agent/current/im/#config-parseeventxml) directive to `TRUE`. When this directive is enabled, the module emulates the output of older versions with some differences in fields, including but not limited to:

Keywords

A hexadecimal number instead of a decimal.

Message

`\n\r` for a newline instead of `\n`.

ProviderGuid

The field is set to `NULL` when empty instead of removing the field.

Opcode

Not present in older versions.

Level

Not always present in older versions.

## Performance considerations

### Parsing events

From version 6 onwards, NXLog Agent uses optimized logic to parse event values. Although the new method is faster, it may produce fields different from the event template in some server configurations. If the module detects such a discrepancy, it falls back to the previous parsing method using the event XML, which is slower but more accurate.

### Setting the message field

Setting the event `$Message` field is a time-consuming process. NXLog Agent version 6 introduces a new [CaptureMessage](https://docs.nxlog.co/agent/current/im/#config-capturemessage) directive to define whether the module retrieves the event message. If you do not use this field, you can set the directive to `FALSE` to reduce the event processing time. The directive is set to `TRUE` by default to maintain backward compatibility with older versions.

When the **CaptureMessage** directive is enabled, the module implements two methods to set the `$Message` field. The first method, also used in older NXLog Agent versions, uses the native Windows function to set the field value. Version 6 introduces another faster method that uses the message template, which is the default. The latter is faster but may produce slightly different results. You can revert to using the native Windows function by switching off the [CaptureMessageFast](https://docs.nxlog.co/agent/current/im/#config-capturemessagefast) directive.

|  | There are some instances where the module cannot use the optimized method even when *CaptureMessageFast* is enabled, including if:  - The message template is not available on the system. - The module parses the event with the older method. |
| --- | --- |

The following are examples of different message field values when using the native Windows versus the custom NXLog Agent function.

| Method | Result |
| --- | --- |
| Windows | File System Filter 'FileCrypt' (10.0, 2002-03-01T12:12:42.000000000Z) has successfully loaded and registered with Filter Manager. |
| NXLog Agent | File System Filter 'FileCrypt' (10.0, 2002-03-01T12:12:42.0000000Z) has successfully loaded and registered with Filter Manager. |

| Method | Result |
| --- | --- |
| Windows | The boot menu policy was 1. |
| NXLog Agent | The boot menu policy was 0x1. |

| Method | Result |
| --- | --- |
| Windows | The kernel power manager has initiated a shutdown transition.\\r\\n\\r\\nShutdown Reason: 5 |
| NXLog Agent | The kernel power manager has initiated a shutdown transition.\\r\\n\\r\\nShutdown Reason: Kernel API |

| Method | Result |
| --- | --- |
| Windows | Volume C: (\\\\Device\\\\HarddiskVolume3) is healthy. No action is needed. |
| NXLog Agent | Volume C: (\\\\Device\\\\HarddiskVolume3) 0 |

| Method | Result |
| --- | --- |
| Windows | Connectivity state in standby: Disconnected, Reason: NIC compliance |
| NXLog Agent | Connectivity state in standby: 2, Reason: 6 |

| Method | Result |
| --- | --- |
| Windows | Group Policy received Preshutdown notification from Service Control Manager. |
| NXLog Agent | Group Policy received 0 notification from Service Control Manager. |

### Resolving SIDs

When the [CaptureMessage](https://docs.nxlog.co/agent/current/im/#config-capturemessage) and [ResolveSID](https://docs.nxlog.co/agent/current/im/#config-resolvesid) directives are enabled, the module resolves SIDs to usernames in the `$Message` field. This process impacts performance when the module uses the native Windows function to set the message field since it has to parse the field again to find and replace SIDs.

### Performance comparison

The following table provides a comparison of event processing times in milliseconds. We ran the test on a Windows Server 2016 virtual machine with the following event counts:

- 70178 total events
- 14746 events where the module parses events with the older method
- 28823 events where the module sets the message field using the native Windows function

| milliseconds | CaptureMessage | CaptureMessageFast | ResolveSID | ResolvedIDOutput |
| --- | --- | --- | --- | --- |
| 5103 | `FALSE` | `TRUE` | `FALSE` | n/a |
| 5542 | `TRUE` | `TRUE` | `FALSE` | n/a |
| 5947 | `FALSE` | `TRUE` | `TRUE` | BOTH |
| 5887 | `TRUE` | `FALSE` | `FALSE` | n/a |
| 6902 | `TRUE` | `TRUE` | `TRUE` | BOTH |
| 8569 | `TRUE` | `FALSE` | `TRUE` | BOTH |

|  | If you enable NXLog Agent [debug logging](https://docs.nxlog.co/agent/current/config/global-settings.html#loglevel) you can determine which parsing and message rendering methods the module uses:  - The module logs `parsing from xml event` when the old parsing method is applied. - It logs `using slower Message render method` when it sets the message field using the native Windows function. - It logs `Replacing SID on message field` when resolving SIDs in the `$Message` field is enabled. |
| --- | --- |

## Fields

The following fields are used by *im\_msvistalog*.

`$raw_event` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

A list of event fields in key-value pairs.

`$AccountName` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The username associated with the event.

`$AccountType` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The type of the account. Possible values are: `User`, `Group`,`Domain`, `Alias`, `Well Known Group`, `Deleted Account`,`Invalid`, `Unknown`, and `Computer`.

`$ActivityID` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

A globally unique identifier for the current activity, as stored in EvtSystemActivityID.

`$Category` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The category name resolved from Task.

`$Channel` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The Channel of the event source (for example, `Security` or `Application`).

`$Domain` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The domain name of the user.

`$ERROR_EVT_UNRESOLVED` (type: [boolean](https://docs.nxlog.co/agent/current/language/types.html#type-boolean))

This field is set to TRUE if the event message cannot be resolved and the insertion strings are not present.

`$EventID` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The event ID (specific to the event source) from the EvtSystemEventID field.

`$EventTime` (type: [datetime](https://docs.nxlog.co/agent/current/language/types.html#type-datetime))

The EvtSystemTimeCreated field.

`$EventType` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The type of the event, which is a string describing the severity. This is translated to its string representation from EvtSystemLevel. Possible values are: `CRITICAL`, `ERROR`,`AUDIT_FAILURE`, `AUDIT_SUCCESS`, `INFO`, `WARNING`, and `VERBOSE`.

`$EventXML` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The raw event data in XML format. This field is available if the module’s [CaptureEventXML](https://docs.nxlog.co/agent/current/im/#config-captureeventxml) directive is set to TRUE.

`$ExecutionProcessID` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The process identifier of the event producer as in EvtSystemProcessID.

`$Hostname` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The EvtSystemComputer field.

`$Keywords` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The value of the Keywords field from EvtSystemKeywords.

`$Level` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The level of the event that was generated.

`$LevelValue` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

An integer indicating the level of the event that was generated.

`$Message` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The message from the event.

`$Opcode` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The Opcode string resolved from OpcodeValue.

`$OpcodeValue` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The Opcode number of the event as in EvtSystemOpcode.

`$ProviderGuid` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The globally unique identifier of the event’s provider as stored in EvtSystemProviderGuid. This corresponds to the name of the provider in the [$SourceName](https://docs.nxlog.co/agent/current/im/#sourcename) field.

`$RecordNumber` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The number of the event record.

`$RelatedActivityID` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

`$Severity` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The normalized severity name of the event. See [$SeverityValue](https://docs.nxlog.co/agent/current/im/#severityvalue).

`$SeverityValue` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The normalized severity number of the event, mapped as follows.

| Event Log Severity | Normalized Severity |
| --- | --- |
| 0/Audit Success | 2/INFO |
| 0/Audit Failure | 4/ERROR |
| 1/Critical | 5/CRITICAL |
| 2/Error | 4/ERROR |
| 3/Warning | 3/WARNING |
| 4/Information | 2/INFO |
| 5/Verbose | 1/DEBUG |

`$SourceName` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The event source which produced the event, from the EvtSystemProviderName field.

`$TaskValue` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The task number from the EvtSystemTask field.

`$ThreadID` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The thread identifier of the event producer as in EvtSystemThreadID.

`$UserID` (type: [string](https://docs.nxlog.co/agent/current/language/types.html#type-string))

The Security Identifier (SID) which resolves to [$AccountName](https://docs.nxlog.co/agent/current/im/#accountname), stored in EvtSystemUserID.

`$Version` (type: [integer](https://docs.nxlog.co/agent/current/language/types.html#type-integer))

The Version number of the event as in EvtSystemVersion.

## Fields by providers

For the fields used by the providers, see the [fields by providers list](https://docs.nxlog.co/agent/current/im/msvistalog_providers.html).

## Examples

|  | Due to a limitation in the Windows Event Log API, queries with more than 22 clauses will fail, producing the following error message:  The workaround for this limitation is grouping clauses and/or splitting the filter across multiple queries. In the example below, the filter consists of 6 EventIDs; however, these count as 2 in terms of the aforementioned limitation.  Combining clauses in groups  ```xml <QueryXML>     <QueryList>         <Query Id="0">             <Select Path="Security">*[System[(EventID=6416 or EventID=6424 or EventID=4732) or (EventID=1102 or EventID=4719 or EventID=4704)]]             </Select>         </Query>     </QueryList> </QueryXML> ```  xml |
| --- | --- |

Example 1. Forwarding logs from Windows Event Log to a remote host in syslog format

nxlog.conf

```config
<Extension syslog>
    Module          xm_syslog
</Extension>

<Input eventlog>
    Module          im_msvistalog
    <QueryXML>
        <QueryList>
            <Query Id='0'>
                <Select Path='Application'>*</Select>
                <Select Path='Security'>*[System/Level&lt;4]</Select>
                <Select Path='System'>*</Select>
            </Query>
        </QueryList>
    </QueryXML>
</Input>

<Output tcp>
    Module          om_tcp
    Host            192.168.1.1:514
    Exec            to_syslog_bsd();
</Output>

<Route eventlog_to_tcp>
    Path            eventlog => tcp
</Route>
```

config

Example 2. Retaining the original EventData and UserData XML

This configuration collects events from Windows Event Log and uses the [extract\_xml()](https://docs.nxlog.co/agent/current/xm/xml.html#func-extractxml) function of the *xm\_xml* module to retain the original `EventData` and `UserData` XML.

nxlog.conf

```config
<Extension xml>
    Module           xm_xml
</Extension>

<Extension json>
    Module           xm_json
</Extension>

<Input eventlog>
    Module           im_msvistalog
    CaptureEventXML  TRUE (1)
    <QueryXML>
        <QueryList>
            <Query Id='0'>
                <Select Path='Application'>*</Select>
                <Select Path='Security'>*[System/Level&lt;4]</Select>
                <Select Path='System'>*</Select>
            </Query>
        </QueryList>
    </QueryXML>
    <Exec>
        $EventData = extract_xml("/Event/EventData", $EventXML);
        if $EventData == ""
        {
            delete($EventData);
        }

        $UserData = extract_xml("/Event/UserData", $EventXML);
        if $UserData == ""
        {
            delete($UserData);
        }

        delete($EventXML); (2)
        to_json(); (3)
    </Exec>
</Input>
```

config

| **1** | The [CaptureEventXML](https://docs.nxlog.co/agent/current/im/#config-captureeventxml) directive is set to `TRUE` to store the raw XML-formatted event data in the `$EventXML` field. |
| --- | --- |
| **2** | Use the [delete()](https://docs.nxlog.co/agent/current/language/core-procedures.html#proc-delete) procedure to remove unnecessary fields after processing. |
| **3** | The [to\_json()](https://docs.nxlog.co/agent/current/xm/json.html#proc-to-json) procedure of the *xm\_json* module is called to convert the record to JSON. |

Output sample

```json
{
  "EventTime": "2022-07-05T08:24:39.522394+02:00",
  "Hostname": "WINAB-2JR3FR9RD",
  "Keywords": "9259400833873739776",
  "LevelValue": 4,
  "EventType": "INFO",
  "SeverityValue": 2,
  "Severity": "INFO",
  "EventID": 7036,
  "SourceName": "Service Control Manager",
  "ProviderGuid": "{555908D1-A6D7-4695-8E1E-26931D2012F4}",
  "Version": 0,
  "TaskValue": 0,
  "OpcodeValue": 0,
  "RecordNumber": 3356,
  "ExecutionProcessID": 528,
  "ExecutionThreadID": 1640,
  "Channel": "System",
  "Message": "The nxlog service entered the running state.",
  "Level": "Information",
  "param1": "nxlog",
  "param2": "running",
  "EventData.Binary": "6E0078006C006F0067002F0034000000",
  "EventReceivedTime": "2022-07-05T08:24:40.725436+02:00",
  "SourceModuleName": "eventlog",
  "SourceModuleType": "im_msvistalog",
  "EventData": "<EventData><Data Name=\"param1\">nxlog</Data><Data Name=\"param2\">running</Data><Binary>6E0078006C006F0067002F0034000000</Binary></EventData>"
}
```

json

|  | If the NXLog Agent service is running as a custom user, errors may be logged in the log file such as:  or  This happens when the user account does not have permission to access the specified Windows Event Log channel. Refer to [Access denied to a Windows Event Log channel](https://docs.nxlog.co/agent/current/troubleshoot/log-access-errors.html#access-denied-to-a-windows-event-log-channel) for instructions on how to resolve these errors. |
| --- | --- |