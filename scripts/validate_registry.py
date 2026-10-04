"""Validate registry structure and evidence references; does not activate experiments."""
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]

def validate(registry, schema):
    Draft202012Validator.check_schema(schema)
    errors = [f"{'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.validator} validation failed"
              for e in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(registry)]
    if errors:
        return errors
    ids = [e['id'] for e in registry['experiments']]
    if ids != [f'{i:03}' for i in range(1, 12)]:
        errors.append('Experiments must appear exactly once in order 001-011.')
    sources = [s['id'] for s in registry['sources']]
    if len(sources) != len(set(sources)):
        errors.append('Source IDs must be unique.')
    for e in registry['experiments']:
        refs = e['evidence_refs']
        if not refs or any(ref not in sources for ref in refs):
            errors.append(f"Experiment {e['id']}: missing or unresolved evidence reference.")
        if any(ref not in sources for ref in e['name_evidence'].split('/')):
            errors.append(f"Experiment {e['id']}: unresolved name evidence.")
        if e['purpose']['evidence'] not in sources:
            errors.append(f"Experiment {e['id']}: unresolved purpose evidence.")
        if e['ui_route']['recommended'] != f"/experiments/{e['id']}":
            errors.append(f"Experiment {e['id']}: recommended route does not match ID.")
    return errors

if __name__ == '__main__':
    try:
        registry = json.loads((ROOT / 'experiments/registry.json').read_text())
        schema = json.loads((ROOT / 'experiments/registry.schema.json').read_text())
        errors = validate(registry, schema)
    except (OSError, ValueError):
        print('Registry validation failed: unreadable file or malformed JSON.', file=sys.stderr)
        sys.exit(1)
    if errors:
        print('Registry validation failed:', file=sys.stderr)
        for error in errors:
            print(f'- {error}', file=sys.stderr)
        sys.exit(1)
    print('Registry valid: experiments 001-011, required fields, status values and evidence references.')
