# pycarrot2
A python wrapper of carrot2 clustering server.



### FAQ

**How to solve "Form too large"?**

The form you sent is too large and exceeds the default value.

Solution: Modify dcs/dcs.sh, add `-Dorg.eclipse.jetty.server.Request.maxFormContentSize=500000` between `java` and `$DCS_OPTS `.