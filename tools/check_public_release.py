#!/usr/bin/env python3
"""Read-only public artifact checks: privacy patterns, syntax, links, manifest.

This does not audit mathematical proofs, establish distribution rights, parse
all LaTeX or inspect rendered pages. It reports potential exposure patterns
without echoing their contents.
"""
from pathlib import Path
import argparse, ast, hashlib, json, re, urllib.parse
from check_obsidian_math import scan_file
MASK=re.compile(r'```[^\n]*\n[\s\S]*?```|~~~[^\n]*\n[\s\S]*?~~~|\$\$[\s\S]*?\$\$|(?<!\$)\$(?!\$)[^\n$]*?\$')
SKIP={'.git','__pycache__','.local-automations','.pytest_cache'}
PATTERNS={
 'personal-home-path':re.compile(r'/Users/[A-Za-z0-9._-]+/'),
 'private-temporary-path':re.compile(r'/var/folders/[A-Za-z0-9]+/'),
 'email-address':re.compile(r'[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'),
 'organization-identifier':re.compile(r'\borg-[A-Za-z0-9]{12,}\b'),
 'credential-like-token':re.compile(r'(?<![A-Za-z])(?:sk-|ghp_|github_pat_)[A-Za-z0-9_]{12,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
 'unrestored-editorial-mask':re.compile(r'@@(?:PUBLICMASK|PROTECTED|LITERAL|M)\d+@@'),
}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('root',type=Path,nargs='?',default=Path('.'));ap.add_argument('--report',type=Path)
 a=ap.parse_args();root=a.root.resolve();errors=[];count=0;links=0
 for p in sorted(root.rglob('*')):
  if not p.is_file() or SKIP.intersection(p.relative_to(root).parts):continue
  rel=str(p.relative_to(root));count+=1
  if p.suffix.lower() in {'.pdf','.png','.jpg','.pem','.key'}:errors.append({'file':rel,'kind':'excluded-source-or-sensitive-file-type'})
  if p.suffix not in {'.md','.py','.json','.yml','.yaml','.txt'} and p.name not in {'LICENSE','.gitignore'}:continue
  try:s=p.read_text()
  except UnicodeError:errors.append({'file':rel,'kind':'unexpected-binary-text'});continue
  for name,pat in PATTERNS.items():
   if pat.search(s):errors.append({'file':rel,'kind':name})
  if p.suffix=='.py':
   try:ast.parse(s)
   except SyntaxError:errors.append({'file':rel,'kind':'python-syntax'})
  if p.suffix=='.json':
   try:json.loads(s)
   except ValueError:errors.append({'file':rel,'kind':'json-syntax'})
  if p.suffix!='.md':continue
  for line,kind,_ in scan_file(p):errors.append({'file':rel,'kind':kind,'line':line})
  prose=MASK.sub('',s)
  for m in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^\n)]+)\)',prose):
   target=urllib.parse.unquote(m.group(1).strip().strip('<>'))
   if re.match(r'^[A-Za-z][A-Za-z0-9+.-]*:',target):continue
   file=target.split('#',1)[0]
   if not file:continue
   links+=1;q=(p.parent/file).resolve()
   if not q.is_relative_to(root):errors.append({'file':rel,'kind':'link-escapes-release'})
   elif not q.is_file():errors.append({'file':rel,'kind':'missing-file-link','target':file})
 manifest=root/'MANIFEST.json'
 if manifest.is_file():
  for x in json.loads(manifest.read_text()):
   q=(root/x['file']).resolve()
   if not q.is_relative_to(root) or not q.is_file() or hashlib.sha256(q.read_bytes()).hexdigest()!=x['sha256']:errors.append({'file':x['file'],'kind':'manifest-hash-mismatch'})
 report={'scope':'public privacy-pattern, Python/JSON syntax, Markdown file-target, delimiter and manifest checks; no proof audit or rights clearance','files_checked':count,'local_file_links_checked':links,'errors':errors,'ok':not errors}
 if a.report:a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(report,ensure_ascii=False,indent=2));return int(bool(errors))
if __name__=='__main__':raise SystemExit(main())
