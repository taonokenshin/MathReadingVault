#!/usr/bin/env python3
"""Restore the public study archive from the five bundled Base64 text parts."""
from pathlib import Path
import argparse
import base64
import hashlib

NAME = 'MathReadingVault_English_Study_Archive_2026-10-20_Public.tar.xz'
SHA256 = '857fc65712729150c71f74fae2f1bbe8bb7835ff9547ba2cb020aa5e4d9dce40'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(NAME))
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    encoded = b''.join((root / ('archive.part%02d.b64' % i)).read_bytes().strip()
                       for i in range(1, 6))
    data = base64.b64decode(encoded, validate=True)
    if hashlib.sha256(data).hexdigest() != SHA256:
        raise SystemExit('Archive checksum mismatch; download the five parts again.')
    if args.output.exists():
        if hashlib.sha256(args.output.read_bytes()).hexdigest() == SHA256:
            print('Existing archive verified: %s' % args.output)
            return
        raise SystemExit('Output already exists with different content; choose --output.')
    with args.output.open('xb') as stream:
        stream.write(data)
    print('Restored and SHA-256 verified: %s (%d bytes)' % (args.output, len(data)))
    print('Open the archive, then read START_HERE.md in the extracted folder.')


if __name__ == '__main__':
    main()
