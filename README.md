# sarif-info
Personal utility to work with SARIF files. [Microsoft/sarif-tools][sarif-tools]
was a pain to contribute to so I made my own utility. Work in progress.

[sarif-tools]: https://github.com/microsoft/sarif-tools

## Installation
We need [Microsoft/sarif-tools][sarif-tools] and [PrettyTable][prettytable].

[prettytable]: https://github.com/jazzband/prettytable

```
python3 -m pip install sarif-tools prettytable
```

## Commands

### stats
Prints a table of ruleIDs and their number of hits. By default, the table is
sorted by count descending. You can pass a single file or a directory containing
one or more SARIF files.

```
$ python3 sarif-info.py stats tests/test2.sarif

List of analyzed files:
/mnt/c/Users/Parsia/Desktop/git-stuff/sarif-info/tests/test2.sarif
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

List of analyzed files:
/mnt/c/Users/Parsia/Desktop/git-stuff/sarif-info/tests/test2.sarif
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

### split
Splits the input file into multiple individual SARIF files filtered by ruleID.
Each SARIF file will only contain hits for one rule. The output files are
created in the same path and with `inputfile-ruleid.sarif` naming convention.

This command copies the rest of the info from the input file. For example, the
`conversion` key is not modified.

```
$ python sarif-info.py split tests/test2.sarif

$ ls -alt tests/

-rwxrwxrwx 1 parsia parsia 2024506 Sep  6 13:15 test2-mobsf.mobsfscan.sha1_hash.sha1_hash.sarif
drwxrwxrwx 1 parsia parsia     512 Sep  6 13:15 .
-rwxrwxrwx 1 parsia parsia 2027786 Sep  6 13:15 test2-mobsf.mobsfscan.secrets.hardcoded_api_key.sarif
-rwxrwxrwx 1 parsia parsia 2025576 Sep  6 13:15 test2-mobsf.mobsfscan.secrets.hardcoded_username.sarif
-rwxrwxrwx 1 parsia parsia 2023509 Sep  6 13:15 test2-java.lang.security.audit.formatted-sql-string.formatted-sql-string.sarif
-rwxrwxrwx 1 parsia parsia 2026823 Sep  6 13:15 test2-contrib.owasp.java.ssrf.ssrf.owasp.java.ssrf.possible.import.statements.sarif
-rwxrwxrwx 1 parsia parsia 2025621 Sep  6 13:15 test2-java.log4j.security.log4j-message-lookup-injection.log4j-message-lookup-injection.sarif
-rwxrwxrwx 1 parsia parsia 2023492 Sep  6 13:15 test2-java.lang.security.audit.sqli.jdbc-sqli.jdbc-sqli.sarif
drwxrwxrwx 1 parsia parsia     512 Sep  6 13:13 ..
-rwxrwxrwx 1 parsia parsia 1213586 May 17 11:57 test2.sarif
-rwxrwxrwx 1 parsia parsia     425 May 17 11:53 test1.sarif
```

## License
MIT, please see [LICENSE](LICENSE).