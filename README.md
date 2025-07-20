# apache-afl

An automated setup for compiling & fuzzing Apache httpd server.

More info about the process/journey can be found here: https://0xbigshaq.github.io/2022/03/12/fuzzing-smarter-part2

# Usage

To start the build process, run:

```
./afl-toolchain.sh
```

To start fuzzing:
```
cd fuzzer-dir/
./afl-runner.sh
```

> Tested on: AFL Version ++4.00c (release) under a `aflplusplus/aflplusplus` docker image

## Fixes

So if you actually try running this on the newest version of AFL, you get an illegal instruction here:

```
Downloading separate debug info for /lib/x86_64-linux-gnu/libstdc++.so.6
Downloading separate debug info for /lib/x86_64-linux-gnu/libgpg-error.so.0
[New Thread 0x7ffff1aff6c0 (LWP 4050705)]
[+] Launched AFL loop
[+] Continue with normal apache execution
[+] Looping

Thread 1 "httpd" received signal SIGILL, Illegal instruction.
0x0000555556199b1b in unique_id_global_init (p=0x525000007928, plog=0x525000070928, ptemp=0x525000075928,
    main_server=0x5250000733e8) at mod_unique_id.c:151
151         unique_id_rec_offset[0] = APR_OFFSETOF(unique_id_rec, stamp);
(gdb) where
#0  0x0000555556199b1b in unique_id_global_init (p=0x525000007928, plog=0x525000070928, ptemp=0x525000075928,
    main_server=0x5250000733e8) at mod_unique_id.c:151
#1  0x00005555559ca26e in ap_run_post_config (pconf=0x525000007928, plog=0x525000070928, ptemp=0x525000075928, s=0x5250000733e8)
    at config.c:102
#2  0x000055555577d148 in main (argc=4, argv=0x7fffffffdd48) at main.c:910
(gdb) quit
A debugging session is active.

        Inferior 1 [process 4050701] will be killed.

Quit anyway? (y or n) y
```

So you actually need to use an older version of AFL for this to work correctly.... This version: "AFLplusplus-4.07c" seems to work fine... So just run `export PATH=/home/oof/oldafl/AFLplusplus-4.07c:$PATH` or something like that...



