Command line used to find this crash:

afl-fuzz -t 200 -m none -i - -o ./out-dir/ -x ./dict/http_request_fuzzer.dict.txt -- /home/oof/apache-afl/fuzzer-dir/../install_dir/bin/httpd -X -f /home/oof/apache-afl/fuzzer-dir/conf/default.conf

If you can't reproduce a bug outside of afl-fuzz, be sure to set the same
memory limit. The limit used for this fuzzing session was 0 B.

Need a tool to minimize test cases before investigating the crashes or sending
them to a vendor? Check out the afl-tmin that comes with the fuzzer!

Found any cool bugs in open-source tools using afl-fuzz? If yes, please post
to https://github.com/AFLplusplus/AFLplusplus/issues/286 once the issues
 are fixed :)

