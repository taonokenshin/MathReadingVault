#!/usr/bin/env python3
"""Build an explicitly scoped, privacy-filtered public study archive locally.

No network access, scheduler operation, proof audit, or source-PDF copying.
Original mathematical bodies retain their historical qualifications. This is
an editorial export, not a rights-clearance or theorem-verification tool.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, shutil, urllib.parse, zipfile

MASK=re.compile(r'```[^\n]*\n[\s\S]*?```|~~~[^\n]*\n[\s\S]*?~~~|\$\$[\s\S]*?\$\$|(?<!\$)\$(?!\$)[^\n$]*?\$')
PRIVATE=re.compile(r'/Users/[^\s`<>"\n]+|/var/folders/[^\s`<>"\n]+')
EMAIL=re.compile(r'[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
SECRET=re.compile(r'(?<![A-Za-z])(?:sk-|ghp_|github_pat_)[A-Za-z0-9_]{12,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();src=a.source.resolve();out=a.output.resolve()
    if out.exists():raise SystemExit('Refusing to replace an existing output')
    if out.is_relative_to(src) or src.is_relative_to(out):raise SystemExit('Source and output must be disjoint')
    records=json.loads((src/'Catalogs/FILE_CATALOG.json').read_text())
    by_original={x['original_source']:x for x in records};by_id={x['id']:x for x in records}
    out.mkdir(parents=True)
    for root in ['English','Reader']:
        shutil.copytree(src/root,out/root)
    (out/'Catalogs').mkdir()
    for name in ['TEXTBOOK_CONTENTS.json','RESULT_AND_EXERCISE_FINDER.md','RESULT_AND_EXERCISE_FINDER.json']:
        shutil.copy2(src/'Catalogs'/name,out/'Catalogs'/name)
    for name in ['CROSS_BOOK_PATHS.md','ASSESSMENT_DESIGN.md','LOCAL_CODEX_HANDOFF.md']:
        shutil.copy2(src/name,out/name)
    # Keep only public provenance fields; operational identity/state is excluded.
    catalog=[]
    for x in records:
        catalog.append({k:x[k] for k in ['id','book','kind','title','textbook_placement','placements','placement_basis','original_record_date','english_file','original_source_sha256','source_linked_records','complete_mathematical_session_text']})
    (out/'Catalogs/FILE_CATALOG.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
    source_lines=['# Source record provenance','',
      'The original-language private archive is not redistributed. Each stable ID below records its original note hash, date, and textbook placement. These are provenance handles, not proof certificates. The English articles and normalized educational records are included.','']
    for x in records:
        source_lines+=['## '+x['id'],'',x['title'],'',
          'Book placement: '+x['textbook_placement']+'. Date: '+str(x['original_record_date'])+'.','',
          'Original-note SHA256: `'+x['original_source_sha256']+'`.','']
    (out/'SOURCE_RECORDS.md').write_text('\n'.join(source_lines))
    (out/'SOURCE_LOCATIONS.md').write_text('''# Textbook sources\n\nUse lawfully accessed copies of Jürgen Neukirch, *Algebraic Number Theory*, and Daniel A. Marcus, *Number Fields*. The archive follows Neukirch Chapters I–VII, including VII §13, and Marcus Chapters 1–8 plus recorded background appendices. There is no Marcus Chapter 9.\n\nPrinted and physical PDF page locators inside articles refer to the editions used in the historical project; verify local pagination before lookup. No PDF, page scan, cached excerpt, library path or publisher text file is bundled. Cited third-party works retain their own rights.\n''')
    (out/'START_HERE.md').write_text('''# MathReadingVault: public English study archive\n\nPublic editorial export, 23 October 2026, of the private English edition frozen on 20 October 2026. This archive contains 1,152 mathematical articles (977 Neukirch; 175 Marcus) and 1,124 normalized educational session records (584 Neukirch; 540 Marcus). These are file counts, including historical drafts and corrections, not distinct theorem, exercise, proof, learner or accepted-session counts.\n\nBegin with [Marcus](Reader/Marcus_Number_Fields/CONTENTS.md) or [Neukirch](Reader/Neukirch_ANT/CONTENTS.md). The learner chooses the primary book, aims and standards. Chapter guides follow the original contents; each article has preparation, scope, route, related reading and recorded qualifications. Use [the finder](Catalogs/RESULT_AND_EXERCISE_FINDER.md) for targeted lookup. Eight session records preserve complete mathematical texts that had no resolved standalone article.\n\nThis public export preserves reader-authored exposition and historical qualifications. No mathematical proofs have been reverified for publication. A source-recorded closed-pass1 or reviewed label keeps its dated scope; cited, conditional, attempted and source-caveat remain different. Earlier articles can be superseded by later corrections. A reader diagnosis is not a publisher's official erratum. NM-HR-073 remains an optional unfinished higher-local supplement in this snapshot, not a prerequisite or a claim that the topic is a public unsolved problem.\n\nThe complete original-language private archive, runtime, account information, original comparison ledgers, PDF caches, commercial textbooks and automation memory are excluded. Links to original notes lead to [hash provenance](SOURCE_RECORDS.md), not to a claim that the omitted originals are bundled. Other exclusions are [registered explicitly](PUBLIC_OMISSIONS.md). Historical commands and continuations are evidence, never instructions to execute on another machine.\n\nUse [the local Codex handoff](LOCAL_CODEX_HANDOFF.md), [assessment design](ASSESSMENT_DESIGN.md) and [cross-book paths](CROSS_BOOK_PATHS.md) to plan learning. No preliminary proof-audit campaign is required. Configure lawfully accessed source books using [source guidance](SOURCE_LOCATIONS.md). Public software is in the main GitHub repository; this archive contains study material, not an installed scheduler.\n\nOriginal released prose is offered under CC BY 4.0 to the extent the maintainer holds the relevant rights. Third-party quotations, textbook statements, bibliographic works and source books are excluded from that grant and retain their owners' rights. Publication does not claim source or publisher endorsement. See the repository's LICENSE-CONTENT.md and THIRD_PARTY_NOTICES.md.\n''')
    omissions={};changes=[]
    def omitted(raw,origin):
        key=hashlib.sha256(raw.encode()).hexdigest()[:12]
        d=omissions.setdefault(key,{'id':key,'reference_label':Path(raw.split('#')[0]).name or 'private reference','records':[]})
        d['reference_label']=PRIVATE.sub('[private location]',d['reference_label'])
        if origin not in d['records']:d['records'].append(origin)
        return 'PUBLIC_OMISSIONS.md#reference-'+key
    for p in sorted(out.rglob('*.md')):
        s=p.read_text();rel=p.relative_to(out);held=[]
        def mask(m):held.append(m.group());return '@@PUBLICMASK'+str(len(held)-1)+'@@'
        t=MASK.sub(mask,s)
        def link(m):
            label,raw=m.group(1),urllib.parse.unquote(m.group(2).strip().strip('<>'))
            if re.match(r'^(https?|mailto|doi):',raw):return m.group()
            if not raw.split('#')[0]:return m.group()
            target=(p.parent/raw.split('#')[0]).resolve()
            if target.is_relative_to(out) and target.is_file():return m.group()
            old_target=(src/rel.parent/raw.split('#')[0]).resolve()
            try:key=str(old_target.relative_to(src))
            except ValueError:key=''
            if key in by_original:
                x=by_original[key];dest='SOURCE_RECORDS.md#'+x['id'].lower();newlabel='Source record '+x['id']
            else:dest=omitted(raw,str(rel));newlabel=label
            file,_,anchor=dest.partition('#');new=os.path.relpath(out/file,p.parent)+(('#'+anchor) if anchor else '')
            changes.append({'file':str(rel),'kind':'public-reference-remap'})
            return '['+newlabel+']('+new+')'
        t=re.sub(r'(?<!!)\[([^\]\n]*)\]\(([^\n)]+)\)',link,t)
        for i,v in enumerate(held):t=t.replace('@@PUBLICMASK'+str(i)+'@@',v)
        # Remove operational timestamps/identifiers while retaining the record date.
        if '/Run_Records/' in '/'+str(rel):
            t=re.sub(r'^- (?:Started at|Ended at|Occurrence|Target occurrences|Sprint id):.*\n','',t,flags=re.M)
        t=re.sub(r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b','[workflow identity omitted]',t,flags=re.I)
        t=PRIVATE.sub('[private local location omitted]',t)
        t=EMAIL.sub('[private email omitted]',t)
        if SECRET.search(t):raise SystemExit('Potential credential-like content: '+str(rel))
        p.write_text(t)
    lines=['# References omitted from this public export','',
      'The public archive omits private provenance ledgers, operational records and source-cache files. A reference here is an explicit omission, not a bundled proof or an assertion of closure. Stable note hashes are in SOURCE_RECORDS.md.','']
    for k,d in sorted(omissions.items()):
        lines+=['## Reference '+k,'','Reference label: `'+d['reference_label'].replace('`','')+'`.','',
          'Reason: outside the public reading-material selection. Referencing files: '+', '.join('`'+v+'`' for v in d['records'])+'.','']
    (out/'PUBLIC_OMISSIONS.md').write_text('\n'.join(lines))
    report={'source_snapshot_date':'2026-10-20','public_export_date':'2026-10-23','mathematical_articles':1152,'normalized_session_records':1124,'excluded_original_files':2299,'public_reference_remaps':len(changes),'omitted_reference_targets':len(omissions),'scope':'editorial privacy and transport export; no mathematical proof audit or rights clearance'}
    (out/'PUBLIC_EXPORT.json').write_text(json.dumps(report,indent=2)+'\n')
    manifest=[{'file':str(p.relative_to(out)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(out.rglob('*')) if p.is_file()]
    (out/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    archive=out.with_suffix('.zip')
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(out.rglob('*')):
            if p.is_file():z.write(p,str(Path(out.name)/p.relative_to(out)))
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:raise SystemExit('ZIP CRC failure')
        for x in manifest:
            assert hashlib.sha256(z.read(str(Path(out.name)/x['file']))).hexdigest()==x['sha256']
    print(json.dumps({**report,'files':len(manifest)+1,'archive_bytes':archive.stat().st_size,'archive_sha256':sha(archive)}))
if __name__=='__main__':main()
