for method in OPTIONS MKCOL PUT DELETE MOVE PROPFIND; do
    curl --digest -u user1:password -X $method http://127.0.0.1:8080/ff/test$RANDOM.txt
done

