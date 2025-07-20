
export PREFIX=/home/oof/apache-afl/install_dir/
export PATH="$PREFIX/pcre/bin:$PATH"
make distclean
PREFIX=/home/oof/apache-afl/install_dir/ \
CC=afl-clang-fast \
CXX=afl-clang-fast++ \
CFLAGS="-Wno-error=declaration-after-statement -g -fsanitize=address -fno-sanitize-recover=all" \
CXXFLAGS="-Wno-error=declaration-after-statement -g -fsanitize=address -fno-sanitize-recover=all" \
LDFLAGS="-fsanitize=address -fno-sanitize-recover=all -lm" \
./configure --with-apr="$PREFIX/apr/" \
            --with-apr-util="$PREFIX/apr-util/" \
            --with-expat="$PREFIX/expat/" \
            --with-pcre="$PREFIX/pcre/" \
            --disable-pie \
            --disable-so \
            --disable-example-ipc \
            --disable-example-hooks \
            --disable-optional-hook-export \
            --disable-optional-hook-import \
            --disable-optional-fn-export \
            --disable-optional-fn-import \
            --with-mpm=prefork \
            --enable-static-support \
            --disable-mods-shared \
            --enable-mods-static=most \
            --enable-debugger-mode \
            --with-crypto --with-openssl \
            --prefix=$PREFIX \
            --disable-shared

# This script originally had enable-mods-static=reallyall , but we actually need to ignore a couple of modules which cause problems during fuzzing...

#  --enable-mods-static=most \
# so,macro,ratelimit,buffer,filter,charset_lite,sed,data,reqtimeout,request,include,proxy_html,substitute,brotli,deflate,ext_filter,xml2enc,reflector,mime,dumpio,bucketeer,proxy_http2,http2,cache,cache_socache,file_cache,socache_dbm,socache_shmcb,socache_dc,socache_memcache,socache_redis,cache_disk,isapi,win32,privileges,unixd,systemd,netware,nw_ssl,dir,speling,vhost_alias,rewrite,userdir,imagemap,negotiation,alias,actions,session_dbd,session_crypto,session,session_cookie,dbd,authnz_ldap,authn_dbd,authn_anon,authz_user,authz_dbm,access_compat,authn_dbm,auth_digest,authn_file,authz_groupfile,auth_form,authn_core,authnz_fcgi,authz_dbd,authz_core,allowmethods,authz_owner,authz_host,authn_socache,auth_basic,ssl,headers,unique_id,expires,ident,cern_meta,mime_magic,remoteip,version,usertrack,setenvif,env,asis,autoindex,status,suexec,info,cgid,cgi,lua,optional_fn_export,optional_fn_import,dialup,optional_hook_export,optional_hook_import,log_debug,logio,log_config,log_forensic,proxy_fcgi,proxy_wstunnel,proxy_express,proxy_connect,proxy_scgi,proxy_ftp,lbmethod_byrequests,lbmethod_bytraffic,lbmethod_bybusyness,proxy_uwsgi,proxy_ajp,proxy_hcheck,proxy,proxy_balancer,proxy_http,proxy_fdpass,echo,example_ipc,case_filter,case_filter_in,example_hooks,md,md_config,md_drive,md_status,md_os,md_ocsp \
