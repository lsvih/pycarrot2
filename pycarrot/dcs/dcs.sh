#!/bin/sh

if [ -z "$DCS_OPTS" ]; then
  DCS_OPTS="-Xms64m -Xmx768m"
fi

java $DCS_OPTS -Ddcs.war=war/carrot2-dcs.war -jar lib/carrot2-dcs-bootstrap-3.17.0-SNAPSHOT.jar $@
