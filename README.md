# sarif-info
Personal utility to work with SARIF files. [Microsoft/sarif-tools][sarif-tools]
was a pain to contribute to so I made my own utility. Work in progress.

[sarif-tools]: https://github.com/microsoft/sarif-tools

## Installation
We need the [Microsoft/sarif-tools][sarif-tools] package and
[PrettyTable][prettytable].

[prettytable]: https://github.com/jazzband/prettytable

```
python3 -m pip install sarif-tools prettytable
```

## Commands
Run `python3 sarif-info.py stats /path/to/sarif/file.sarif` to view a table of
ruleIDs and their number of hits. By default, the table is sorted by count
descending.

```
$ python3 sarif-info.py stats tests/test2.sarif

+-----------------------------------------------------------------------------------+-------+
| rule ID                                                                           | count |
+-----------------------------------------------------------------------------------+-------+
| mobsf.mobsfscan.secrets.hardcoded_api_key                                         |   5   |
| contrib.owasp.java.ssrf.ssrf.owasp.java.ssrf.possible.import.statements           |   4   |
| mobsf.mobsfscan.secrets.hardcoded_username                                        |   3   |
| java.log4j.security.log4j-message-lookup-injection.log4j-message-lookup-injection |   2   |
| mobsf.mobsfscan.sha1_hash.sha1_hash                                               |   2   |
| java.lang.security.audit.sqli.jdbc-sqli.jdbc-sqli                                 |   1   |
| java.lang.security.audit.formatted-sql-string.formatted-sql-string                |   1   |
+-----------------------------------------------------------------------------------+-------+
```

To sort the table in reverse (smaller counts first) use `--asc` or
`--ascending`.

```
$ python3 sarif-info.py stats tests/test2.sarif --asc
+-----------------------------------------------------------------------------------+-------+
| rule ID                                                                           | count |
+-----------------------------------------------------------------------------------+-------+
| java.lang.security.audit.sqli.jdbc-sqli.jdbc-sqli                                 |   1   |
| java.lang.security.audit.formatted-sql-string.formatted-sql-string                |   1   |
| java.log4j.security.log4j-message-lookup-injection.log4j-message-lookup-injection |   2   |
| mobsf.mobsfscan.sha1_hash.sha1_hash                                               |   2   |
| mobsf.mobsfscan.secrets.hardcoded_username                                        |   3   |
| contrib.owasp.java.ssrf.ssrf.owasp.java.ssrf.possible.import.statements           |   4   |
| mobsf.mobsfscan.secrets.hardcoded_api_key                                         |   5   |
+-----------------------------------------------------------------------------------+-------+
```

## License
MIT, please see [LICENSE](LICENSE).