mods=$(find httpd-2.4.64/modules -name mod_*.c | sed 's#.*/mod_##;s#\.c##' | \
  grep -v -E 'slotmem_shm|watchdog|heartmonitor|dav|dav_fs' | \
  tr '\n' ',' | sed 's/,$//')

echo "Safe modules: $mods"

