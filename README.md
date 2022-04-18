# Anki Menu Config Bug

This repo provides a repro for an anki bug. On macOS, plugins can't add menu
entries that start with "Config".

## Reproduction from source

On macOS:

1. Package the plugin.

   ```shell
   ./dev/bin/package
   ```

1. Import `menubug.ankiaddon` in Anki.
1. Restart Anki.

In the tools menu you'll see entries such as "Confi" "Just a random text", but
not "Config" or "Configure", which the plugin also tries to add.
