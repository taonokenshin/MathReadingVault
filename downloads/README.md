# Public English study archive

The complete 20 October 2026 study snapshot is included in this directory as five Base64 text parts. They preserve one compressed archive byte for byte. This distribution avoids a stalled binary-attachment upload channel.

Download or clone the repository, open Terminal in its root directory, and run:

```sh
python3 downloads/restore_archive.py
```

The command uses only Python's standard library, verifies SHA-256, and writes `MathReadingVault_English_Study_Archive_2026-10-20_Public.tar.xz` in the current directory. Open that archive with macOS Archive Utility, then open `START_HERE.md` in the extracted folder. No model/API call or account credential is needed. An existing different output file is never overwritten.

The snapshot contains 1,152 English mathematical articles and 1,124 normalized educational session records, with textbook-order guides, reader prefaces, stable source handles and honest proof-status labels. See the [archive guide](../docs/ARCHIVE.md) for scope and unresolved boundaries.

The restored archive is 3,266,528 bytes. Its SHA-256 appears in [SHA256SUMS.txt](SHA256SUMS.txt). The [editorial validation report](archive_validation.json) checks privacy patterns, file links, syntax and transport; it does not certify proofs or distribution rights. The [restoration script](restore_archive.py) and parts [01](archive.part01.b64), [02](archive.part02.b64), [03](archive.part03.b64), [04](archive.part04.b64), [05](archive.part05.b64) are all included in the ordinary repository download.

Source PDFs, page images, the raw private archive, account information, automation memory and operational state are excluded. Original prose licensing and third-party exclusions follow the repository licenses and notices. The [dated release](https://github.com/taonokenshin/MathReadingVault/releases/tag/study-edition-2026-10-20) documents this export.
